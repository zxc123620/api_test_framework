#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :mysql_conn.py
# @Time      :2025-05-19 21:40
# @Author    :zhouxiaochuan
# @description:
import json
import re

import logging

import pymysql
import pymysql.cursors

from automated_test_framework.mysql.model.case_data_model import MysqlDataModel
from automated_test_framework.mysql.model.json_path_model import JsonPathDataModel
from automated_test_framework.load_config import global_config_obj
from automated_test_framework.temp_data import TempData


class MysqlObj:
    __CONN = None
    __CUR = None

    @classmethod
    def get_conn(cls):
        if not cls.__CONN:
            logging.info("连接数据库")
            cls.connect()
            logging.info("数据库连接成功")
        return cls.__CONN

    @classmethod
    def connect(cls):
        conn = pymysql.connect(
            host=global_config_obj.MySqlConfig.host,
            user=global_config_obj.MySqlConfig.username,
            password=global_config_obj.MySqlConfig.password,
            database=global_config_obj.MySqlConfig.database,
            charset="utf8mb4",
            port=global_config_obj.MySqlConfig.port,
            cursorclass=pymysql.cursors.DictCursor
        )
        cls.__CONN = conn
        cls.__CUR = conn.cursor()

    @classmethod
    def close(cls):
        if cls.__CONN:
            cls.__CONN.close()
            cls.__CUR.close()


def variable_convert(data):
    """
    变量替换
    :param data:
    :return:
    """

    def convert(match):
        temp_data = match.group(1)
        logging.info(f"匹配到{temp_data},转换为:{TempData.TEMP_DATA.get(temp_data, None)}")
        return TempData.TEMP_DATA.get(temp_data, None)

    data_new = re.sub(r"\$\{([^}]*)}", convert, data)
    return data_new


def get_sql_data(case_key):
    """
    根据key值返回获取到的SQL数据
    :param case_key:
    :return:
    """
    sql = "SELECT * FROM `data` WHERE `key`=%s"
    connection = MysqlObj.get_conn()
    cursor = connection.cursor()
    cursor.execute(sql, (case_key,))
    result = cursor.fetchone()
    if result is None:
        raise Exception(f"未获取到数据(key:{case_key})")
    logging.info(result)
    return result


def get_converted_data(data_key):
    """
    获取转换过的数据
    :param data_key:
    :return:
    """
    result = get_sql_data(data_key)
    result["data"] = json.loads(variable_convert(result.get("data")))
    return result


if __name__ == '__main__':
    get_sql_data("xlza.camera.getCameraInfo1")
