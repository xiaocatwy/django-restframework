from django.urls import path
from . import views

urlpatterns = [

]

from rest_framework import routers
from .viewsets.dangerused_viewset import DangerUsedViewset
from .viewsets.dangerouscategory_viewset import DangerousCategoryViewset
from .viewsets.dangername_viewset import DangerNameViewset
from .viewsets.priorscheme_viewset import PriorSchemeViewset
from .viewsets.specialscheme_viewset import SpecialSchemeViewset
from .viewsets.method_viewset import MethodViewset

# 危险品使用记录
router = routers.DefaultRouter()
router.register('dangeruseds', DangerUsedViewset, base_name='dangeruseds' )

urlpatterns += router.urls


# 危险品分类
router = routers.DefaultRouter()
router.register('dangerouscategorys', DangerousCategoryViewset, base_name='dangerouscategorys' )

urlpatterns += router.urls


# 危险品名称
router = routers.DefaultRouter()
router.register('dangernames', DangerNameViewset, base_name='dangernames' )

urlpatterns += router.urls


# 应急方案
router = routers.DefaultRouter()
router.register('priorschemes', PriorSchemeViewset, base_name='priorschemes' )

urlpatterns += router.urls


# 专项方案
router = routers.DefaultRouter()
router.register('specialschemes', SpecialSchemeViewset, base_name='specialschemes' )

urlpatterns += router.urls

router = routers.DefaultRouter()
router.register('method', MethodViewset , base_name='method' )

urlpatterns += router.urls