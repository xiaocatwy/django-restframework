from django.db import models

# Create your models here.
from auth_system.models import Part
from db.base_model import TimeBaseModel, SortBaseModel
from equipment.models import Factory, Model
from staff.models import Company, Staff
from work_area.models import CarInfo


class DeviceCategory(SortBaseModel):
    id = models.CharField(max_length=50, verbose_name='安全设备分类', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称')

    class Meta:
        db_table = 'tb_device_category'
        verbose_name = '安全设备分类'
        verbose_name_plural = verbose_name


class IPSwitch(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ip = models.CharField(max_length=50, verbose_name="远程电源ip")
    port = models.CharField(max_length=10, verbose_name="远程电源端口")
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    note = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True, blank=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True, blank=True)

    class Meta:
        db_table = 'tb_ip_switch'
        verbose_name = 'ip开关'
        verbose_name_plural = verbose_name


class IPSwitchDetail(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    number = models.CharField(max_length=50, verbose_name="开关号")
    ipswitch = models.ForeignKey(IPSwitch, on_delete=models.CASCADE, verbose_name="所属开关", related_name="detail")
    content = models.CharField(max_length=100, verbose_name="开关控制内容")
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField(max_length=500, verbose_name="备注", null=True)

    class Meta:
        db_table = 'tb_ip_switch_detail'
        verbose_name = 'ip开关'
        verbose_name_plural = verbose_name


class VoiceServer(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ip = models.CharField(max_length=50, verbose_name="音响服务器ip")
    port = models.CharField(max_length=10, verbose_name="音响服务器端口")
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='名称')
    note = models.CharField(max_length=50, verbose_name="备注", null=True)

    class Meta:
        db_table = 'tb_voice_server'
        verbose_name = '音响服务器'
        verbose_name_plural = verbose_name


class Voice(models.Model):
    id = models.CharField(max_length=50, verbose_name='音箱序列号', primary_key=True)
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    # number = models.CharField(max_length=50, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    factory = models.CharField(verbose_name='生产厂家', null=True, max_length=50, blank=True)
    model = models.CharField(verbose_name='型号', null=True, max_length=50, blank=True)
    # company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT, null=True)
    # manager = models.ForeignKey(Staff, verbose_name='负责人', on_delete=models.PROTECT, null=True)
    # category = models.ForeignKey(DeviceCategory, verbose_name='所属分类', on_delete=models.PROTECT, null=True)
    time = models.DateField(verbose_name='安装时间', null=True, blank=True)
    # location = models.CharField(max_length=50, verbose_name="位置")
    x = models.CharField(max_length=20, verbose_name="x位置", null=True, blank=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True, blank=True)
    note = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='是否损坏')
    is_used = models.BooleanField(default=True, verbose_name='是否在用')
    server = models.ForeignKey(VoiceServer, verbose_name="所属音响服务器", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'tb_voice'
        verbose_name = '音响设备信息'
        verbose_name_plural = verbose_name


class Music(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    note = models.CharField(max_length=100, verbose_name="播放音频的备注信息", null=True, blank=True)
    path = models.FileField(verbose_name="音频文件", upload_to="music")
    is_used = models.BooleanField(verbose_name="是否使用", default=True)

    class Meta:
        db_table = 'tb_music'
        verbose_name = '音频文件'
        verbose_name_plural = verbose_name


class LEDInfo(models.Model):
    id = models.CharField(max_length=50, verbose_name='设备id', primary_key=True)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    area_name = models.CharField(max_length=20, verbose_name='区域名称')
    nScreenNo = models.IntegerField(verbose_name='屏幕号')
    pScreenName = models.CharField(max_length=150, null=True, blank=True, verbose_name='屏幕名称')
    nWidth = models.IntegerField(verbose_name='LED屏宽度')
    nHeight = models.IntegerField(verbose_name='LED屏高度')
    nScreenType = models.IntegerField(verbose_name='屏幕类型')
    nPixelMode = models.IntegerField(verbose_name='像素模式')
    # number = models.CharField(max_length=50, verbose_name='编号')
    # name = models.CharField(max_length=50, verbose_name='名称')
    factory = models.CharField(verbose_name='生产厂家', null=True, max_length=50, blank=True)
    model = models.CharField(verbose_name='型号', null=True, max_length=50, blank=True)
    # company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT, null=True)
    # manager = models.ForeignKey(Staff, verbose_name='负责人', on_delete=models.PROTECT, null=True)
    time = models.DateField(verbose_name='安装时间', null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True, blank=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True, blank=True)
    # location = models.CharField(max_length=50, verbose_name="位置", null=True, blank=True)
    note = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='是否损坏', null=True)
    is_used = models.BooleanField(default=True, verbose_name='是否在用', null=True)
    # part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    ip = models.CharField(max_length=50, verbose_name="服务器ip", null=True)
    port = models.CharField(max_length=10, verbose_name="服务器端口", null=True)
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True, blank=True)

    class Meta:
        db_table = 'tb_led_info'
        verbose_name = 'led设备基础信息'
        verbose_name_plural = verbose_name


# led节目信息的处理
class LedProgramme(models.Model):
    id = models.CharField(max_length=50, verbose_name='节目id', primary_key=True)
    name = models.CharField(max_length=50, verbose_name="节目名字")
    w_x = models.IntegerField(verbose_name="显示区域的宽度")
    h_y = models.IntegerField(verbose_name="显示区域的高度")
    font_name = models.CharField(max_length=50, verbose_name="字体名字", default="宋体")
    font_size = models.IntegerField(verbose_name="字体大小")
    font_bold = models.IntegerField(verbose_name="字体粗细", default=1)
    x_align = models.IntegerField(verbose_name="水平居中显示", default=0)
    y_align = models.IntegerField(verbose_name="垂直居中显示", default=1)
    font_stunt = models.IntegerField(verbose_name="显示的特效")
    font_showtime = models.IntegerField(verbose_name="停留的时间")
    font_run = models.IntegerField(verbose_name="移动的速度")

    class Meta:
        db_table = 'tb_led_programme'
        verbose_name = 'led节目样式'
        verbose_name_plural = verbose_name
#
#
# # led功能的处理
# class LedWork(models.Model):
#     id = models.CharField(max_length=50, verbose_name='led工作内容', primary_key=True)
#     work_name = models.CharField(max_length=50, verbose_name="工作类型")
#
#     class Meta:
#         db_table = 'tb_led_work'
#         verbose_name = 'led的功能'
#         verbose_name_plural = verbose_name
#
#
# # led当前信息的二次处理
# class LedWorkStatus(models.Model):
#     id = models.CharField(max_length=50, verbose_name='led现在的状态的id', primary_key=True)
#     content = models.TextField(verbose_name='显示的内容', null=True)
#     led_work_name = models.CharField(max_length=50, verbose_name="工作类型")
#     led_programme = models.CharField(max_length=50, verbose_name="节目名字")
#
#     class Meta:
#         db_table = 'tb_led_work_status'
#         verbose_name = 'led的显示状态'
#         verbose_name_plural = verbose_name


class MonitorInfo(models.Model):
    id = models.CharField(max_length=50, verbose_name='设备id', primary_key=True)
    number = models.CharField(max_length=50, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    factory = models.CharField(verbose_name='生产厂家', null=True, max_length=50, blank=True)
    model = models.CharField(verbose_name='型号', null=True, max_length=50, blank=True)
    # company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT, null=True)
    # manager = models.ForeignKey(Staff, verbose_name='负责人', on_delete=models.PROTECT, null=True)
    time = models.DateField(verbose_name='安装时间', null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True, blank=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True, blank=True)
    note = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='是否损坏')
    is_used = models.BooleanField(default=True, verbose_name='是否在用')
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)
    ip = models.CharField(max_length=50, verbose_name="服务器ip")
    port = models.CharField(max_length=10, verbose_name="服务器端口")

    class Meta:
        db_table = 'tb_monitor_info'
        verbose_name = '监控设备基础信息'
        verbose_name_plural = verbose_name



