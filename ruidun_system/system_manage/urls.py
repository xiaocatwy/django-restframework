from django.urls import include, path
from rest_framework import routers
from .viewsets import group_permission_viewset, user_viewset, artificial_log_viewset, artificial_log_category_viewset

urlpatterns = []

# 角色权限相关
router = routers.DefaultRouter()
router.register('group_permission', group_permission_viewset.GroupPermissionViewSet, base_name="group_permission")

urlpatterns += router.urls

# 用户相关
router = routers.DefaultRouter()
router.register('user_permission', user_viewset.UserPermissionViewSet, base_name="user_permission")

urlpatterns += router.urls

# 日志相关
router = routers.DefaultRouter()
router.register('artificial_log', artificial_log_viewset.ArtificialLogViewSet, base_name="artificial_log")

urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('artificial_log_category', artificial_log_category_viewset.ArtificialLogCategoryViewSet, base_name="artificial_log_category")

urlpatterns += router.urls
