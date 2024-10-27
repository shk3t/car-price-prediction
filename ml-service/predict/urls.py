from django.urls import path
from predict.views import FineTuneView, PredictView

urlpatterns = [
    path("predict", PredictView.as_view()),
    path("fine_tune", FineTuneView.as_view()),
]