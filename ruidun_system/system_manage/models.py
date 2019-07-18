import django_filters
from django.db import models

from auth_system.models import User
from db.base_model import SortBaseModel


class ArtificialLogCategory(SortBaseModel):
    name = models.CharField(max_length=100, verbose_name="人工日子分类名字")

    class Meta:
        db_table = "tb_artificial_log_category"
        verbose_name = "人工日志分类"
        verbose_name_plural = verbose_name


class ArtificialLog(models.Model):
    """人工日志类"""
    id = models.CharField(max_length=50, verbose_name="主键", primary_key=True)
    object = models.CharField(max_length=100, verbose_name="操作对象")
    user = models.CharField(verbose_name="作者", max_length=50)
    category = models.CharField(verbose_name="日志分类", max_length=50)
    time = models.DateTimeField(verbose_name="日志时间")
    # status = models.BooleanField(default=True, verbose_name="是否删除")
    # level = models.SmallIntegerField(verbose_name="日志等级")

    class Meta:
        db_table = "tb_artificial_log"
        verbose_name = "人工日志"
        verbose_name_plural = verbose_name

