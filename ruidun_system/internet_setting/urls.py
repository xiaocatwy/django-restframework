from django.urls import include, path
from rest_framework import routers
from .viewsets import device_category_viewset, car_pass_viewset, caution_record_viewset, device_info_viewset, staff_pass_viewset, location_card_viewset, device_upkeep_viewset, staff_location_viewset, voice_server_viewset, voice_viewset, led_viewset, ipswitch_detail_viewset, ipswitch_viewset, monitor_viewset, music_viewset, bstaion_viewset, led_programme_viewset

router = routers.DefaultRouter()
router.register('device_categories', device_category_viewset.DeviceCategoryViewSet, base_name="device_categories")

urlpatterns = []
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('car_pass', car_pass_viewset.CarPassViewSet, base_name="car_pass")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('staff_pass', staff_pass_viewset.StaffPassViewSet, base_name="staff_pass")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('device_info', device_info_viewset.DeviceInfoViewSet, base_name="device_info")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('caution_record', caution_record_viewset.CautionRecordViewSet, base_name="caution_record")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('location_card', location_card_viewset.LocationCardViewSet, base_name="location_card")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('device_upkeep', device_upkeep_viewset.DeviceUpkeepViewSet, base_name="device_upkeep")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('staff_location', staff_location_viewset.StaffLocationViewSet, base_name="staff_location")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('voice_server', voice_server_viewset.VoiceServerViewSet, base_name="voice_server")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('voice', voice_viewset.VoiceViewSet, base_name="voice")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('led', led_viewset.LEDInfoViewSet, base_name="led")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('monitor', monitor_viewset.MonitorInfoViewSet, base_name="monitor")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('ipswitch_detail', ipswitch_detail_viewset.IPSwitchDetailViewSet, base_name="ipswitch_detail")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('ipswitch', ipswitch_viewset.IPSwitchViewSet, base_name="ipswitch")
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('music', music_viewset.MusicViewSet, base_name="music")
urlpatterns += router.urls

# 定位基站
router = routers.DefaultRouter()
router.register('bstaions', bstaion_viewset.BsTaionViewSet, base_name="bstaions")
urlpatterns += router.urls

# led节目
router = routers.DefaultRouter()
router.register('ledprogramme', led_programme_viewset.LedProgrammeViewset, base_name="ledprogramme")
urlpatterns += router.urls