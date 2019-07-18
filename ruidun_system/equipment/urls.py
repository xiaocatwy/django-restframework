urlpatterns = [

]

#车辆信息
from rest_framework import routers
from .viewsets.equipmentinfo_viewset import EquipmentInfoViewSet
router = routers.DefaultRouter()
router.register('equipmentinfos', EquipmentInfoViewSet, base_name='equipment')

urlpatterns += router.urls

# 使用信息
from .viewsets.equipmentuser_viewset import EquipmentUsedViewSet
router = routers.DefaultRouter()
router.register('equipmentuseds', EquipmentUsedViewSet, base_name='equipmentused')

urlpatterns += router.urls


# 保养信息
from .viewsets.equipmentupkeep_viewset import EquipmentUpkeepViewSet
router = routers.DefaultRouter()
router.register('equipmentupkeeps', EquipmentUpkeepViewSet, base_name='equipmentupkeep')

urlpatterns += router.urls


# 修理信息
from .viewsets.equipmentrepair_viewset import EquipmentRepairViewSet
router = routers.DefaultRouter()
router.register('equipmentrepairs', EquipmentRepairViewSet, base_name='equipmentrepair')

urlpatterns += router.urls


# 定位信息
from .viewsets.equipmentlocation_viewset import EquipmentLocationViewSet
router = routers.DefaultRouter()
router.register('equipmentlocations', EquipmentLocationViewSet, base_name='equipmentlocation')

urlpatterns += router.urls