class DeviceInfo(models.Model):
    id = models.CharField(max_length=50, verbose_name='设备id', primary_key=True)
    number = models.CharField(max_length=50, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称')
    factory = models.CharField(verbose_name='生产厂家', null=True, max_length=50, blank=True)
    model = models.CharField(verbose_name='型号', null=True, max_length=50, blank=True)
    # company = models.ForeignKey(Company, verbose_name='所属单位', on_delete=models.PROTECT, null=True)
    # manager = models.ForeignKey(Staff, verbose_name='负责人', on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(DeviceCategory, verbose_name='所属分类', on_delete=models.PROTECT, null=True)
    time = models.DateField(verbose_name='安装时间', null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True, blank=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True, blank=True)
    note = models.CharField(max_length=50, verbose_name="备注", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='是否损坏')
    is_used = models.BooleanField(default=True, verbose_name='是否在用')
    part = models.ForeignKey(Part, verbose_name="所属工区", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'tb_device_info'
        verbose_name = '安全设备基础信息'
        verbose_name_plural = verbose_name


class DeviceUpkeep(models.Model):
    """安全设备保养记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='保养记录编号')
    device = models.ForeignKey(DeviceInfo, verbose_name="安全设备", on_delete=models.PROTECT)
    manager = models.ForeignKey(Staff, verbose_name="负责人", on_delete=models.PROTECT)
    upkeep_man = models.CharField(max_length=50, verbose_name="维护人")
    time = models.DateTimeField(verbose_name='维护时间')

    class Meta:
        db_table = "tb_device_upkeep"
        verbose_name = "安全设备维护记录"
        verbose_name_plural = verbose_name


class CautionRecord(models.Model):
    """安全设备报警记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='报警记录编号')
    device = models.ForeignKey(DeviceInfo, verbose_name="安全设备", on_delete=models.PROTECT)
    content = models.CharField(max_length=200, verbose_name="报警内容", default=None)
    time = models.DateTimeField(verbose_name='报警时间')
    disposer = models.ForeignKey(Staff, verbose_name="处置人", on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name="是否被处理")

    class Meta:
        db_table = "tb_caution_record"
        verbose_name = "安全设备报警记录"
        verbose_name_plural = verbose_name


class CarPass(models.Model):
    """车辆通行证模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='通行证id')
    code = models.CharField(max_length=50, verbose_name='通行证编号')
    car = models.ForeignKey(CarInfo, verbose_name="车辆", on_delete=models.PROTECT, null=True)
    status = models.BooleanField(verbose_name="状态", default=False)
    time = models.DateTimeField(verbose_name="发放时间")
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "tb_car_pass"
        verbose_name = "车辆通行证"
        verbose_name_plural = verbose_name


class StaffPass(models.Model):
    """人员通行证模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='通行证id')
    code = models.CharField(max_length=50, verbose_name='通行证编号')
    staff = models.ForeignKey(Staff, verbose_name="员工", on_delete=models.PROTECT, null=True)
    status = models.BooleanField(verbose_name="状态", default=False)
    time = models.DateTimeField(verbose_name="发放时间")
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "tb_staff_pass"
        verbose_name = "人员通行证"
        verbose_name_plural = verbose_name


