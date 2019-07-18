from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings

from auth_system.models import User, Part, Project, User_Department
from lib.model_viewset import ModelViewSet
from staff.models import Staff
from system_manage.serializers.password_serializer import PasswordSerializer
from system_manage.serializers.user_serializer import UserSerializer


class UserPermissionViewSet(ModelViewSet):
    """对角色基本信息及相关权限进行设置的视图"""

    queryset = User.objects.filter(is_active=1)
    serializer_class = UserSerializer

    # def get_serializer_class(self, request):
    #     # if self.request.method == "GET":
    #     return UserSerializer(context={"request":request})
    # def create(self, request, *args, **kwargs):
    #     pass

    @action(methods=["PUT"], detail=True)
    def change_password(self, request, pk):
        # 更改密码
        serializer = PasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        password = serializer.data.get("password")
        user = self.get_object()
        user.set_password(password)
        user.save()
        return Response(data={"message": "修改成功"}, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = 0
        user.save()
        return Response(data={"message": "删除成功"}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["PUT"], detail=True)
    def change_defaultgroup(self, request, pk):
        user = self.get_object()
        group_id = request.data.get('group_id')

        if Group.objects.filter(id=group_id).count():
            user.default_group_id = group_id

        user.save()
        return Response(data={"default_group_id": user.default_group_id }, status=status.HTTP_205_RESET_CONTENT)

    @action(methods=["PUT"], detail=True)
    def change_defaultpart(self, request, pk):
        user = self.get_object()
        part_id = request.data.get('part_id')

        if Part.objects.filter(id=part_id).count():
            user.default_part_id = part_id

        user.save()
        return Response(data={"default_part_id": user.default_part_id }, status=status.HTTP_205_RESET_CONTENT)

    @action(methods=["PUT"], detail=True)
    def change_staff(self, request, pk):
        # 给用户设置员工
        user = self.get_object()
        staff_id = request.data.get('staff_id')

        if Staff.objects.filter(id=staff_id).count():
            user.staff_id = staff_id

        user.save()
        return Response(data={"staff_id": user.staff_id}, status=status.HTTP_205_RESET_CONTENT)

    @action(methods=["PUT"], detail=True)
    def change_user_department(self, request, pk):
        # 给用户设置部门
        user = self.get_object()
        user_department_id = request.data.get('user_department_id')

        if User_Department.objects.filter(id=user_department_id).count():
            user.department_id = user_department_id

        user.save()
        return Response(data={"user_department_id": user.department_id}, status=status.HTTP_205_RESET_CONTENT)

    @action(methods=["GET"], detail=False)
    def get_groups(self, request):
        # 获取所有的选择的角色
        groups = Group.objects.all()
        data = map(lambda g: {"id": g.id, "name": g.name}, groups)
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def get_parts(self, request):
        # 返回所有可以选择的工区
        projects = Project.objects.all()
        data = map(lambda p: {"id": p.id, "name": p.name, "parts": map(lambda pt: {"id": pt.id, "name": pt.name}, p.parts.all())}, projects)
        return Response(data=data, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     # 获取序列化器
    #     serializer = self.get_serializer(data=request.data)
    #     # 验证
    #     if not serializer.is_valid():
    #         s = serializer.errors
    #         k = list(s)[:-1]
    #         s['errno'] = s.pop(k[0])
    #         print(s)
    #         return Response(s, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # 保存
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}