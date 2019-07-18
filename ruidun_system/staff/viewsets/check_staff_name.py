from django.http import HttpResponse, JsonResponse

from staff.models import Staff
from staff.serializers.staff_serializer import StaffSerializer
from rest_framework.response import Response


def check_staff_name(request):
    # 检查人员是否存在
    if request.method == "GET":
        staff_name = request.GET.get('staff_name', None)
        if not staff_name:
            return JsonResponse(data={"detail": "请求参数错误"}, status=400)

        staffs = Staff.objects.filter(name=staff_name)
        count = staffs.count()
        data = {"count": count}
        # 如果没有找到
        if not count:
            data["message"] = "这个名字不存在"
        elif count == 1:
            data["message"] = "不存在重名现象"
            data["id"] = staffs.first().pk
        else:
            # 存在重名现象
            data["message"] = '存在重名现象'
            serializer = StaffSerializer(staffs.all(), many=True)
            data["staffs"] = serializer.data
            for s in data["staffs"]:
                del s["folks"]
            # print(data["staffs"])
        return JsonResponse(data=data, status=200)
    else:
        return JsonResponse(data={"detail": "请求方式错误"}, status=405)

    # if len(staffs) == 1:
    #     return HttpResponse(staff_names[0].id)
    #
    # elif len(staff_names) > 1:
    #     for name in staff_names:
    #         id_list.append(name.id)
    #         return HttpResponse(id_list)