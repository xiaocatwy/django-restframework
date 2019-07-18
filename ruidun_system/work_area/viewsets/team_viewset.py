from rest_framework import status
from rest_framework.response import Response
from lib.model_viewset import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from staff.models import Team, Staff
from work_area.serializers.team_serializer import TeamSerializer
from work_area.serializers.staffstatus_serializer import StaffSerializer


class TeamViewset(ModelViewSet):
    """施工班组"""

    # TODO 等待传入当前工区id
    # part_id = 2
    # queryset = Team.objects.filter(part__id=part_id)
    serializer_class = TeamSerializer
    # filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    # ordering_fields = ('name',)

    def get_queryset(self):
        part_id = self.request.query_params.get("part_id", self.request.user.default_part_id if self.request.user.default_part_id else "88888")
        return Team.objects.filter(part__id=part_id)

    def list(self, request, *args, **kwargs):
        # 过滤
        queryset = self.filter_queryset(self.get_queryset())
        # 分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data

            if not data:
                return Response({'error':'请求数据不存在'}, status=status.HTTP_400_BAD_REQUEST)

            group_id = data[0]['id']
            a = Staff.objects.filter(group_id=group_id)
            staff = StaffSerializer(a, many=True).data

            data[0]['staff'] = staff
            return self.get_paginated_response(data)
        # 序列化
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        if not data:
            return Response({'error': '请求数据不存在'}, status=status.HTTP_400_BAD_REQUEST)

        group_id = data[0]['id']
        a = Staff.objects.filter(group_id=group_id)
        staff = StaffSerializer(a, many=True).data

        data[0]['staff'] = staff

        return Response(data)