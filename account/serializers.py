from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = [
            "last_updated",
            "created",
        ]
