from rest_framework import serializers

from internet_setting.models import CautionRecord


class CautionRecordSerializer(serializers.ModelSerializer):

    device = serializers.SlugRelatedField(slug_field="name", read_only=True)
    device_id = serializers.CharField()
    disposer_id = serializers.CharField()
    disposer = serializers.SlugRelatedField(slug_field="name", read_only=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = CautionRecord
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def get_category(self, obj):
        return obj.device.category.name

