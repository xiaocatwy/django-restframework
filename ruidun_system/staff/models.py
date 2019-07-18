# from django.contrib.auth.models import User
from django.db import models

from auth_system.models import Part, Company
from db.base_model import TimeBaseModel, SortBaseModel

#
# class Company(SortBaseModel):
#     """单位模型类"""
#     id = models.CharField(primary_key=True, max_length=50, verbose_name='单位编号')
#     name = models.CharField(max_length=50, verbose_name="单位名称")
#
#     class Meta:
#         db_table = 'tb_company'
#         verbose_name = "单位信息"
#         verbose_name_plural = verbose_name
#
#
# class Project(SortBaseModel):
#     """项目模型类"""
#     id = models.CharField(primary_key=True, max_length=50, verbose_name='项目编号')
#     name = models.CharField(max_length=50, verbose_name="项目名称")
#     company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'tb_project'
#         verbose_name = "项目信息"
#         verbose_name_plural = verbose_name
#
#
# class Part(SortBaseModel):
#     """工区模型类"""
#     id = models.CharField(primary_key=True, max_length=50, verbose_name='工区编号')
#     name = models.CharField(max_length=50, verbose_name="工区名称")
#     project = models.ForeignKey(Project, verbose_name='所属项目', on_delete=models.PROTECT)
#     users = models.ManyToManyField(User, related_name="parts", blank=True)
#
#     class Meta:
#         db_table = 'tb_part'
#         verbose_name = "工区信息"
#         verbose_name_plural = verbose_name
#


class Department(SortBaseModel):
    """班组模型类(工地工人)"""
    # id = models.CharField(primary_key=True, max_length=50, verbose_name='部门编号')
    id = models.IntegerField(primary_key=True, verbose_name='部门/班组id')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID', null=True, blank=True)
    # number = models.IntegerField(verbose_name='部门/班组id')
    department = models.CharField(max_length=200, verbose_name='部门', default='默认部门', null=True, blank=True)
    group_name = models.CharField(max_length=200, verbose_name='班组')
    remarks = models.CharField(max_length=800, verbose_name='备注', null=True, blank=True)
    update_status = models.IntegerField(null=True, blank=True)
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)
    staff_id = models.CharField(max_length=50, verbose_name='班组负责人', null=True, blank=True)
    status = models.IntegerField(verbose_name='操作（增1、删2、改3）', null=True, blank=True)
    # name = models.CharField(max_length=50, verbose_name="部门名称")

    class Meta:
        db_table = 'tb_department'
        verbose_name = "班组信息"
        verbose_name_plural = verbose_name


class JobStation(SortBaseModel):
    """岗位模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='岗位编号')
    name = models.CharField(max_length=50, verbose_name="岗位名称")

    class Meta:
        db_table = 'tb_job_station'
        verbose_name = "岗位信息"
        verbose_name_plural = verbose_name


# 工种问题
class Trades(SortBaseModel):
    """工种模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='工种编号')
    trades_name = models.CharField(max_length=50, verbose_name="工种名称")
    colour = models.CharField(max_length=20, verbose_name="工种颜色")

    class Meta:
        db_table = 'tb_trade'
        verbose_name = "工种信息"
        verbose_name_plural = verbose_name


class Team(SortBaseModel):
    """施工班组模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='施工班组编号')
    name = models.CharField(max_length=50, verbose_name="施工班组名称")
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'tb_team'
        verbose_name = "施工班组信息"
        verbose_name_plural = verbose_name


class Staff(models.Model):
    """人员模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='员工卡号')
    job_number = models.CharField(max_length=20, verbose_name='工号')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    department = models.ForeignKey(Department, verbose_name='部门', on_delete=models.PROTECT, null=True, blank=True, related_name="staff")
    job_station = models.ForeignKey(JobStation, verbose_name='岗位', on_delete=models.PROTECT, null=True, blank=True)
    trade = models.ForeignKey(Trades, verbose_name='工种', on_delete=models.PROTECT, null=True, blank=True)
    # group = models.ForeignKey(Team, verbose_name='施工班组', on_delete=models.PROTECT, null=True, blank=True)
    # company = models.ForeignKey(Company, verbose_name='单位', on_delete=models.PROTECT, null=True, blank=True)
    id_organ = models.CharField(max_length=300, null=True, blank=True, verbose_name='发证机关')
    company = models.CharField(max_length=200, null=True, blank=True, verbose_name='单位名称')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)
    # part_id = models.CharField(max_length=20, verbose_name='工区id')
    group_number = models.IntegerField(null=True, blank=True, verbose_name='班组')
    # group_number = models.ForeignKey(Department, verbose_name='施工班组', on_delete=models.PROTECT, null=True, blank=True, related_name='group_number')
    name = models.CharField(max_length=50, verbose_name='姓名')
    sex = models.CharField(verbose_name='性别', max_length=5, null=True)
    age = models.IntegerField( verbose_name="年龄", null=True)
    birth_place = models.CharField(max_length=50, verbose_name="籍贯", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="详细地址", null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name="手机号", null=True)
    id_card = models.CharField(max_length=18, verbose_name="身份证号", null=True, blank=True)
    id_card_photo = models.ImageField(null=True, verbose_name="身份证照片", blank=True, upload_to="images/id_card_photo")
    card_photo = models.ImageField(null=True, verbose_name="证件照片", blank=True, upload_to="images/card_photo")
    # blood = models.CharField(max_length=10, null=True, verbose_name='血型')
    medical_history = models.CharField(max_length=50, null=True, verbose_name='既往病史', blank=True)
    state = models.BooleanField(default=True, verbose_name="在职状态", null=True)
    note = models.CharField(max_length=100, null=True, verbose_name='备注信息', blank=True)
    time = models.DateField(verbose_name="入职时间", null=True, blank=True, auto_now_add=True)
    is_used = models.SmallIntegerField(default=1, verbose_name="是否已经删除", null=True)
    status = models.IntegerField(verbose_name='操作（增1、删2、改3）', null=True, blank=True)
    the_id = models.IntegerField(null=True, blank=True)
    # car_number = models.CharField(max_length=13, verbose_name='定位卡/员工卡号')

    class Meta:
        db_table = 'tb_staff'
        verbose_name = "人员信息"
        verbose_name_plural = verbose_name
        # unique_together = ("sysid", "id")


class Folk(models.Model):
    """家属模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='家属编号')
    staff = models.ForeignKey(Staff, verbose_name="员工", on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name="姓名")
    phone = models.CharField(max_length=50, verbose_name="联系方式")
    address = models.CharField(max_length=50, verbose_name="联系地址")

    class Meta:
        verbose_name = "家属信息"
        verbose_name_plural = verbose_name


class UserWork(models.Model):
    """个人考勤日模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='个人考勤编号')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    time = models.DateField(verbose_name="个人考勤日期")
    # card_no = models.CharField(max_length=13)
    staff = models.ForeignKey(Staff, verbose_name="考勤人", on_delete=models.PROTECT, related_name='staff')
    work_time = models.IntegerField(null=True, verbose_name='工作时长')
    detail = models.CharField(max_length=100, null=True, verbose_name='备注信息')
    enter_time = models.DateTimeField(verbose_name='进入时间', null=True)
    leave_time = models.DateTimeField(verbose_name='离开时间', null=True)
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = 'tb_userworks'
        verbose_name = "个人考勤信息"
        verbose_name_plural = verbose_name

