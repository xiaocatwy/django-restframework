-- 必须先有班组信息， 才可以插入人员信息
--

-- 车辆通行记录 数据库触发器
-- 用到临时表：ls_mycargooutrecord
-- 映射数据库：tb_car_record
--
delimiter $$
create trigger carrecord after insert
on ls_mycargooutrecord for each row
begin
insert into tb_car_record(id, sysid, cardid, cardnumber, inplace, intime, outplace, outtime, part_id) values(new.uuid, new.sysid, new.cardid, new.cardnumber, new.inplace, new.intime, new.outplace, new.outtime, new.part_id);
end $$


-- 定位卡 数据库触发器
-- 用到临时表：ls_location_card
-- 映射数据库：tb_location_card
--
delimiter $$
create trigger locationcard after insert
on ls_location_card for each row
begin
insert into tb_location_card(id, sysid, card_id, uuid, utype, status, time) values(new.my_uuid, new.sysid, new.card_id, new.uuid, new.utype, new.status, new.update_time);
end $$


-- 人员信息 数据库触发器
-- 用到临时表：ls_consumer
-- 映射数据库：tb_staff
--
delimiter $$
create trigger staff after insert
on ls_consumer for each row
begin

-- 插入工区信息到tb_part（工区id重复不插入）
INSERT INTO tb_part(`index`, is_used, id, name, sysid) SELECT 0, 1, new.part_id, concat(new.unit, '（默认工区）'), new.sysid FROM DUAL WHERE NOT EXISTS(SELECT id FROM tb_part WHERE id = new.part_id);

insert into tb_staff(id, sysid, group_number, name, sex, age, address, phone, id_card, time, company, id_organ, department_id, is_used, part_id, job_number) values(new.card_no, new.sysid, new.group_number, new.names, new.gender, new.age, new.address, new.phone, new.id_number, new.start_date, new.unit, new.id_organ, new.group_number, new.is_used, new.part_id, new.number);

-- 插入单位信息到tb_company（单位名字重复不插入）
INSERT INTO tb_company(`index`, is_used, id, name) SELECT 0, 1, new.uuid, new.unit FROM DUAL WHERE NOT EXISTS(SELECT name FROM tb_company WHERE name = new.unit);
end $$


-- LED 数据库触发器
-- 用到临时表：ls_screen
-- 映射数据库：tb_led_info
--
delimiter $$
create trigger LED after insert
on ls_screen for each row
begin
insert into tb_led_info(id, sysid, area_name, nScreenNo, pScreenName, nWidth, nHeight, nScreenType, nPixelMode, ip, port, is_used, part_id) values(new.uuid, new.sysid, new.area_name, new.nScreenNo, new.pScreenName, new.nWidth, new.nHeight, new.nScreenType, new.nPixelMode, new.pSocketIP, new.nSocketPort, new.is_used, new.part_id);
end $$


-- 人员通行记录 数据库触发器
-- 用到临时表：ls_swipe_record
-- 映射数据库：tb_staff_record
--
delimiter $$
create trigger staffrecord after insert
on ls_swipe_record for each row
begin
insert into tb_staff_record(id, sysid, zone_name, device_name, names, group_number, inouts, time, card_number, part_id) values(new.uuid, new.sysid, new.zone_name, new.device_name, new.names, new.group_number, new.inouts, new.update_time, new.card_no, new.part_id);
end $$


-- 车辆基础信息 数据库触发器
-- 用到临时表：ls_myfaxingssue
-- 映射数据库：tb_car_msg
--
delimiter $$
create trigger carinfo after insert
on ls_myfaxingssue for each row
begin
insert into tb_car_msg(id, sysid, cphm, clys, clxh, part_id) values(new.uuid, new.sysid, new.cphm, new.clys, new.clxh, new.part_id);
insert into tb_car_pass()
end $$


-- 隧道定位基站 数据库触发器
-- 用到临时表：ls_bstation
-- 映射数据库：tb_bs_tation
--
delimiter $$
create trigger bstation after insert
on ls_bstation for each row
begin
insert into tb_bs_tation(id, sysid, bs_addr, bs_posx, bs_posy, bs_posz, part_id) values(new.uuid, new.sysid, new.bs_addr, new.bs_posx, new.bs_posy, new.bs_posz, new.part_id);
end $$


-- 考勤记录 数据库触发器
-- 用到临时表：ls_attend
-- 映射数据库：tb_userworks
--
delimiter $$
create trigger userworks after insert
on ls_attend for each row
begin
insert into tb_userworks(id, sysid, time, staff_id, work_time, enter_time, leave_time, part_id) values(new.uuid, new.sysid, new.in_datetime, new.card_no, new.working_msecs, new.in_datetime, new.out_datetime, new.part_id);
end $$


-- 部门信息 数据库触发器
-- 用到临时表：ls_group
-- 映射数据库：tb_department
--
delimiter $$
create trigger department after insert
on ls_group for each row
begin
insert into tb_department(id, sysid, department, group_name, update_status, is_used) values(new.number, new.sysid, new.department, new.group_name, new.update_status, new.is_used);
end $$



-- from threading import Timer
-- -- from work_area.models import *
-- --
-- -- g_lenght = 0
-- --
-- -- def carrecord():
-- --
-- --     carrecords = CarRecords.objects.all()
-- --
-- --     lenght = carrecords.count()  # 获取表数据总长度
-- --
-- --     global g_lenght
-- --
-- --     # 判断是否有新数据插入
-- --     if g_lenght == lenght:
-- --         pass
-- --
-- --     # 取出新数据
-- --     result = carrecords[g_lenght : lenght+1]
-- --     # 写入车辆通行记录表中
-- --     for carrecord in result:
-- --         CarRecord.objects.create(
-- --             uuid=carrecord.uuid,
-- --             sysid=carrecord.sysid,
-- --             id=carrecord.id,
-- --             cardid=carrecord.cardid,
-- --             cardnumber=carrecord.cardnumber,
-- --             intime=carrecord.intime,
-- --             outtime=carrecord.outtime,
-- --             inplace=carrecord.inplace,
-- --             outplace=carrecord.outplace,
-- --
-- --         )
-- --
-- --     g_lenght = lenght
-- --
-- --
-- -- t = Timer(10, carrecord)
-- -- t.start()