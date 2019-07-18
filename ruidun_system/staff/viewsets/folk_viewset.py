from lib.model_viewset import ModelViewSet
import django_filters as filters
from ..models import Folk
from ..serializers.folk_serializer import FolkSerializer



class FolkFilter(filters.FilterSet):
    create_time = filters.DateTimeFilter(field_name="create_time", lookup_expr='gte')
    update_time = filters.DateTimeFilter(field_name="update_time", lookup_expr='lte')
    staff_name = filters.CharFilter(field_name="staff_id", lookup_expr="name")

    class Meta:
        model = Folk
        fields = ["create_time", "update_time", "staff_name", "name"]


class FolkViewset(ModelViewSet):
    """人员家属信息"""
    queryset = Folk.objects.all()
    serializer_class = FolkSerializer
    filterset_class = FolkFilter