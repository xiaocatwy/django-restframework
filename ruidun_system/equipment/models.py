from django.db import models
from auth_system.models import Part
from db.base_model import TimeBaseModel, SortBaseModel
from staff.models import Company, Staff


class Model(SortBaseModel):
    """型号模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='型号编号')
    name = models.CharField(max_length=50, verbose_name="型号名称")

    class Meta:
        db_table = "tb_model"
        verbose_name = "型号信息"
        verbose_name_plural = verbose_name


# class ModelFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Model
#         fields = ['model_id', 'name']


class Factory( SortBaseModel):
    """厂家模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='厂家编号')
    name = models.CharField(max_length=50, verbose_name="厂家名称")

    class Meta:
        db_table = "tb_factory"
        verbose_name = "厂家信息"
        verbose_name_plural = verbose_name


# class FactoryFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Factory
#         fields = ['factory_id', 'name']


# 定义工程设备基础信息类EquipmentInfo
class EquipmentInfo(models.Model):
    id = models.CharField(max_length=50, verbose_name='工程车辆编号', primary_key=True)
    # number = models.CharField(max_length=50, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    factory = models.CharField(max_length=50, verbose_name='生产厂家', null=True)
    model = models.CharField(max_length=50, verbose_name='型号', null=True)
    # factory = models.ForeignKey(Factory, verbose_name='生产厂家', on_delete=models.PROTECT, null=True)
    # model = models.ForeignKey(Model, verbose_name='型号', on_delete=models.PROTECT, null=True, related_name="model")
    x_len = models.CharField(max_length=30, verbose_name="x轴", null=True)
    y_len = models.CharField(max_length=30, verbose_name="y轴", null=True)
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.PROTECT, null=True, related_name="equipmentinfo")
    company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT, null=True, related_name="company")
    bought_time = models.DateTimeField(verbose_name='购买时间', null=True)
    is_used = models.BooleanField(default=False, verbose_name='是否在用')
    mileage = models.FloatField(max_length=8, verbose_name='行驶里程', default=0)

    class Meta:
        db_table = 'tb_equipment_info'
        verbose_name = '生产设备基础信息'
        verbose_name_plural = verbose_name


# class EquipmentInfoFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = EquipmentInfo
#         fields = ['engineering_car_id', 'name', 'factory', 'model', 'company']


class EquipmentUsed(models.Model):
    """工程车辆使用记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='使用记录编号')
    equipment = models.ForeignKey(EquipmentInfo, verbose_name="工程车辆", on_delete=models.PROTECT)
    manager = models.ForeignKey(Staff, verbose_name="负责人", on_delete=models.PROTECT, related_name="equipment_manager")
    user = models.ForeignKey(Staff, verbose_name="使用人", on_delete=models.PROTECT, related_name="equipment_user")
    start_time = models.DateTimeField(verbose_name='使用时间')
    end_time = models.DateTimeField(verbose_name='归还时间', null=True)

    class Meta:
        db_table = "tb_equipment_used"
        verbose_name = "工程车辆使用记录"
        verbose_name_plural = verbose_name


# class EquipmentUsedFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = EquipmentUsed
#         fields = ['equipment', 'user', 'start_time']


class EquipmentRepair(models.Model):
    """工程车辆维修记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='维修记录编号')
    equipment = models.ForeignKey(EquipmentInfo, verbose_name="工程车辆", on_delete=models.PROTECT)
    manager = models.ForeignKey(Staff, verbose_name="负责人", on_delete=models.PROTECT)
    serviceman = models.CharField(max_length=50, verbose_name="维修人")
    time = models.DateTimeField(verbose_name='维修时间')

    class Meta:
        db_table = "tb_equipment_repair"
        verbose_name = "工程车辆维修记录"
        verbose_name_plural = verbose_name


# class EquipmentRepairFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = EquipmentRepair
#         fields = ['equipment', 'manager', 'time']


class EquipmentUpkeep(models.Model):
    """工程车辆保养记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='保养记录编号')
    equipment = models.ForeignKey(EquipmentInfo, verbose_name="工程车辆", on_delete=models.PROTECT)
    manager = models.ForeignKey(Staff, verbose_name="负责人", on_delete=models.PROTECT)
    upkeep_man = models.CharField(max_length=50, verbose_name="保养人")
    time = models.DateTimeField(verbose_name='保养时间')

    class Meta:
        db_table = "tb_equipment_upkeep"
        verbose_name = "工程车辆保养记录"
        verbose_name_plural = verbose_name


# class EquipmentUpkeepFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = EquipmentUpkeep
#         fields = ['equipment', 'manager', 'time']


# class EquipmentLocation(models.Model):
#     """工程车辆定位记录模型类"""
#     id = models.CharField(primary_key=True, max_length=50, verbose_name='保养记录编号')
#     equipment = models.ForeignKey(EquipmentInfo, verbose_name="工程车辆", on_delete=models.PROTECT)
#     location = models.CharField(max_length=50, verbose_name="位置")
#     time = models.DateTimeField(verbose_name='时间')
#
#     class Meta:
#         db_table = "tb_equipment_location"
#         verbose_name = "工程车辆定位记录"
#         verbose_name_plural = verbose_name

# 因为逻辑中不需要直接来查数据库里的位置信息，而是看转换过的地图形式，所以查询类先没写


class EquipmentLocationCard(models.Model):
    """定位卡模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='定位卡编号')
    # equipment = models.ForeignKey(Staff, verbose_name="工程车辆", on_delete=models.PROTECT, null=True)
    equipment = models.ForeignKey(EquipmentInfo, verbose_name="工程车辆", on_delete=models.PROTECT,
                                  related_name="equipment")
    status = models.IntegerField(verbose_name="状态")
    time = models.DateTimeField(verbose_name="发放时间")

    class Meta:
        db_table = "tb_equipment_location_card"
        verbose_name = "车辆定位卡"
        verbose_name_plural = verbose_name


class EquipmentLocation(models.Model):
    """工程车辆定位记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='保养记录编号')
    location_card = models.ForeignKey(EquipmentLocationCard, verbose_name="车辆定位卡", on_delete=models.PROTECT,
                                      related_name="location_card")
    location = models.CharField(max_length=50, verbose_name="位置")
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        db_table = "tb_equipment_location"
        verbose_name = "工程车辆定位记录"
        verbose_name_plural = verbose_name

# 因为逻辑中不需要直接来查数据库里的位置信息，而是看转换过的地图形式，所以查询类先没写





# class EquipmentLocationCardFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = EquipmentLocationCard
#         fields = ['equipment', 'location_card_id']
