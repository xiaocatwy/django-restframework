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
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import settings
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

def red(request):
    # 默认进去主页
    return redirect("static/index.html")

def demo(request):
    # 海康web
    return redirect("static/demo/index.html")

urlpatterns = [
    path('', red),
    path('haikang', demo),
    # path('^$', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),

    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('crud/', include('crudbuilder.urls')),

    # path('home', views.home, name='home'),
    path('staff/', include('staff.urls'), name='staff'),
    path('work_area/', include('work_area.urls'), name='work_area'),
    # path('bridge_and_tunnel/', include('bridge_and_tunnel.urls'), name='bridge_and_tunnel'),
    path('equipment/', include('equipment.urls'), name='equipment'),
    path('safe/', include('safe.urls'), name='safe'),
    # path('internet_operate/', include('internet_operate.urls'), name='internet_operate'),
    path('internet_setting/', include('internet_setting.urls'), name='internet_setting'),
    path('system_manage/', include('system_manage.urls'), name='system_manage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)