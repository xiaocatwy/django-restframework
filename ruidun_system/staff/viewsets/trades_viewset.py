from lib.model_viewset import ModelViewSet

from ..models import Trades
from ..serializers.trades_serializer import TradesSerializer


class TradesViewset(ModelViewSet):
    """施工组信息"""

    queryset = Trades.objects.filter(is_used=1)
    serializer_class = TradesSerializer
    filter_fields = ('trades_name',)