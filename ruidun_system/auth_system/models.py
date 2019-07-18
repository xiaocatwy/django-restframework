from django.db import models
from django.contrib.auth.models import Group, AbstractUser

# Create your models here.


class ContentTypeCat(models.Model):
    '''
    菜单类别表
    '''
    name = models.CharField("名称", max_length=50)
    icon = models.CharField("图标名", max_length=50)
    order_by = models.IntegerField("排序", default=0)

    is_active = models.BooleanField("是否有效", default=True)
    has_sub = models.BooleanField("是否有二级菜单", default=True)
    path = models.CharField("无二级菜单使重定向路径", null=True, max_length=50)

    class Meta:
        ordering = ["order_by"]
        verbose_name = "菜单类别"


class ContentTypeCatRel(models.Model):
    '''
    菜单分类明细表
    '''
    name = models.CharField("菜单名称", max_length=50)
    icon = models.CharField("图标名", max_length=50)
    order_by = models.IntegerField("排序", default=0)
    is_active = models.BooleanField("是否有效", default=True)
    content_type = models.ForeignKey(
        "contenttypes.ContentType", related_name="content_type_cat_rel", verbose_name="资源类型", on_delete=models.CASCADE)
    content_type_cat = models.ForeignKey(
        "ContentTypeCat", verbose_name="所属类别", on_delete=models.CASCADE)

    front_path = models.CharField(
        "前端路径", max_length=60, null=True, blank=True)
    front_redirect = models.CharField(
        "前端重定向路径", max_length=60, null=True, blank=True)
    front_component = models.CharField(
        "前端component", max_length=60, null=True, blank=True)

    class Meta:
        ordering = ["order_by"]
        verbose_name = "菜单分类明细表"

    def __str__(self):
        return self.name


# class CustomGroup(Group):
#     '''
#     定制django group对象
#     '''
#     class Meta:
#         proxy = True
#
#     def get_content_types(self):
#         """
#         获取当前group可操作的资源
#         """
#         return map(lambda perm: perm.content_type, self.permissions.all())
#
#     def get_content_type_cat_rels(self):
#         """
#         获取当前组可以操作的content_type_cat_rels
#         """
#
#         content_type_cat_rels = map(
#             lambda ct: ct.content_type_cat_rel, self.get_content_types())
#         return content_type_cat_rels
#
#     def get_content_type_cats(self):
#         """
#         获取当前组可以操作的content_type_cat
#         """
#
#         content_type_cats = map(
#             lambda ctcr: ctcr.content_type_cat, self.get_content_type_cat_rels())
#         return content_type_cats


class SortBaseModel(models.Model):
    """模型抽象基类"""

    index = models.IntegerField(verbose_name='排序', default=0)
    is_used = models.IntegerField(verbose_name='是否启用', default=True)
    # is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True


class Company(SortBaseModel):
    """单位模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='单位编号')
    name = models.CharField(max_length=50, verbose_name="单位名称", null=True)
    boss_name = models.CharField(max_length=30, verbose_name="老板姓名", null=True)
    phone_num = models.CharField(max_length=30, verbose_name="联系方式", null=True)
    company_address = models.CharField(max_length=100, verbose_name="单位地址", null=True)

    class Meta:
        db_table = 'tb_company'
        verbose_name = "单位信息"
        verbose_name_plural = verbose_name


class Project(SortBaseModel):
    """项目模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='项目编号')
    name = models.CharField(max_length=50, verbose_name="项目名称")
    company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT)
    manager = models.CharField(max_length=30, verbose_name="项目负责人", null=True)
    manager_phone = models.CharField(max_length=30, verbose_name="项目负责人联系方式", null=True)

    class Meta:
        db_table = 'tb_project'
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name


class Part(SortBaseModel):
    """工区模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='工区编号')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="工区名称")
    project = models.ForeignKey(Project, verbose_name='所属项目', on_delete=models.PROTECT, related_name="parts", null=True)
    manager = models.CharField(max_length=30, verbose_name="工区负责人", null=True)
    manager_phone = models.CharField(max_length=30, verbose_name="工区负责人联系方式", null=True)
    map_path = models.FileField(verbose_name="地图路径",  upload_to='maps', null=True)
    status = models.IntegerField(verbose_name='工区0、桥隧1', null=True, blank=True)

    class Meta:
        db_table = 'tb_part'
        verbose_name = "工区信息"
        verbose_name_plural = verbose_name


# class Sysid(SortBaseModel):
#     """工区下系统id"""
#     id = models.CharField(primary_key=True, max_length=50)
#     sysid = models.CharField(max_length=50, verbose_name='原系统ID')
#     part = models.ForeignKey(Part, verbose_name='所属工区', on_delete=models.PROTECT, related_name="sysids")
#
#     class Meta:
#         db_table = 'tb_sysid'
#         verbose_name = "工区下系统id"
#         verbose_name_plural = verbose_name


class ExtraGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="extra_group")
    note = models.CharField(max_length=200, verbose_name="备注", null=True, blank=True)
    is_used = models.SmallIntegerField(default=1, verbose_name="是否启用")
    index = models.IntegerField(default=1, verbose_name="排序")

    class Meta:
        db_table = 'auth_extra_group'
        verbose_name = "用户组额外信息"
        verbose_name_plural = verbose_name


class User_Department(SortBaseModel):
    """部门（登录用户所属部门）"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='部门id')
    name = models.CharField(max_length=50, verbose_name="部门名称")

    class Meta:
        db_table = 'tb_user_department'
        verbose_name = "登录用户班组信息"
        verbose_name_plural = verbose_name


from staff.models import Staff


class User(AbstractUser):
    parts = models.ManyToManyField(Part, related_name="users", blank=True)
    default_part = models.ForeignKey(Part, verbose_name="默认选择工区", on_delete=models.CASCADE, null=True)
    default_group = models.ForeignKey(Group, verbose_name="默认选择用户组", on_delete=models.CASCADE, null=True, related_name="default_user")
    # department = models.ForeignKey(User_Department, verbose_name="用户所属部门", on_delete=models.CASCADE, null=True, related_name="department")
    # log_level = models.SmallIntegerField(default=0, verbose_name="可查阅日志等级权限")
    staff = models.OneToOneField(Staff, verbose_name="使用者", on_delete=models.SET_NULL, null=True, blank=True, related_name="user")
    # default_group = models.ForeignKey(Group, verbose_name="默认用户组", on_delete=models.CASCADE, null=True)

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'

