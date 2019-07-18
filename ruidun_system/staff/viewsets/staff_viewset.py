from lib import model_viewset
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from staff.models import Staff
from staff.serializers.staff_serializer import StaffSerializer
# from lib.user_permission import get_user_permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd
import os


#人员查询
class StaffFilter(filters.FilterSet):
    '''可以根据入职时间，公司名称等来过滤'''
    time__gt = filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    time__lt = filters.DateTimeFilter(field_name="time", lookup_expr='lte')
    # company_name = filters.CharFilter(field_name="company_id", lookup_expr='name')
    # department_name = filters.CharFilter(field_name="department_id", lookup_expr="name")
    # group_number = filters.CharFilter(field_name="group_id", lookup_expr="name")
    job_station_name = filters.CharFilter(field_name="job_station_id", lookup_expr="name")
    part_name = filters.CharFilter(field_name="part_id", lookup_expr="name")

    class Meta:
        model = Staff
        fields = ["time__gt", "time__lt", "company", "department_id", "group_number", "job_station_name","part_name", "state", "name", "part_id"]


class StaffViewSet(model_viewset.ModelViewSet):
    queryset = Staff.objects.filter(is_used=1).all().order_by('-time')
    serializer_class = StaffSerializer
    filterset_class = StaffFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("id", "age")

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = dict(request.data)

        data = {key:value[0] for key, value in data.items()}
        # print(data)
        # print(len(data.get("id_card_photo")))
        if len(data.get("id_card_photo")) == 4:

            del data["id_card_photo"]
        if len(data.get("card_photo")) == 4:
            del data["card_photo"]
        # print(data)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_used = 0
        instance.status = 2
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["GET"], detail=False)
    def staff_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")
            value = self.queryset.filter(id__in=id_list).values("name", 'sex', 'age', "birth_place", "address", "phone",
                                                                "id_card", "medical_history", "department_id__department",
                                                                "job_station_id__name", "group_number", "company")
            array = [list(array.values()) for array in value]
            for i in range(len(array)):
                if str(array[i][1]) == '1':
                    array[i][1] = "男"
                else:
                    array[i][1] = "女"
            excel = pd.DataFrame(np.array(array), columns=["姓名", "性别", "年龄", "出生地", "地址", "手机号", "身份证", "病史", "部门"
                                                          , "职位", "施工组", "公司"])
            filepath = "media/xlsx/staff.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)

    @action(methods=["GET"], detail=False)
    def get_staffs(self, request):
        name = request.query_params.get("name")
        if name:
            query = self.queryset.filter(name__contains=name)

        else:
            query = self.queryset

        data = map(lambda obj: {"id": obj.pk, "name": "%s(%s/%s)" % (obj.name, obj.department.department, obj.department.group_name) if obj.department else obj.name}, query)
        return Response(data=data, status=200)

    # def create(self, request, *args, **kwargs):
    #     data_ori = request.data  # 获取原始数据
    #     id_card_photo = data_ori.get("id_card_photo")  # 取出去除身份证照片和证件照
    #     card_photo = data_ori.get("card_photo")
    #     if id_card_photo:
    #         del data_ori["id_card_photo"]
    #     if card_photo:
    #         del data_ori["card_photo"]
    #
    #     serializer = self.get_serializer(data=data_ori)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = serializer.data
    #
    #     staff_id = self.staff_id
    #     instance = Staff.objects.get(pk=staff_id)
    #     # 保存照片
    #     if id_card_photo:
    #         # 传过来了base64格式的图片，内容为dataimage/jpeg;base64,/9j/4QAY的形式，，后边为内容，所以要进行预处理。
    #         # 获取内容和文件格式
    #         end, id_card_photo = id_card_photo.split(",")
    #         # 获取文件据图格式
    #         end = end.split("/")[-1].rstrip(";")
    #         path_id_card_photo = "static/images/%s_id_card_photo.%s" % (uuid.uuid4(), end)
    #         with open(path_id_card_photo, "wb") as f:
    #             f.write(base64.b64decode(id_card_photo.encode()))
    #             instance.id_card_photo = path_id_card_photo
    #     if card_photo:
    #         end, card_photo = card_photo.split(",")
    #         # 获取文件据图格式
    #         end = end.split("/")[-1].rstrip(";")
    #         path_card_photo = "static/images/%s_card_photo.%s" % (uuid.uuid4(), end)
    #         with open(path_card_photo, "wb") as f:
    #             f.write(base64.b64decode(card_photo.encode()))
    #             instance.card_photo = path_card_photo
    #     instance.save()
    #
    #     # data.update({"id_card_photo": path_id_card_photo, "card_photo": path_card_photo})
    #     return Response(data=self.get_serializer(instance).data, status=status.HTTP_201_CREATED)

    # 下面自定义两个方法
    # @action(methods=['PUT'], detail=True)
    # def update_id_card_photo(self, request, pk):
    #     obj = self.get_object()
    #     file = request.data.get('id_card_photo')
    #     if not file:
    #         return Response(data={"msg":"参数错误"}, status=status.HTTP_400_BAD_REQUEST)
    #     path_id_card_photo = "static/images/%s_id_card_photo.jpg" % obj.pk
    #     with open(path_id_card_photo, "wb") as f:
    #         for data in file.chunks():
    #             f.write(data)
    #         obj.id_card_photo = path_id_card_photo
    #         obj.save()
    #     serializer = self.get_serializer(obj)
    #     return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
    #
    # @action(methods=['PUT'], detail=True)
    # def update_card_photo(self, request, pk):
    #     obj = self.get_object()
    #     file = request.data.get('card_photo')
    #     if not file:
    #         return Response(data={"msg": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
    #     path_card_photo = "static/images/%s_card_photo.jpg" % obj.pk
    #     with open(path_card_photo, "wb") as f:
    #         for data in file.chunks():
    #             f.write(data)
    #         obj.card_photo = path_card_photo
    #         obj.save()
    #     serializer = self.get_serializer(obj)
    #     return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)

    # @action(methods=['POST'], detail=False)
    # def up_id_card_photo(self, request):
    #     # obj = self.get_object()
    #     file = request.data.get('id_card_photo')
    #     if not file:
    #         return Response(data={"msg": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
    #     path_id_card_photo = "static/images/%s_id_card_photo.jpg" % time.time()
    #     with open(path_id_card_photo, "wb") as f:
    #         for data in file.chunks():
    #             f.write(data)
    #         obj.id_card_photo = path_id_card_photo
    #         obj.save()
    #     serializer = self.get_serializer(obj)
    #     return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
    #
    # @action(methods=['POST'], detail=False)
    # def update_card_photo(self, request, pk):
    #     obj = self.get_object()
    #     file = request.data.get('card_photo')
    #     if not file:
    #         return Response(data={"msg": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
    #     path_card_photo = "static/images/%s_card_photo.jpg" % obj.pk
    #     with open(path_card_photo, "wb") as f:
    #         for data in file.chunks():
    #             f.write(data)
    #         obj.card_photo = path_card_photo
    #         obj.save()
    #     serializer = self.get_serializer(obj)
    #     return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)


    # permission_classes = [SelfPermission]

    # def get_queryset(self):
    #     company = self.request.query_params.get("company", None)
    #     department_id = self.request.query_params.get("department_id", None)
    #     group_id = self.request.query_params.get("group_id", None)
    #     job_station_id = self.request.query_params.get("job_station_id", None)
    #     name = self.request.query_params.get("name", None)
    #     conditions = {}  # 查询的条件
    #     if company:
    #         conditions["company"] = company
    #     # if department_id:
    #     #     conditions["department_id"] = department_id
    #     # if group_id:
    #     #     conditions["group_id"] = group_id
    #     # if job_station_id:
    #     #     conditions["job_station_id"] = job_station_id
    #     if name:
    #         conditions['name'] = name
    #
    #     queryset = Staff.objects.filter(**conditions).all()
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     # request = get_user_permissions(request)
    #     # print(request.permissions)
    #     # print(request.user.id)
    #     return super().list(request, *args, **kwargs)