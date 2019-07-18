from lib.model_viewset import ModelViewSet

from ..models import Team
from ..serializers.team_serializer import TeamSerializer


class TeamViewset(ModelViewSet):
    """施工组信息"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer