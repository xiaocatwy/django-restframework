from lib.model_viewset import ModelViewSet
from system_manage.models import ArtificialLogCategory
from system_manage.serializers.artificial_log_category_serializer import ArtificialLogCategorySerializer


class ArtificialLogCategoryViewSet(ModelViewSet):
    """人工日志类视图"""

    serializer_class = ArtificialLogCategorySerializer
    queryset = ArtificialLogCategory.objects.filter(is_used=1).all()
