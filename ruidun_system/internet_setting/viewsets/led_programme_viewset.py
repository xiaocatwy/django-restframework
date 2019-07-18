from lib.model_viewset import ModelViewSet
import django_filters as filters
from ..models import LedProgramme
from internet_setting.serializers.led_programme_serializer import LedProgrammeSerializer


# class FolkFilter(filters.FilterSet):
#     create_time = filters.DateTimeFilter(field_name="create_time", lookup_expr='gte')
#     update_time = filters.DateTimeFilter(field_name="update_time", lookup_expr='lte')
#     staff_name = filters.CharFilter(field_name="staff_id", lookup_expr="name")
#
#     class Meta:
#         model = LedProgramme
#         fields = ["create_time", "update_time", "staff_name", "name"]


class LedProgrammeViewset(ModelViewSet):

    """LED节目信息"""
    queryset = LedProgramme.objects.all()
    serializer_class = LedProgrammeSerializer
    # filterset_class = FolkFilter