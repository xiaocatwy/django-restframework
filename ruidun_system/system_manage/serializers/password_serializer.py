from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    origin_password = serializers.CharField(required=False)
    password = serializers.CharField(min_length=6, max_length=18)
    password2 = serializers.CharField(min_length=6, max_length=18)  # 确认密码

    class Meta:
        fields = ["password", 'password2']

    def validate_origin_password(self, value):
        user = self.context["request"].user
        if user.is_superuser:
            # 如果是超级管理员，可以更改其他人的密码
            return value
        if not user.check_password(value):
            raise serializers.ValidationError("原密码不正确")
        return value

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:  # 防止为空
            raise serializers.ValidationError("两次密码不一致")
        return attrs
