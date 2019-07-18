import django_filters
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from lib.model_viewset import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from staff.models import Team, Staff, Part, Department
from work_area.serializers.staffstatus_serializer import StaffSerializer


# def filter_group_id(request):
#     # 判断group_id是否属于当前工区
#
#     # 1.取出当前工区的id和department_id
#     part_id = request.GET.get('part_id', '0')
#     department_id = request.GET.get('department_id')
#
#     # 2.查询当前工区下的班组
#     departments = Department.objects.filter(part_id=part_id)
#
#     # if not group_id:
#     #     group_id = teams[0].id
#
#     # 3.判断传入的部门/班组id是否在2中
#     department = departments.filter(id=department_id)
#
#     if len(department) == 0:
#         raise serializers.ValidationError("当前工区下无此班组")
#         # return Response({'error':'当前工区下无此班组'}, status=status.HTTP_400_BAD_REQUEST)
#
#     return department


# class StaffStatusFilter(django_filters.FilterSet):
#     # 工区人员状态过滤器
#     # department_id = django_filters.ModelChoiceFilter(queryset=filter_group_id)
#
#     class Meta:
#         model = Staff
#         fields = ['part_id', 'department_id']


class StaffStatusViewset(ModelViewSet):
    """工区人员状态"""

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # filterset_class = StaffStatusFilter
    filter_fields = ('part_id', 'department_id')
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('time',)


# class StaffStatusAPIView(GenericAPIView):
#
#     def get(self, request, pk=None):
#         s_dict = {"team_name":[], 'staff':[]}
#
#         # 查出工区对应的班组信息
#         # 传过来工区ID时，把1替换成工区ID即可
#         tems = Team.objects.filter(part__id=2)
#
#         # 对查询集再进行过滤，查询当前工区下的全部/单个班组
#         if pk == None:
#             tems = tems.filter(is_used=True)
#         else:
#             # 不是本工区下的班组，传入pk值查出来的tems为空
#             tems = tems.filter(pk=pk, is_used=True)
#
#         for tem in tems:
#             s_dict['team_name'].append({
#                 'team_id': tem.id,
#                 'team_name': tem.name,
#                 'index': tem.index,
#             })
#
#         # 班组下的人员信息
#         # 不是本工区下的班组，（上方）传入pk值查出来的tems为空
#         if pk != None and len(tems) == 0:
#             return Response(s_dict)
#
#         elif pk == None and len(tems) >= 1:
#             pk = tems[0].id
#
#         # 查询当前班组下的人员
#         staffstaus = Staff.objects.filter(group__id=pk)
#
#         for staffstau in staffstaus:
#             s_dict['staff'].append({
#                 'staff_name': staffstau.name,
#                 'phone': staffstau.phone,
#                 'medical_history': staffstau.medical_history
#             })
#
#         return Response(s_dict)
