from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from predict.serializers import CarEntrySerializer
from predict.services import model_manager
import pandas as pd


class PredictView(APIView):
    def post(self, request: Request):
        serializer = CarEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input_data = pd.DataFrame([serializer.data])
        prepared_input_data = model_manager.prepare_data(input_data)
        result = model_manager.predict(prepared_input_data)

        return Response({"price_rub": result[0]})
