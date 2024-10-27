from __future__ import annotations
import os

import keras.api.backend as K
import numpy as np
import pandas as pd
from keras.src.callbacks import LearningRateScheduler
from keras.src.layers import Concatenate, Dense, Embedding, Flatten, Input
from keras.src.metrics import RootMeanSquaredError
from keras.src.models import Model
from keras.src.optimizers import Adam
from sklearn.model_selection import KFold
import random


def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


VER = 1


class ModelManager:
    class DataMeta:
        nums: list
        cats: list
        cat_size: list
        cat_emb: list
        cat_rare: list

        num_mean: dict
        num_std: dict

        cat_fact: dict
        cat_uniq: dict
        cat_min: dict

    EPOCHS = 3
    LRS = [0.001, 0.001, 0.0001]
    FOLDS = 5
    # Learning schedule
    lr_callback = LearningRateScheduler(
        lambda epoch: ModelManager.LRS[epoch],
        verbose=True,
    )

    def __init__(self, train: pd.DataFrame, test: pd.DataFrame):
        self.dm = self.DataMeta()

        TRAIN_LN = len(train)
        all_data = pd.concat([train, test], axis=0, ignore_index=True)

        self.dm.nums = [
            "model_year",
            "milage_km",
            "engine_volume",
            "engine_power",
            "transmission_speed",
        ]
        self.dm.num_mean = {}
        self.dm.num_std = {}

        # STANDARIZE NUMERICAL FEATURES
        for c in self.dm.nums:
            self.dm.num_mean[c] = all_data[c].mean()
            self.dm.num_std[c] = all_data[c].std()

        # LABEL ENCODE CATEGORICAL FEATURES
        self.dm.cats = [
            c for c in all_data.columns if c not in ["id", "price_usd"] + self.dm.nums
        ]
        self.dm.cat_size = []
        self.dm.cat_emb = []
        self.dm.cat_rare = []
        self.dm.cat_fact = {}
        self.dm.cat_min = {}

        for c in self.dm.cats:
            # LABEL ENCODE
            self.dm.cat_fact[c] = factorization = {
                k: v for v, k in zip(all_data[c].factorize()[0], all_data[c])
            }
            all_data[c] = all_data[c].apply(lambda x: factorization[x])

            self.dm.cat_min[c] = all_data[c].min()
            all_data[c] -= self.dm.cat_min[c]
            vc = all_data[c].value_counts()

            # IDENTIFY RARE VALUES
            self.dm.cat_rare.append(vc.loc[vc < 40].index.values)
            mx = all_data[c].max()

            # RELABEL RARE VALUES AS ZERO
            self.dm.cat_size.append(mx + 1 + 1)  # ADD ONE FOR RARE
            self.dm.cat_emb.append(
                int(np.ceil(np.sqrt(mx + 1 + 1)))
            )  # ADD ONE FOR RARE

        train = all_data.iloc[TRAIN_LN:]
        self.dm.cat_uniq = {c: train[c].unique() for c in self.dm.cats}

        self.models = []

        # CATEGORICAL FEATURES
        x_input_cats = Input(shape=(len(self.dm.cats),))
        embs = []
        for j in range(len(self.dm.cats)):
            e = Embedding(self.dm.cat_size[j], self.dm.cat_emb[j])
            x = e(x_input_cats[:, j])  # type: ignore
            x = Flatten()(x)
            embs.append(x)

        # NUMERICAL FEATURES
        x_input_nums = Input(shape=(len(self.dm.nums),))

        # COMBINE
        x = Concatenate(axis=-1)(embs + [x_input_nums])
        x = Dense(256, activation="relu")(x)
        x = Dense(256, activation="relu")(x)
        x = Dense(256, activation="relu")(x)
        x = Dense(1, activation="linear")(x)

        self._build = lambda: Model(inputs=[x_input_cats, x_input_nums], outputs=x)

    @staticmethod
    def _data_clearing(data: pd.DataFrame) -> pd.DataFrame:
        data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)  # type: ignore
        data["engine_volume"] = (
            data["engine"]
            .str.split()
            .apply(
                lambda vals: (
                    [
                        float(v[:-1])
                        for v in vals
                        if v.endswith("l") and is_float(v[:-1])
                    ]
                    or [np.nan]
                )[0]
            )
        )
        data["engine_power"] = (
            data["engine"]
            .str.split()
            .apply(
                lambda vals: (
                    [
                        int(float(v[:-2]))
                        for v in vals
                        if v.endswith("hp") and is_float(v[:-2])
                    ]
                    or [np.nan]
                )[0]
            )
        )
        data["transmission_speed"] = (
            data["transmission"]
            .str.split()
            .apply(
                lambda vals: (
                    [
                        int(v[:-6])
                        for v in vals
                        if v.endswith("-speed") and v[:-6].isdigit()
                    ]
                    or [np.nan]
                )[0]
            )
        )
        data["transmission_type"] = (
            data["transmission"]
            .str.split()
            .apply(
                lambda vals: (
                    ["automatic" for v in vals if "a/t" in v or "/dual" in v]
                    or ["manual" for v in vals if "m/t" in v]
                    or [None]
                )[0]
            )
        )
        data["milage_km"] = data["milage"] * 1.60934
        # data["price_rub"] = data["price"] * 95.0  # ruble exchange rate
        data = data.rename(
            columns={
                "ext_col": "color",
                "int_col": "interior_color",
                "price": "price_usd",
            }
        )
        data["clean_title"] = data["clean_title"] == "yes"
        return data.drop(columns=["engine", "transmission", "milage"])

    @classmethod
    def clean_init(cls):
        train = pd.read_csv("../data/train.csv")
        test = pd.read_csv("../data/test.csv")
        test["price"] = 0
        train = cls._data_clearing(train)
        test = cls._data_clearing(test)
        return cls(train, test)

    def prepare_data(self, data):
        # STANDARIZE NUMERICAL FEATURES
        for c in self.dm.nums:
            data[c] = (data[c] - self.dm.num_mean[c]) / self.dm.num_std[c]
            data[c] = data[c].fillna(0)

        # LABEL ENCODE CATEGORICAL FEATURES
        for c in self.dm.cats:
            # LABEL ENCODE
            factorization = self.dm.cat_fact[c]
            data[c] = data[c].apply(lambda x: factorization.get(x, -1))
            data[c] -= self.dm.cat_min[c]
            data[c] += 1
            data.loc[data[c].isin(self.dm.cat_rare[-1]), c] = 0

        for c in self.dm.cats:
            # COMPARE TEST CAT VALUES TO TRAIN CAT VALUES
            A = self.dm.cat_uniq[c]
            B = data[c].unique()
            C = np.setdiff1d(B, A)
            # RELABEL UNSEEN TEST VALUES AS ZERO
            data.loc[data[c].isin(C), c] = 0

        return data

    def new_model(self):
        return self._build()

    def base_compile(self, model) -> Model:
        model.compile(
            optimizer=Adam(0.001),
            loss="mean_squared_error",
            metrics=[RootMeanSquaredError()],
        )
        return model

    def base_fit(self, model, X_train_cats, X_train_nums, y_train) -> Model:
        model.fit(
            [X_train_cats, X_train_nums],
            y_train,
            validation_data=([X_train_cats, X_train_nums], y_train),
            callbacks=[self.lr_callback],
            batch_size=64,
            epochs=self.EPOCHS,
            verbose=2,  # type: ignore
        )
        return model

    def base_predict(self, model, X_test_cats, X_test_nums) -> Model:
        return model.predict(
            [X_test_cats, X_test_nums],
            verbose=1,  # type: ignore
            batch_size=512,
        ).flatten()

    def add(self, model):
        self.models.append(model)

    def fit(self, train):
        kf = KFold(n_splits=self.FOLDS, random_state=42, shuffle=True)

        for i, (train_index, test_index) in enumerate(kf.split(train)):
            X_train_cats = train.loc[train_index, self.dm.cats].values
            X_train_nums = train.loc[train_index, self.dm.nums].values
            y_train = train.loc[train_index, "price_usd"].values

            # TRAIN MODEL
            K.clear_session()
            model = self.new_model()
            self.base_compile(model)
            self.base_fit(model, X_train_cats, X_train_nums, y_train)
            self.add(model)

    def predict(self, test):
        pred = np.zeros(len(test))
        X_test_cats = test[self.dm.cats].values
        X_test_nums = test[self.dm.nums].values

        for i, model in enumerate(self.models):
            test_preds = self.base_predict(model, X_test_cats, X_test_nums)
            if i == 0:
                pred = test_preds
            else:
                pred += test_preds

        pred /= len(self.models)
        return pred

    def fine_tune(self, train):
        X_train_cats = train[self.dm.cats].values
        X_train_nums = train[self.dm.nums].values
        y_train = train["price_usd"].values

        model = random.choice(self.models)
        model.trainable = True
        model.compile(
            optimizer=Adam(0.001),
            loss="mean_squared_error",
            metrics=[RootMeanSquaredError()],
        )
        model.fit(
            [X_train_cats, X_train_nums],
            y_train,
            validation_data=([X_train_cats, X_train_nums], y_train),
            callbacks=[self.lr_callback],
            batch_size=64,
            epochs=self.EPOCHS,
            verbose=2,  # type: ignore
        )

    def print_rmse(self, oof, train):
        # COMPUTE AND DISPLAY CV RMSE SCORE
        rmse = np.sqrt(np.mean((oof - train.price_usd.values) ** 2))
        print("Overall CV RMSE =", rmse)

    def save_models(self, folder="../model_weights"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        for i, model in enumerate(self.models):
            model.save_weights(f"{folder}/NN_v{VER}_f{i}.weights.h5")

    def load_models(self, folder="../model_weights"):
        i = 0
        while True:
            filename = f"{folder}/NN_v{VER}_f{i}.weights.h5"
            if not os.path.exists(filename):
                break

            model = self.new_model()
            model.load_weights(filename)
            self.add(model)
            i += 1

    @classmethod
    def clean_refit(cls):
        train = pd.read_csv("../data/train.csv")
        test = pd.read_csv("../data/test.csv")
        test["price"] = 0
        train = cls._data_clearing(train)
        test = cls._data_clearing(test)

        model_manager = cls(train, test)
        train = model_manager.prepare_data(train)
        test = model_manager.prepare_data(test)

        model_manager.fit(train)
        oof = model_manager.predict(train)

        model_manager.print_rmse(oof, train)
        model_manager.save_models()


if __name__ == "__main__":
    ModelManager.clean_refit()
    pass
else:
    # FOR EXPORT
    model_manager = ModelManager.clean_init()
    model_manager.load_models()
