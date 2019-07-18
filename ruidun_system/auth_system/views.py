# from django.contrib.auth.models import Group
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import viewsets, status
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
#
# from .models import User, Part
#
#
# class DeforChangeViewset(GenericAPIView):
#     """修改默认组和工区"""
#
#     def post(self, request):
#         user_id = request.data.get('user_id')
#         group_id = request.data.get('group_id')
#         part_id = request.data.get('part_id')
#
#         try:
#             user = User.objects.get(id=user_id)
#         except Exception as e:
#             return Response({'error': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if Part.objects.filter(id=part_id).count():
#             user.default_part_id = part_id
#
#         if Group.objects.filter(id=group_id).count():
#             user.default_group_id = group_id
#
#         user.save()
#
#         user_dict = dict()
#         user_dict['default_group_id'] = user.default_group_id
#         user_dict['default_part_id'] = user.default_part_id
#
#         return Response(user_dict, status=status.HTTP_400_BAD_REQUEST)
#
