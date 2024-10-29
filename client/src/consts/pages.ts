import ImportPage from "../pages/ImportPage"
import FitPage from "../pages/FitPage"
import PredictPage from "../pages/PredictPage"

export const IMPORT_PATH = "/start"
export const FIT_PATH = "/fit"
export const PREDICT_PATH = "/predict"

export const routes = [
  {path: IMPORT_PATH, Component: ImportPage, title: "import ml"},
  {path: FIT_PATH, Component: FitPage, title: "ml.fit()"},
  {path: PREDICT_PATH, Component: PredictPage, title: "ml.predict()"},
]