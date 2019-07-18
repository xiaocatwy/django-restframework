from rest_framework import serializers

from system_manage.models import ArtificialLogCategory


class ArtificialLogCategorySerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField()
    permission_ids = serializers.ListField(write_only=True)

    class Meta:
        model = ArtificialLogCategory
        fields = "__all__"
