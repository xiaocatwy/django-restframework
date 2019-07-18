from django.db import models

from auth_system.models import Part
from db.base_model import TimeBaseModel, SortBaseModel

#
#
# # Create your models here.
# # 定义工区管理车辆信息类CarInfo
# from db.base_model import TimeBaseModel, SortBaseModel
# from staff.models import Staff
#
#
from staff.models import Staff


class CarInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    # id = models.CharField(max_length=50, verbose_name='车牌号', primary_key=True)
    # car_owner = models.CharField(max_length=50, verbose_name='车主')
    # phone_number = models.CharField(max_length=50, verbose_name='车主联系方式')
    cphm = models.CharField(max_length=20, null=True, blank=True, verbose_name='车牌号码')
    clys = models.BigIntegerField(null=True, blank=True, verbose_name='车辆颜色')
    clxh = models.CharField(max_length=100, null=True, blank=True, verbose_name='车辆型号')
    kphm = models.CharField(max_length=30, null=True, blank=True, verbose_name='卡片号码')
    ccfxrq = models.DateTimeField(null=True, blank=True, verbose_name='车辆发卡日期')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = 'tb_car_msg'
        verbose_name = '车辆信息'
        verbose_name_plural = verbose_name
#
#
# class CarInfoFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = CarInfo
#         fields = ['registration_number', 'car_owner']


# 定义车辆道闸信息类CarBreak
class CarBreak(TimeBaseModel, SortBaseModel):
    id = models.CharField(max_length=50, verbose_name='车辆道闸编号', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='道闸名称')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True)

    class Meta:
        db_table = 'tb_car_brake'
        verbose_name = '车辆道闸信息'
        verbose_name_plural = verbose_name


# class CarBreakFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = CarBreak
#         fields = ['name']


# 定义人员道闸信息类StaffBreak
class StaffBreak(TimeBaseModel, SortBaseModel):
    id = models.CharField(max_length=50, verbose_name='人员道闸编号', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='道闸名称')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)
    x = models.CharField(max_length=20, verbose_name="x位置", null=True)
    y = models.CharField(max_length=20, verbose_name="y位置", null=True)

    class Meta:
        db_table = 'tb_staff_brake'
        verbose_name = '人员道闸信息'
        verbose_name_plural = verbose_name


# class StaffBreakFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = StaffBreak
#         fields = ['name']


class CarRecord(models.Model):
    """车辆通行记录模型类"""
    # id = models.CharField(primary_key=True, max_length=50, verbose_name='通行记录编号')
    # car = models.ForeignKey(CarInfo, verbose_name="车辆", on_delete=models.PROTECT)
    # car_break = models.ForeignKey(CarBreak, verbose_name="道闸", on_delete=models.PROTECT)
    # in_out = models.BooleanField(verbose_name="进出", default=False)
    # time = models.DateTimeField(verbose_name="时间")
    #
    # class Meta:
    #     db_table = "tb_car_record"
    #     verbose_name = "车辆通行记录"
    #     verbose_name_plural = verbose_name

    id = models.CharField(primary_key=True, max_length=50, default='1')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    # id = models.IntegerField(verbose_name='原系统流水ID')
    cardid = models.CharField(max_length=30, verbose_name='卡片号码')
    cardnumber = models.CharField(max_length=20, null=True, verbose_name='车牌号码')
    intime = models.DateTimeField(null=True, blank=True, verbose_name='入场时间')
    outtime = models.DateTimeField(null=True, blank=True, verbose_name='出场时间')
    inplace = models.CharField(max_length=100, null=True, blank=True, verbose_name='入场名称')
    outplace = models.CharField(max_length=100, null=True, blank=True, verbose_name='出场名称')
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = "tb_car_record"
        verbose_name = "车辆通行记录"
        verbose_name_plural = verbose_name
        # unique_together = ("sysid", "id")


# class CarRecordFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = CarRecord
#         fields = ['car', 'car_break']


# class CarPassFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = CarPass
#         fields = ['staff', 'staff_pass_id']


