from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from client.ipswitch import Client


class IPSwitchViewSet(ModelViewSet):
    """控制ip开关接口"""

    pass
