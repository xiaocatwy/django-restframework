from django.contrib.auth.models import Group
from rest_framework import serializers

from auth_system.models import User, Part, Project
from auth_system.serializers import GroupSerializer


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=False)  # 确认密码
    parts_up = serializers.ListField(write_only=True)
    groups_up = serializers.ListField(write_only=True)
    projects = serializers.SerializerMethodField()
    # groups = serializers.SerializerMethodField()
    staff_id = serializers.CharField(label='账号使用人')
    staff = serializers.SlugRelatedField(slug_field="name", read_only=True)
    company = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "password2", "projects", "groups", "parts_up", "groups_up", "is_active", 'company', 'staff', 'department', 'staff_id']
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"max_length": 18,
                         "min_length": 6,
                         "write_only": True,
                         "required": False},
            "username": {"required": False},
            "staff_id": {"required": False}
        }

    def get_company(self, obj):
        if obj.staff:
            return obj.staff.company

    def get_department(self, obj):
        if obj.staff:
            return obj.staff.department.department + obj.staff.department.group_name

    def get_groups(self, obj):
        groups = obj.groups.all()
        return map(lambda g:{"id": g.pk, "name": g.name}, groups)

    def get_projects(self, obj):
        parts = obj.parts.all()
        projects = map(lambda p: p.project, parts)  #根据工区得到项目
        projects = list(set(projects))  # 得到去重的列表
        return map(lambda pj: {"id": pj.id, "name": pj.name, "parts": map(lambda p: {"id":p.id, "name":p.name,}, set(pj.parts.all()) & set(parts))}, projects)  # 通过两个集合的交集得到当前项目下可以操作的工区

    def validate_username(self, value):
        # 判断账号名是否存在
        if User.objects.filter(username=value).count():
            raise serializers.ValidationError("该账号已存在")
        else:
            return value

    def validate_staff_id(self, value):
        # 判断该员工是否有账号
        if User.objects.filter(staff_id = value).count():
            raise serializers.ValidationError("该员工已经有账号")
        else:
            return value

    def validate_parts_up(self, value):
        # 校验工区id是否合法
        # value = set(eval(value))
        value = set(value)
        ori_part_ids = set([p.pk for p in Part.objects.all()])
        if value <= ori_part_ids:  # 判断集合是否是另一个的子集
            return value
        else:
            raise serializers.ValidationError("id列表中有不存在的工区id")

    def validate_groups_up(self, value):
        # 校验工区id是否合法
        # value = set(eval(value))
        value = set(value)
        ori_group_ids = set([p.pk for p in Group.objects.all()])
        if value <= ori_group_ids:
            return value
        else:
            raise serializers.ValidationError("id列表中有不存在的角色id")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        print(password, password2)
        if password != password2:  # 防止为空
            raise serializers.ValidationError("两次密码不一致")
        return attrs

    def create(self, validated_data):
        del validated_data["password2"]
        groups = validated_data.pop("groups_up")
        parts = validated_data.pop("parts_up")
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        if parts:
            # validated_data['default_part_id'] = list(parts)[0]
            user.default_part_id = list(parts)[0]
        if groups:
            user.default_group_id = list(groups)[0]
        user.save()
        user.parts.set(parts)
        user.groups.set(groups)
        user.save()

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(user)
        # token = jwt_encode_handler(payload)
        # user.token = token

        return user

    def update(self, instance, validated_data):
        username = validated_data.get("username")
        if username:
            instance.username = username
        groups = validated_data.get("groups_up")
        if groups:
            instance.groups.set(groups)
        parts = validated_data.get("parts_up")
        if parts:
            instance.parts.set(parts)
        staff_id = validated_data.get("staff_id")
        if staff_id:
            instance.staff_id = staff_id
        instance.save()

        return instance