from lib.model_viewset import ModelViewSet

from ..models import JobStation
from ..serializers.jobstation_serializer import JobStationSerializer


class JobStationViewset(ModelViewSet):
    """岗位信息"""
    queryset = JobStation.objects.filter(is_used=1)
    serializer_class = JobStationSerializer