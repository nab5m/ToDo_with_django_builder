from rest_framework import serializers

from . import models


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = [
            "name",
            "completion",
            "created",
            "last_updated",
        ]
