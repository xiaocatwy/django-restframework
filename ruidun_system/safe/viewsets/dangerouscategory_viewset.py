from lib.model_viewset import ModelViewSet
from ..models import DangerousCategory
from ..serializers.dangerouscategory_serializer import DangerousCategorySerializer


class DangerousCategoryViewset(ModelViewSet):
    """危险物品分类序列化器"""

    queryset = DangerousCategory.objects.filter(is_used=1)
    serializer_class = DangerousCategorySerializer