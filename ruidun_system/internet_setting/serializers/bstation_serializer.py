from rest_framework import serializers
from internet_setting.models import BsTation


class BsTaionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BsTation
        fields = '__all__'

