"""base_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from .viewsets import company_viewset, staff_viewset, check_staff_name

router = routers.DefaultRouter()
router.register('companies', company_viewset.CompanyViewSet, base_name="companies")

urlpatterns = [path('check_staff_name/',  check_staff_name.check_staff_name)]  # 人名
urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('staffs', staff_viewset.StaffViewSet, base_name="staffs")
urlpatterns += router.urls

# 家属
from .viewsets.folk_viewset import FolkViewset
router = routers.DefaultRouter()
router.register('folks', FolkViewset, base_name='folk')

urlpatterns += router.urls

# 部门
from .viewsets.department_viewset import DepartmentViewset
router = routers.DefaultRouter()
router.register('departments', DepartmentViewset, base_name='departments')

urlpatterns += router.urls

# 岗位
from .viewsets.jobstation_viewset import JobStationViewset
router = routers.DefaultRouter()
router.register('jobstations', JobStationViewset, base_name='jobstations')

urlpatterns += router.urls

# 项目
from .viewsets.project_viewset import ProjectViewset
router = routers.DefaultRouter()
router.register('projects', ProjectViewset, base_name='projects')

urlpatterns += router.urls

# 工区
from .viewsets.part_viewset import PartViewset
router = routers.DefaultRouter()
router.register('parts', PartViewset, base_name='part')

urlpatterns += router.urls


# 施工组
from .viewsets.team_viewset import TeamViewset
router = routers.DefaultRouter()
router.register('teams', TeamViewset, base_name='team')

urlpatterns += router.urls

# 班组考勤
from .viewsets.departmentwork_viewset import DepartmentworkViewset
router = routers.DefaultRouter()
router.register('departmentworks', DepartmentworkViewset, base_name='departmentWork')

urlpatterns += router.urls

# 个人考勤
from .viewsets.userwork_viewset import UserWorkViewset
router = routers.DefaultRouter()
router.register('userworks', UserWorkViewset, base_name='userwork')

urlpatterns += router.urls


# 月个人考勤
from .viewsets.usermouthwork_viewset import UserMouthWorkViewset
router = routers.DefaultRouter()
router.register('usermouthworks', UserMouthWorkViewset, base_name='usermouthwork')

urlpatterns += router.urls

# 月考勤详情
from .viewsets.usermouthwork_detail_viewset import UserMouthWorkDetailViewset
router = routers.DefaultRouter()
router.register('usermouthworkdetails', UserMouthWorkDetailViewset, base_name='usermouthworkdetails')

urlpatterns += router.urls


# 工种
from .viewsets.trades_viewset import TradesViewset
router = routers.DefaultRouter()
router.register('trades', TradesViewset, base_name='trades')

urlpatterns += router.urls


# 部门（登录用户）
from .viewsets.user_departement_viewset import UserDepartementViewset
router = routers.DefaultRouter()
router.register('userdepartements', UserDepartementViewset, base_name='userdepartements')

urlpatterns += router.urls