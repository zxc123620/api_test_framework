#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :global_vars.py
# @Time      :2025/4/8 16:31
# @Author    :zhouxiaochuan
# @Description:
from peewee import MySQLDatabase
from pydantic import BaseModel

import logging
import os

import yaml

from automated_test_framework.framework_error import NoConfigError


class ServerConfig(BaseModel):
    host: str
    port: int
    protocol: str


class MySqlConfig(BaseModel):
    host: str
    username: str
    password: str
    database: str
    port: int


class MqttConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str


class VirtualFaItem(BaseModel):
    desc: str
    radar_camera_bind: list
    device_no_list: list


class PimsConfig(BaseModel):
    VirtualFa: list[VirtualFaItem]


#
# class PimsGlobalConfig(GlobalConfig):
#     PimsConfig: PimsConfig


config_path = None
temp_dir = os.getcwd()
while True:
    temp_path = os.path.join(temp_dir, "config.yml")
    if os.path.exists(temp_path):
        config_path = temp_path
        break
    else:
        raise NoConfigError("没有配置文件")

config_data = {}

def config(cls_1):
    def inner():
        global config_data
        if not config_data:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = yaml.load(f.read(), Loader=yaml.FullLoader)
                logging.info(f"加载配置文件:{config_data}")
        return cls_1(**config_data)

    return inner


@config
class GlobalConfig(BaseModel):
    ServerConfig: ServerConfig
    MySqlConfig: MySqlConfig
    MqttConfig: MqttConfig


# global_config_obj = None
#
# def init_config():
#     global global_config_obj
#     if global_config_obj is not None:
#         return
#     with open(config_path, 'r', encoding='utf-8') as f:
#         result = yaml.load(f.read(), Loader=yaml.FullLoader)
#         logging.info(f"加载配置文件:{result}")
#         sub_class = GlobalConfig.__subclasses__()
#         if sub_class:
#             logging.info(f"检测到子类,使用子类:{sub_class[0]}")
#             global_config_obj= sub_class[0](**result)
#         else:
#             logging.info("使用默认类")
#             global_config_obj =  GlobalConfig(**result)
#

# logging.info(global_config_obj)

if __name__ == '__main__':
    data = {'ServerConfig': {'host': '10.168.2.118', 'port': 9082, 'protocol': 'http'}, 'MySqlConfig': {'host': 'localhost', 'username': 'root', 'password': 'root', 'database': 'auto_test_db', 'port': 3306}, 'MqttConfig': {'host': '10.168.2.118', 'port': 1883, 'username': 'admin', 'password': 'CSRD_PASS@2023user'}, 'SftpConfig': {'server_ip': '10.168.2.118', 'port': 2222, 'username': 'xlza', 'password': 'CsrdXljc1', 'path': '/opt/alarmfile'}, 'PimsConfig': {'VirtualFa': [{'desc': '单线', 'radar_camera_bind': [[1, 1], [2, 2], [3, 3], [4, 4]], 'device_no_list': ['75001']}, {'desc': '双线', 'device_no_list': ['75002'], 'radar_camera_bind': [[1, 1], [2, 1], [3, 2], [4, 2]]}, {'desc': '单线', 'device_no_list': ['75003'], 'radar_camera_bind': [[1, 1], [2, 2], [3, 3]]}]}}
    # data2 = {'ServerConfig': {'host': '10.168.2.118', 'port': 9082, 'protocol': 'http'}, 'MySqlConfig': {'host': 'localhost', 'username': 'root', 'password': 'root', 'database': 'auto_test_db', 'port': 3306}, 'MqttConfig': {'host': '10.168.2.118', 'port': 1883, 'username': 'admin', 'password': 'CSRD_PASS@2023user'}, 'SftpConfig': {'server_ip': '10.168.2.118', 'port': 2222, 'username': 'xlza', 'password': 'CsrdXljc1', 'path': '/opt/alarmfile'}, 'PimsConfig': {'VirtualFa': [{'desc': '单线', 'radar_camera_bind': [[1, 1], [2, 2], [3, 3], [4, 4]], 'device_no_list': ['75001']}, {'desc': '双线', 'device_no_list': ['75002'], 'radar_camera_bind': [[1, 1], [2, 1], [3, 2], [4, 2]]}, {'desc': '单线', 'device_no_list': ['75003'], 'radar_camera_bind': [[1, 1], [2, 2], [3, 3]]}]}}
    # print(id(GlobalConfig(**data).MySqlConfig))
    # print(id(GlobalConfig(**data).MySqlConfig))
    # print(id(GlobalConfig().MySqlConfig))
    # print(id(GlobalConfig().MySqlConfig))

