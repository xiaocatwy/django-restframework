from django.db import models

# Create your models here.
from auth_system.models import Part
from db.base_model import TimeBaseModel, SortBaseModel
from staff.models import Staff


class DangerousCategory(TimeBaseModel, SortBaseModel):
    """危险品分类模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='危险品分类编号')
    name = models.CharField(max_length=50, verbose_name="名称")

    class Meta:
        db_table = "tb_dangerous_category"
        verbose_name = "危险品分类信息"
        verbose_name_plural = verbose_name


# class DangerousCategoryFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = DangerousCategory
#         fields = ['name']


class Danger(TimeBaseModel, SortBaseModel):
    """危险品模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='危险品编号')
    category = models.ForeignKey(DangerousCategory, verbose_name="分类", on_delete=models.PROTECT)
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name="名称")
    count = models.IntegerField(verbose_name="数量")

    class Meta:
        db_table = "tb_danger"
        verbose_name = "危险品信息"
        verbose_name_plural = verbose_name


# class DangerFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Danger
#         fields = ['name', 'category']


class DangerUsed(TimeBaseModel):
    """危险品使用记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='使用记录编号')
    danger = models.ForeignKey(Danger, verbose_name="危险品", on_delete=models.PROTECT)
    count = models.IntegerField(verbose_name="数量")
    manager = models.ForeignKey(Staff, verbose_name="负责人", on_delete=models.PROTECT, related_name="danger_manager", null=True)
    user = models.ForeignKey(Staff, verbose_name="使用人", on_delete=models.PROTECT, related_name="danger_user", null=True)
    is_need_back = models.BooleanField(default=False, verbose_name="是否需要归还")
    is_back = models.BooleanField(default=False, verbose_name="是否归还")
    start_time = models.DateTimeField(verbose_name='使用时间')
    end_time = models.DateTimeField(verbose_name='归还时间', null=True)

    class Meta:
        db_table = "tb_danger_used"
        verbose_name = "危险品使用记录"
        verbose_name_plural = verbose_name


# class DangerUsedFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = DangerUsed
#         fields = ['danger', 'user']


class SpecialScheme(SortBaseModel):
    """专项方案模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='专项方案编号')
    staff = models.ForeignKey(Staff, verbose_name="提交人", on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name="名称")
    path = models.FileField(verbose_name="路径",  upload_to='texts/specialscheme')
    download_times = models.IntegerField(verbose_name="下载次数", default=0)
    reate_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = "tb_special_scheme"
        verbose_name = "专项方案"
        verbose_name_plural = verbose_name


# class SpecialSchemeFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = SpecialScheme
#         fields = ['staff', 'name']


class PriorScheme(SortBaseModel):
    """应急方案模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='应急方案编号')
    staff = models.ForeignKey(Staff, verbose_name="提交人", on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name="名称")
    path = models.FileField(verbose_name="路径", upload_to='texts/priorscheme')
    download_times = models.IntegerField(verbose_name="下载次数", default=0)
    reate_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = "tb_prior_scheme"
        verbose_name = "专项方案"
        verbose_name_plural = verbose_name


# class PriorSchemeFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = PriorScheme
#         fields = ['staff', 'name']


class Problem(models.Model):
    """反馈问题模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='问题编号')
    people = models.CharField(max_length=50, verbose_name="报告人")
    phone = models.CharField(max_length=50, verbose_name="联系方式")
    describe = models.TextField(verbose_name="问题描述")
    status = models.IntegerField(verbose_name="状态", default=0)
    time = models.DateTimeField(verbose_name="时间")

    class Meta:
        db_table = "tb_problem"
        verbose_name = "反馈问题"
        verbose_name_plural = verbose_name


# class ProblemFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Problem
#         fields = []


class Method(models.Model):

    id = models.CharField(primary_key=True, max_length=50, verbose_name='应急方案id')
    name= models.CharField(max_length=100, verbose_name='方案名称')
    people = models.CharField(max_length=50, verbose_name="制定人")
    phone = models.CharField(max_length=50, verbose_name="联系方式")
    time = models.DateField(verbose_name="制定时间")
    use_message = models.BooleanField(verbose_name="是否使用短信")
    message_content = models.CharField(max_length=100, null=True, blank=True, verbose_name="短信内容")
    set_light = models.IntegerField(verbose_name="设置警灯开启模式")
    set_ling = models.IntegerField(verbose_name="设置静铃开启模式")
    set_voice = models.IntegerField(verbose_name="设置应急广播开启模式")

    class Meta:
        db_table = "tb_method"
        verbose_name = "应急演练"
        verbose_name_plural = verbose_name