class LocationCard(models.Model):
    """定位卡模型类"""
    id = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    # id = models.IntegerField(verbose_name='原系统流水ID')
    # staff = models.ForeignKey(Staff, verbose_name="员工", on_delete=models.PROTECT)
    card_id = models.IntegerField(verbose_name='定位卡卡号')
    uuid = models.IntegerField(verbose_name='唯一id')
    utype = models.IntegerField(verbose_name='类型,0没有类型，1人员，2物品')
    status = models.IntegerField(verbose_name='状态：0未使用，1使用中，2报废', null=True, blank=True)
    comment = models.CharField(max_length=500, verbose_name='备注', null=True)
    # status = models.BooleanField(verbose_name="状态", default=False)
    time = models.DateTimeField(verbose_name="发放时间")
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True, related_name='location_card')

    class Meta:
        db_table = "tb_location_card"
        verbose_name = "人员定位卡"
        verbose_name_plural = verbose_name
        # unique_together = ("sysid", "id")


class StaffLocation(models.Model):
    """工程车辆定位记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='定位记录编号')
    location_card = models.ForeignKey(LocationCard, verbose_name="员工定位卡", on_delete=models.PROTECT,
                                      related_name="location_card")
    location = models.CharField(max_length=50, verbose_name="位置")
    time = models.DateTimeField(verbose_name='时间')

    class Meta:
        db_table = "tb_staff_location"
        verbose_name = "人员定位记录"
        verbose_name_plural = verbose_name


class BsTation(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    bs_addr = models.IntegerField(verbose_name='基站地址')
    bs_posx = models.FloatField(default=0)
    bs_posy = models.FloatField(default=0)
    bs_posz = models.FloatField(default=0)
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = "tb_bs_tation"
        verbose_name = "隧道定位基站"
        verbose_name_plural = verbose_name