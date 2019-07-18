from rest_framework import serializers

from auth_system.models import ExtraGroup


class ExtraGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraGroup
        fields = ["note", "index", "is_used"]
