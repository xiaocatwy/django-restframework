import uuid
import calendar
from rest_framework import serializers

from staff.models import UserWork, Staff

import datetime

now_time =datetime.datetime.now().strftime("%Y-%m-%d")


class UserWorkSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='department', read_only=True)
    department_id = serializers.CharField(allow_null=True, required=False)
    daywork = serializers.SerializerMethodField()
    daytime = serializers.SerializerMethodField()
    department_group = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('id', 'name', 'department', 'department_group', "department_id", 'daywork', "daytime")
        extra_kwargs = {
                "id": {"required": False}
            }

    def get_daytime(self,obj):
        time = self.context["request"].query_params.get('time')
        if time:
            return time
        else:
            return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_daywork(self, obj):
        time = self.context["request"].query_params.get('time', now_time)
        if time:
            work = UserWork.objects.filter(time=time, staff_id=obj.id).values("work_time","detail",
                                                                       'enter_time', 'leave_time').order_by("-work_time")
            if work:
                for i in work:
                    if i["work_time"] >= 720000:
                        i["work_time"] = "正常"
                    elif 0 < i["work_time"] < 720000:
                        i["work_time"] = "缺工"
                    else:
                        i["work_time"] = "旷工"
                return work
            else:
                userwork = UserWork(id=uuid.uuid4(), time=time, sysid=obj.sysid, work_time=0, staff_id=obj.id, part_id=obj.part_id)
                userwork.save()
                work = UserWork.objects.filter(time=time, staff_id=obj.id).values("work_time", "detail",
                                                                          'enter_time', 'leave_time')
                for i in work:
                    i["work_time"] = "旷工"
                return work

    def get_department_group(self, obj):
        return obj.department.department+'/'+obj.department.group_name
    #
    # def get_department_id(self, obj):
    #     return obj.staff.department.id

    def validate_staff_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        validated_data["id"] = uuid.uuid4()  # 添加一个唯一的UUID为主键
        return UserWork.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 因为有可能没有传过来，所以用字典.get() 方法
        instance.time = validated_data.get("time", instance.time)
        instance.work_time = validated_data.get("work_time", instance.work_time)
        instance.detail = validated_data.get("detail", instance.detail)
        instance.enter_time = validated_data.get("enter_time", instance.enter_time)
        instance.leave_time = validated_data.get("leave_time", instance.leave_time)
        instance.save()
        return instance