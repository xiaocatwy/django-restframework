import datetime
import uuid

from rest_framework import serializers
from staff.models import UserWork
from staff.models import Department


class DepartmentworkSerializer(serializers.ModelSerializer):
    department_group = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    fact = serializers.SerializerMethodField()
    real = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()


    class Meta:
        model = Department
        fields = "__all__"
        extra_kwargs = {
            "id": {"required": False}
        }

    def get_department_group(self, obj):
        return obj.department+'/'+obj.group_name

    def get_time(self, obj):
        yes_time = (datetime.datetime.now() + datetime.timedelta()).strftime("%Y-%m-%d")
        time = self.context["request"].query_params.get("time", yes_time)
        return time

    def get_fact(self, obj):
        return obj.staff.count()

    def get_real(self, obj):
        yes_time = (datetime.datetime.now()+datetime.timedelta()).strftime("%Y-%m-%d")
        time = self.context["request"].query_params.get("time", yes_time)
        ids = obj.staff.all().values("id")
        lists = [i["id"] for i in ids]
        real = UserWork.objects.filter(time=time, staff_id__in=lists, work_time__gt=0).count()
        return real

    def get_rate(self, obj):
        if self.get_fact(obj) == 0:
            return "0.0%"
        else:
            return str((self.get_real(obj)/self.get_fact(obj))*100)[0:5]+"%"

    def validate_department_id(self, value):
        if Department.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value


