from django.urls import path

from predict.views import PredictView

urlpatterns = [
    path("predict", PredictView.as_view()),
]