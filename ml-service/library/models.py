from itertools import cycle
from typing import Any, Collection, Sequence

from asgiref.sync import sync_to_async
from django.db import models
from django.db.models.base import ModelBase
from django.db.models.functions import Trunc
from pandas import DataFrame
import env

from library.typipng.querysets import TypedQuerySet


class Fieldmeta:
    "Предоставляет дополнительную информацию о полях модели"

    def __init__(self, model: models.Model):
        self.all = tuple(
            f.attname for f in model._meta.fields if isinstance(f, models.Field)
        )
        self.updatable = tuple(set(self.all).difference((model._meta.pk.attname,)))  # type: ignore
        self.datetimes = tuple(
            f.attname for f in model._meta.fields if isinstance(f, models.DateTimeField)
        )

        self.verbose_names = {
            f.attname: f.verbose_name
            for f in model._meta.fields
            if isinstance(f, models.Field)
        }

    def describe(self, instance: models.Model, fields: Sequence[str]):
        "Описывает поля экземпляра модели в виде `{verbose_name: value}`"
        return {
            self.verbose_names[field]: str(getattr(instance, field, ""))
            for field in fields
        }


class FieldmetaModelBase(ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        model = super().__new__(cls, name, bases, attrs)
        if not model._meta.abstract:  # type: ignore
            model._fieldmeta = Fieldmeta(model)  # type: ignore
        return model


class PerformantModel(models.Model, metaclass=FieldmetaModelBase):
    """
    Добавляет некоторые методы (`bulk_upsert()`, `to_dataframe()`) и поля (`_fieldmeta`),
    для производительной обработки больших объемов данных
    """

    class Meta:
        abstract = True

    class PerformantQuerySet(TypedQuerySet):
        async def alist(self) -> list:
            """
            Явная отправка асинхронного SQL запроса
            и материализация результата в список
            """
            return await sync_to_async(list)(self)

        async def aset(self) -> set:
            "Аналог метода `alist()`, возвращает `set`"
            return await sync_to_async(set)(self)

        def bulk_upsert(self, objs: Collection[Any], batch_size: int | None = 1000):
            """
            Совершает производительный "INSERT ... ON CONFLICT UPDATE"
            для большого объема данных
            """
            Model: PerformantModel = self.model

            if Model._fieldmeta.updatable:
                return self.bulk_create(
                    objs,
                    batch_size=batch_size,
                    update_conflicts=True,
                    update_fields=Model._fieldmeta.updatable,
                    unique_fields=(Model._meta.pk.attname,),  # type: ignore
                )
            else:
                return self.bulk_create(objs, ignore_conflicts=True)

        async def abulk_upsert(
            self, objs: Collection[Any], batch_size: int | None = 1000
        ):
            "Асинхронная версия `bulk_upsert()`"
            return await sync_to_async(self.bulk_upsert)(
                objs=objs, batch_size=batch_size
            )

        # INFO: typecheck narrowing
        def to_dataframe(self, extra_fields: Collection[Any] = tuple()) -> DataFrame:
            """
            Преобразует QuerySet в безопасный DataFrame:
            используются поля модели как колонки, даже если DataFrame пустой.

            Поля из параметра `extra_fields` добавляются в колонки путстого DataFrame'а.
            """
            df = DataFrame(self.values() if self._fields is None else self)  # type: ignore

            if df.empty:
                return self._make_empty_df_with_columns(extra_fields)

            return df

        async def ato_dataframe(
            self, extra_fields: Collection[Any] = tuple()
        ) -> DataFrame:
            "Асинхронная версия `to_dataframe()`"
            df = DataFrame(
                await self.values().alist()
                if self._fields is None  # type: ignore
                else await self.alist()
            )

            if df.empty:
                return self._make_empty_df_with_columns(extra_fields)

            return df

        def _make_empty_df_with_columns(self, extra_fields: Collection[Any] = tuple()):
            trunc_columns = tuple(
                column
                for column, function in self.query.annotation_select.items()
                if isinstance(function, Trunc)
            )

            if self.query.group_by or self._fields:  # type: ignore
                columns = set(
                    tuple(self.query.annotation_select)
                    + self.query.values_select
                    + tuple(extra_fields)
                )
            else:
                columns = set(
                    self.model._fieldmeta.all
                    + tuple(self.query.annotation_select)
                    + tuple(extra_fields)
                )

            datetime_columns = columns.intersection(
                self.model._fieldmeta.datetimes + trunc_columns
            )

            df = DataFrame(columns=list(columns))  # type: ignore
            for col in datetime_columns:
                df[col] = df[col].astype("datetime64[ns]").dt.tz_localize(env.TZ)
            return df

        def raw_as_dataframe(
            self,
            raw_query: str,
            params: Any = None,
            translations: dict[str, str] | None = None,
        ) -> DataFrame:
            """
            Упаковывывает результат Raw SQL запроса в безопасный DataFrame:
            используются поля модели как колонки, даже если DataFrame пустой
            """
            raw_qs = self.raw(
                raw_query=raw_query, params=params, translations=translations
            )

            df = DataFrame(x.__dict__ for x in raw_qs)

            if df.empty:
                return DataFrame(columns=raw_qs.columns)  # type: ignore
            else:
                return df[raw_qs.columns]  # type: ignore

    objects: PerformantQuerySet = PerformantQuerySet.as_manager()  # type: ignore
    _fieldmeta: Fieldmeta


PerformantQuerySet = PerformantModel.PerformantQuerySet


class NamedForeignKey(models.ForeignKey):
    """
    Внешний ключ, к которому можно обращаться по `<db_column>`,
    а не по `<field_name>_id`.
    """

    def get_attname(self):
        if not self.db_column:
            raise Exception("`db_column` is not set")
        return self.db_column
