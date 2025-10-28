-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: auto_test_db
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `project` int DEFAULT NULL COMMENT '所属项目',
  `module` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '所属模块',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '标题',
  `key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '唯一值,定位用',
  `data` json DEFAULT NULL COMMENT '数据',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '备注',
  `interfaceName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '接口名称',
  PRIMARY KEY (`key`) USING BTREE,
  KEY `data_ibfk_1` (`project`) USING BTREE,
  CONSTRAINT `data_ibfk_1` FOREIGN KEY (`project`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (1,'报警列表','验证报警列表中的报警信息','xlza.alarm.validAlarmInfo','{\"expect_data\": {\"level\": null, \"width\": null, \"xAxis\": null, \"yAxis\": null, \"height\": null, \"length\": null, \"alarmId\": null, \"endTime\": null, \"deviceId\": \"75001RA011\", \"lineName\": null, \"alarmTime\": null, \"cabinetId\": \"75001\", \"isAlarmed\": null, \"levelName\": null, \"deviceName\": null, \"isClassify\": 0, \"cabinetName\": null, \"endDateTime\": null, \"stationName\": null, \"staySeconds\": null, \"handlingTime\": null, \"handlingType\": 0, \"obstacleType\": null, \"positionName\": null, \"alarmDateTime\": null, \"handlingReason\": null, \"handlingUserId\": null, \"handlingOpinion\": \"待确认报警\", \"handlingTimeStr\": null, \"handlingUserName\": null, \"obstacleTypeName\": null, \"handlingReasonName\": \"\"}, \"jsonpath_exp\": \"$.data.list[0:10]\"}','验证报警列表中的报警信息',NULL),(1,'报警列表','验证正在报警列表中的报警ID','xlza.alarm.validAlarmingInfo','{\"expect_data\": \"${alarm_code_list}\", \"jsonpath_exp\": \"$.data.list[*].alarmId\"}','验证正在报警列表中的报警数据',NULL),(1,'报警列表','验证正在报警列表中的总数-1','xlza.alarm.validAlarmingTotalNumIs1','{\"expect_data\": [1], \"jsonpath_exp\": \"$.data.total\"}','验证正在报警列表中的总数',NULL),(1,'报警列表','验证正在报警列表中的总数-2','xlza.alarm.validAlarmingTotalNumIs2','{\"expect_data\": [2], \"jsonpath_exp\": \"$.data.total\"}','验证正在报警列表中的总数',NULL),(1,'报警列表','验证报警中的时间信息','xlza.alarm.validAlarmRange','{\"expect_data\": {\"end_time\": \"${end_time}\", \"start_time\": \"${start_time}\"}, \"jsonpath_exp\": \"$..list[*].alarmTime\"}','验证报警中的时间信息',NULL),(1,'报警列表','验证取消报警列表中的总数','xlza.alarm.validCancelAlarmNum','{\"expect_data\": \"${canceled_alarm_num}\", \"jsonpath_exp\": \"$.data.total\"}','验证正在报警列表中的总数',NULL),(1,'报警列表','验证正在报警列表中的ISAlarm字段-数量1','xlza.alarm.validIsAlarmDataIs1','{\"expect_data\": [\"1\"], \"jsonpath_exp\": \"$.data.list[*].isAlarmed\"}','验证正在报警列表中的ISAlarm字段',NULL),(1,'报警列表','验证正在报警列表中的ISAlarm字段-数量2','xlza.alarm.validIsAlarmDataIs2','{\"expect_data\": [\"1\", \"1\"], \"jsonpath_exp\": \"$.data.list[*].isAlarmed\"}','验证正在报警列表中的ISAlarm字段',NULL),(1,'报警列表','验证待处理报警列表中的总数+1','xlza.alarm.validUnclassifiedAlarmingTotalNum','{\"expect_data\": \"${unclassify_total_alarm}\", \"jsonpath_exp\": \"$.data.total\"}','验证待处理报警列表中的总数+1',NULL),(1,'摄像头管理','查询75001CA011摄像头信息','xlza.camera.getCameraInfo1','{\"name\": \"75001CA011\", \"pageNum\": 1, \"pageSize\": 10}','查询75001CA011摄像头信息',NULL),(1,'摄像头管理','查询75001CA012摄像头信息','xlza.camera.getCameraInfo2','{\"name\": \"75001CA012\", \"pageNum\": 1, \"pageSize\": 10}','查询75001CA011摄像头信息',NULL),(1,'摄像头管理','更新75001CA011摄像头流媒体地址','xlza.camera.updateCamera1','{\"id\": \"75001CA011\", \"streamUrl\": \"75001CA011StreamUrl\", \"accessMode\": \"1\"}','更新75001CA011摄像头流媒体地址',NULL),(1,'摄像头管理','更新75001CA012摄像头流媒体地址','xlza.camera.updateCamera2','{\"id\": \"75001CA012\", \"streamUrl\": \"75001CA012StreamUrl\", \"accessMode\": \"1\"}','更新75001CA011摄像头流媒体地址',NULL),(1,'获取线路监测点列表','验证监测点状态(报警)-监测点1','xlza.getMainPageStationList.stationAlarm','{\"expect_data\": {\"lineNameStr\": \"自动线路1\", \"stationName\": \"自动监测点1\", \"stationType\": \"1\", \"stationStatus\": \"3\", \"stationTypeName\": \"激光雷达\", \"stationStatusName\": \"报警\"}, \"jsonpath_exp\": \"$..stationPoint[?(@.stationName== \'自动监测点1\')]\"}','验证监测点状态(报警)-监测点1','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证监测点状态(正常)-监测点1','xlza.getMainPageStationList.stationNormal','{\"expect_data\": {\"lineNameStr\": \"自动线路1\", \"stationName\": \"自动监测点1\", \"stationType\": \"1\", \"stationStatus\": \"1\", \"stationTypeName\": \"激光雷达\", \"stationStatusName\": \"正常\"}, \"jsonpath_exp\": \"$..stationPoint[?(@.stationName== \'自动监测点1\')]\"}','验证监测点状态(正常)-监测点1','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证监测点状态(正常)-监测点2','xlza.getMainPageStationList.stationNormal2','{\"expect_data\": {\"lineNameStr\": \"自动线路1\", \"stationName\": \"自动监测点2\", \"stationType\": \"1\", \"stationStatus\": \"1\", \"stationTypeName\": \"激光雷达\", \"stationStatusName\": \"正常\"}, \"jsonpath_exp\": \"$..stationPoint[?(@.stationName== \'自动监测点2\')]\"}','验证监测点状态(正常)-监测点2','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证线路1内部信息','xlza.getMainPageStationList.validLineInfo1','{\"expect_data\": {\"lineEnd\": \"线路1结束站Line1End\", \"lineName\": \"自动线路1\", \"lineStart\": \"线路1起始站Line1Start\"}, \"jsonpath_exp\": \"$.data[?(@.lineName == \'自动线路1\')]\"}','验证线路1信息','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证线路2内部信息','xlza.getMainPageStationList.validLineInfo2','{\"expect_data\": {\"lineEnd\": \"线路2结束站Line2End\", \"lineName\": \"自动线路2\", \"lineStart\": \"线路2起始站Line2Start\"}, \"jsonpath_exp\": \"$.data[?(@.lineName == \'自动线路2\')]\"}','验证线路2信息','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证监测点1内部信息(不包括状态)','xlza.getMainPageStationList.validStationInfo1','{\"expect_data\": {\"deviceCount\": 4, \"lineNameStr\": \"自动线路1\", \"stationName\": \"自动监测点1\", \"stationType\": \"1\", \"stationTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..stationPoint[?(@.stationName== \'自动监测点1\')]\"}','验证监测点1信息(不包括状态)','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证监测点1内部信息(不包括状态)','xlza.getMainPageStationList.validStationInfo2','{\"expect_data\": {\"deviceCount\": 3, \"lineNameStr\": \"自动线路1\", \"stationName\": \"自动监测点3\", \"stationType\": \"1\", \"stationTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..stationPoint[?(@.stationName== \'自动监测点3\')]\"}','验证监测点1信息(不包括状态)','/pims/station/getMainPageStationList'),(1,'获取线路监测点列表','验证是否line1线路下面的监测点个数','xlza.getMainPageStationList.validStationInfo3','{\"expect_data\": [\"自动监测点1\", \"自动监测点2\", \"自动监测点3\", \"自动监测点4\", \"自动监测点5\", \"自动监测点6\", \"自动监测点7\", \"自动监测点8\", \"自动监测点9\", \"自动监测点10\"], \"jsonpath_exp\": \"$.data[?(@.lineName== \'自动线路1\')].stationPoint[*].stationName\"}','验证是否不同线路下面的监测点信息不同',NULL),(1,'获取线路监测点列表','验证是否line2线路下面的监测点个数','xlza.getMainPageStationList.validStationInfo4','{\"expect_data\": [\"自动监测点11\", \"自动监测点12\", \"自动监测点13\", \"自动监测点14\", \"自动监测点15\", \"自动监测点16\", \"自动监测点17\", \"自动监测点18\", \"自动监测点19\", \"自动监测点20\"], \"jsonpath_exp\": \"$.data[?(@.lineName== \'自动线路2\')].stationPoint[*].stationName\"}','验证是否不同线路下面的监测点信息不同',NULL),(1,'监测点雷达信息','验证摄像头75001CA011流媒体地址','xlza.getMainPageStationRadarList.validCamearUrl1','{\"expect_data\": [\"75001CA011StreamUrl\"], \"jsonpath_exp\": \"$..children[?(@.id== \'75001RA011\')].streamUrl\"}','验证摄像头75001CA011流媒体地址',NULL),(1,'监测点雷达信息','验证摄像头75001CA012流媒体地址','xlza.getMainPageStationRadarList.validCamearUrl2','{\"expect_data\": [\"75001CA012StreamUrl\"], \"jsonpath_exp\": \"$..children[?(@.id== \'75001RA012\')].streamUrl\"}','验证摄像头75001CA012流媒体地址',NULL),(1,'获取监测点雷达列表','验证雷达禁用','xlza.getMainPageStationRadarList.validRadarDisable','{\"expect_data\": {\"id\": \"75001RA011\", \"status\": 2}, \"jsonpath_exp\": \"$..children[?(@.id== \'75001RA011\')]\"}','验证雷达禁用','/pims/station/getMainPageStationList'),(1,'获取监测点雷达列表','验证雷达离线','xlza.getMainPageStationRadarList.validRadarOffline','{\"expect_data\": {\"id\": \"75001RA011\", \"status\": 0}, \"jsonpath_exp\": \"$..children[?(@.id== \'75001RA011\')]\"}','验证雷达离线','/pims/station/getMainPageStationList'),(1,'获取监测点雷达列表','验证雷达在线','xlza.getMainPageStationRadarList.validRadarOnline','{\"expect_data\": {\"id\": \"75001RA011\", \"status\": 1}, \"jsonpath_exp\": \"$..children[?(@.id== \'75001RA011\')]\"}','验证雷达在线','/pims/station/getMainPageStationList'),(1,'登录','登录成功','xlza.login.success','{\"name\": \"api_test接口用户\", \"password\": \"Csrd!0269\", \"username\": \"api_test\"}','测试登录','login'),(1,'故障列表','验证NVR故障','xlza.malfunctionData.validNvrOffline','{\"expect_data\": {\"state\": 0, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": null, \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"1\", \"hasRecovered\": \"故障\", \"equipmentTypeName\": \"NVR设备\"}, \"jsonpath_exp\": \"$..list[?(@.equipmentTypeName == \'NVR设备\' && @.hasRecovered==\'故障\')]\"}','验证NVR故障',NULL),(1,'故障列表','验证NVR故障恢复','xlza.malfunctionData.validNvrOnline','{\"expect_data\": {\"state\": 1, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": \"${recovery_time}\", \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"1\", \"hasRecovered\": \"恢复\", \"equipmentTypeName\": \"NVR设备\"}, \"jsonpath_exp\": \"$..list[?(@.equipmentTypeName == \'NVR设备\')]\"}','验证NVR故障恢复',NULL),(1,'故障列表','验证雷达离线信息','xlza.malfunctionData.validRadarOffLine','{\"expect_data\": {\"state\": 0, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": null, \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"75001RA011\", \"hasRecovered\": \"故障\", \"equipmentTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..list[?(@.hasRecovered==\'故障\'&&@.equipmentIdx==\'75001RA011\')]\"}','验证雷达离线信息',NULL),(1,'故障列表','验证2号雷达离线信息','xlza.malfunctionData.validRadarOffLine2','{\"expect_data\": {\"state\": 0, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time_2}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": null, \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"75001RA012\", \"hasRecovered\": \"故障\", \"equipmentTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..list[?(@.hasRecovered==\'故障\'&&@.equipmentIdx==\'75001RA012\')]\"}','验证雷达离线信息',NULL),(1,'故障列表','验证雷达离线后恢复','xlza.malfunctionData.validRadarOnLine','{\"expect_data\": {\"state\": 1, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": \"${recovery_time}\", \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"75001RA011\", \"hasRecovered\": \"恢复\", \"equipmentTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..list[?(@.hasRecovered==\'恢复\'&&@.equipmentIdx==\'75001RA011\')]\"}','验证雷达离线后恢复',NULL),(1,'故障列表','验证雷达3离线后恢复','xlza.malfunctionData.validRadarOnLine3','{\"expect_data\": {\"state\": 1, \"lineName\": \"自动线路1\", \"errorDesc\": \"离线\", \"errorTime\": \"${error_time}\", \"deviceName\": \"自动工控机1\", \"recoverTime\": \"${recovery_time}\", \"stationName\": \"自动监测点1\", \"equipmentIdx\": \"75001RA013\", \"hasRecovered\": \"恢复\", \"equipmentTypeName\": \"激光雷达\"}, \"jsonpath_exp\": \"$..list[?(@.hasRecovered==\'恢复\'&&@.equipmentIdx==\'75001RA013\')]\"}','验证雷达3离线后恢复',NULL),(1,'mqtt硬盘录像机状态','发送硬盘录像机离线','xlza.mqtt.nvr.offline','{\"device_no\": \"75001\", \"nvr_state\": 0}','发送硬盘录像机离线',NULL),(1,'mqtt硬盘录像机状态','发送硬盘录像机在线','xlza.mqtt.nvr.online','{\"device_no\": \"75001\", \"nvr_state\": 1}','发送硬盘录像机在线',NULL),(1,'mqtt报警','发送一条75011RA011固定障碍物二级报警','xlza.mqtt.secondAlarm','{\"level\": 2, \"obs_h\": 20.3, \"obs_l\": 20.1, \"obs_w\": 20.2, \"obs_x\": 21.1, \"obs_y\": 21.2, \"obs_z\": 21.3, \"is_alarm\": 1, \"obs_type\": 1, \"radar_no\": \"75001RA011\", \"device_no\": \"75001\", \"is_history\": 0, \"stay_seconds\": 0}','发送一条75011RA011二级报警',NULL),(1,'mqtt报警','发送一条75011RA012固定障碍物二级报警','xlza.mqtt.secondAlarm2','{\"level\": 2, \"obs_h\": 99.3, \"obs_l\": 99.1, \"obs_w\": 99.2, \"obs_x\": 100.1, \"obs_y\": 100.2, \"obs_z\": 100.3, \"is_alarm\": 1, \"obs_type\": 1, \"radar_no\": \"75001RA012\", \"device_no\": \"75001\", \"is_history\": 0, \"stay_seconds\": 0}','发送一条75011RA012二级报警',NULL),(1,'mqtt报警','发送一条75011RA011固定障碍物二级历史报警','xlza.mqtt.secondHistoryAlarm','{\"level\": 2, \"obs_h\": 20.3, \"obs_l\": 20.1, \"obs_w\": 20.2, \"obs_x\": 21.1, \"obs_y\": 21.2, \"obs_z\": 21.3, \"is_alarm\": 0, \"obs_type\": 1, \"radar_no\": \"75001RA011\", \"device_no\": \"75001\", \"is_history\": 0, \"stay_seconds\": 0}','发送一条75011RA011固定障碍物二级历史报警',NULL),(1,'mqtt设备状态','发送75001中的一号雷达禁用','xlza.mqtt.sendRadarDisable','{\"radar_no\": \"75001RA011\", \"device_no\": \"75001\", \"radar_enable\": 0, \"radar_status\": 1}','发送雷达禁用',NULL),(1,'mqtt设备状态','发送75001中的一号雷达离线','xlza.mqtt.sendRadarOffline1','{\"radar_no\": \"75001RA011\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 0}','发送雷达离线',NULL),(1,'mqtt设备状态','发送75001中的二号雷达离线','xlza.mqtt.sendRadarOffline2','{\"radar_no\": \"75001RA012\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 0}','发送75001中的二号雷达离线',NULL),(1,'mqtt设备状态','发送75001中的三号雷达离线','xlza.mqtt.sendRadarOffline3','{\"radar_no\": \"75001RA013\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 0}','发送75001中的三号雷达离线',NULL),(1,'mqtt设备状态','发送75001中的一号雷达在线','xlza.mqtt.sendRadarOnline1','{\"radar_no\": \"75001RA011\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 1}','发送75001中的一号雷达在线',NULL),(1,'mqtt设备状态','发送75001中的二号雷达在线','xlza.mqtt.sendRadarOnline2','{\"radar_no\": \"75001RA012\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 1}','发送75001中的一号雷达在线',NULL),(1,'mqtt设备状态','发送75001中的三号雷达在线','xlza.mqtt.sendRadarOnline3','{\"radar_no\": \"75001RA013\", \"device_no\": \"75001\", \"radar_enable\": 1, \"radar_status\": 1}','发送75001中的三号雷达在线',NULL),(1,'角色管理','获取角色下的监测点、雷达列表信息','xlza.role.getStationIds','{\"role_name\": \"api_test\"}','获取角色下的监测点信息',NULL);
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interface`
--

DROP TABLE IF EXISTS `interface`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interface` (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '接口名字',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '接口描述',
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id,自增',
  `project` int DEFAULT NULL COMMENT '项目名称',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project` (`project`) USING BTREE,
  CONSTRAINT `interface_ibfk_1` FOREIGN KEY (`project`) REFERENCES `project` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interface`
--

LOCK TABLES `interface` WRITE;
/*!40000 ALTER TABLE `interface` DISABLE KEYS */;
INSERT INTO `interface` VALUES ('pub/login/loginIn.do','登录接口',1,1),('pims/station/getMainPageStationList','获取线路监测点列表信息',2,1);
/*!40000 ALTER TABLE `interface` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locate_type`
--

DROP TABLE IF EXISTS `locate_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locate_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `loc_type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locate_type`
--

LOCK TABLES `locate_type` WRITE;
/*!40000 ALTER TABLE `locate_type` DISABLE KEYS */;
INSERT INTO `locate_type` VALUES (1,'CLASS_NAME'),(2,'CSS_SELECTOR'),(3,'ID'),(4,'LINK_TEXT'),(5,'NAME'),(6,'PARTIAL_LINK_TEXT'),(7,'TAG_NAME'),(8,'XPATH');
/*!40000 ALTER TABLE `locate_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `page_locate`
--

DROP TABLE IF EXISTS `page_locate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `page_locate` (
  `locate_type` int NOT NULL COMMENT '定位方式',
  `key` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'ID-主键',
  `page` varchar(100) DEFAULT NULL COMMENT '页面',
  `locate_value` varchar(100) NOT NULL COMMENT '定位值',
  `desc` varchar(100) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`key`),
  KEY `locate_type` (`locate_type`),
  CONSTRAINT `page_locate_locate_type_FK` FOREIGN KEY (`locate_type`) REFERENCES `locate_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `page_locate`
--

LOCK TABLES `page_locate` WRITE;
/*!40000 ALTER TABLE `page_locate` DISABLE KEYS */;
INSERT INTO `page_locate` VALUES (2,'login_btn','登录页面','.login-btns button','登录按钮'),(2,'login_input_elements','登录页面','input.el-input__inner','登录界面账号密码输入框');
/*!40000 ALTER TABLE `page_locate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '项目名称',
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '项目描述',
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES ('线路障碍','线路监测',1);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `url_save`
--

DROP TABLE IF EXISTS `url_save`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `url_save` (
  `key` varchar(100) NOT NULL,
  `protocol` varchar(100) NOT NULL,
  `host` varchar(100) NOT NULL,
  `port` int NOT NULL,
  `path` varchar(255) NOT NULL,
  `desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `url_save`
--

LOCK TABLES `url_save` WRITE;
/*!40000 ALTER TABLE `url_save` DISABLE KEYS */;
INSERT INTO `url_save` VALUES ('login','https','10.168.2.118',10443,'pimsui/login','登录界面'),('monitor','https','10.168.2.118',10443,'pimsui/panel/monitor/line','主页');
/*!40000 ALTER TABLE `url_save` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'auto_test_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-28 22:19:57
