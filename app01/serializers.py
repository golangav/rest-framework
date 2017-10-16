
from rest_framework import serializers
from app01 import models


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = (
            "id",
            "name",
            "address"
        )
