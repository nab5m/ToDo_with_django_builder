from rest_framework import viewsets, permissions

from . import serializers
from . import models


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the Account class"""

    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
