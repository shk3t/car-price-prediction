from rest_framework import serializers

from predict.models import CarInfo


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = "__all__"

    # def prepare_for_prediction(self) -> dict:
    #     if "transmission_speed" in self.data:
    #         self.data["transmission_speed"] = self.data["transmission_speed"] and None
    #     return self.data

    # def prepare_as_response(self) -> dict:
    #     self.data["recommended_price_rub"] -= self.data["recommended_price_rub"] % 1000
    #     self.data["interior_color"] = self.data["interior_color"] or None
    #     self.data["accident"] = self.data["accident"] or None
    #     return self.data