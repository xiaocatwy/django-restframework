import uuid
import calendar
from rest_framework import serializers

from staff.models import UserWork, Staff

import datetime

now_time =datetime.datetime.now().strftime("%Y-%m-%d")


class UserMouthWorkDetailSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='department', read_only=True)
    department_id = serializers.CharField(allow_null=True, required=False)
    daywork = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('id', 'name', 'department', "department_id", 'daywork')
        extra_kwargs = {
                "id": {"required": False}
            }

    def get_daywork(self, obj):
        mouth = self.context["request"].query_params.get('mouth')
        if mouth:
            year, month = [int(a) for a in mouth.split("-")]
            # 得出该年这个月份的第一天是周几和共多少天(monthrange)
            weekday, monthrange = calendar.monthrange(year, month)
            time_gt = datetime.date(year=year, month=month, day=1)
            time_lt = datetime.date(year=year, month=month, day=monthrange)
            work = UserWork.objects.filter(staff_id=obj.id, time__gte=time_gt, time__lte=time_lt).values("id", "time", "work_time", "detail",'enter_time', 'leave_time').order_by("time")
            for i in work:
                if i["work_time"] >= 720000:
                    i["work_time"] = "正常"
                elif 0 < i["work_time"] < 720000:
                    i["work_time"] = "缺工"
                else:
                    i["work_time"] = "旷工"
            return work

    def get_department(self, obj):
        return obj.staff.department.department

    def get_department_id(self, obj):
        return obj.staff.department.id

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