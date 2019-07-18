import base64
import uuid

import os
from rest_framework import serializers

from staff.models import Staff, Department, JobStation, Part, Company, Team


class StaffSerializer(serializers.ModelSerializer):

    # 指定外键同时显示id和name，name只序列化的时候使用，id为反序列化时使用，可以不用传
    # 如果外键仅仅是主键就不用下面的了
    # department = serializers.SlugRelatedField(slug_field='department', read_only=True)
    department_id = serializers.CharField(allow_null=True, required=False)
    department = serializers.SerializerMethodField()
    job_station = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # group = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    trade_id = serializers.CharField(allow_null=True, required=False)
    trade = serializers.SlugRelatedField(slug_field='trades_name', read_only=True)
    # company = serializers.SlugRelatedField(slug_field='name', read_only=True)
    job_station_id = serializers.CharField(allow_null=True, required=False)
    # group_id = serializers.CharField(allow_null=True, required=False)
    part_id = serializers.CharField(allow_null=True, required=False)
    # company_id = serializers.CharField(allow_null=True, required=False)
    # id_card_photo = serializers.CharField(allow_null=True, required=False)
    # card_photo = serializers.CharField(allow_null=True, required=False)
    # folks = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},  # 主键系统生成，不需要传
            "job_number": {"required": False},
            "id_organ": {"read_only": True},
            "company": {"read_only": True},
            "sysid": {"read_only": True},
            "id_card_photo": {"required": False},
            "card_photo": {"required": False},
            "id_card":{
                "max_length":18,
                "min_length": 18,
            },
            "group_number": {"read_only": True},
            "time": {"read_only": True},
        }

    #家属信息问题(多个家属如何展示和修改 1.另写家属界面)
    # def get_folks(self, obj):
    #     folks = obj.folk.all()
    #     return map(lambda f: [{"id": f.id, "name": f.name, 'phone': f.phone, "address": f.address}], folks)
    #
    # def validate_id_card_photo(self, value):
    #     if value:
    #         end = value.name.split(".")[-1]
    #         path_id_card_photo = "static/images/%s_id_card_photo.%s" % (uuid.uuid4(), end)
    #         with open(path_id_card_photo, "wb") as f:
    #             for data in value.chunks():
    #                 f.write(data)
    #             value = path_id_card_photo
    #     return value
    #
    # def validate_card_photo(self, value):
    #     if value:
    #         end = value.name.split(".")[-1]
    #         path_card_photo = "static/images/%s_card_photo.%s" % (uuid.uuid4(), end)
    #         with open(path_card_photo, "wb") as f:
    #             for data in value.chunks():
    #                 f.write(data)
    #             value = path_card_photo
    #             print(value)
    #     return value

    def get_department(self, obj):
        department_id = obj.department_id
        department = Department.objects.get(id=department_id)
        return department.department + '/' + department.group_name

    # 关于外键的需要单独验证,因为外键字段指定两个序列化字段会出现问题
    def validate_department_id(self, value):
        if Department.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_job_station_id(self, value):
        if JobStation.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    # def validate_group_id(self, value):
    #     if Team.objects.filter(pk=value).count() == 0:
    #         raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
    #     return value

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_company_id(self, value):
        if Company.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        # validated_data["id"] = uuid.uuid4()  # 添加一个唯一的UUID为主键
        return Staff.objects.create(**validated_data)

    # def destory(self, validated_data):
    #     return Staff.o

    def update(self, instance, validated_data):
        # 因为有可能没有传过来，所以用字典.get() 方法
        instance.id = validated_data.get("id", instance.id)
        instance.job_number = validated_data.get("job_number", instance.job_number)
        instance.trade_id = validated_data.get("trade_id", instance.trade_id)
        instance.name = validated_data.get("name", instance.name)
        instance.sex = validated_data.get("sex", instance.sex)
        instance.age = validated_data.get("age", instance.age)
        instance.birth_place = validated_data.get("birth_place", instance.birth_place)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.id_card = validated_data.get("id_card", instance.id_card)
        instance.department_id = validated_data.get("department_id", instance.department_id)
        instance.job_station_id = validated_data.get("job_station_id", instance.job_station_id)
        # instance.group_id = validated_data.get("group_id", instance.group_id)
        instance.part_id = validated_data.get("part_id", instance.part_id)
        instance.company = validated_data.get("company", instance.company)
        instance.group_number = validated_data.get("group_number", instance.group_number)
        instance.time = validated_data.get("time", instance.time)

        # 如果图片更新，删除之前的文件，保存为现在的路径
        card_photo = validated_data.get("card_photo")
        if card_photo:
            os.remove(instance.card_photo.path)
            instance.card_photo = card_photo

        id_card_photo = validated_data.get("id_card_photo")
        if id_card_photo:
            os.remove(instance.id_card_photo.path)
            instance.id_card_photo = id_card_photo

        instance.medical_history = validated_data.get("medical_history", instance.medical_history)
        instance.state = validated_data.get("state", instance.state)
        instance.note = validated_data.get("note", instance.note)
        instance.time = validated_data.get("time", instance.time)
        instance.status = validated_data.get("status", instance.status)

        instance.save()
        return instance


