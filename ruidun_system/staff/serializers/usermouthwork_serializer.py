import calendar
import datetime
import uuid
import datetime
from django.db.models import Q
from rest_framework import serializers

from staff.models import UserWork, Staff

now_time =datetime.datetime.now().strftime("%Y-%m")

class UserMouthWorkSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='department', read_only=True)
    department_id = serializers.CharField(allow_null=True, required=False)
    mouthwork = serializers.SerializerMethodField()
    mouth = serializers.SerializerMethodField()
    department_group = serializers.SerializerMethodField()
    class Meta:
        model = Staff
        fields = ('id', 'name', 'department', "department_id", "department_group", 'mouthwork', "mouth")
        extra_kwargs = {
            "id": {"required": False}
        }

    def get_department_group(self, obj):
        return obj.department.department+'/'+obj.department.group_name

    def get_mouth(self,obj):
        mouth = self.context["request"].query_params.get('time_limit',now_time)
        return mouth

    def get_mouthwork(self, obj):
        # 获取想要的月份(格式为2019-01)
        time_limit = self.context["request"].query_params.get('time_limit')
        if time_limit:
            year, month = [int(a) for a in time_limit.split("-")]
            # 得出该年这个月份的第一天是周几和共多少天(monthrange)
            weekday, monthrange = calendar.monthrange(year, month)
            time_gt = datetime.date(year=year, month=month, day=1)
            time_lt = datetime.date(year=year, month=month, day=monthrange)
            # 将一个月天数的个数用0填到一个列表
            day_list = [0]*monthrange
            # 取出考勤为正常的日期对应的号
            list_1 = (str(u['time'])[8:10] for u in UserWork.objects.filter(staff_id=obj.id).filter(time__gte=time_gt, time__lte=time_lt, work_time__gte=720000).all().order_by("time").values("time"))
            a = 0
            for i in list_1:
                a+=1
                day_list[int(i)-1] = 1
            # 取出考勤不正常的日期对应的号
            list_1 = (str(u['time'])[8:10] for u in UserWork.objects.filter(staff_id=obj.id).filter(time__gte=time_gt, time__lte=time_lt, work_time__gt=0, work_time__lte=720000).all().order_by("time").values("time"))
            for i in list_1:
                day_list[int(i) - 1] = 2
            return day_list, str(a/len(day_list)*100)[0:4]+"%"
        else:
            date = datetime.datetime.now()
            year, month = [date.year, date.month]
            weekday, monthrange = calendar.monthrange(year, month)
            time_gt = datetime.date(year=year, month=month, day=1)
            time_lt = datetime.date(year=year, month=month, day=monthrange)
            day_list = [0]*monthrange
            list_1 = (str(u['time'])[8:10] for u in UserWork.objects.filter(staff_id=obj.id).filter(time__gte=time_gt, time__lte=time_lt, work_time__gte=720000).all().order_by("time").values("time"))
            a = 0
            for i in list_1:
                a += 1
                day_list[int(i)-1] = 1
            list_1 = (str(u['time'])[8:10] for u in UserWork.objects.filter(staff_id=obj.id).filter(time__gte=time_gt, time__lte=time_lt, work_time__lte=720000, work_time__gt=0).all().order_by("time").values("time"))
            for i in list_1:
                day_list[int(i) - 1] = 2
            return day_list, str(a/len(day_list)*100)[0:4]+"%"