from django.db import models
from rest_framework.exceptions import ValidationError


class TimeBaseModel(models.Model):
    """模型抽象基类"""

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True


class SortBaseModel(models.Model):
    """模型抽象基类"""

    index = models.IntegerField(verbose_name='排序', default=0, null=True)
    is_used = models.IntegerField(verbose_name='是否启用', default=True, null=True)
    # is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True


# 自定义捕获异常
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)

    if response:
        s = response.data
        s['errno'] = s.pop(list(s)[0])
    # 在此处补充自定义的异常处理
    # if response is not None:
    #     view = context['view']
    #     if isinstance(exc, ValidationError):
    #         response.data['errno'] = exc

    return response
