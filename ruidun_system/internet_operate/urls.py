from django.urls import include, path
from . import viewsets

urlpatterns = [
    path('internetindex', viewsets.internetindex, name='internetindex'),
]