from lib.model_viewset import ModelViewSet

from auth_system.models import User_Department
from ..serializers.user_department_serializer import UserDepartementSerializer


class UserDepartementViewset(ModelViewSet):
    """施工组信息"""

    queryset = User_Department.objects.filter(is_used=1)
    serializer_class = UserDepartementSerializer