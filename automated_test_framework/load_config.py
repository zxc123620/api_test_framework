#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :global_vars.py
# @Time      :2025/4/8 16:31
# @Author    :zhouxiaochuan
# @Description:
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


class GlobalConfig(BaseModel):
    ServerConfig: ServerConfig
    MySqlConfig: MySqlConfig
    MqttConfig: MqttConfig


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
global_config_obj = None

def init_config():
    global global_config_obj
    if global_config_obj is not None:
        return
    with open(config_path, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        logging.info(f"加载配置文件:{result}")
        sub_class = GlobalConfig.__subclasses__()
        if sub_class:
            logging.info(f"检测到子类,使用子类:{sub_class[0]}")
            global_config_obj= sub_class[0](**result)
        else:
            logging.info("使用默认类")
            global_config_obj =  GlobalConfig(**result)


logging.info(global_config_obj)
