from rest_framework import serializers
from staff.models import Team


class TeamSerializer(serializers.ModelSerializer):
    """班组序列化器"""
    staff_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'staff_set')

