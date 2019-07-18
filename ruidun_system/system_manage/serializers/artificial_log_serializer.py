import uuid

from rest_framework import serializers

from auth_system.models import User
from system_manage.models import ArtificialLog, ArtificialLogCategory


class ArtificialLogSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    # user_id = serializers.CharField(read_only=True)
    # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # category_id = serializers.CharField()

    class Meta:
        model = ArtificialLog
        fields = "__all__"
        # exclude = ["status", 'level']
        extra_kwargs = {
            "id": {"read_only": True},
        }
    #
    # def validate_category_id(self, value):
    #     if ArtificialLogCategory.objects.filter(pk=value).count() == 0:
    #         raise serializers.ValidationError("无效的分类id")
    #     return value
    #
    # def create(self, validated_data):
    #     user = self.context["request"].user
    #     # 日志的用户id和等级都由系统自己生成
    #     validated_data["level"] = user.log_level
    #     validated_data["user"] = user.pk
    #     return ArtificialLog.objects.create(pk=uuid.uuid4(), **validated_data)