class StaffRecord(models.Model):
    """人员通行记录模型类"""
    id = models.CharField(primary_key=True, max_length=50, verbose_name='通行记录编号')
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    # staff = models.ForeignKey(Staff, verbose_name="员工", on_delete=models.PROTECT)
    zone_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='区域')
    device_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='识别设备')
    names = models.CharField(max_length=15, null=True, blank=True, verbose_name='人员姓名')
    # staff_break = models.ForeignKey(StaffBreak, verbose_name="道闸", on_delete=models.PROTECT)
    # in_out = models.BooleanField(verbose_name="进出")
    inouts = models.CharField(max_length=4)
    time = models.DateTimeField(verbose_name="时间")
    card_number = models.CharField(max_length=10, verbose_name='人员卡号')
    group_number = models.IntegerField(null=True, blank=True, verbose_name='人员部门id')
    part = models.ForeignKey(Part, verbose_name='工区', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = "tb_staff_record"
        verbose_name = "人员通行记录"
        verbose_name_plural = verbose_name


# class StaffRecordFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = StaffRecord
#         fields = ['staff', 'staff_break']



# class StaffLocationCardFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = StaffLocationCard
#         fields = ['staff', 'location_card_id']


class GTSwipeRecord(models.Model):
    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    update_status = models.IntegerField(null=True, blank=True)
    synced = models.IntegerField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)
    swipe_image = models.ImageField(null=True, blank=True)
    ny = models.FloatField(null=True, blank=True)
    nx = models.FloatField(null=True, blank=True)
    rssi_vale = models.IntegerField(null=True, blank=True)
    swipe_status = models.CharField(max_length=4, null=True, blank=True)
    inouts = models.CharField(max_length=4)
    reader_no = models.IntegerField()
    door_no = models.IntegerField()
    zone_name = models.CharField(max_length=100, null=True, blank=True)
    device_name = models.CharField(max_length=100, null=True, blank=True)
    names = models.CharField(max_length=15, null=True, blank=True)
    device_sn = models.CharField(max_length=18)
    group_number = models.IntegerField(null=True, blank=True)
    card_no = models.CharField(max_length=10)
    pattern_card = models.CharField(max_length=13)
    theid = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20)
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)

    class Meta:
        # db_table = "g_t_swipe_record"
        db_table = "ls_swipe_record"
        unique_together = ("sysid", "id")


class GTConsumer(models.Model):
    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    synced = models.IntegerField(null=True, blank=True)
    theid = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20)
    number = models.IntegerField()
    number_back = models.CharField(max_length=20, null=True, blank=True)
    pattern_card = models.CharField(max_length=13)
    card_no = models.CharField(max_length=13)
    dwcard_no = models.CharField(max_length=13, null=True, blank=True)
    enabled = models.IntegerField()
    group_number = models.IntegerField(null=True, blank=True)
    names = models.CharField(max_length=15)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=4, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    nation = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.CharField(max_length=20, null=True, blank=True)
    id_organ = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=18, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=600, null=True, blank=True)
    id_image = models.ImageField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField()
    statuss = models.IntegerField(null=True, blank=True)
    faceid1 = models.TextField(null=True, blank=True)
    featureKey1 = models.TextField(null=True, blank=True)
    feature1 = models.TextField(null=True, blank=True)
    face1 = models.TextField(null=True, blank=True)
    faceid2 = models.TextField(null=True, blank=True)
    featureKey2 = models.TextField(null=True, blank=True)
    feature2 = models.TextField(null=True, blank=True)
    face2 = models.TextField(null=True, blank=True)
    faceid3 = models.TextField(null=True, blank=True)
    featureKey3 = models.TextField(null=True, blank=True)
    feature3 = models.TextField(null=True, blank=True)
    face3 = models.ImageField(null=True, blank=True)
    face4 = models.ImageField(null=True, blank=True)
    face5 = models.ImageField(null=True, blank=True)
    face6 = models.ImageField(null=True, blank=True)
    creater = models.CharField(null=True, blank=True, max_length=50)
    remarks = models.CharField(null=True, blank=True, max_length=200)
    update_status = models.IntegerField(null=True, blank=True)
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    is_used = models.IntegerField(verbose_name='是否启用', default=True, null=True)

    class Meta:
        # db_table = "g_t_consumer"
        db_table = "ls_consumer"
        unique_together = ("sysid", "id")


class CarRecords(models.Model):
    """数据同步，车辆通行记录（生成一条）"""
    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    cardid = models.CharField(max_length=30, verbose_name='卡片号码')
    cardnumber = models.CharField(max_length=20, null=True, verbose_name='车牌号码')
    intime = models.DateTimeField(null=True, blank=True, verbose_name='入场时间')
    outtime = models.DateTimeField(null=True, blank=True, verbose_name='出场时间')
    inplace = models.CharField(max_length=100, null=True, blank=True, verbose_name='入场名称')
    outplace = models.CharField(max_length=100, null=True, blank=True, verbose_name='出场名称')
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')

    class Meta:
        db_table = "ls_mycargooutrecord"
        unique_together = ("sysid", "id")


