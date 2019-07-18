-- MySQL dump 10.13  Distrib 5.7.22, for Win64 (x86_64)
--
-- Host: 47.92.26.15    Database: ruidun
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_extra_group`
--

DROP TABLE IF EXISTS `auth_extra_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_extra_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` varchar(200) NOT NULL,
  `is_used` smallint(6) NOT NULL,
  `index` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_extra_group_group_id_782fd680_uniq` (`group_id`),
  CONSTRAINT `auth_extra_group_group_id_782fd680_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_extra_group`
--

LOCK TABLES `auth_extra_group` WRITE;
/*!40000 ALTER TABLE `auth_extra_group` DISABLE KEYS */;
INSERT INTO `auth_extra_group` VALUES (1,'角色1',1,1,1),(2,'角色2',1,1,2),(3,'测试',0,3,5),(4,'测试2',1,3,6);
/*!40000 ALTER TABLE `auth_extra_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin_group'),(5,'group_3'),(6,'group_9'),(2,'user_group');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (54,1,9),(51,1,10),(52,1,11),(53,1,12),(46,1,28),(1,1,41),(2,1,42),(3,1,43),(4,1,44),(36,1,68),(21,1,76),(22,1,84),(23,1,88),(24,1,92),(45,1,104),(40,1,116),(44,1,120),(43,1,124),(28,1,140),(55,1,143),(33,1,144),(48,1,148),(34,1,152),(26,1,164),(7,1,180),(25,1,184),(29,1,193),(30,1,194),(31,1,195),(32,1,196),(35,1,197),(37,1,198),(38,1,199),(39,1,200),(41,1,201),(42,1,202),(47,1,203),(49,1,204),(50,1,205),(5,2,41),(6,2,42),(15,5,25),(20,6,26);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=289 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (5,'增加基础权限',2,'add_permission'),(6,'修改基础权限',2,'change_permission'),(7,'删除基础权限',2,'delete_permission'),(8,'查看基础权限',2,'view_permission'),(9,'增加角色',3,'add_group'),(10,'修改角色信息',3,'change_group'),(11,'删除角色',3,'delete_group'),(12,'查看角色信息',3,'view_group'),(25,'增加用户',7,'add_user'),(26,'修改用户',7,'change_user'),(27,'删除用户',7,'delete_user'),(28,'查看用户信息',7,'view_user'),(29,'新增公司信息',8,'add_company'),(30,'修改公司信息',8,'change_company'),(31,'删除公司',8,'delete_company'),(32,'查看公司信息',8,'view_company'),(41,'新增工区信息',11,'add_part'),(42,'修改工区信息',11,'change_part'),(43,'删除工区信息',11,'delete_part'),(44,'查看工区信息',11,'view_part'),(45,'新增项目信息',12,'add_project'),(46,'修改项目信息',12,'change_project'),(47,'删除项目信息',12,'delete_project'),(48,'查看项目信息',12,'view_project'),(53,'新增部门信息',14,'add_department'),(54,'修改部门信息',14,'change_department'),(55,'删除部门信息',14,'delete_department'),(56,'查看部门信息',14,'view_department'),(57,'新增家属信息',15,'add_folk'),(58,'修改家属信息',15,'change_folk'),(59,'删除家属信息',15,'delete_folk'),(60,'查看家属信息',15,'view_folk'),(61,'增加岗位信息',16,'add_jobstation'),(62,'修改岗位信息',16,'change_jobstation'),(63,'删除岗位信息',16,'delete_jobstation'),(64,'查看岗位信息',16,'view_jobstation'),(66,'修改人员信息',17,'change_staff'),(67,'删除人员信息',17,'delete_staff'),(68,'查看人员信息',17,'view_staff'),(73,'新增生产设备基础信息',19,'add_equipmentinfo'),(74,'修改生产设备基础信息',19,'change_equipmentinfo'),(75,'删除生产设备基础信息',19,'delete_equipmentinfo'),(76,'查看生产设备基础信息',19,'view_equipmentinfo'),(78,'修改车辆定位卡',20,'change_equipmentlocationcard'),(79,'删除车辆定位卡',20,'delete_equipmentlocationcard'),(80,'查看车辆定位卡',20,'view_equipmentlocationcard'),(81,'新增工程车辆维修记录',21,'add_equipmentrepair'),(82,'修改工程车辆维修记录',21,'change_equipmentrepair'),(83,'删除工程车辆维修记录',21,'delete_equipmentrepair'),(84,'查看工程车辆维修记录',21,'view_equipmentrepair'),(85,'新增工程车辆保养记录',22,'add_equipmentupkeep'),(86,'修改工程车辆保养记录',22,'change_equipmentupkeep'),(87,'删除工程车辆保养记录',22,'delete_equipmentupkeep'),(88,'查看工程车辆保养记录',22,'view_equipmentupkeep'),(89,'新增工程车辆使用记录',23,'add_equipmentused'),(90,'修改工程车辆使用记录',23,'change_equipmentused'),(91,'删除工程车辆使用记录',23,'delete_equipmentused'),(92,'查看工程车辆使用记录',23,'view_equipmentused'),(102,'修改车辆通行证',26,'change_carpass'),(103,'删除车辆通行证',26,'delete_carpass'),(104,'查看车辆通行证',26,'view_carpass'),(107,'删除安全设备报警记录',27,'delete_cautionrecord'),(108,'查看安全设备报警记录',27,'view_cautionrecord'),(109,'新增安全设备分类',28,'add_devicecategory'),(110,'修改安全设备分类',28,'change_devicecategory'),(111,'删除安全设备分类',28,'delete_devicecategory'),(112,'查看安全设备分类',28,'view_devicecategory'),(113,'新增安全设备基础信息',29,'add_deviceinfo'),(114,'修改安全设备基础信息',29,'change_deviceinfo'),(115,'删除安全设备基础信息',29,'delete_deviceinfo'),(116,'查看安全设备基础信息',29,'view_deviceinfo'),(117,'新增安全设备维护记录',30,'add_deviceupkeep'),(118,'修改安全设备维护记录',30,'change_deviceupkeep'),(119,'删除安全设备维护记录',30,'delete_deviceupkeep'),(120,'查看安全设备维护记录',30,'view_deviceupkeep'),(122,'修改人员定位卡',31,'change_locationcard'),(123,'删除人员定位卡',31,'delete_locationcard'),(124,'查看人员定位卡',31,'view_locationcard'),(126,'修改人员通行证',32,'change_staffpass'),(127,'删除人员通行证',32,'delete_staffpass'),(128,'查看人员通行证',32,'view_staffpass'),(129,'新增危险品信息',33,'add_danger'),(130,'修改危险品信息',33,'change_danger'),(131,'删除危险品信息',33,'delete_danger'),(132,'查看危险品信息',33,'view_danger'),(133,'新增危险品分类信息',34,'add_dangerouscategory'),(134,'修改危险品分类信息',34,'change_dangerouscategory'),(135,'删除危险品分类信息',34,'delete_dangerouscategory'),(136,'查看危险品分类信息',34,'view_dangerouscategory'),(137,'新增危险品使用记录',35,'add_dangerused'),(138,'修改危险品使用记录',35,'change_dangerused'),(139,'删除危险品使用记录',35,'delete_dangerused'),(140,'查看危险品使用记录',35,'view_dangerused'),(141,'新增专项方案',36,'add_priorscheme'),(142,'修改专项方案',36,'change_priorscheme'),(143,'删除专项方案',36,'delete_priorscheme'),(144,'查看专项方案',36,'view_priorscheme'),(145,'新增反馈问题',37,'add_problem'),(146,'修改反馈问题',37,'change_problem'),(147,'删除反馈问题',37,'delete_problem'),(148,'查看反馈问题',37,'view_problem'),(149,'新增专项方案',38,'add_specialscheme'),(150,'修改专项方案',38,'change_specialscheme'),(151,'删除专项方案',38,'delete_specialscheme'),(152,'查看专项方案',38,'view_specialscheme'),(153,'新增车辆道闸信息',39,'add_carbreak'),(154,'修改车辆道闸信息',39,'change_carbreak'),(155,'删除车辆道闸信息',39,'delete_carbreak'),(156,'查看车辆道闸信息',39,'view_carbreak'),(158,'修改车辆信息',40,'change_carinfo'),(159,'删除车辆信息',40,'delete_carinfo'),(160,'查看车辆信息',40,'view_carinfo'),(163,'导出车辆通行记录',41,'export#_carrecord'),(164,'查看车辆通行记录',41,'view_carrecord'),(165,'新增人员道闸信息',42,'add_staffbreak'),(166,'修改人员道闸信息',42,'change_staffbreak'),(167,'删除人员道闸信息',42,'delete_staffbreak'),(168,'查看人员道闸信息',42,'view_staffbreak'),(171,'导出人员通行记录',43,'export#_staffrecord'),(172,'查看人员通行记录',43,'view_staffrecord'),(175,'导出部门考勤记录',44,'export#_departmentwork'),(176,'查看部门考勤记录',44,'view_departmentwork'),(178,'修改考勤记录',45,'change_userwork'),(179,'导出考勤记录',45,'delete_userwork'),(180,'查看考勤记录',45,'view_userwork'),(184,'查看工程车辆定位记录',46,'view_equipmentlocation'),(188,'查看人员定位记录',47,'view_stafflocation'),(193,'查看炸药库监控',49,'view_explosivedepot'),(194,'查看安全基础资料',50,'view_safetydata'),(195,'查看签章管理',51,'view_signaturemanagement'),(196,'查看安全培训',52,'view_safetytraining'),(197,'查看应急演练管理',53,'view_emergencydrill'),(198,'查看监控管理',54,'view_monitor'),(199,'查看应急广播',55,'view_emergency broadcast\r\nemergency broadcast\r\nemergencybroadcast'),(200,'查看远程电源管理',56,'view_remotepower'),(201,'查看警示管理',57,'view_warning'),(202,'查看中央控制室LED',58,'view_centralroom'),(203,'查看帮助中心',59,'view_helpcenter'),(204,'查看版权信息',60,'view_copyright'),(205,'查看操作日志',61,'view_journal'),(208,'导出日志',62,'export#_artificiallog'),(209,'查看日志',62,'view_artificiallog'),(214,'新增安全设备基础信息',64,'add_voice'),(215,'修改安全设备基础信息',64,'change_voice'),(216,'删除安全设备基础信息',64,'delete_voice'),(217,'查看安全设备基础信息',64,'view_voice'),(228,'删除隧道定位基站',67,'delete_bstation'),(229,'查看隧道定位基站',67,'view_bstation'),(230,'新增ip开关',68,'add_ipswitch'),(231,'修改ip开关',68,'change_ipswitch'),(232,'删除ip开关',68,'delete_ipswitch'),(233,'查看ip开关',68,'view_ipswitch'),(238,'新增led设备基础信息',70,'add_ledinfo'),(239,'修改led设备基础信息',70,'change_ledinfo'),(240,'删除led设备基础信息',70,'delete_ledinfo'),(241,'查看led设备基础信息',70,'view_ledinfo'),(242,'新增监控设备基础信息',71,'add_monitorinfo'),(243,'修改监控设备基础信息',71,'change_monitorinfo'),(244,'删除监控设备基础信息',71,'delete_monitorinfo'),(245,'查看监控设备基础信息',71,'view_monitorinfo'),(246,'新增音响服务器',72,'add_voiceserver'),(247,'修改音响服务器',72,'change_voiceserver'),(248,'删除音响服务器',72,'delete_voiceserver'),(249,'查看音响服务器',72,'view_voiceserver'),(250,'增加应急演练',73,'add_method'),(251,'修改应急演练',73,'change_method'),(252,'删除应急演练',73,'delete_method'),(253,'查看应急演练',73,'view_method'),(264,'导出车辆定位卡',76,'export#_carpasscard'),(265,'查看车辆定位卡',76,'view_carpasscard'),(268,'导出车辆通行记录',77,'export#_carrecords'),(269,'查看车辆通行记录',77,'view_carrecords'),(278,'新增led',80,'add_led'),(279,'修改led',80,'change_led'),(280,'删除led',80,'delete_led'),(281,'查看led',80,'view_led'),(282,'新增定位卡',81,'add_locationcard'),(283,'修改定位卡',81,'change_locationcard'),(284,'删除定位卡',81,'delete_locationcard'),(285,'查看定位卡',81,'view_locationcard'),(286,'控制led设备',70,'control_ledinfo'),(287,'控制ip开关',68,'control_ipswitch'),(288,'控制音响',72,'control_voiceserver');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_contenttypecat`
--

DROP TABLE IF EXISTS `auth_system_contenttypecat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_contenttypecat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `order_by` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `has_sub` tinyint(1) NOT NULL,
  `path` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_contenttypecat`
--

LOCK TABLES `auth_system_contenttypecat` WRITE;
/*!40000 ALTER TABLE `auth_system_contenttypecat` DISABLE KEYS */;
INSERT INTO `auth_system_contenttypecat` VALUES (1,'人员管理','fa fa-user-circle',1,1,1,NULL),(2,'设备管理','fa fa-truck',2,1,0,'equipmentinfos'),(3,'工区管理','fa fa-cubes ',3,1,1,NULL),(4,'桥隧管理','fa fa-th-large ',4,1,1,NULL),(5,'安全管理','fa fa-shield ',5,1,1,NULL),(6,'物联网硬件系统','fa fa-rss-square',6,1,1,NULL),(7,'设置','fa fa-cog ',7,1,1,NULL),(8,'BIM接口','fa fa-tag ',8,1,1,NULL),(9,'查询中心','fa fa-search',9,1,0,'searchcenters'),(10,'帮助','fa fa-question-circle',10,1,1,NULL),(11,'系统管理','fa fa-television',11,1,1,NULL);
/*!40000 ALTER TABLE `auth_system_contenttypecat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_contenttypecatrel`
--

DROP TABLE IF EXISTS `auth_system_contenttypecatrel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_contenttypecatrel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `order_by` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `front_path` varchar(60) DEFAULT NULL,
  `front_redirect` varchar(60) DEFAULT NULL,
  `front_component` varchar(60) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `content_type_cat_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_system_contentt_content_type_cat_id_1f543c86_fk_auth_syst` (`content_type_cat_id`),
  KEY `auth_system_contenttypecatrel_content_type_id_941a0584` (`content_type_id`),
  CONSTRAINT `auth_system_contentt_content_type_cat_id_1f543c86_fk_auth_syst` FOREIGN KEY (`content_type_cat_id`) REFERENCES `auth_system_contenttypecat` (`id`),
  CONSTRAINT `auth_system_contentt_content_type_id_941a0584_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_contenttypecatrel`
--

LOCK TABLES `auth_system_contenttypecatrel` WRITE;
/*!40000 ALTER TABLE `auth_system_contenttypecatrel` DISABLE KEYS */;
INSERT INTO `auth_system_contenttypecatrel` VALUES (1,'人员管理','fa fa-address-book-o',1,1,'staffs',NULL,NULL,11,1),(2,'工作岗位','fa fa-square  ',1,1,NULL,NULL,NULL,8,1),(3,'考勤记录','fa fa-bar-chart ',2,1,'userworks',NULL,NULL,45,1),(4,'设备信息','coffee',1,1,NULL,NULL,NULL,19,2),(5,'设备使用记录','coffee',2,1,NULL,NULL,NULL,21,2),(6,'设备保养记录','coffee',3,1,NULL,NULL,NULL,22,2),(7,'设备维修记录','coffee',4,1,NULL,NULL,NULL,23,2),(8,'设备定位记录','coffee',5,1,NULL,NULL,NULL,46,2),(9,'通道状态','fa fa-dot-circle-o',1,1,'carrecords',NULL,NULL,41,3),(10,'工区人员状态','fa fa-user-circle',2,1,'teams',NULL,NULL,11,3),(11,'工区设备状态','fa fa-gavel',3,1,'channelstate',NULL,NULL,19,3),(12,'工区数据统计','fa fa-bars ',4,1,'datastatistics',NULL,NULL,11,3),(13,'通道状态','fa fa fa-dot-circle-o',1,1,'carrecords',NULL,NULL,41,4),(14,'桥隧人员状态','fa fa-user-circle',2,1,'teams',NULL,NULL,11,4),(15,'桥隧设备状态','fa fa-gavel',3,1,'channelstate',NULL,NULL,19,4),(16,'桥隧数据统计','fa fa-bars ',4,1,'datastatistics',NULL,NULL,11,4),(17,'危险物品管理','fa fa-hand-paper-o ',1,1,'dangeruseds',NULL,NULL,35,5),(18,'炸药库监控','fa fa-industry',2,1,'pass',NULL,NULL,49,5),(19,'安全基础资料','fa fa-file-archive-o',3,1,'pass',NULL,NULL,50,5),(20,'签章管理','fa fa-info',4,1,'pass',NULL,NULL,51,5),(21,'安全培训','fa fa-university',5,1,'pass',NULL,NULL,52,5),(22,'应急方案管理','fa fa-reply-all ',6,1,'priorschemes',NULL,NULL,36,5),(23,'专项施工方案管理','fa fa-reply',7,1,'specialschemes',NULL,NULL,38,5),(24,'应急演练管理','fa fa-heart',8,1,'pass',NULL,NULL,53,5),(25,'定位系统管理','fa fa-map-marker ',1,1,'location_manage',NULL,NULL,17,6),(26,'监控管理','fa fa-camera-retro',2,1,'monitor_manage',NULL,NULL,54,6),(27,'门禁管理 ','fa fa-times-circle',3,1,'carrecords',NULL,NULL,41,6),(28,'应急广播管理','fa fa-star-half-o ',4,1,'vioce_manage',NULL,NULL,55,6),(29,'远程电源管理','fa fa-power-off',5,1,'ipswitch_manage',NULL,NULL,56,6),(30,'LED屏管理','fa fa-desktop ',6,1,'led_manage',NULL,NULL,29,6),(31,'警示管理','fa fa-exclamation-triangle',7,1,'cautious_manage',NULL,NULL,57,6),(32,'中央控制室LED','fa fa-eye ',8,1,'center_manage',NULL,NULL,58,6),(33,'定位系统设置','fa fa-street-view ',1,1,'location_card',NULL,NULL,31,7),(34,'监控设置','fa fa-camera-retro ',2,1,'monitor',NULL,NULL,30,7),(35,'门禁设置','fa fa-times-circle',3,1,'car_pass',NULL,NULL,26,7),(36,'应急广播设置','fa fa-star-half-o ',4,1,'voice',NULL,NULL,55,7),(37,'远程电源设置','fa fa-toggle-on',5,1,'ipswitch',NULL,NULL,56,7),(38,'LED屏设置 ','fa fa-desktop',6,1,'led',NULL,NULL,29,7),(39,'警示设置','fa fa-exclamation-triangle',7,1,'cautious',NULL,NULL,57,7),(40,'帮助中心','fa fa-question-circle',1,1,'pass',NULL,NULL,59,10),(41,'报告问题','fa fa-exclamation',2,1,'pass',NULL,NULL,37,10),(42,'版权信息','fa fa-copyright ',3,1,'pass',NULL,NULL,60,10),(43,'用户资料管理','fa fa-table',1,1,'user',NULL,NULL,7,11),(44,'操作日志','fa fa-window-maximize',2,1,'log',NULL,NULL,61,11),(45,'权限管理','fa fa-code',3,1,'permission',NULL,NULL,3,11),(46,'设备总览','fa fa-globe',8,1,'all_equipment			',NULL,NULL,11,3),(47,'项目设置','fa fa-window-restore',9,1,'part',NULL,NULL,11,7),(48,'设备总览','fa fa-globe',8,1,'all_equipment			','','',11,4);
/*!40000 ALTER TABLE `auth_system_contenttypecatrel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_user`
--

DROP TABLE IF EXISTS `auth_system_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `default_part_id` varchar(50) DEFAULT NULL,
  `default_group_id` int(11) DEFAULT NULL,
  `log_level` smallint(6) NOT NULL,
  `staff_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `staff_id` (`staff_id`),
  KEY `auth_system_user_default_part_id_26bb2eb9_fk_tb_part_id` (`default_part_id`),
  KEY `auth_system_user_default_group_id_5d473280_fk_auth_group_id` (`default_group_id`),
  CONSTRAINT `auth_system_user_default_group_id_5d473280_fk_auth_group_id` FOREIGN KEY (`default_group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_system_user_default_part_id_26bb2eb9_fk_tb_part_id` FOREIGN KEY (`default_part_id`) REFERENCES `tb_part` (`id`),
  CONSTRAINT `auth_system_user_staff_id_e888a288_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_user`
--

LOCK TABLES `auth_system_user` WRITE;
/*!40000 ALTER TABLE `auth_system_user` DISABLE KEYS */;
INSERT INTO `auth_system_user` VALUES (1,'pbkdf2_sha256$120000$zKyX2PG2OYuJ$r4OGOMT0dPbHRqhan1K9qn32W8WXhpmtMEV/e96oqfY=',NULL,1,'admin','','','admin@a.com',1,1,'2019-02-22 11:57:28.673000','1',1,0,'123456'),(10,'pbkdf2_sha256$120000$zKyX2PG2OYuJ$r4OGOMT0dPbHRqhan1K9qn32W8WXhpmtMEV/e96oqfY=',NULL,0,'user_1','admin','管理员','admin@a.com',0,1,'2019-02-27 10:55:18.875000','1',1,6,'160001'),(11,'pbkdf2_sha256$120000$s5REOBax3B0G$YT1d7Y1SfZjUaj0++QQn62yA82WqgyBFM0L9LPKPYkY=',NULL,0,'user_2','普通用户','','user_2@a.com',0,1,'2019-02-27 10:55:18.897000',NULL,NULL,2,'160002'),(12,'pbkdf2_sha256$120000$mkTpNwI2hsGB$e/AkzE9qBoNhii+79iF2f/fPuSv0m6lY40IaI1WD/mM=',NULL,0,'user_22','','','',0,0,'2019-03-22 02:36:02.266435',NULL,NULL,0,NULL),(13,'pbkdf2_sha256$120000$s9MONeGh2CgC$KQhQMtG+6+yccotktSgKMdkORo1xWOLA1zc+lLg9NRE=',NULL,0,'','','','',0,1,'2019-04-16 03:23:52.278853',NULL,NULL,0,NULL);
/*!40000 ALTER TABLE `auth_system_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_user_groups`
--

DROP TABLE IF EXISTS `auth_system_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_system_user_groups_user_id_group_id_8b902f94_uniq` (`user_id`,`group_id`),
  KEY `auth_system_user_groups_group_id_20093601_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_system_user_groups_group_id_20093601_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_system_user_groups_user_id_dc576211_fk_auth_system_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_system_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_user_groups`
--

LOCK TABLES `auth_system_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_system_user_groups` DISABLE KEYS */;
INSERT INTO `auth_system_user_groups` VALUES (5,1,1),(6,1,2),(1,10,1),(2,11,2),(3,12,1),(4,12,2),(7,13,1),(8,13,2),(9,13,5),(10,13,6);
/*!40000 ALTER TABLE `auth_system_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_user_parts`
--

DROP TABLE IF EXISTS `auth_system_user_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_user_parts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `part_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_system_user_parts_user_id_part_id_3b681073_uniq` (`user_id`,`part_id`),
  KEY `auth_system_user_parts_part_id_026dd4b5_fk_tb_part_id` (`part_id`),
  CONSTRAINT `auth_system_user_parts_part_id_026dd4b5_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`),
  CONSTRAINT `auth_system_user_parts_user_id_958dc61d_fk_auth_system_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_system_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_user_parts`
--

LOCK TABLES `auth_system_user_parts` WRITE;
/*!40000 ALTER TABLE `auth_system_user_parts` DISABLE KEYS */;
INSERT INTO `auth_system_user_parts` VALUES (5,1,'1'),(1,10,'1'),(2,10,'2'),(3,12,'1'),(4,12,'2'),(6,13,'1');
/*!40000 ALTER TABLE `auth_system_user_parts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_system_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_system_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_system_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_system_user_user_pe_user_id_permission_id_71d8796f_uniq` (`user_id`,`permission_id`),
  KEY `auth_system_user_use_permission_id_d568c7cb_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_system_user_use_permission_id_d568c7cb_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_system_user_use_user_id_a535ce11_fk_auth_syst` FOREIGN KEY (`user_id`) REFERENCES `auth_system_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_system_user_user_permissions`
--

LOCK TABLES `auth_system_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_system_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_system_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_system_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_system_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_system_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','权限相关'),(3,'auth','角色相关'),(9,'auth_system','contenttypecat'),(10,'auth_system','contenttypecatrel'),(13,'auth_system','customgroup'),(48,'auth_system','extragroup'),(61,'auth_system','journal'),(66,'auth_system','sysid'),(8,'auth_system','公司相关'),(11,'auth_system','工区'),(7,'auth_system','用户相关'),(12,'auth_system','项目'),(4,'contenttypes','contenttype'),(23,'equipment','车辆使用记录'),(19,'equipment','车辆信息'),(46,'equipment','车辆定位'),(20,'equipment','车辆定位卡'),(21,'equipment','车辆维修记录'),(22,'equipment','车辆维护记录'),(59,'help','帮助中心'),(60,'help','版权'),(55,'internet_operate','emergency broadcast\r\nemergency broadcast\r\nemergencybroadcast'),(54,'internet_operate','monitor'),(56,'internet_operate','remotepower'),(57,'internet_operate','warning'),(58,'internet_opreate','centralroom'),(68,'internet_setting','IP开关'),(72,'internet_setting','IP开关服务'),(69,'internet_setting','IP开关细节'),(70,'internet_setting','LED'),(47,'internet_setting','人员定位'),(32,'internet_setting','人员通行证'),(29,'internet_setting','安全设备信息'),(28,'internet_setting','安全设备分裂'),(30,'internet_setting','安全设备维护记录'),(31,'internet_setting','定位卡'),(67,'internet_setting','定位基站'),(27,'internet_setting','报警记录'),(71,'internet_setting','监控设备'),(26,'internet_setting','车辆通行证'),(64,'internet_setting','音响'),(6,'rest_framework_tracking','apirequestlog'),(53,'safe','emergencydrill'),(49,'safe','explosivedepot'),(50,'safe','safetydata'),(52,'safe','safetytraining'),(51,'safe','signaturemanagement'),(38,'safe','专项方案'),(33,'safe','危险品'),(35,'safe','危险品使用记录'),(34,'safe','危险品分类'),(37,'safe','反馈问题'),(36,'safe','应急方案'),(73,'safe','应急演练'),(5,'sessions','session'),(18,'staff','team'),(17,'staff','员工'),(15,'staff','家属'),(16,'staff','岗位'),(45,'staff','考勤'),(14,'staff','部门'),(44,'staff','部门考勤'),(62,'system_manage','日志'),(74,'work_area','attend'),(75,'work_area','bstation'),(76,'work_area','carpasscard'),(77,'work_area','carrecords'),(78,'work_area','group'),(79,'work_area','gtconsumer'),(65,'work_area','gtswiperecord'),(80,'work_area','led'),(81,'work_area','locationcard'),(43,'work_area','人员通行记录'),(42,'work_area','人员道闸'),(40,'work_area','车辆信息'),(41,'work_area','车辆通行记录'),(39,'work_area','车辆道闸');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-13 14:16:56.386100'),(2,'auth','0001_initial','2019-04-13 14:16:56.565448'),(3,'auth_system','0001_initial','2019-04-13 14:16:57.167657'),(4,'admin','0001_initial','2019-04-13 14:16:57.251417'),(5,'staff','0001_initial','2019-04-13 14:16:57.614121'),(6,'auth_system','0002_auto_20190412_2037','2019-04-13 14:16:57.791587'),(7,'equipment','0001_initial','2019-04-13 14:16:58.379452'),(8,'work_area','0001_initial','2019-04-13 14:16:59.008418'),(9,'internet_setting','0001_initial','2019-04-13 14:17:00.360789'),(10,'rest_framework_tracking','0001_initial','2019-04-13 14:17:00.479685'),(11,'rest_framework_tracking','0002_auto_20170118_1713','2019-04-13 14:17:00.588450'),(12,'rest_framework_tracking','0003_add_errors','2019-04-13 14:17:00.638224'),(13,'rest_framework_tracking','0004_add_verbose_name','2019-04-13 14:17:00.659395'),(14,'rest_framework_tracking','0005_auto_20171219_1537','2019-04-13 14:17:00.750316'),(15,'rest_framework_tracking','0006_view_and_view_method_nullable','2019-04-13 14:17:00.881751'),(16,'rest_framework_tracking','0006_auto_20180315_1442','2019-04-13 14:17:01.190080'),(17,'rest_framework_tracking','0007_merge_20180419_1646','2019-04-13 14:17:01.198811'),(18,'safe','0001_initial','2019-04-13 14:17:02.146607'),(19,'sessions','0001_initial','2019-04-13 14:17:02.174980'),(20,'staff','0002_auto_20190413_0840','2019-04-13 14:17:02.259127'),(21,'system_manage','0001_initial','2019-04-13 14:17:02.307235'),(22,'auth_system','0003_auto_20190414_2206','2019-04-15 03:07:37.036472'),(23,'internet_setting','0002_auto_20190414_2206','2019-04-15 03:07:37.143266'),(24,'staff','0003_auto_20190414_2206','2019-04-15 03:07:37.378309'),(25,'work_area','0002_auto_20190414_2206','2019-04-15 03:07:37.808091'),(26,'internet_setting','0003_auto_20190414_2353','2019-04-15 04:53:47.057832'),(27,'staff','0004_auto_20190414_2353','2019-04-15 04:53:47.586266'),(28,'work_area','0003_auto_20190414_2353','2019-04-15 04:53:48.220136');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ls_attend`
--

DROP TABLE IF EXISTS `ls_attend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_attend` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `theid` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `pattern_card` varchar(13) NOT NULL,
  `card_no` varchar(13) NOT NULL,
  `in_datetime` datetime(6) DEFAULT NULL,
  `out_datetime` datetime(6) DEFAULT NULL,
  `working_msecs` int(11) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `update_status` int(11) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_attend_sysid_id_55cdd0b8_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_attend`
--

LOCK TABLES `ls_attend` WRITE;
/*!40000 ALTER TABLE `ls_attend` DISABLE KEYS */;
INSERT INTO `ls_attend` VALUES ('2019041514221900001b8ae1d1c0e4951a025879ec676fd2d','SYS0101',16,'ATT_150213867867','Gilianda-001','dw160003','160003','2019-04-02 15:02:12.000000','2019-04-02 17:16:40.000000',8054564,'2019-04-02 17:16:40.000000',0,0,'1'),('2019041514221900001eff5b602384c9fb028b47d04b51298','SYS0101',7,'ATT_102131245245','Gilianda-001','dw18438','18438','2019-03-02 10:21:30.000000','2019-03-02 10:25:49.000000',259302,'2019-03-02 10:25:49.000000',0,0,'1'),('2019041514221900007e2395403ca4b9f8103ca2ca6c30a35','SYS0101',23,'ATT_093851154154','Gilianda-001','dw123456','123456','2019-04-12 09:38:49.000000','2019-04-12 09:41:26.000000',156183,'2019-04-12 09:54:20.000000',0,0,'1'),('2019041514221900011372dd99b6e4f608088e6630fa9c950','SYS0101',11,'ATT_111631999999','Gilianda-001','dw160004','160004','2019-03-30 11:16:30.000000','2019-03-30 11:25:32.000000',531064,'2019-03-30 11:38:08.000000',0,0,'1'),('2019041514221900013ca9d53d7644fa68694737bf4025eb3','SYS0101',2,'ATT_115019138138','Gilianda-001','dw18438','18438','2019-02-16 11:50:17.000000','2019-02-16 11:53:33.000000',195911,'2019-02-16 11:53:33.000000',0,0,'1'),('2019041514221900025432eaa493c4f459751714c2e53aa21','SYS0101',14,'ATT_155632395395','Gilianda-001','dw160004','160004','2019-04-01 15:56:31.000000','2019-04-01 16:44:31.000000',2880173,'2019-04-01 16:44:31.000000',0,0,'1'),('20190415142219000395604ad766945d49dbc9f331a52cc41','SYS0101',22,'ATT_093510156156','Gilianda-001','dw160003','160003','2019-04-12 09:33:33.000000','2019-04-12 09:54:20.000000',1151009,'2019-04-12 09:54:20.000000',0,0,'1'),('20190415142219000432d0cece283449494d14917b4c571b1','SYS0101',17,'ATT_150218869869','Gilianda-001','dw160002','160002','2019-04-02 15:02:18.000000','2019-04-02 15:02:24.000000',5533,'2019-04-02 17:16:40.000000',0,0,'1'),('2019041514221900048bc1b670cdc460182ec479b9745a93a','SYS0101',9,'ATT_163909841841','Gilianda-001','dw160003','160003','2019-03-19 16:39:07.000000','2019-03-19 17:28:21.000000',2953898,'2019-03-19 17:28:21.000000',0,0,'1'),('201904151422190004a8f57df1051415bac3e0a7a5ff54028','SYS0101',12,'ATT_111636007007','Gilianda-001','dw160002','160002','2019-03-30 11:16:34.000000','2019-03-30 11:16:46.000000',10894,'2019-03-30 11:38:08.000000',0,0,'1'),('201904151422190004e49f034d340452487931ec0ea2b9689','SYS0101',4,'ATT_103730938938','Gilianda-001','dw18438','18438','2019-02-21 10:37:29.000000','2019-02-21 10:58:23.000000',698055,'2019-02-21 10:58:23.000000',0,0,'1'),('201904151422190004fad75921df74ceb8f59d34628787e57','SYS0101',3,'ATT_103730934934','Gilianda-001','dw16479','16479','2019-02-21 10:37:29.000000','2019-02-21 10:58:23.000000',698038,'2019-02-21 10:58:23.000000',0,0,'1'),('2019041514221900069bd0f4b43e047e281b56590d75926d5','SYS0101',6,'ATT_102131241241','Gilianda-001','dw16479','16479','2019-03-02 10:21:30.000000','2019-03-02 10:25:49.000000',259290,'2019-03-02 10:25:49.000000',0,0,'1'),('201904151422190006e174ed0cfc34dfb968a61f02203d71d','SYS0101',19,'ATT_091546362362','Gilianda-001','dw160002','160002','2019-04-12 09:15:45.000000','2019-04-12 09:20:29.000000',284329,'2019-04-12 09:20:29.000000',0,0,'1'),('20190415142219000700b60b671d7471cb3f926f13d1dd0d8','SYS0101',15,'ATT_142845903903','Gilianda-001','dw160004','160004','2019-04-02 14:28:45.000000','2019-04-02 17:16:40.000000',7784537,'2019-04-02 17:16:40.000000',0,0,'1'),('20190415142219000710a6aed840743b5aa1e556680b1a520','SYS0101',10,'ATT_111348005005','Gilianda-001','dw160001','160001','2019-03-30 11:13:47.000000','2019-03-30 11:38:08.000000',1460587,'2019-03-30 11:38:08.000000',0,0,'1'),('2019041514221900073f7dbbe87874fa19c5d44c703173355','SYS0101',13,'ATT_112855011011','Gilianda-001','dw160003','160003','2019-03-30 11:28:54.000000','2019-03-30 11:38:08.000000',553023,'2019-03-30 11:38:08.000000',0,0,'1'),('201904151422190007bba37f12d404930975b628abd938ae8','SYS0101',5,'ATT_105533204204','Gilianda-001','dw160004','160004','2019-02-21 10:55:32.000000','2019-02-21 10:55:40.000000',7862,'2019-02-21 10:58:23.000000',0,0,'1'),('20190415142219000c18ac35443084c26ac4fc6102488e4ce','SYS0101',1,'ATT_114244171171','Gilianda-001','dw16479','16479','2019-02-16 11:42:43.000000','2019-02-16 11:53:33.000000',649306,'2019-02-16 11:53:33.000000',0,0,'1'),('20190415142219000c6d8efdbafc640a793930d069e196bc5','SYS0101',20,'ATT_092341159159','Gilianda-001','dw160004','160004','2019-04-12 09:23:41.000000','2019-04-12 09:54:20.000000',1839047,'2019-04-12 09:54:20.000000',0,0,'1'),('20190415142219000ea0d27eae06d4d7dbe814f4eaa0be0a1','SYS0101',8,'ATT_163615842842','Gilianda-001','dw160004','160004','2019-03-19 16:36:15.000000','2019-03-19 17:28:21.000000',3126297,'2019-03-19 17:28:21.000000',0,0,'1');
/*!40000 ALTER TABLE `ls_attend` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger userworks after insert
on ls_attend for each row
begin
insert into tb_userworks(id, sysid, time, staff_id, work_time, enter_time, leave_time, part_id) values(new.uuid, new.sysid, new.in_datetime, new.card_no, new.working_msecs, new.in_datetime, new.out_datetime, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_bstation`
--

DROP TABLE IF EXISTS `ls_bstation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_bstation` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `pk_bs_id` int(11) NOT NULL,
  `fk_network_id` int(11) NOT NULL,
  `fk_subnet_id` int(11) NOT NULL,
  `bs_addr` int(11) NOT NULL,
  `bs_order` int(11) DEFAULT NULL,
  `bs_type` int(11) NOT NULL,
  `bs_major_enable` int(11) NOT NULL,
  `bs_posx` double NOT NULL,
  `bs_posy` double NOT NULL,
  `bs_posz` double NOT NULL,
  `bs_ant_error` double NOT NULL,
  `bs_feeder_error` double NOT NULL,
  `bs_board_error` double NOT NULL,
  `bs_tof_enable` int(11) NOT NULL,
  `scene` int(11) NOT NULL,
  `building_unit` int(11) NOT NULL,
  `floor` int(11) NOT NULL,
  `is_zgb_comm` int(11) NOT NULL,
  `is_auto_coor` int(11) NOT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_bstation_sysid_bs_addr_d1738bb8_uniq` (`sysid`,`bs_addr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_bstation`
--

LOCK TABLES `ls_bstation` WRITE;
/*!40000 ALTER TABLE `ls_bstation` DISABLE KEYS */;
/*!40000 ALTER TABLE `ls_bstation` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger bstation after insert
on ls_bstation for each row
begin
insert into tb_bs_tation(id, sysid, bs_addr, bs_posx, bs_posy, bs_posz, part_id) values(new.uuid, new.sysid, new.bs_addr, new.bs_posx, new.bs_posy, new.bs_posz, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_consumer`
--

DROP TABLE IF EXISTS `ls_consumer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_consumer` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `synced` int(11) DEFAULT NULL,
  `theid` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `number` int(11) NOT NULL,
  `number_back` varchar(20) DEFAULT NULL,
  `pattern_card` varchar(13) NOT NULL,
  `card_no` varchar(13) NOT NULL,
  `dwcard_no` varchar(13) DEFAULT NULL,
  `enabled` int(11) NOT NULL,
  `group_number` int(11) DEFAULT NULL,
  `names` varchar(15) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(4) DEFAULT NULL,
  `id_number` varchar(20) DEFAULT NULL,
  `nation` varchar(20) DEFAULT NULL,
  `birthday` varchar(20) DEFAULT NULL,
  `id_organ` varchar(300) DEFAULT NULL,
  `phone` varchar(18) DEFAULT NULL,
  `unit` varchar(200) DEFAULT NULL,
  `address` varchar(600) DEFAULT NULL,
  `id_image` varchar(100) DEFAULT NULL,
  `start_date` datetime(6) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `statuss` int(11) DEFAULT NULL,
  `faceid1` longtext,
  `featureKey1` longtext,
  `feature1` longtext,
  `face1` longtext,
  `faceid2` longtext,
  `featureKey2` longtext,
  `feature2` longtext,
  `face2` longtext,
  `faceid3` longtext,
  `featureKey3` longtext,
  `feature3` longtext,
  `face3` varchar(100) DEFAULT NULL,
  `face4` varchar(100) DEFAULT NULL,
  `face5` varchar(100) DEFAULT NULL,
  `face6` varchar(100) DEFAULT NULL,
  `creater` varchar(50) DEFAULT NULL,
  `remarks` varchar(200) DEFAULT NULL,
  `update_status` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_consumer_sysid_id_0a47c389_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_consumer`
--

LOCK TABLES `ls_consumer` WRITE;
/*!40000 ALTER TABLE `ls_consumer` DISABLE KEYS */;
INSERT INTO `ls_consumer` VALUES ('201904151422030002e9de0e2544a4ada9ac7fb52ebc97860','SYS0101',1,0,'CON_114243651651','Gilianda-001',1,NULL,'dw16479','16479','',1,0,'N16479',30,'男',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-02-16 00:00:00.000000','2029-12-30 00:00:00.000000','2019-03-02 10:25:49.000000',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Gilianda-001',NULL,1,1,'1'),('201904151422030003193e9bb76fd4a1fb13acb395a01ca94','SYS0101',10,0,'CON_093746267267','Gilianda-001',8,NULL,'dw160004','160004','',1,3,'160004',28,'男','1234556779x','','','','','','',NULL,'2019-04-12 00:00:00.000000','2029-12-30 00:00:00.000000','2019-04-12 09:38:38.000000',1,NULL,'c840765a1b198c55354e60877ad6296f','01′',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,'1'),('2019041514220300038baa205b87c40d1b906e54fdabcea1a','SYS0101',5,0,'CON_104851721721','Gilianda-001',5,NULL,'dw160002','160002','',1,4,'测试员',30,'男','','','','','','','',NULL,'2019-02-21 00:00:00.000000','2029-12-30 00:00:00.000000','2019-04-12 08:59:13.000000',1,NULL,'15dee9ebdaafcd83bc6ad1fa437d7c7e','01′\0\0\0\0\0\0\0\0?D(??o?;?¨?El~=×ó=i?￥=-ü3=@￠??Bé?<?mù?z??=????-N=7?í=???=s?|?ˉ?ù<YCù;i6L9?ab=F??)<?=h-?=>T6=g1?<? ì?????zˉ?;?>q20?3???μ?à?TH￡?ìr=?ò*=[?G=~?′??μ=>_ì?Y?s<1.?2B=!?á?é????1F5?B6??R9a?(\r]???=?/\n>???<6?\"=ü=???=o$z=A]P;00?=@èo=@ˉ?ào?|=o2￥?5?????==$?<±a÷??)?=§>81>￥u??,×<?7?;????=sy-??°\r=??×?u±?qe?àì-???·;F??oS&?=n÷??o￡??????f??w?3??V¨=?#???￥?U???fyJ?#o?<?k???)??í2ê1ó?T?#ˉ!?h?=R?=???;üJ??¨§?=±??????#^?<???;e?é:_Q&;3nê?2? <29?)B?<b§\"???H=1Y=C???8?=ˉ;M?ó=?s?|^??:=wo??|~?????R,=_n<NTg?3Z?<d=￥￠???9Y;??y=?áh<G-:=?hz=Dz=μeJ?a???·8=ácr?5!j<übo=cD??P,?=?j?<B6<(?F=D\"n=ê????v;?;??óa??′?í?1pQ?ê¤?=!$??Vd{={?J?R??+sü?êe??w?(?￠m??ó?=Qó?<?^ù??¨?,aM=z?ó??ím?Ve-???|??c¤=e\n<g$=@è=??§?§????n??l????E=??x=?aè?\n?8=M?<???q???=L;?Sd?×&?<???=?09?-%G??co<7-??Z?$?§_A?.|W1°??-3?=×~=%Gc=oü§=~?N<×Q????=*0?=?\'?<\r??=?Y×=Yo?=	?3=p<|=en?<2\n???y\'??·Z<??&?d??????s??=,??\n<?ì#??μ?°??o?)=]??;yF???ù??üy(<??X;?X?=n~\Z?!C???ò7?ù???o\"=??a?#]A=\'?9??à,?}??=Xio?Xx?<?I;01￡?×Fü?WU?1a?oq?S@\0\0\0àésNà\0\0\0àasS@\0\0\0`?Qà\0\0\0@bxS@\0\0\0\0?Nà\0\0\0\0\nóS@\0\0\0àR4Là\0\0\0??T@\0\0\0à\"Jà\0\0\0\0??S@?Y??\0\0?yd1?yd1\0\0\0\0\0\0\0\042??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?\0\0?yd1?yd1\0\0\0\0\0\0\0\0,2??\0\0\0à?+ù&??à??-6)f￠@\0óTT?gàajù?M?@ a^￡ˉ&t@?0?gV￠?@D?ì^|?@à′%???@?\'A?&+?@?wì?á??@ ????@°§í?X?@ (áêê?@\0a°na1XàLYJ^}￡?@à?P~÷￥?à°???f??@h>?O?à?1?2(??@°O3m~?à`B??a?@?ìD?￥??àà?T±?$}@8?f??à?μ-?dà¨é?m?y?à??\r?à??à??g¨?àET2,??àe??\n@?àèáóá20?à&óC?c?@.Iè3?à??<¨???@???LL??à?,ícì?@è?èVT?à0ò3áμ?@02?)ò?à°j5-;ó?@¨4M??a?à\0?μn?sàP???ù??à ?íMH4?àe￥S?gá?à??$Q!ù?à0?Tü??à V-?=?à?àét?P?à???3??à??_7?à@dK?×?f@D??\"é??à\0?--?¤_@?¤??à\0ü0kR@\0àê1?D^à\0$R3?@@@?*U,pj@ ??S-G~@@5?éBTx@`?`￥@?q@`aC??c{@\0o!PDh:@à?d3?|@à? ??ákàà????mw@?Cí?Qyà@êp(?q@t?AN?-?@0~>`??àhv§/?@èáó??\"?àà\r0(\03?@??o?è?àà?òQ?@0e8\"G?àí ???@0tUXH??àxG?′￥??@D?8éó?à?z?\ZpwàH?;(ò??à>if?a?àà^×?óè?à0\nUY?×?à@4ó?s?à???7ah?à0￠êh=s?àà?????à??ê(ù?à?\0?GY\n?àa?èòT?à\0]!\"?2?@?T￡??@0?(LM\n?@cd???@?ê??[i@ *TêúH?@\0?ùE?2àà?!?<ó?@àR??Gílà g??à??@p_￠-O??àp÷?è¤a?@?BEü\'5?à0X?ó?@p:]?xA?à?]??·??@?~7?ewà°???¨W?@\0?QF?Jà?ì???@\0.?~×p@(	W???@Dé￡3?j?@?3So?<?@à? ?)R?@??±ù_p?@\0??Qüàq@°è￥6e¨?@\0àíí7à?ìX??f?@à??Entà?m?1e??@?J?:?d?àDa?BZ??@`$s7?tàx?Y**?@\0′?j*x>à?(ó:ù??@ ?I?§?q@? e?R?@\0\0\0à9\0\0\0~d1\0~d1\0\0\0\0\0\0\0\0 2??\0\0\0~d1~d1\0\0\0\0\0\0\0\0 2??\0\0\0\0\0\0\0\0\0e?\0\0\0?úm@\0\0\0`a?x@\0\0\0\0\0\0e?\0\0\0`4n@\0\0\0à)|x@\0\0\0\0\0\0e?\0\0\0`??o@\0\0\0?x?x@\0\0\0\0\0\0e?\0\0\0?×cp@\0\0\0àg|x@\0\0\0\0\0\0e?\0\0\0?=×p@\0\0\0à??x@\0\0\0\0\0\0e?\0\0\0à?§q@\0\0\0 m?x@\0\0\0\0\0\0e?\0\0\0?ù\"r@\0\0\0`ù1x@\0\0\0\0\0\0e?\0\0\0\0?q@\0\0\0\0?>y@\0\0\0\0\0\0e?\0\0\0à?\0q@\0\0\0à??y@\0\0\0\0\0\0e?\0\0\0??Wp@\0\0\0`\01y@\0\0\0\0\0\0e?\0\0\0?òao@\0\0\0?±¤y@\0\0\0\0\0\0e?\0\0\0`?Fn@\0\0\0àDEy@\0\0\0\0\0\0e?\0\0\0@?m@\0\0\0\0ó?x@\0\0\0\0\0\0e?\0\0\0àS|o@\0\0\0?èYx@\0\0\0\0\0\0e?\0\0\0\0?_p@\0\0\0?\"?x@\0\0\0\0\0\0e?\0\0\0à(\0q@\0\0\0??ùx@\0\0\0\0\0\0e?\0\0\0??r@\0\0\0?N±x@\0\0\0\0\0\0e?\0\0\0às?p@\0\0\0àHy@\0\0\0\0\0\0e?\0\0\0@èZp@\0\0\0?(1y@\0\0\0\0\0\0e?\0\0\0@so@\0\0\0?{y@\0\0\0\0\0\0e??>\0\0\0à???(±??\0\0\0\0\0\0\0\0?\0\0j\0\0hw??#s,@?h??zB@\0\0\0\0\0\0e?0ü?\rOd.@dR5}^oG@\0\0\0\0\0\0e??a??71@háD?ìIL@\0\0\0\0\0\0e??????2@?{o?ónP@\0\0\0\0\0\0e?@&?@I?6@à?j4	S@\0\0\0\0\0\0e?H?U	?¤<@ ò??BrU@\0\0\0\0\0\0e?fp?XieA@ \"P?dW@\0\0\0\0\0\0e?ì?WoútF@?0^JY@\0\0\0\0\0\0e??j??EL@?y?é7μY@\0\0\0\0\0\0e?N>.0÷P@D/IF&?X@\0\0\0\0\0\0e??ò?S@D?ó\ZW@\0\0\0\0\0\0e?dr?1T@$Oê&\nU@\0\0\0\0\0\0e?X??V@xké??R@\0\0\0\0\0\0e??^êè1YV@??Wn[?O@\0\0\0\0\0\0e?Z?@ì°2W@Doví7K@\0\0\0\0\0\0e?Z`V??W@0Pè0?+F@\0\0\0\0\0\0e??áC??2W@}???é@@\0\0\0\0\0\0e??1￥??7@4?,cA@\0\0\0\0\0\0e??éêB[?<@t{?/-a@@\0\0\0\0\0\0e?¨`?>￥nA@L?n?[@@\0\0\0\0\0\0e?8qúZ?VD@??1??@@\0\0\0\0\0\0e?`!Sè??F@????¤A@\0\0\0\0\0\0e?NQêé￥wP@üt?1?aA@\0\0\0\0\0\0e?B#ú.·?Q@L4?dp@@\0\0\0\0\0\0e??z?′? S@@?′Yu?@\0\0\0\0\0\0e?￠é ￡T@H?OW? ?@\0\0\0\0\0\0e?x(°,u?U@?C???d@@\0\0\0\0\0\0e??S?o?,L@?yW￠?!G@\0\0\0\0\0\0e?¨AóZL@???t?J@\0\0\0\0\0\0e??dù4x?L@$úF!rtN@\0\0\0\0\0\0e?¨w?×B?L@f?á??2P@\0\0\0\0\0\0e?Dù￡&?H@T??%ZQ@\0\0\0\0\0\0e?????￠=J@ì?;?/?Q@\0\0\0\0\0\0e?/Cμf?L@?_PYfíQ@\0\0\0\0\0\0e?ì7 (?N@l\n?s?Q@\0\0\0\0\0\0e??c???/P@?7mTC2Q@\0\0\0\0\0\0e???TH×>@??2ZüE@\0\0\0\0\0\0e??ù?kA@à#?+s?E@\0\0\0\0\0\0e?àò?t-<D@?y.gE@\0\0\0\0\0\0e??àE}?·F@?E?,,DF@\0\0\0\0\0\0e???￠oyD@?\'6 G@\0\0\0\0\0\0e?\"d?w?A@?Xè?	\rG@\0\0\0\0\0\0e???Y~??P@ü\Z?\0sóE@\0\0\0\0\0\0e???H?íéQ@@ua×±?D@\0\0\0\0\0\0e??￠?h^1S@aˉ?òüD@\0\0\0\0\0\0e?lavk+T@déù<6E@\0\0\0\0\0\0e????e*S@???í′UF@\0\0\0\0\0\0e??)l9?Q@??\'?¤F@\0\0\0\0\0\0e?Pó3??D@6VqA?/T@\0\0\0\0\0\0e??D??G@?úeM?S@\0\0\0\0\0\0e?¨?[á?J@?Pê?S@\0\0\0\0\0\0e???i??L@ì>Z??S@\0\0\0\0\0\0e?à-SDY\0\0 ?d1',NULL,'','','',NULL,'','','',NULL,NULL,NULL,NULL,'Gilianda-001','',1,1,'1'),('201904151422030006ee815095f3c46578023d3dd227c29e6','SYS0101',4,0,'CON_104851678678','Gilianda-001',4,NULL,'dw160001','160001','',1,5,'测试',30,'男','','','','','','','',NULL,'2019-02-21 00:00:00.000000','2029-12-30 00:00:00.000000','2019-03-30 11:16:38.000000',1,NULL,'','',NULL,'67f03ac1de234ef29004aff3d1a4d228','65d31e22aa7025c45e8132128a7f0d01','01′\0\0\0\0\0\0\0\0a?7?′?￡???=mè*=?=S??=ò±?S?t?Pb??F6Y??¨?:PR>o???a???B?=-ü??à??k|￥????<íá:?O&??p??á7?ácD??Pè=?8?Xá=??=hI#=me??ó5^=Qμ??Ba9???ù?19L?yR|?3???á?é=9\0>ee=??=4??\r??=?s?<????p=?|￠???c?\Z9\Z??÷?ê?o??·J<?W???e?{ >????{y???6A<&?\'?oN±=?b????¤?F[=`2???-??_ˉ=/D??μí<A?#=s??t\'?Zí^??íx???x=Tt￡=?8?8?T??=yB(?pSá?	èi?H?D?ú?S?9b=o???#;??DY=ú9+?~Iq??~??q[???Fw=???wl?a?e??F?D|q?aê\n?í?n=JLà<{8?=%a\Z?m??=?y?<?D>????áB;??9??ˉ?=?-?±?A?ê<?vé<ˉ?2?)?e?3b¤??7?<Rùi=μi)?????d??\n|??hR??<\r???&9÷:3Z???.D<*ó<=óQJ?è? ?u#=}<Y???g??O=?c=áì?<	§???)2<?~???=ò_o??￡?=rtó<?*?=\"I?=?6á?s￥<)n???a><ê^??a?o\0>[R?<ì-D<×%?<9y??′3?ùM??X3?A?????Y?-????á\0?ì°;?~|??à?gh1?3?p=°G′=C0?<{?\Z??(???ì?<6Q??? ???G=vk??\'??????=X?2<Má?ò??=×ú<\ZB??é8?<′]<C;?{è</?à=p)??0(§?{AJ?\r?.=??\0=D%???v=]<Dò???Oˉ?_×??j??;??>?ùA<òM????Q?à?￠<b`è=Qù??Ow9=èJa?x/?=\0?=íc′=aà>?4G???nD?\nY=é>mg9?2?r??L???r??(8=I?v<3?=???=?B?<???T:?,??hêI?àí???=G￠??e?==?D?\n??y?G?\n?=?-?×h???#?êm<??ˉ=-j????±?ù??=tèD=?L?=?×(=òA$?ù#ò<???,?è=\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,'','','',NULL,NULL,NULL,NULL,'Gilianda-001','',1,1,'1'),('2019041514220300096ec08ba926c418a8120d1f0b5dcccfd','SYS0101',8,0,'CON_093746267267','Gilianda-001',6,NULL,'dw123456','123456','',1,3,'XYZ',28,'男','1234556779x','','','','','','',NULL,'2019-04-12 00:00:00.000000','2029-12-30 00:00:00.000000','2019-04-12 09:38:38.000000',1,NULL,'c840765a1b198c55354e60877ad6296f','01′\0\0\0\0\0\0\0\0?J????:n=?X=y/ì?.\r>2vn?à?j;á\r<???(?¤é?=à{W?P??=??+=(￡?Y?M=ú??<j^@<ù?<í?,=?ê?{?!?G#=?x<?±-=±·d=?±ê<PPo???H?????2=M*&??	\0?éP??6?2?à=|ì?=????i=?y;>\n?==2?<?à9?ià??Zí?H8ü;_???A??9?<D??=U{ú;?ù?=1′\n=M?l=t?′=°Y<:V<e?\"=?<?F~5<^áG<T??=·?\"<?é??	fV?0Q?y?????J;=3á?M￥=l.?;Ty?44￠=2A?é??p?g=êμa;?????o=??T1?Kn??8?y ?±e?=R?^?~à???ì=èz{;??í\0-?[?<k?=I_??_é?=???á?àR<=?u?T?<=án???75?sD?=ágY=?R??¤?.=μE!?@?áo<%i??U=_y??Z???óà?!;=???????<?=S???=1z=????Lc=\"v?=z]?=*?????#où?2=át,?G?×?1i?=\n!<?<á?pq=?:7a<????hI<>à8=￡?=ì~??<]=èù????=?N1??à?,???TM?n?§?\r2×=kK=?μ;\"?=??=?mj=?Ha=Pi?=)￠w<Z}?1T?=%??í???í?q?82?=Yá#:±?????;=b~?aEq?1S?=>?ó9=???=Dù =??;z?ù<??=??ú<f6?)?<^I.oùJ-?òò??q??fQ??ú\Zè?F?ü?>b??&?o3??$ó??a1<4ó?=?ü￥<y±a?????7??′?;>?|?#?ˉ<9ì=?Yê??-@?á>ú??;á?????út?\n?>ü?==gμ}<y?<;?\0??cè=üe??h?;??<?Th=`?<e*?<??;|￡&>f?;?H?o·=\nP?<????J?????§o?o?\0??Cé?1ò?}=??üIa?.?ˉ??t?=?′?U!=|??t??= ê?= p???@|???>??￡t÷??k9??íó?A￡;??v????=???=êvˉ=u?g|? Fì?¤1y?]?\0\0??\0\0\0\0xü3?	\0\0\0Pü3?\0\0\0ày3?\0\0\0\0\0\0\0\0\0\0\0\0\0C\0\0\0B\0\0-C\0\0PA\0??C\0\0B\0\0\0\0\0-C\0\0\0A\0??C\0\0 B\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0-C\0\0\0A\0\0\0\0\0\0??\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0-C\0\0PA\0??C\0\0B\0\0\0\0\0-C\0\0\0A\0??C\0\0 B\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0-C\0\0\0A\0\0\0\0\0\0??\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0xü3?	\0\0\0Pü3?\0\0\0ày3?\0\0\0\0\0\0\0\0\0\0\0\0\0eC\0\0VCxü3?	\0\0\0Pü3?\0\0\0ày3?\0\0\0\0\0\0\0\0\0\0\0\0\0@B\0\0@Bxü3?	\0\0\0xü3?\0\0\0xü3?\0\0\0xü3?\0\0\0xü3?\0\0\0xü3?\0\0\0xü3?\0\0\0xü3?\0\0\0\0\0\0\0??\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0o\0\0\0\0\0o\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0ìU\0\0\0\0\0ìU\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0	7\0\0\0\0\0	7\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0nB\0\0\0\0\0nB\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0á\0\0\0\0\0á\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0)\0\0\0\0\0)\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0lè\0\0\0\0\0\0lè\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0§ú\0\0\0\0\0\0§ú\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0lè\0\0\0\0\0\0lè\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?ù\0\0\0\0\0\0?ù\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?ù\0\0\0\0\0\0?ù\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0x?\0\0\0\0\0\0x?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?ù\0\0\0\0\0\0?ù\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0Y\0\0\0\0\0\0Y\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0x?\0\0\0\0\0\0x?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0H?\0\0\0\0\0\0H?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0×?\0\0\0\0\0\0×?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\01?\0\0\0\0\0\01?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0-ò\0\0\0\0\0\0-ò\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0e?\0\0\0\0\0\0e?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\05?\0\0\0\0\0\05?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0[?\0\0\0\0\0\0[?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0á?\0\0\0\0\0á?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0M?\0\0\0\0\0M?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\02\0\0\0\0\02\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0??\0\0\0\0\0??\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?á\0\0\0\0\0\0?á\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0-ò\0\0\0\0\0\0-ò\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?ù\0\0\0\0\0\0?ù\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?ó\0\0\0\0\0\0?ó\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0U×\0\0\0\0\0\0U×\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0B?\0\0\0\0\0\0B?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0Yn\0\0\0\0\0Yn\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?\0\0\0\0\0?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\06?\0\0\0\0\06?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0D?\0\0\0\0\0D?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?\"\0\0\0\0\0?\"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0ks\0\0\0\0\0ks\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0;\0\0\0\0\0\0;\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0A\n\0\0\0\0\0\0A\n\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0á\0\0\0\0\0á\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0|\0\0\0\0\0\0|\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0	\0\0\0\0\0\0	\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0?\0\0\0\0\0\0?\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0????)[\0\0FinishPhase\0s\0dLocal[\0\0cationStacks\0+??UWí??¨t??e??Z\0\0?Pè=cn?>?0(?\nà`??￡????????fêó?fêó?3\Zí????íq>t?>?0(?à·d?@O??????J??fêó?fêó?-???8#??íq>′Y?>???ˉ d?S???S????t??í??ìê???Q??￥I?K:ò=R{:>à??>yFV?ùm??ùm??z????2?t????$D?Z?-?&?,?D?n<?í?>,ì\n???7?b￠W?z?????????????×?¨??R-¤??ú?$?I>G?>G?>b￠W??Cb?l?????a?à???k?????8?ò?O>?O?>\nB?>Où)?Où)?\0?;Q?X=à?J=?>e?×=???<u??=??3>j->è+=è+=à\r?<?￠=>ê?Q>\nHW=°o{=?Si=a?]=??l=?i=@I=?uà<-?>-?>?B>?|^>1?>??\">a>?>ù3>HU×>HU×>-?>-?>òq=?|^>1?>??\">a>òvi>2?>HU×>HU×>??=+\n?=$Z>?20=?ey=o?=?t=?t=¨%?<ì?=èJ?=t/?=??=$Z>?20=?6=o?=?t=?t=?C°<ì?=èJ?=áX\0\0h Q1h Q1\0\0\0\0\0\0\0\0H?é?\0\0\0Kú?>?6?>%/k·[A·ct°?ü\03=]??]???S??<???k?@k?@Qà??íy¤?à÷?à÷?\n??§???èó?D÷è?t @t @rêê?íy¤?à÷?à÷?J-?z?=ó??>D÷è?t @t @rêê??M/?ê???ê????9??z?=áA?·±??>nG>?nG>??[?·Yú?>￠^??￠^??oox·2C?·xó?·??μ??H>?(??B?%@e?B@e?B@ ?μ??·?í\r·ea	?′4?=??H>?(??B?%@e?B@e?B@ ?μ??c·?ù >??·′4?=3e???3???3??oa???d??k??8??|?!@V???`·3e???3???3??oa???d??k??$?o?PJ@?1	?\n·X>&¨S>&¨S>\'ê>áùa>`è?<?+ μ§?&@±?^@èYj?á~d?Q`5?CU?|+2=\0\0\0p?w?',NULL,'','','',NULL,'','','',NULL,NULL,NULL,NULL,'Gilianda-001','',1,1,'1'),('20190415142203000e1af9880a6a2469d916f7e90f02a6635','SYS0101',2,0,'CON_115017189189','Gilianda-001',2,NULL,'dw18438','18438','',1,0,'N18438',30,'男',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2019-02-16 00:00:00.000000','2029-12-30 00:00:00.000000','2019-03-02 10:25:49.000000',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Gilianda-001',NULL,1,1,'1'),('20190415142203000e21c0d03f828439a903daa7ed97c786e','SYS0101',9,0,'CON_093746267267','Gilianda-001',7,NULL,'dw160003','160003','',1,3,'160003',28,'男','1234556779x','','','','','','',NULL,'2019-04-12 00:00:00.000000','2029-12-30 00:00:00.000000','2019-04-12 09:38:38.000000',1,NULL,'c840765a1b198c55354e60877ad6296f','01′',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,1,'1');
/*!40000 ALTER TABLE `ls_consumer` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger staff after insert
on ls_consumer for each row
begin
insert into tb_staff(id, sysid, group_number, name, sex, age, address, phone, id_card, time, company, id_organ, department_id, is_used, part_id) values(new.card_no, new.sysid, new.group_number, new.names, new.gender, new.age, new.address, new.phone, new.id_number, new.start_date, new.unit, new.id_organ, new.group_number, new.is_used, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_group`
--

DROP TABLE IF EXISTS `ls_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_group` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `theid` varchar(20) NOT NULL,
  `area_name` varchar(20) DEFAULT NULL,
  `number` int(11) NOT NULL,
  `department` varchar(200) DEFAULT NULL,
  `group_name` varchar(200) NOT NULL,
  `remarks` varchar(800) DEFAULT NULL,
  `update_status` int(11) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_group_sysid_id_a9bf4758_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_group`
--

LOCK TABLES `ls_group` WRITE;
/*!40000 ALTER TABLE `ls_group` DISABLE KEYS */;
INSERT INTO `ls_group` VALUES ('2019041514215100000f7c23f0de84838a9e2c69d0f09dac3','SYS0101',13,'GRO_12114344627627','Gilianda-001',12,'默认部门','普工班组',NULL,1,0,1,'1'),('2019041514215100002df0791dcee419fbb92724e093e69e9','SYS0101',6,'GRO_5114344612612','Gilianda-001',5,'默认部门','开挖班组',NULL,1,0,1,'1'),('201904151421510000a924aa350b34d20824f4f2800c1eb1a','SYS0101',12,'GRO_11114344625625','Gilianda-001',11,'默认部门','车辆班组',NULL,1,0,1,'1'),('201904151421510000ab91ab6769845cca3d87fc92c53ce9e','SYS0101',4,'GRO_3114344593593','Gilianda-001',3,'默认部门','来宾人员',NULL,1,0,1,'1'),('20190415142151000139c09c7d7894624bc728227033cbe18','SYS0101',9,'GRO_8114344618618','Gilianda-001',8,'默认部门','喷浆班组',NULL,1,0,1,'1'),('20190415142151000499feb8ed5eb469bb7035b9963172183','SYS0101',8,'GRO_7114344616616','Gilianda-001',7,'默认部门','二衬班组',NULL,1,0,1,'1'),('2019041514215100050521794f69f45ccbbb7986e41d908bd','SYS0101',10,'GRO_9114344621621','Gilianda-001',9,'默认部门','电工班组',NULL,1,0,1,'1'),('201904151421510008cb407eaffcd4ceda0753478223898df','SYS0101',11,'GRO_10114344623623','Gilianda-001',10,'默认部门','出碴班组',NULL,1,0,1,'1'),('20190415142151000cd1a308cd6c943ea9cc404fee06b0f39','SYS0101',5,'GRO_4114344595595','Gilianda-001',4,'默认部门','测量班组',NULL,1,0,1,'1'),('20190415142151000d79212999a75497d99d945a20c8b4adf','SYS0101',1,'GRO_1114344536536','Gilianda-001',0,'默认部门','未定义班组',NULL,1,0,1,'1'),('20190415142151000e49f1a55a8ac470b9b19ce8772a81096','SYS0101',3,'GRO_211434459059','Gilianda-001',2,'默认部门','监理单位',NULL,1,0,1,'1'),('20190415142151000f8b5474d1ef347d5bc4eadcfb1f2cfff','SYS0101',7,'GRO_6114344614614','Gilianda-001',6,'默认部门','支护班组',NULL,1,0,1,'1');
/*!40000 ALTER TABLE `ls_group` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger department after insert
on ls_group for each row
begin
insert into tb_department(id, sysid, department, group_name, update_status, is_used, part_id) values(new.number, new.sysid, new.department, new.group_name, new.update_status, new.is_used, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_location_card`
--

DROP TABLE IF EXISTS `ls_location_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_location_card` (
  `my_uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `card_id` int(11) NOT NULL,
  `uuid` int(11) NOT NULL,
  `utype` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `update_time` datetime(6) NOT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`my_uuid`),
  UNIQUE KEY `ls_location_card_sysid_id_d91b6b19_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_location_card`
--

LOCK TABLES `ls_location_card` WRITE;
/*!40000 ALTER TABLE `ls_location_card` DISABLE KEYS */;
/*!40000 ALTER TABLE `ls_location_card` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger locationcard after insert
on ls_location_card for each row
begin
insert into tb_location_card(id, sysid, card_id, uuid, utype, status, time) values(new.my_uuid, new.sysid, new.card_id, new.uuid, new.utype, new.status, new.update_time);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_mycargooutrecord`
--

DROP TABLE IF EXISTS `ls_mycargooutrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_mycargooutrecord` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `cardid` varchar(30) NOT NULL,
  `cardnumber` varchar(20) DEFAULT NULL,
  `intime` datetime(6) DEFAULT NULL,
  `outtime` datetime(6) DEFAULT NULL,
  `inplace` varchar(100) DEFAULT NULL,
  `outplace` varchar(100) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_mycargooutrecord_sysid_id_94205bd4_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_mycargooutrecord`
--

LOCK TABLES `ls_mycargooutrecord` WRITE;
/*!40000 ALTER TABLE `ls_mycargooutrecord` DISABLE KEYS */;
INSERT INTO `ls_mycargooutrecord` VALUES ('201904111734040003b741c5ac2b7463b85ac01b99ef13d62','SYS0101',111,'006A2924-20190402','6666666','2019-04-02 17:10:00.000000','2019-04-02 17:13:00.000000','集成控制1脱机','集成控制1脱机',0,'1');
/*!40000 ALTER TABLE `ls_mycargooutrecord` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger carrecord after insert
on ls_mycargooutrecord for each row
begin
insert into tb_car_record(id, sysid, cardid, cardnumber, inplace, intime, outplace, outtime, part_id) values(new.uuid, new.sysid, new.cardid, new.cardnumber, new.inplace, new.intime, new.outplace, new.outtime, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_myfaxingssue`
--

DROP TABLE IF EXISTS `ls_myfaxingssue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_myfaxingssue` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `kphm` varchar(30) NOT NULL,
  `rybh` varchar(30) NOT NULL,
  `kpzt` varchar(1) DEFAULT NULL,
  `cckl` varchar(20) DEFAULT NULL,
  `ccfxrq` datetime(6) DEFAULT NULL,
  `ccfxrkh` varchar(30) DEFAULT NULL,
  `ccyxqr` datetime(6) DEFAULT NULL,
  `ccyxzr` datetime(6) DEFAULT NULL,
  `cphm` varchar(20) DEFAULT NULL,
  `clys` bigint(20) DEFAULT NULL,
  `clxh` varchar(100) DEFAULT NULL,
  `cccw` varchar(100) DEFAULT NULL,
  `cctkrq` datetime(6) DEFAULT NULL,
  `cctkrkh` varchar(30) DEFAULT NULL,
  `ccyxjh` varchar(256) DEFAULT NULL,
  `ccyxqh` varchar(16) DEFAULT NULL,
  `clbz` varchar(255) DEFAULT NULL,
  `mjkl` varchar(20) DEFAULT NULL,
  `mjfxrq` datetime(6) DEFAULT NULL,
  `mjfxrkh` varchar(30) DEFAULT NULL,
  `mjjsrq` datetime(6) DEFAULT NULL,
  `yxkssj` varchar(2) DEFAULT NULL,
  `yxjssj` varchar(2) DEFAULT NULL,
  `mjyxjh` varchar(256) DEFAULT NULL,
  `mjtkrq` datetime(6) DEFAULT NULL,
  `mjtkrkh` varchar(30) DEFAULT NULL,
  `mjbz` varchar(255) DEFAULT NULL,
  `fxrq` datetime(6) DEFAULT NULL,
  `tkrq` datetime(6) DEFAULT NULL,
  `fxrkh` varchar(30) DEFAULT NULL,
  `tkrkh` varchar(30) DEFAULT NULL,
  `gsrq` datetime(6) DEFAULT NULL,
  `gsrkh` varchar(30) DEFAULT NULL,
  `kpwlh` varchar(30) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_myfaxingssue_sysid_kphm_d2f89aca_uniq` (`sysid`,`kphm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_myfaxingssue`
--

LOCK TABLES `ls_myfaxingssue` WRITE;
/*!40000 ALTER TABLE `ls_myfaxingssue` DISABLE KEYS */;
/*!40000 ALTER TABLE `ls_myfaxingssue` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger carinfo after insert
on ls_myfaxingssue for each row
begin
insert into tb_car_msg(id, sysid, cphm, clys, clxh, part_id) values(new.uuid, new.sysid, new.cphm, new.clys, new.clxh, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_screen`
--

DROP TABLE IF EXISTS `ls_screen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_screen` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `theid` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `nControlType` int(11) NOT NULL,
  `nScreenNo` int(11) NOT NULL,
  `nSendMode` int(11) DEFAULT NULL,
  `pScreenName` varchar(150) DEFAULT NULL,
  `nWidth` int(11) NOT NULL,
  `nHeight` int(11) NOT NULL,
  `nScreenType` int(11) NOT NULL,
  `nPixelMode` int(11) NOT NULL,
  `nDataDA` int(11) NOT NULL,
  `nDataOE` int(11) NOT NULL,
  `nRowOrder` int(11) NOT NULL,
  `nDataFlow` int(11) DEFAULT NULL,
  `nFreqPar` double NOT NULL,
  `pCom` varchar(50) DEFAULT NULL,
  `nBaud` int(11) DEFAULT NULL,
  `pSocketIP` varchar(50) DEFAULT NULL,
  `nSocketPort` int(11) DEFAULT NULL,
  `nStaticIPMode` int(11) DEFAULT NULL,
  `nServerMode` int(11) DEFAULT NULL,
  `pBarcode` varchar(50) DEFAULT NULL,
  `pNetworkID` varchar(50) DEFAULT NULL,
  `pServerIP` varchar(50) DEFAULT NULL,
  `nServerPort` int(11) DEFAULT NULL,
  `pServerAccessUser` varchar(50) DEFAULT NULL,
  `pServerAccessPassword` varchar(50) DEFAULT NULL,
  `pWiFiIP` varchar(50) DEFAULT NULL,
  `nWiFiPort` int(11) DEFAULT NULL,
  `pGprsIP` varchar(50) DEFAULT NULL,
  `nGprsPort` int(11) DEFAULT NULL,
  `pGprsID` varchar(50) DEFAULT NULL,
  `pScreenStatusFile` varchar(50) DEFAULT NULL,
  `remarks` varchar(250) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_screen_sysid_id_4026a920_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_screen`
--

LOCK TABLES `ls_screen` WRITE;
/*!40000 ALTER TABLE `ls_screen` DISABLE KEYS */;
/*!40000 ALTER TABLE `ls_screen` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger LED after insert
on ls_screen for each row
begin
insert into tb_led_info(id, sysid, area_name, nScreenNo, pScreenName, nWidth, nHeight, nScreenType, nPixelMode, ip, port, is_used, part_id) values(new.uuid, new.sysid, new.area_name, new.nScreenNo, new.pScreenName, new.nWidth, new.nHeight, new.nScreenType, new.nPixelMode, new.pSocketIP, new.nSocketPort, new.is_used, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ls_swipe_record`
--

DROP TABLE IF EXISTS `ls_swipe_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ls_swipe_record` (
  `uuid` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `update_status` int(11) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `swipe_image` varchar(100) DEFAULT NULL,
  `ny` double DEFAULT NULL,
  `nx` double DEFAULT NULL,
  `rssi_vale` int(11) DEFAULT NULL,
  `swipe_status` varchar(4) DEFAULT NULL,
  `inouts` varchar(4) NOT NULL,
  `reader_no` int(11) NOT NULL,
  `door_no` int(11) NOT NULL,
  `zone_name` varchar(100) DEFAULT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `names` varchar(15) DEFAULT NULL,
  `device_sn` varchar(18) NOT NULL,
  `group_number` int(11) DEFAULT NULL,
  `card_no` varchar(10) NOT NULL,
  `pattern_card` varchar(13) NOT NULL,
  `theid` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `part_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `ls_swipe_record_sysid_id_9a9851b5_uniq` (`sysid`,`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ls_swipe_record`
--

LOCK TABLES `ls_swipe_record` WRITE;
/*!40000 ALTER TABLE `ls_swipe_record` DISABLE KEYS */;
INSERT INTO `ls_swipe_record` VALUES ('2019041514221400011ebe290ee1e436489fb3c356d91ced8','SYS0101',332,0,0,'2019-04-12 09:15:45.000000',NULL,0,0,0,'F1','in',1,1,'全部区域','人脸识别1','测试员','84E0F42096D800B0',4,'160002','dw160002','SWR_091545031031','Gilianda-001','1'),('2019041514221400012e080c97e7643e3b2be4d53ac5ee98a','SYS0101',331,0,0,'2019-04-12 08:59:13.000000',NULL,0,0,0,'F2','out',1,1,'全部区域','人脸识别2','测试员','84E0F4209A5300B0',4,'160002','dw160002','SWR_085913159159','Gilianda-001','1'),('20190415142214000211d79644ac44c50abd2682b1098fc7d','SYS0101',337,0,0,'2019-04-12 09:41:26.000000',NULL,0,0,0,'F2','out',1,1,'全部区域','人脸识别2','XYZ','84E0F4209A5300B0',3,'123456','dw123456','SWR_094126023023','Gilianda-001','1'),('201904151422140005e25ae86452f474ca90df4fbc8ac3c75','SYS0101',335,0,0,'2019-04-12 09:35:22.000000',NULL,0,0,0,'F1','in',1,1,'全部区域','人脸识别1','YY','84E0F42096D800B0',3,'160003','dw160003','SWR_09352261061','Gilianda-001','1'),('20190415142214000efe1f934d1ac4e7ca571b2639cfc07f3','SYS0101',333,0,0,'2019-04-12 09:23:41.000000',NULL,0,0,0,'F1','in',1,1,'全部区域','人脸识别1','888855','84E0F42096D800B0',7,'160004','dw160004','SWR_092341114114','Gilianda-001','1'),('20190415142214000f0928b605f1a41048f6e4398071110ff','SYS0101',336,0,0,'2019-04-12 09:38:49.000000',NULL,0,0,0,'F1','in',1,1,'全部区域','人脸识别1','XYZ','84E0F42096D800B0',3,'123456','dw123456','SWR_093849838838','Gilianda-001','1');
/*!40000 ALTER TABLE `ls_swipe_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = gbk */ ;
/*!50003 SET character_set_results = gbk */ ;
/*!50003 SET collation_connection  = gbk_chinese_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 trigger staffrecord after insert
on ls_swipe_record for each row
begin
insert into tb_staff_record(id, sysid, zone_name, device_name, names, group_number, inouts, time, card_number, part_id) values(new.uuid, new.sysid, new.zone_name, new.device_name, new.names, new.group_number, new.inouts, new.update_time, new.card_no, new.part_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `rest_framework_tracking_apirequestlog`
--

DROP TABLE IF EXISTS `rest_framework_tracking_apirequestlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rest_framework_tracking_apirequestlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `requested_at` datetime(6) NOT NULL,
  `response_ms` int(10) unsigned NOT NULL,
  `path` varchar(200) NOT NULL,
  `remote_addr` char(39) NOT NULL,
  `host` varchar(200) NOT NULL,
  `method` varchar(10) NOT NULL,
  `query_params` longtext,
  `data` longtext,
  `response` longtext,
  `status_code` int(10) unsigned DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `view` varchar(200) DEFAULT NULL,
  `view_method` varchar(27) DEFAULT NULL,
  `errors` longtext,
  PRIMARY KEY (`id`),
  KEY `rest_framework_tracking_apirequestlog_requested_at_b6f1c2f2` (`requested_at`),
  KEY `rest_framework_tracking_apirequestlog_path_fe81f91b` (`path`),
  KEY `rest_framework_tracking_apirequestlog_view_5bd1e407` (`view`),
  KEY `rest_framework_tracking_apirequestlog_view_method_dd790881` (`view_method`),
  KEY `rest_framework_track_user_id_671b70b7_fk_auth_syst` (`user_id`),
  CONSTRAINT `rest_framework_track_user_id_671b70b7_fk_auth_syst` FOREIGN KEY (`user_id`) REFERENCES `auth_system_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rest_framework_tracking_apirequestlog`
--

LOCK TABLES `rest_framework_tracking_apirequestlog` WRITE;
/*!40000 ALTER TABLE `rest_framework_tracking_apirequestlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `rest_framework_tracking_apirequestlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_folk`
--

DROP TABLE IF EXISTS `staff_folk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff_folk` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `staff_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_folk_staff_id_5d33c73e_fk_tb_staff_id` (`staff_id`),
  CONSTRAINT `staff_folk_staff_id_5d33c73e_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_folk`
--

LOCK TABLES `staff_folk` WRITE;
/*!40000 ALTER TABLE `staff_folk` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_folk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_artificial_log`
--

DROP TABLE IF EXISTS `tb_artificial_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_artificial_log` (
  `id` varchar(50) NOT NULL,
  `object` varchar(100) NOT NULL,
  `user` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_artificial_log`
--

LOCK TABLES `tb_artificial_log` WRITE;
/*!40000 ALTER TABLE `tb_artificial_log` DISABLE KEYS */;
INSERT INTO `tb_artificial_log` VALUES ('04ffae46-4d0f-421b-9666-4505a18d034f','人员信息','user_1','增加数据','2019-04-16 21:35:14.094465'),('0d4277bf-d510-4116-bbe1-6ea989c1c0b6','人员信息','user_1','修改数据','2019-04-16 22:24:45.284883'),('17eb41ad-a3d8-4fb6-a508-99a9e70295bc','人员信息','user_1','增加数据','2019-04-16 21:49:22.155470'),('1858981e-9c13-4552-8a5f-9171e1c0e31c','人员信息','user_1','修改数据','2019-04-16 22:14:30.691880'),('20d9f9ac-28c0-4577-af5e-4f849dee5792','生产设备基础信息','user_1','修改数据','2019-04-17 14:25:58.235809'),('29ea43a8-4983-4ecd-95ec-1e0b1c384c01','人员信息','user_1','修改数据','2019-04-16 22:17:53.046681'),('2a6bb2b8-b45a-4cf4-9899-a55b711bad89','人员信息','user_1','修改数据','2019-04-16 22:24:02.472483'),('3095b881-7c70-4387-9237-96e2d8506c95','人员信息','user_1','修改数据','2019-04-16 22:00:43.443674'),('3193c608-d0c4-4c42-bbc0-f5943ea8d352','人员信息','user_1','修改数据','2019-04-16 22:27:03.975284'),('337545ad-9aae-4c59-83d6-d1573064f849','人员信息','user_1','修改数据','2019-04-16 22:30:12.911685'),('35fc622d-a318-4741-aa99-f4286982aa18','人员信息','user_1','修改数据','2019-04-16 21:56:38.022673'),('3a072ec3-a0ed-4a8d-bcc6-246a5d097af8','人员信息','user_1','修改数据','2019-04-16 21:57:42.458673'),('41fc511d-8047-4e58-928f-632cf6b413e7','人员信息','user_1','修改数据','2019-04-16 22:04:17.303876'),('42437fed-0ffb-4a77-88a9-ade9f48bbcaf','生产设备基础信息','user_1','修改数据','2019-04-17 14:26:13.165009'),('44a874be-fc96-46c9-9c5e-22262c51e6de','人员信息','user_1','修改数据','2019-04-16 21:58:36.910674'),('4559e24a-459c-4d9f-8224-c89e88a2562d','人员信息','user_1','增加数据','2019-04-16 21:54:07.523072'),('4820248d-f05b-48ca-addd-d1103c75ae6e','人员信息','user_1','增加数据','2019-04-16 21:51:47.591671'),('4c6ff708-637f-4388-b57a-dfa717fac6b1','人员信息','user_1','增加数据','2019-04-16 21:46:53.312469'),('561fe961-d4e2-4c2f-bdae-3c2b512251b9','人员信息','user_1','增加数据','2019-04-16 21:37:33.120066'),('5a0fcd2b-7403-44f6-815e-648a5c387d98','人员信息','user_1','增加数据','2019-04-16 21:52:03.880071'),('61e7107b-0d54-4306-8714-528829dc09e5','人员信息','user_1','增加数据','2019-04-16 21:48:42.356870'),('687762a6-dd63-45d2-8a3d-3036a8b9f857','人员信息','user_1','增加数据','2019-04-16 21:43:39.568668'),('68bdcd3d-7ffe-4438-aae5-1eb1bac5b7bd','人员信息','user_1','增加数据','2019-04-16 21:43:54.203468'),('68c5fda3-3254-46e8-b887-63662cbc6aea','人员信息','user_1','修改数据','2019-04-16 22:23:56.591283'),('6be206d0-f363-40b5-a29a-8c052a4a94fd','人员信息','user_1','增加数据','2019-04-16 21:51:04.952871'),('6e0ff657-bd64-460e-a1e3-dd34e1a6a8d6','人员信息','user_1','修改数据','2019-04-16 22:05:59.059077'),('6fab9623-a307-4507-bbea-e7d6b54ec47a','生产设备基础信息','user_1','修改数据','2019-04-17 14:26:18.484609'),('72f9c451-a176-4387-a573-cba4ffcc1441','人员信息','user_1','增加数据','2019-04-16 21:41:39.691867'),('7fec0f02-e7ce-48f6-ac1f-194f0dc8dbd9','人员信息','user_1','增加数据','2019-04-16 21:35:37.963465'),('83bec084-61f5-4d43-b264-f617eb22786d','人员信息','user_1','修改数据','2019-04-16 22:03:25.784676'),('8621b87d-41df-449a-a4b3-358bb2aa7352','音响服务器','user_1','增加数据','2019-04-16 23:46:34.668515'),('96070bb6-dada-4bce-aa21-55f654df9b57','人员信息','user_1','修改数据','2019-04-16 22:22:01.928882'),('9d83056d-48f6-41b7-a1d5-f63218fd38ed','人员信息','user_1','增加数据','2019-04-16 21:37:11.372665'),('a34e1796-ff1a-482c-bbe2-2b20795df691','人员信息','user_1','增加数据','2019-04-16 21:48:37.224470'),('a3dd95ea-9d8d-41d5-9044-fd0b98f7bf21','人员信息','user_1','增加数据','2019-04-16 21:41:34.246467'),('ada41fe6-9324-46e2-943e-492a75fef458','人员信息','user_1','增加数据','2019-04-16 21:34:47.804465'),('b02fba94-7050-45cf-a3f7-13bf0c7e7bfc','人员信息','user_1','修改数据','2019-04-16 22:02:11.140275'),('b707f0b7-5cf5-4204-b421-d91486781f08','人员信息','user_1','增加数据','2019-04-16 21:33:42.669264'),('bfb85142-ed5e-4c85-bf31-df056a8129b5','人员信息','user_1','修改数据','2019-04-16 22:01:54.258075'),('c0ec2935-15c0-4664-b5df-cd9d7bd53712','人员信息','user_1','增加数据','2019-04-16 21:50:02.780870'),('d051fc8c-1e5f-4d71-b34e-1be11fd51330','人员信息','user_1','增加数据','2019-04-16 21:34:11.157864'),('d30676a7-60a0-4979-823d-4e4aa7822cad','人员信息','user_1','修改数据','2019-04-16 22:21:52.038482'),('d41d5d4b-817c-4b42-a5b8-a2eb194f143f','人员信息','user_1','修改数据','2019-04-16 22:31:34.496086'),('dec25fbe-f398-4b29-a164-0e88c96c7135','人员信息','user_1','增加数据','2019-04-16 21:36:52.727665'),('e538d17a-21ee-49f2-a106-4c997e87de5d','人员信息','user_1','增加数据','2019-04-16 21:35:26.981065'),('ebd87860-e078-4804-bc13-08a05df1850c','人员信息','user_1','修改数据','2019-04-16 22:27:10.840284'),('f077d17d-a6e2-4188-bf20-0e54c2d5e646','人员信息','user_1','修改数据','2019-04-16 22:09:51.303078'),('feac50af-623e-4bee-b8b6-54fae346b0be','人员信息','user_1','增加数据','2019-04-16 21:54:38.836272');
/*!40000 ALTER TABLE `tb_artificial_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_artificial_log_category`
--

DROP TABLE IF EXISTS `tb_artificial_log_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_artificial_log_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_artificial_log_category`
--

LOCK TABLES `tb_artificial_log_category` WRITE;
/*!40000 ALTER TABLE `tb_artificial_log_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_artificial_log_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_bs_tation`
--

DROP TABLE IF EXISTS `tb_bs_tation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_bs_tation` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `bs_addr` int(11) NOT NULL,
  `bs_posx` double NOT NULL,
  `bs_posy` double NOT NULL,
  `bs_posz` double NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_bs_tation_part_id_9b7ad530_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_bs_tation_part_id_9b7ad530_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_bs_tation`
--

LOCK TABLES `tb_bs_tation` WRITE;
/*!40000 ALTER TABLE `tb_bs_tation` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_bs_tation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_car_brake`
--

DROP TABLE IF EXISTS `tb_car_brake`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_car_brake` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_car_brake_part_id_d9d507cd_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_car_brake_part_id_d9d507cd_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_car_brake`
--

LOCK TABLES `tb_car_brake` WRITE;
/*!40000 ALTER TABLE `tb_car_brake` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_car_brake` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_car_msg`
--

DROP TABLE IF EXISTS `tb_car_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_car_msg` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `cphm` varchar(20) DEFAULT NULL,
  `clys` bigint(20) DEFAULT NULL,
  `clxh` varchar(100) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_car_msg_part_id_41a7746f_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_car_msg_part_id_41a7746f_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_car_msg`
--

LOCK TABLES `tb_car_msg` WRITE;
/*!40000 ALTER TABLE `tb_car_msg` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_car_msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_car_pass`
--

DROP TABLE IF EXISTS `tb_car_pass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_car_pass` (
  `id` varchar(50) NOT NULL,
  `code` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `time` datetime(6) NOT NULL,
  `car_id` varchar(50) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_car_pass_car_id_39f25585_fk_tb_car_msg_id` (`car_id`),
  KEY `tb_car_pass_part_id_c5259fc0_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_car_pass_car_id_39f25585_fk_tb_car_msg_id` FOREIGN KEY (`car_id`) REFERENCES `tb_car_msg` (`id`),
  CONSTRAINT `tb_car_pass_part_id_c5259fc0_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_car_pass`
--

LOCK TABLES `tb_car_pass` WRITE;
/*!40000 ALTER TABLE `tb_car_pass` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_car_pass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_car_record`
--

DROP TABLE IF EXISTS `tb_car_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_car_record` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `cardid` varchar(30) NOT NULL,
  `cardnumber` varchar(20) DEFAULT NULL,
  `intime` datetime(6) DEFAULT NULL,
  `outtime` datetime(6) DEFAULT NULL,
  `inplace` varchar(100) DEFAULT NULL,
  `outplace` varchar(100) DEFAULT NULL,
  `synced` int(11) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_car_record_part_id_4df37772_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_car_record_part_id_4df37772_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_car_record`
--

LOCK TABLES `tb_car_record` WRITE;
/*!40000 ALTER TABLE `tb_car_record` DISABLE KEYS */;
INSERT INTO `tb_car_record` VALUES ('201904111734040003b741c5ac2b7463b85ac01b99ef13d62','SYS0101','006A2924-20190402','6666666','2019-04-02 17:10:00.000000','2019-04-02 17:13:00.000000','集成控制1脱机','集成控制1脱机',NULL,'1');
/*!40000 ALTER TABLE `tb_car_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_caution_record`
--

DROP TABLE IF EXISTS `tb_caution_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_caution_record` (
  `id` varchar(50) NOT NULL,
  `content` varchar(200) NOT NULL,
  `time` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `device_id` varchar(50) NOT NULL,
  `disposer_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_caution_record_device_id_14f5a0ee_fk_tb_device_info_id` (`device_id`),
  KEY `tb_caution_record_disposer_id_c372d29f_fk_tb_staff_id` (`disposer_id`),
  CONSTRAINT `tb_caution_record_device_id_14f5a0ee_fk_tb_device_info_id` FOREIGN KEY (`device_id`) REFERENCES `tb_device_info` (`id`),
  CONSTRAINT `tb_caution_record_disposer_id_c372d29f_fk_tb_staff_id` FOREIGN KEY (`disposer_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_caution_record`
--

LOCK TABLES `tb_caution_record` WRITE;
/*!40000 ALTER TABLE `tb_caution_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_caution_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_company`
--

DROP TABLE IF EXISTS `tb_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_company` (
  `index` int(11) NOT NULL,
  `is_used` int(11) NOT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `boss_name` varchar(30) NOT NULL,
  `phone_num` varchar(30) NOT NULL,
  `company_address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_company`
--

LOCK TABLES `tb_company` WRITE;
/*!40000 ALTER TABLE `tb_company` DISABLE KEYS */;
INSERT INTO `tb_company` VALUES (1,1,'1','公司1','老板','13676666','公司地址'),(0,1,'4c86d709-b40c-4bc0-8f80-d4635d0a78f4','公司3','HH','1234532000','龙子湖啊'),(0,1,'c3d03bee-9e28-4713-b857-2cf418dd572e','公司2','赵飞','130000000','龙子湖');
/*!40000 ALTER TABLE `tb_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_danger`
--

DROP TABLE IF EXISTS `tb_danger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_danger` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `count` int(11) NOT NULL,
  `category_id` varchar(50) NOT NULL,
  `part_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_danger_category_id_478cd4e4_fk_tb_dangerous_category_id` (`category_id`),
  KEY `tb_danger_part_id_2499553a_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_danger_category_id_478cd4e4_fk_tb_dangerous_category_id` FOREIGN KEY (`category_id`) REFERENCES `tb_dangerous_category` (`id`),
  CONSTRAINT `tb_danger_part_id_2499553a_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_danger`
--

LOCK TABLES `tb_danger` WRITE;
/*!40000 ALTER TABLE `tb_danger` DISABLE KEYS */;
INSERT INTO `tb_danger` VALUES ('2019-04-15 13:59:43.227519','2019-04-15 13:59:43.227519',0,1,'a43bb20c-05e9-4869-b310-39fadb576778','CNC',100,'f3c20826-eb72-4e0a-81a0-48966128c2cf','1'),('2019-04-15 14:40:56.304269','2019-04-15 14:40:56.305268',0,1,'b558ec95-b325-485d-9b8e-6ec0f5ac33fe','c4',1,'d16fcaae-b907-4411-9c11-19ec7332d604','1'),('2019-04-15 11:51:11.041178','2019-04-15 11:51:11.041178',0,1,'d1f74873-642b-484c-930a-027e512de2da','炸药',20,'d16fcaae-b907-4411-9c11-19ec7332d604','1');
/*!40000 ALTER TABLE `tb_danger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_danger_used`
--

DROP TABLE IF EXISTS `tb_danger_used`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_danger_used` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `id` varchar(50) NOT NULL,
  `count` int(11) NOT NULL,
  `is_need_back` tinyint(1) NOT NULL,
  `is_back` tinyint(1) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `danger_id` varchar(50) NOT NULL,
  `manager_id` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_danger_used_danger_id_66d96081_fk_tb_danger_id` (`danger_id`),
  KEY `tb_danger_used_manager_id_f4449d75_fk_tb_staff_id` (`manager_id`),
  KEY `tb_danger_used_user_id_bd097c6a_fk_tb_staff_id` (`user_id`),
  CONSTRAINT `tb_danger_used_danger_id_66d96081_fk_tb_danger_id` FOREIGN KEY (`danger_id`) REFERENCES `tb_danger` (`id`),
  CONSTRAINT `tb_danger_used_manager_id_f4449d75_fk_tb_staff_id` FOREIGN KEY (`manager_id`) REFERENCES `tb_staff` (`id`),
  CONSTRAINT `tb_danger_used_user_id_bd097c6a_fk_tb_staff_id` FOREIGN KEY (`user_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_danger_used`
--

LOCK TABLES `tb_danger_used` WRITE;
/*!40000 ALTER TABLE `tb_danger_used` DISABLE KEYS */;
INSERT INTO `tb_danger_used` VALUES ('2019-04-16 03:47:04.449469','2019-04-16 03:47:04.449469','382d614a-b0d2-4240-a55f-38f2d3c62de1',10,0,0,'2019-04-15 18:59:43.227519',NULL,'a43bb20c-05e9-4869-b310-39fadb576778','160001','160002');
/*!40000 ALTER TABLE `tb_danger_used` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dangerous_category`
--

DROP TABLE IF EXISTS `tb_dangerous_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_dangerous_category` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dangerous_category`
--

LOCK TABLES `tb_dangerous_category` WRITE;
/*!40000 ALTER TABLE `tb_dangerous_category` DISABLE KEYS */;
INSERT INTO `tb_dangerous_category` VALUES ('2019-04-15 10:58:16.051323','2019-04-15 14:03:52.498354',0,1,'6dcd967b-242a-4c3c-9be0-49953ae92af3','腐蚀物品888'),('2019-04-15 10:57:32.732340','2019-04-15 13:52:54.465245',0,1,'d16fcaae-b907-4411-9c11-19ec7332d604','爆破品'),('2019-04-15 14:00:32.395000','2019-04-15 14:00:32.395000',0,1,'d188eca7-f900-4a18-9b0c-f9cecca01fe0','腐蚀物品14'),('2019-04-15 13:31:35.356781','2019-04-15 13:34:46.404381',0,1,'f13d9349-d97e-4082-b738-48b378f94df6','废品'),('2019-04-15 11:55:51.757601','2019-04-15 13:53:23.372494',0,1,'f3c20826-eb72-4e0a-81a0-48966128c2cf','消耗品');
/*!40000 ALTER TABLE `tb_dangerous_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_department`
--

DROP TABLE IF EXISTS `tb_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_department` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `department` varchar(200) DEFAULT NULL,
  `group_name` varchar(200) NOT NULL,
  `remarks` varchar(800) DEFAULT NULL,
  `update_status` int(11) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_department_part_id_59c21d8e_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_department_part_id_59c21d8e_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_department`
--

LOCK TABLES `tb_department` WRITE;
/*!40000 ALTER TABLE `tb_department` DISABLE KEYS */;
INSERT INTO `tb_department` VALUES (NULL,1,0,'SYS0101','默认部门1','未定义班组',NULL,1,'1'),(1,1,1,'1','默认部门2','未定义班组','1',1,'1'),(NULL,1,2,'SYS0101','默认部门3','监理单位',NULL,1,'1'),(NULL,1,3,'SYS0101','默认部门4','来宾人员',NULL,1,'1'),(NULL,1,4,'SYS0101','默认部门5','测量班组',NULL,1,'1'),(NULL,1,5,'SYS0101','默认部门6','开挖班组',NULL,1,'1'),(NULL,1,6,'SYS0101','默认部门7','支护班组',NULL,1,'1'),(NULL,1,7,'SYS0101','默认部门8','二衬班组',NULL,1,'1'),(NULL,1,8,'SYS0101','默认部门9','喷浆班组',NULL,1,'1'),(NULL,1,9,'SYS0101','默认部门','电工班组',NULL,1,'1'),(NULL,1,10,'SYS0101','默认部门','出碴班组',NULL,1,'1'),(NULL,1,11,'SYS0101','默认部门','车辆班组',NULL,1,'1'),(NULL,1,12,'SYS0101','默认部门','普工班组',NULL,1,'1');
/*!40000 ALTER TABLE `tb_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_device_category`
--

DROP TABLE IF EXISTS `tb_device_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_device_category` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_device_category`
--

LOCK TABLES `tb_device_category` WRITE;
/*!40000 ALTER TABLE `tb_device_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_device_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_device_info`
--

DROP TABLE IF EXISTS `tb_device_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_device_info` (
  `id` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `factory` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  `x` varchar(20) NOT NULL,
  `y` varchar(20) NOT NULL,
  `note` varchar(50) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  `category_id` varchar(50) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_device_info_category_id_f1b5cb3b_fk_tb_device_category_id` (`category_id`),
  KEY `tb_device_info_part_id_374a8435_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_device_info_category_id_f1b5cb3b_fk_tb_device_category_id` FOREIGN KEY (`category_id`) REFERENCES `tb_device_category` (`id`),
  CONSTRAINT `tb_device_info_part_id_374a8435_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_device_info`
--

LOCK TABLES `tb_device_info` WRITE;
/*!40000 ALTER TABLE `tb_device_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_device_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_device_upkeep`
--

DROP TABLE IF EXISTS `tb_device_upkeep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_device_upkeep` (
  `id` varchar(50) NOT NULL,
  `upkeep_man` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  `device_id` varchar(50) NOT NULL,
  `manager_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_device_upkeep_device_id_d62bd65f_fk_tb_device_info_id` (`device_id`),
  KEY `tb_device_upkeep_manager_id_dbc6cdbd_fk_tb_staff_id` (`manager_id`),
  CONSTRAINT `tb_device_upkeep_device_id_d62bd65f_fk_tb_device_info_id` FOREIGN KEY (`device_id`) REFERENCES `tb_device_info` (`id`),
  CONSTRAINT `tb_device_upkeep_manager_id_dbc6cdbd_fk_tb_staff_id` FOREIGN KEY (`manager_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_device_upkeep`
--

LOCK TABLES `tb_device_upkeep` WRITE;
/*!40000 ALTER TABLE `tb_device_upkeep` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_device_upkeep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_info`
--

DROP TABLE IF EXISTS `tb_equipment_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_info` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `factory` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `x_len` varchar(30) DEFAULT NULL,
  `y_len` varchar(30) DEFAULT NULL,
  `bought_time` datetime(6) DEFAULT NULL,
  `is_used` tinyint(1) NOT NULL,
  `mileage` double NOT NULL,
  `company_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_info_company_id_cfec6995_fk_tb_company_id` (`company_id`),
  CONSTRAINT `tb_equipment_info_company_id_cfec6995_fk_tb_company_id` FOREIGN KEY (`company_id`) REFERENCES `tb_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_info`
--

LOCK TABLES `tb_equipment_info` WRITE;
/*!40000 ALTER TABLE `tb_equipment_info` DISABLE KEYS */;
INSERT INTO `tb_equipment_info` VALUES ('1','asdd','sanron1','11','12','4','2019-04-16 09:07:40.215000',1,0,'1'),('2','的撒大','ccc','sadd1','13','25','2019-04-16 09:09:07.037000',1,0,'4c86d709-b40c-4bc0-8f80-d4635d0a78f4'),('543de141-54d6-4ced-afaa-80ceb80fd04c','hgfhfg','三1','s101','12','15','2019-04-15 06:14:29.000000',1,0,'1'),('649de582-6532-4d1f-afd5-a7abb7a48a23','滴滴','三融','01','12','5','2019-04-15 06:16:07.000000',1,0,'1');
/*!40000 ALTER TABLE `tb_equipment_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_location`
--

DROP TABLE IF EXISTS `tb_equipment_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_location` (
  `id` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  `location_card_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_locatio_location_card_id_45c18a65_fk_tb_equipm` (`location_card_id`),
  CONSTRAINT `tb_equipment_locatio_location_card_id_45c18a65_fk_tb_equipm` FOREIGN KEY (`location_card_id`) REFERENCES `tb_equipment_location_card` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_location`
--

LOCK TABLES `tb_equipment_location` WRITE;
/*!40000 ALTER TABLE `tb_equipment_location` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_equipment_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_location_card`
--

DROP TABLE IF EXISTS `tb_equipment_location_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_location_card` (
  `id` varchar(50) NOT NULL,
  `status` int(11) NOT NULL,
  `time` datetime(6) NOT NULL,
  `equipment_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_locatio_equipment_id_2a612d2e_fk_tb_equipm` (`equipment_id`),
  CONSTRAINT `tb_equipment_locatio_equipment_id_2a612d2e_fk_tb_equipm` FOREIGN KEY (`equipment_id`) REFERENCES `tb_equipment_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_location_card`
--

LOCK TABLES `tb_equipment_location_card` WRITE;
/*!40000 ALTER TABLE `tb_equipment_location_card` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_equipment_location_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_repair`
--

DROP TABLE IF EXISTS `tb_equipment_repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_repair` (
  `id` varchar(50) NOT NULL,
  `serviceman` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  `equipment_id` varchar(50) NOT NULL,
  `manager_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_repair_equipment_id_667dfdb2_fk_tb_equipm` (`equipment_id`),
  KEY `tb_equipment_repair_manager_id_e5db1407_fk_tb_staff_id` (`manager_id`),
  CONSTRAINT `tb_equipment_repair_equipment_id_667dfdb2_fk_tb_equipm` FOREIGN KEY (`equipment_id`) REFERENCES `tb_equipment_info` (`id`),
  CONSTRAINT `tb_equipment_repair_manager_id_e5db1407_fk_tb_staff_id` FOREIGN KEY (`manager_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_repair`
--

LOCK TABLES `tb_equipment_repair` WRITE;
/*!40000 ALTER TABLE `tb_equipment_repair` DISABLE KEYS */;
INSERT INTO `tb_equipment_repair` VALUES ('1','最新韩国','2019-04-15 17:39:15.000000','543de141-54d6-4ced-afaa-80ceb80fd04c','123456'),('2','axda1','2019-04-16 09:12:18.209000','1','123456');
/*!40000 ALTER TABLE `tb_equipment_repair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_upkeep`
--

DROP TABLE IF EXISTS `tb_equipment_upkeep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_upkeep` (
  `id` varchar(50) NOT NULL,
  `upkeep_man` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  `equipment_id` varchar(50) NOT NULL,
  `manager_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_upkeep_equipment_id_99896ce0_fk_tb_equipm` (`equipment_id`),
  KEY `tb_equipment_upkeep_manager_id_a9c26d26_fk_tb_staff_id` (`manager_id`),
  CONSTRAINT `tb_equipment_upkeep_equipment_id_99896ce0_fk_tb_equipm` FOREIGN KEY (`equipment_id`) REFERENCES `tb_equipment_info` (`id`),
  CONSTRAINT `tb_equipment_upkeep_manager_id_a9c26d26_fk_tb_staff_id` FOREIGN KEY (`manager_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_upkeep`
--

LOCK TABLES `tb_equipment_upkeep` WRITE;
/*!40000 ALTER TABLE `tb_equipment_upkeep` DISABLE KEYS */;
INSERT INTO `tb_equipment_upkeep` VALUES ('1','占山','2019-04-15 17:38:52.000000','543de141-54d6-4ced-afaa-80ceb80fd04c','123456'),('2','zxaas','2019-04-16 09:11:55.499000','1','123456');
/*!40000 ALTER TABLE `tb_equipment_upkeep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_equipment_used`
--

DROP TABLE IF EXISTS `tb_equipment_used`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_equipment_used` (
  `id` varchar(50) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `equipment_id` varchar(50) NOT NULL,
  `manager_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_equipment_used_equipment_id_de587dd9_fk_tb_equipment_info_id` (`equipment_id`),
  KEY `tb_equipment_used_manager_id_515a1b5f_fk_tb_staff_id` (`manager_id`),
  KEY `tb_equipment_used_user_id_011b6143_fk_tb_staff_id` (`user_id`),
  CONSTRAINT `tb_equipment_used_equipment_id_de587dd9_fk_tb_equipment_info_id` FOREIGN KEY (`equipment_id`) REFERENCES `tb_equipment_info` (`id`),
  CONSTRAINT `tb_equipment_used_manager_id_515a1b5f_fk_tb_staff_id` FOREIGN KEY (`manager_id`) REFERENCES `tb_staff` (`id`),
  CONSTRAINT `tb_equipment_used_user_id_011b6143_fk_tb_staff_id` FOREIGN KEY (`user_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_equipment_used`
--

LOCK TABLES `tb_equipment_used` WRITE;
/*!40000 ALTER TABLE `tb_equipment_used` DISABLE KEYS */;
INSERT INTO `tb_equipment_used` VALUES ('1','2019-04-15 17:38:07.000000','2019-04-15 17:38:09.000000','543de141-54d6-4ced-afaa-80ceb80fd04c','123456','123456'),('2','2019-03-16 09:10:03.280000','2019-04-16 09:10:10.019000','1','123456','123456'),('3','2019-04-16 09:10:39.606000','2019-04-16 09:10:42.467000','1','123456','123456');
/*!40000 ALTER TABLE `tb_equipment_used` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_factory`
--

DROP TABLE IF EXISTS `tb_factory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_factory` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_factory`
--

LOCK TABLES `tb_factory` WRITE;
/*!40000 ALTER TABLE `tb_factory` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_factory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_ip_switch`
--

DROP TABLE IF EXISTS `tb_ip_switch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_ip_switch` (
  `id` varchar(50) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `port` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `note` varchar(50) DEFAULT NULL,
  `x` varchar(20) NOT NULL,
  `y` varchar(20) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_ip_switch_part_id_e6f436de_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_ip_switch_part_id_e6f436de_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_ip_switch`
--

LOCK TABLES `tb_ip_switch` WRITE;
/*!40000 ALTER TABLE `tb_ip_switch` DISABLE KEYS */;
INSERT INTO `tb_ip_switch` VALUES ('1','192.168.1.166','1234','远程电源','远程电源的备注','22','33','1');
/*!40000 ALTER TABLE `tb_ip_switch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_ip_switch_detail`
--

DROP TABLE IF EXISTS `tb_ip_switch_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_ip_switch_detail` (
  `id` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL,
  `content` varchar(100) NOT NULL,
  `note` varchar(500) DEFAULT NULL,
  `ipswitch_id` varchar(50) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_ip_switch_detail_ipswitch_id_b6eeb585_fk_tb_ip_switch_id` (`ipswitch_id`),
  KEY `tb_ip_switch_detail_part_id_3fde4a19_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_ip_switch_detail_ipswitch_id_b6eeb585_fk_tb_ip_switch_id` FOREIGN KEY (`ipswitch_id`) REFERENCES `tb_ip_switch` (`id`),
  CONSTRAINT `tb_ip_switch_detail_part_id_3fde4a19_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_ip_switch_detail`
--

LOCK TABLES `tb_ip_switch_detail` WRITE;
/*!40000 ALTER TABLE `tb_ip_switch_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_ip_switch_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_job_station`
--

DROP TABLE IF EXISTS `tb_job_station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_job_station` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_job_station`
--

LOCK TABLES `tb_job_station` WRITE;
/*!40000 ALTER TABLE `tb_job_station` DISABLE KEYS */;
INSERT INTO `tb_job_station` VALUES (1,1,'1','1');
/*!40000 ALTER TABLE `tb_job_station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_led_info`
--

DROP TABLE IF EXISTS `tb_led_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_led_info` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `nScreenNo` int(11) NOT NULL,
  `pScreenName` varchar(150) DEFAULT NULL,
  `nWidth` int(11) NOT NULL,
  `nHeight` int(11) NOT NULL,
  `nScreenType` int(11) NOT NULL,
  `nPixelMode` int(11) NOT NULL,
  `factory` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `time` datetime(6) DEFAULT NULL,
  `x` varchar(20) DEFAULT NULL,
  `y` varchar(20) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `note` varchar(50) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `is_used` tinyint(1) DEFAULT NULL,
  `ip` varchar(50) DEFAULT NULL,
  `port` varchar(10) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_led_info_part_id_e5fe9ab7_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_led_info_part_id_e5fe9ab7_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_led_info`
--

LOCK TABLES `tb_led_info` WRITE;
/*!40000 ALTER TABLE `tb_led_info` DISABLE KEYS */;
INSERT INTO `tb_led_info` VALUES ('1','1','区域',1,'1',100,50,1,1,'厂商','型号',NULL,'10','30','安装位置','备注',1,1,'192.168.1.112','5000',NULL);
/*!40000 ALTER TABLE `tb_led_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_location_card`
--

DROP TABLE IF EXISTS `tb_location_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_location_card` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `card_id` int(11) NOT NULL,
  `uuid` int(11) NOT NULL,
  `utype` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_location_card_part_id_2b7bf5c7_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_location_card_part_id_2b7bf5c7_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_location_card`
--

LOCK TABLES `tb_location_card` WRITE;
/*!40000 ALTER TABLE `tb_location_card` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_location_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_method`
--

DROP TABLE IF EXISTS `tb_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_method` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `people` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `time` date NOT NULL,
  `use_message` tinyint(1) NOT NULL,
  `message_content` varchar(100) DEFAULT NULL,
  `set_light` int(11) NOT NULL,
  `set_ling` int(11) NOT NULL,
  `set_voice` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_method`
--

LOCK TABLES `tb_method` WRITE;
/*!40000 ALTER TABLE `tb_method` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_model`
--

DROP TABLE IF EXISTS `tb_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_model` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_model`
--

LOCK TABLES `tb_model` WRITE;
/*!40000 ALTER TABLE `tb_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_monitor_info`
--

DROP TABLE IF EXISTS `tb_monitor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_monitor_info` (
  `id` varchar(50) NOT NULL,
  `number` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `factory` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  `x` varchar(20) NOT NULL,
  `y` varchar(20) NOT NULL,
  `note` varchar(50) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `port` varchar(10) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_monitor_info_part_id_1ee706d2_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_monitor_info_part_id_1ee706d2_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_monitor_info`
--

LOCK TABLES `tb_monitor_info` WRITE;
/*!40000 ALTER TABLE `tb_monitor_info` DISABLE KEYS */;
INSERT INTO `tb_monitor_info` VALUES ('1','1','监控1','厂家1','型号1','2019-04-16 09:45:06.019000','1','1','监控1的备注',1,1,'192.168.0.111','111','1');
/*!40000 ALTER TABLE `tb_monitor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_music`
--

DROP TABLE IF EXISTS `tb_music`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_music` (
  `id` varchar(50) NOT NULL,
  `note` varchar(100) NOT NULL,
  `path` varchar(100) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_music`
--

LOCK TABLES `tb_music` WRITE;
/*!40000 ALTER TABLE `tb_music` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_music` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_part`
--

DROP TABLE IF EXISTS `tb_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_part` (
  `index` int(11) NOT NULL,
  `is_used` int(11) NOT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `manager` varchar(30) DEFAULT NULL,
  `manager_phone` varchar(30) DEFAULT NULL,
  `map_path` varchar(100) DEFAULT NULL,
  `project_id` varchar(50) DEFAULT NULL,
  `sysid` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_part_project_id_99897f5b_fk_tb_project_id` (`project_id`),
  CONSTRAINT `tb_part_project_id_99897f5b_fk_tb_project_id` FOREIGN KEY (`project_id`) REFERENCES `tb_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_part`
--

LOCK TABLES `tb_part` WRITE;
/*!40000 ALTER TABLE `tb_part` DISABLE KEYS */;
INSERT INTO `tb_part` VALUES (1,1,'1','工区1','工区经理','13676997634','maps/part_map.png','1','');
/*!40000 ALTER TABLE `tb_part` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_prior_scheme`
--

DROP TABLE IF EXISTS `tb_prior_scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_prior_scheme` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `path` varchar(100) NOT NULL,
  `download_times` int(11) NOT NULL,
  `reate_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `staff_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_prior_scheme_staff_id_a7e070e1_fk_tb_staff_id` (`staff_id`),
  CONSTRAINT `tb_prior_scheme_staff_id_a7e070e1_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_prior_scheme`
--

LOCK TABLES `tb_prior_scheme` WRITE;
/*!40000 ALTER TABLE `tb_prior_scheme` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_prior_scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_problem`
--

DROP TABLE IF EXISTS `tb_problem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_problem` (
  `id` varchar(50) NOT NULL,
  `people` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `describe` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_problem`
--

LOCK TABLES `tb_problem` WRITE;
/*!40000 ALTER TABLE `tb_problem` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_problem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_project`
--

DROP TABLE IF EXISTS `tb_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_project` (
  `index` int(11) NOT NULL,
  `is_used` int(11) NOT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `manager` varchar(30) DEFAULT NULL,
  `manager_phone` varchar(30) DEFAULT NULL,
  `company_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_project_company_id_04e5a18b_fk_tb_company_id` (`company_id`),
  CONSTRAINT `tb_project_company_id_04e5a18b_fk_tb_company_id` FOREIGN KEY (`company_id`) REFERENCES `tb_company` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_project`
--

LOCK TABLES `tb_project` WRITE;
/*!40000 ALTER TABLE `tb_project` DISABLE KEYS */;
INSERT INTO `tb_project` VALUES (1,1,'1','工程1','张三','1367688777','1'),(0,1,'60cf0678-9ff0-46e9-a3d5-983f0ebab0e7','项目2','赵飞','13478945612','4c86d709-b40c-4bc0-8f80-d4635d0a78f4'),(0,1,'8d1c537d-926d-402e-af26-2f59658049fe','项目①','曹华振','12345678900','c3d03bee-9e28-4713-b857-2cf418dd572e'),(0,1,'c25d3951-d233-409f-9c3c-e03506ce0a74','项目3','姚毅','1346797946','1');
/*!40000 ALTER TABLE `tb_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_special_scheme`
--

DROP TABLE IF EXISTS `tb_special_scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_special_scheme` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `path` varchar(100) NOT NULL,
  `download_times` int(11) NOT NULL,
  `reate_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `staff_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_special_scheme_staff_id_0f8d5df0_fk_tb_staff_id` (`staff_id`),
  CONSTRAINT `tb_special_scheme_staff_id_0f8d5df0_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_special_scheme`
--

LOCK TABLES `tb_special_scheme` WRITE;
/*!40000 ALTER TABLE `tb_special_scheme` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_special_scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_staff`
--

DROP TABLE IF EXISTS `tb_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_staff` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `id_organ` varchar(300) DEFAULT NULL,
  `company` varchar(200) DEFAULT NULL,
  `group_number` int(11) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `sex` varchar(5) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `birth_place` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `id_card` varchar(18) DEFAULT NULL,
  `id_card_photo` varchar(100) DEFAULT NULL,
  `card_photo` varchar(100) DEFAULT NULL,
  `medical_history` varchar(50) DEFAULT NULL,
  `state` tinyint(1) DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  `time` date DEFAULT NULL,
  `is_used` smallint(6) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `job_station_id` varchar(50) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_staff_job_station_id_09897341_fk_tb_job_station_id` (`job_station_id`),
  KEY `tb_staff_department_id_58777d19_fk_tb_department_id` (`department_id`),
  KEY `tb_staff_part_id_c55ef814_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_staff_department_id_58777d19_fk_tb_department_id` FOREIGN KEY (`department_id`) REFERENCES `tb_department` (`id`),
  CONSTRAINT `tb_staff_job_station_id_09897341_fk_tb_job_station_id` FOREIGN KEY (`job_station_id`) REFERENCES `tb_job_station` (`id`),
  CONSTRAINT `tb_staff_part_id_c55ef814_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_staff`
--

LOCK TABLES `tb_staff` WRITE;
/*!40000 ALTER TABLE `tb_staff` DISABLE KEYS */;
INSERT INTO `tb_staff` VALUES ('123456','SYS0101','','asd',3,'XYZ','男',28,NULL,'','','1234556779x',NULL,NULL,NULL,NULL,NULL,'2019-04-12',1,3,NULL,'1'),('15cf826c-e7df-4ce3-9456-92c6969350c0','',NULL,'阿瓦达',NULL,'赵飞01','0',25,'河南','金水区','17533153553','123456789012345678','','','无',1,'note',NULL,1,1,'1','1'),('160001','SYS0101','','达到',5,'测试','男',30,NULL,'','','',NULL,NULL,NULL,NULL,NULL,'2019-02-21',1,5,NULL,'1'),('160002','SYS0101','','打',4,'测试员','男',30,NULL,'','','',NULL,NULL,NULL,NULL,NULL,'2019-02-21',1,4,NULL,'1'),('160003','SYS0101','','大苏打',3,'160003','男',28,NULL,'','','1234556779x',NULL,NULL,NULL,NULL,NULL,'2019-04-12',1,3,NULL,'1'),('160004','SYS0101','','打打',3,'160004','男',28,NULL,'','','1234556779x',NULL,NULL,NULL,NULL,NULL,'2019-04-12',1,3,NULL,'1'),('16479','SYS0101',NULL,'大苏打',0,'N16479','男',30,NULL,NULL,'18637985630',NULL,NULL,NULL,NULL,NULL,NULL,'2019-02-16',1,0,NULL,'1'),('164790','1','1','大苏打',1,'李','1',1,'1','1','1','1','1','1','1',1,'1','2019-04-13',1,1,'1',NULL),('18438','SYS0101',NULL,'打打',0,'N18438','男',30,NULL,NULL,'13526453785',NULL,NULL,NULL,NULL,NULL,NULL,'2019-02-16',1,1,NULL,'1'),('184380','1','1','啊是大',1,'张','1',1,'1','1','1','1','1','1','1',1,'1','2019-04-12',1,1,'1',NULL),('5aa32a75-b17f-43dc-931a-292d1ae498f2','',NULL,'打打',NULL,'曹华振','0',25,'反倒是','反倒是','17638153553','123456789912345678','','','无',1,'note',NULL,1,1,'1','1'),('6f38f64c-011d-43cb-8646-f577e1d2746d','',NULL,NULL,NULL,'钱钱钱','0',25,'大苏打','撒旦撒','12345678912','123456789123456789','','','无',1,'note',NULL,1,1,'1','1'),('e4c28453-e9fc-4b93-9081-dc6b1c8e0c70','',NULL,'大苏打',NULL,'沙发脚','0',25,'驱蚊器翁','驱蚊器翁','13266666666','123456789912345678','','','无',1,'note',NULL,1,1,'1','1');
/*!40000 ALTER TABLE `tb_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_staff_brake`
--

DROP TABLE IF EXISTS `tb_staff_brake`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_staff_brake` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_staff_brake_part_id_5f454d5f_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_staff_brake_part_id_5f454d5f_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_staff_brake`
--

LOCK TABLES `tb_staff_brake` WRITE;
/*!40000 ALTER TABLE `tb_staff_brake` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_staff_brake` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_staff_location`
--

DROP TABLE IF EXISTS `tb_staff_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_staff_location` (
  `id` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `time` datetime(6) NOT NULL,
  `location_card_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_staff_location_location_card_id_08b306b3_fk_tb_locati` (`location_card_id`),
  CONSTRAINT `tb_staff_location_location_card_id_08b306b3_fk_tb_locati` FOREIGN KEY (`location_card_id`) REFERENCES `tb_location_card` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_staff_location`
--

LOCK TABLES `tb_staff_location` WRITE;
/*!40000 ALTER TABLE `tb_staff_location` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_staff_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_staff_pass`
--

DROP TABLE IF EXISTS `tb_staff_pass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_staff_pass` (
  `id` varchar(50) NOT NULL,
  `code` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `time` datetime(6) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  `staff_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_staff_pass_part_id_50f2d418_fk_tb_part_id` (`part_id`),
  KEY `tb_staff_pass_staff_id_c41bfd5c_fk_tb_staff_id` (`staff_id`),
  CONSTRAINT `tb_staff_pass_part_id_50f2d418_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`),
  CONSTRAINT `tb_staff_pass_staff_id_c41bfd5c_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_staff_pass`
--

LOCK TABLES `tb_staff_pass` WRITE;
/*!40000 ALTER TABLE `tb_staff_pass` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_staff_pass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_staff_record`
--

DROP TABLE IF EXISTS `tb_staff_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_staff_record` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `zone_name` varchar(100) DEFAULT NULL,
  `device_name` varchar(100) DEFAULT NULL,
  `names` varchar(15) DEFAULT NULL,
  `inouts` varchar(4) NOT NULL,
  `time` datetime(6) NOT NULL,
  `card_number` varchar(10) NOT NULL,
  `group_number` int(11) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_staff_record_part_id_b68ff166_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_staff_record_part_id_b68ff166_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_staff_record`
--

LOCK TABLES `tb_staff_record` WRITE;
/*!40000 ALTER TABLE `tb_staff_record` DISABLE KEYS */;
INSERT INTO `tb_staff_record` VALUES ('2019041514221400011ebe290ee1e436489fb3c356d91ced8','SYS0101','全部区域','人脸识别1','测试员','in','2019-04-12 09:15:45.000000','160002',4,'1'),('2019041514221400012e080c97e7643e3b2be4d53ac5ee98a','SYS0101','全部区域','人脸识别2','测试员','out','2019-04-12 08:59:13.000000','160002',4,'1'),('20190415142214000211d79644ac44c50abd2682b1098fc7d','SYS0101','全部区域','人脸识别2','XYZ','out','2019-04-12 09:41:26.000000','123456',3,'1'),('201904151422140005e25ae86452f474ca90df4fbc8ac3c75','SYS0101','全部区域','人脸识别1','YY','in','2019-04-12 09:35:22.000000','160003',3,'1'),('20190415142214000efe1f934d1ac4e7ca571b2639cfc07f3','SYS0101','全部区域','人脸识别1','888855','in','2019-04-12 09:23:41.000000','160004',7,'1'),('20190415142214000f0928b605f1a41048f6e4398071110ff','SYS0101','全部区域','人脸识别1','XYZ','in','2019-04-12 09:38:49.000000','123456',3,'1');
/*!40000 ALTER TABLE `tb_staff_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_sysid`
--

DROP TABLE IF EXISTS `tb_sysid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_sysid` (
  `index` int(11) NOT NULL,
  `is_used` int(11) NOT NULL,
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `part_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_sysid_part_id_cb28f858_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_sysid_part_id_cb28f858_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sysid`
--

LOCK TABLES `tb_sysid` WRITE;
/*!40000 ALTER TABLE `tb_sysid` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_sysid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_team`
--

DROP TABLE IF EXISTS `tb_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_team` (
  `index` int(11) DEFAULT NULL,
  `is_used` int(11) DEFAULT NULL,
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_team_part_id_e2d094fd_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_team_part_id_e2d094fd_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_team`
--

LOCK TABLES `tb_team` WRITE;
/*!40000 ALTER TABLE `tb_team` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_userworks`
--

DROP TABLE IF EXISTS `tb_userworks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_userworks` (
  `id` varchar(50) NOT NULL,
  `sysid` varchar(50) NOT NULL,
  `time` date NOT NULL,
  `work_time` int(11) DEFAULT NULL,
  `detail` varchar(100) DEFAULT NULL,
  `enter_time` datetime(6) DEFAULT NULL,
  `leave_time` datetime(6) DEFAULT NULL,
  `staff_id` varchar(50) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_userworks_staff_id_087562e0_fk_tb_staff_id` (`staff_id`),
  KEY `tb_userworks_part_id_41561cd9_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_userworks_part_id_41561cd9_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`),
  CONSTRAINT `tb_userworks_staff_id_087562e0_fk_tb_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `tb_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_userworks`
--

LOCK TABLES `tb_userworks` WRITE;
/*!40000 ALTER TABLE `tb_userworks` DISABLE KEYS */;
INSERT INTO `tb_userworks` VALUES ('2019041514221900001b8ae1d1c0e4951a025879ec676fd2d','SYS0101','2019-04-02',8054564,NULL,'2019-04-02 15:02:12.000000','2019-04-02 17:16:40.000000','160003','1'),('2019041514221900001eff5b602384c9fb028b47d04b51298','SYS0101','2019-03-02',259302,NULL,'2019-03-02 10:21:30.000000','2019-03-02 10:25:49.000000','18438','1'),('2019041514221900007e2395403ca4b9f8103ca2ca6c30a35','SYS0101','2019-04-12',156183,NULL,'2019-04-12 09:38:49.000000','2019-04-12 09:41:26.000000','123456','1'),('2019041514221900011372dd99b6e4f608088e6630fa9c950','SYS0101','2019-03-30',531064,NULL,'2019-03-30 11:16:30.000000','2019-03-30 11:25:32.000000','160004','1'),('2019041514221900013ca9d53d7644fa68694737bf4025eb3','SYS0101','2019-02-16',195911,NULL,'2019-02-16 11:50:17.000000','2019-02-16 11:53:33.000000','18438','1'),('2019041514221900025432eaa493c4f459751714c2e53aa21','SYS0101','2019-04-01',2880173,NULL,'2019-04-01 15:56:31.000000','2019-04-01 16:44:31.000000','160004','1'),('20190415142219000395604ad766945d49dbc9f331a52cc41','SYS0101','2019-04-12',1151009,NULL,'2019-04-12 09:33:33.000000','2019-04-12 09:54:20.000000','160003','1'),('20190415142219000432d0cece283449494d14917b4c571b1','SYS0101','2019-04-02',5533,NULL,'2019-04-02 15:02:18.000000','2019-04-02 15:02:24.000000','160002','1'),('2019041514221900048bc1b670cdc460182ec479b9745a93a','SYS0101','2019-03-19',2953898,NULL,'2019-03-19 16:39:07.000000','2019-03-19 17:28:21.000000','160003','1'),('201904151422190004a8f57df1051415bac3e0a7a5ff54028','SYS0101','2019-03-30',10894,NULL,'2019-03-30 11:16:34.000000','2019-03-30 11:16:46.000000','160002','1'),('201904151422190004e49f034d340452487931ec0ea2b9689','SYS0101','2019-02-21',698055,NULL,'2019-02-21 10:37:29.000000','2019-02-21 10:58:23.000000','18438','1'),('201904151422190004fad75921df74ceb8f59d34628787e57','SYS0101','2019-02-21',698038,NULL,'2019-02-21 10:37:29.000000','2019-02-21 10:58:23.000000','16479','1'),('2019041514221900069bd0f4b43e047e281b56590d75926d5','SYS0101','2019-03-02',259290,NULL,'2019-03-02 10:21:30.000000','2019-03-02 10:25:49.000000','16479','1'),('201904151422190006e174ed0cfc34dfb968a61f02203d71d','SYS0101','2019-04-12',284329,NULL,'2019-04-12 09:15:45.000000','2019-04-12 09:20:29.000000','160002','1'),('20190415142219000700b60b671d7471cb3f926f13d1dd0d8','SYS0101','2019-04-02',7784537,NULL,'2019-04-02 14:28:45.000000','2019-04-02 17:16:40.000000','160004','1'),('20190415142219000710a6aed840743b5aa1e556680b1a520','SYS0101','2019-03-30',1460587,NULL,'2019-03-30 11:13:47.000000','2019-03-30 11:38:08.000000','160001','1'),('2019041514221900073f7dbbe87874fa19c5d44c703173355','SYS0101','2019-03-30',553023,NULL,'2019-03-30 11:28:54.000000','2019-03-30 11:38:08.000000','160003','1'),('201904151422190007bba37f12d404930975b628abd938ae8','SYS0101','2019-02-21',7862,NULL,'2019-02-21 10:55:32.000000','2019-02-21 10:55:40.000000','160004','1'),('20190415142219000c18ac35443084c26ac4fc6102488e4ce','SYS0101','2019-02-16',649306,NULL,'2019-02-16 11:42:43.000000','2019-02-16 11:53:33.000000','16479','1'),('20190415142219000c6d8efdbafc640a793930d069e196bc5','SYS0101','2019-04-12',1839047,NULL,'2019-04-12 09:23:41.000000','2019-04-12 09:54:20.000000','160004','1'),('20190415142219000ea0d27eae06d4d7dbe814f4eaa0be0a1','SYS0101','2019-03-19',3126297,NULL,'2019-03-19 16:36:15.000000','2019-03-19 17:28:21.000000','160004','1');
/*!40000 ALTER TABLE `tb_userworks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_voice`
--

DROP TABLE IF EXISTS `tb_voice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_voice` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `factory` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `time` datetime(6) NOT NULL,
  `x` varchar(20) NOT NULL,
  `y` varchar(20) NOT NULL,
  `note` varchar(50) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  `server_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_voice_part_id_ba1b1f6e_fk_tb_part_id` (`part_id`),
  KEY `tb_voice_server_id_e6419f38_fk_tb_voice_server_id` (`server_id`),
  CONSTRAINT `tb_voice_part_id_ba1b1f6e_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`),
  CONSTRAINT `tb_voice_server_id_e6419f38_fk_tb_voice_server_id` FOREIGN KEY (`server_id`) REFERENCES `tb_voice_server` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_voice`
--

LOCK TABLES `tb_voice` WRITE;
/*!40000 ALTER TABLE `tb_voice` DISABLE KEYS */;
INSERT INTO `tb_voice` VALUES ('1','阿三','政策执行差','11asx','2019-04-13 15:09:18.557000','3','4','11',1,1,'1','1');
/*!40000 ALTER TABLE `tb_voice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_voice_server`
--

DROP TABLE IF EXISTS `tb_voice_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_voice_server` (
  `id` varchar(50) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `port` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `note` varchar(50) DEFAULT NULL,
  `part_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_voice_server_part_id_1c7d6e5a_fk_tb_part_id` (`part_id`),
  CONSTRAINT `tb_voice_server_part_id_1c7d6e5a_fk_tb_part_id` FOREIGN KEY (`part_id`) REFERENCES `tb_part` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_voice_server`
--

LOCK TABLES `tb_voice_server` WRITE;
/*!40000 ALTER TABLE `tb_voice_server` DISABLE KEYS */;
INSERT INTO `tb_voice_server` VALUES ('1','192.168.0.112','6002','11','111','1');
/*!40000 ALTER TABLE `tb_voice_server` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-17  9:31:25
