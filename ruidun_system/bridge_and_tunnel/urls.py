from django.urls import include, path
from . import views

urlpatterns = [
    path('bandtindex', views.bandtindex, name='bandtindex'),
]