class CarPassCard(models.Model):
    """数据同步，车辆通行证"""
    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    # id = models.IntegerField(verbose_name='原系统流水ID')
    kphm = models.CharField(max_length=30, verbose_name='卡片号码')
    rybh = models.CharField(max_length=30, verbose_name='人员编号')
    kpzt = models.CharField(max_length=1, null=True, blank=True, verbose_name='卡片状态')
    # c = models.DecimalField( max_digits=10, decimal_places=5, null=True, blank=True, verbose_name='发卡押金')
    cckl = models.CharField(max_length=20, null=True, blank=True, verbose_name='车场卡类')
    ccfxrq = models.DateTimeField(null=True, blank=True, verbose_name='车场发卡日期')
    ccfxrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='车场发行人卡号')
    ccyxqr = models.DateTimeField(null=True, blank=True, verbose_name='车场有效起日')
    ccyxzr = models.DateTimeField(null=True, blank=True, verbose_name='车场有效止日')
    cphm = models.CharField(max_length=20, null=True, blank=True, verbose_name='车牌号码')
    clys = models.BigIntegerField(null=True, blank=True, verbose_name='车辆颜色')
    clxh = models.CharField(max_length=100, null=True, blank=True, verbose_name='车辆型号')
    cccw = models.CharField(max_length=100, null=True, blank=True, verbose_name='车场车位')
    cctkrq = models.DateTimeField(null=True, blank=True, verbose_name='车场退卡日期')
    cctkrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='车场退卡人卡号')
    ccyxjh = models.CharField(max_length=256, null=True, blank=True, verbose_name='车场有效机号')
    ccyxqh = models.CharField(max_length=16, null=True, blank=True, verbose_name='车场有效区号')
    clbz = models.CharField(max_length=255, null=True, blank=True, verbose_name='车场备注')
    mjkl = models.CharField(max_length=20, null=True, blank=True, verbose_name='门禁卡类')
    mjfxrq = models.DateTimeField(null=True, blank=True, verbose_name='门禁卡发行日期')
    mjfxrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='门禁发行人卡号')
    mjjsrq = models.DateTimeField(null=True, blank=True, verbose_name='门禁卡结束日期')
    yxkssj = models.CharField(max_length=2, null=True, blank=True, verbose_name='有效开始时间')
    yxjssj = models.CharField(max_length=2, null=True, blank=True, verbose_name='有效结束时间')
    mjyxjh = models.CharField(max_length=256, null=True, blank=True, verbose_name='门禁有效机号')
    mjtkrq = models.DateTimeField(null=True, blank=True, verbose_name='门禁退卡日期')
    mjtkrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='门禁退卡人卡号')
    mjbz = models.CharField(max_length=255, null=True, blank=True, verbose_name='门禁备注')
    fxrq = models.DateTimeField(null=True, blank=True, verbose_name='发卡日期')
    tkrq = models.DateTimeField(null=True, blank=True, verbose_name='退卡日期')
    fxrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='发行人卡号')
    tkrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='退卡人卡号')
    gsrq = models.DateTimeField(null=True, blank=True, verbose_name='挂失日期')
    gsrkh = models.CharField(max_length=30, null=True, blank=True, verbose_name='挂失人卡号')
    kpwlh = models.CharField(max_length=30, null=True, blank=True, verbose_name='卡片物理号')
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')


    class Meta:
        db_table = 'ls_myfaxingssue'
        unique_together = ("sysid", "kphm")


class BsTation(models.Model):
    """同步数据， 定位基站"""
    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    pk_bs_id = models.IntegerField(verbose_name='原系统流水ID')
    fk_network_id = models.IntegerField(default=0)
    fk_subnet_id = models.IntegerField(default=0)
    bs_addr = models.IntegerField()
    bs_order = models.IntegerField(default=None, null=True, blank=True)
    bs_type = models.IntegerField(default=1)
    bs_major_enable = models.IntegerField(default=0)
    bs_posx = models.FloatField(default=0)
    bs_posy = models.FloatField(default=0)
    bs_posz = models.FloatField(default=0)
    bs_ant_error = models.FloatField(default=0)
    bs_feeder_error = models.FloatField(default=0)
    bs_board_error = models.FloatField(default=0)
    bs_tof_enable = models.IntegerField(default=0)
    scene = models.IntegerField(default=0)
    building_unit = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    is_zgb_comm = models.IntegerField(default=0)
    is_auto_coor = models.IntegerField(default=0)
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')

    class Meta:
        db_table = 'ls_bstation'
        unique_together = ("sysid", "bs_addr")


