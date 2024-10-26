from rest_framework import serializers

from predict.models import CarInfo


class CarEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = "__all__"