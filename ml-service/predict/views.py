from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from predict.serializers import CarInfoSerializer
from predict.services import model_manager
from core import env
import pandas as pd


class PredictView(APIView):
    def post(self, request: Request):
        serializer = CarInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input_data = pd.DataFrame([serializer.data])
        prepared_input_data = model_manager.prepare_data(input_data)
        result = model_manager.predict(prepared_input_data)

        recommended_price_rub = result[0] * env.USD_TO_RUB_EX_RATE
        recommended_price_rub -= recommended_price_rub % 1000

        return Response({"recommended_price_rub": recommended_price_rub})


class FineTuneView(APIView):
    def post(self, request: Request):
        serializer = CarInfoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        input_data = pd.DataFrame(serializer.data)
        prepared_input_data = model_manager.prepare_data(input_data)
        model_manager.fine_tune(prepared_input_data)

        serializer.save()
        return Response("OK")