class LocationCard(models.Model):
    """数据同步， 定位卡"""

    my_uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    card_id = models.IntegerField(verbose_name='定位卡卡号')
    uuid = models.IntegerField(verbose_name='唯一id')
    utype = models.IntegerField(verbose_name='类型,0没有类型，1人员，2物品')
    status = models.IntegerField(verbose_name='状态：0未使用，1使用中，2报废', null=True, blank=True)
    comment = models.CharField(max_length=500, verbose_name='备注', null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间')
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')

    class Meta:
        # db_table = 'tb_card'
        db_table = "ls_location_card"
        unique_together = ("sysid", "id")


class LED(models.Model):
    """数据同步， LED"""

    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    theid = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20, verbose_name='区域名称')
    nControlType = models.IntegerField(verbose_name='控制类型')
    nScreenNo = models.IntegerField(verbose_name='屏幕号')
    nSendMode = models.IntegerField(null=True, blank=True)
    pScreenName = models.CharField(max_length=150, null=True, blank=True, verbose_name='屏幕名称')
    nWidth = models.IntegerField(verbose_name='LED屏宽度')
    nHeight = models.IntegerField(verbose_name='LED屏高度')
    nScreenType = models.IntegerField(verbose_name='屏幕类型')
    nPixelMode = models.IntegerField(verbose_name='像素模式')
    nDataDA = models.IntegerField()
    nDataOE = models.IntegerField()
    nRowOrder = models.IntegerField()
    nDataFlow = models.IntegerField(null=True, blank=True)
    nFreqPar = models.FloatField()
    pCom = models.CharField(max_length=50, null=True, blank=True)
    nBaud = models.IntegerField(null=True, blank=True)
    pSocketIP = models.CharField(max_length=50, null=True, blank=True)
    nSocketPort = models.IntegerField(null=True, blank=True)
    nStaticIPMode = models.IntegerField(null=True, blank=True)
    nServerMode = models.IntegerField(null=True, blank=True)
    pBarcode = models.CharField(max_length=50, null=True, blank=True)
    pNetworkID = models.CharField(max_length=50, null=True, blank=True)
    pServerIP = models.CharField(max_length=50, null=True, blank=True)
    nServerPort = models.IntegerField(null=True, blank=True)
    pServerAccessUser = models.CharField(max_length=50, null=True, blank=True)
    pServerAccessPassword = models.CharField(max_length=50, null=True, blank=True)
    pWiFiIP = models.CharField(max_length=50, null=True, blank=True)
    nWiFiPort = models.IntegerField(null=True, blank=True)
    pGprsIP = models.CharField(max_length=50, null=True, blank=True)
    nGprsPort = models.IntegerField(null=True, blank=True)
    pGprsID = models.CharField(max_length=50, null=True, blank=True)
    pScreenStatusFile = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    is_used = models.IntegerField(verbose_name='是否启用', default=True, null=True)

    class Meta:
        # db_table = 'l_t_screen'
        db_table = "ls_screen"
        unique_together = ("sysid", "id")


class Attend(models.Model):
    """数据同步, 考勤数据"""

    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    theid = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20)
    pattern_card = models.CharField(max_length=13)
    card_no = models.CharField(max_length=13)
    in_datetime = models.DateTimeField(null=True, blank=True)
    out_datetime = models.DateTimeField(null=True, blank=True)
    working_msecs = models.IntegerField(null=True, blank=True)
    update_time = models.DateTimeField()
    update_status = models.IntegerField(null=True, blank=True)
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')

    class Meta:
        # db_table = 'l_t_screen'
        db_table = "ls_attend"
        unique_together = ("sysid", "id")


class Group(models.Model):
    """数据同步， 班组信息"""

    uuid = models.CharField(primary_key=True, max_length=50)
    sysid = models.CharField(max_length=50, verbose_name='原系统ID')
    id = models.IntegerField(verbose_name='原系统流水ID')
    theid = models.CharField(max_length=20)
    area_name = models.CharField(max_length=20, null=True, blank=True)
    number = models.IntegerField()
    department = models.CharField(max_length=200, verbose_name='部门', default='默认部门', null=True, blank=True)
    group_name = models.CharField(max_length=200, verbose_name='班组')
    remarks = models.CharField(max_length=800, verbose_name='备注', null=True, blank=True)
    update_status = models.IntegerField(null=True, blank=True)
    synced = models.IntegerField(null=True, blank=True, verbose_name='是否同步处理')
    part_id = models.CharField(max_length=20, verbose_name='工区id', null=True)
    is_used = models.IntegerField(verbose_name='是否启用', default=True, null=True)

    class Meta:
        # db_table = 'l_t_screen'
        db_table = "ls_group"
        unique_together = ("sysid", "id")