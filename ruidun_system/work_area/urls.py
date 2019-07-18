from django.urls import path, re_path

from work_area.viewsets.staff_location import StaffLocationViewSet
from .viewsets.open_carbreak_view import OpenCarbreak
from .viewsets.open_staffbreak_view import OpenStaffbreak
# from .viewsets.staffstatus_viewset import StaffStatusAPIView

urlpatterns = [
    # path('staffstatus/', StaffStatusAPIView.as_view()),  # 工区人员状态
    # re_path(r'staffstatus/(?P<pk>\d+)/$', StaffStatusAPIView.as_view()),
    path("open_carbreak/", OpenCarbreak.as_view()),  # 开启车辆道闸
    path("open_staffbreak/", OpenStaffbreak.as_view())  # 开启人员道闸
]

from rest_framework import routers
from .viewsets.carrecord_viewset import CarRecordViewset
from .viewsets.carbreak_viewset import CarBreakViewset
from .viewsets.staffrecord_viewset import StaffRecordViewset
from .viewsets.staffbreak_viewset import StaffBreakViewset
from .viewsets.team_viewset import TeamViewset
from .viewsets.staffstatus_viewset import StaffStatusViewset
from .viewsets.deviceinfo_viewset import DeviceInfoViewset
from .viewsets.department_viewset import DepartmentViewset

# 车辆通行记录
router = routers.DefaultRouter()
router.register('carrecords', CarRecordViewset, base_name='carrecords' )

urlpatterns += router.urls


# 车辆道闸
router = routers.DefaultRouter()
router.register('carbreaks', CarBreakViewset, base_name='carbreaks' )

urlpatterns += router.urls


# 人员通行记录
router = routers.DefaultRouter()
router.register('staffrecords', StaffRecordViewset, base_name='staffrecords' )

urlpatterns += router.urls


# 人员道闸
router = routers.DefaultRouter()
router.register('staffbreaks', StaffBreakViewset, base_name='staffbreaks' )

urlpatterns += router.urls


# 工区下的施工班组(加班组下的第一组人员信息)
router = routers.DefaultRouter()
router.register('teams', TeamViewset, base_name='teams' )

urlpatterns += router.urls


# 工区人员状态(当前工区施工班组下的人员)
router = routers.DefaultRouter()
router.register('staffstatus', StaffStatusViewset, base_name='staffstatus' )

urlpatterns += router.urls

#
# # 工区设备信息
# router = routers.DefaultRouter()
# router.register('deviceinfos', DeviceInfoViewset, base_name='deviceinfos' )
#
# urlpatterns += router.urls


# 工区下的部门/班组
router = routers.DefaultRouter()
router.register('departments', DepartmentViewset, base_name='departments' )

urlpatterns += router.urls


# 人员定位信息
router = routers.DefaultRouter()
router.register('stafflocations', StaffLocationViewSet, base_name='stafflocations' )

urlpatterns += router.urls


