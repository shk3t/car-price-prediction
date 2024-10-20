from rest_framework import serializers

from predict.models import CarEntry


class CarEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEntry
        fields = "__all__"
