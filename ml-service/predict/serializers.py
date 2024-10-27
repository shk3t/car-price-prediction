from rest_framework import serializers

from predict.models import CarInfo


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = "__all__"