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
from peewee import MySQLDatabase

import automated_test_framework
from automated_test_framework.load_config import  GlobalConfig
from automated_test_framework.meta_class import SingletonMeta
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
            host=GlobalConfig().MySqlConfig.host,
            user=GlobalConfig().MySqlConfig.username,
            password=GlobalConfig().MySqlConfig.password,
            database=GlobalConfig().MySqlConfig.database,
            charset="utf8mb4",
            port=GlobalConfig().MySqlConfig.port,
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
        res = TempData.get_temp_data(temp_data)
        logging.info(f"匹配到{temp_data},转换为:{res}")
        return str(res)

    data_new = re.sub(r"\$\{([^}]*)}", convert, data)
    return data_new


def get_sql_data(case_key, table="data"):
    """
    根据key值返回获取到的SQL数据
    :param table:
    :param case_key:
    :return:
    """
    sql = f"SELECT * FROM {table} WHERE `key`=%s"
    connection = MysqlObj.get_conn()
    cursor = connection.cursor()
    cursor.execute(sql, (case_key,))
    result = cursor.fetchone()
    if result is None:
        raise Exception(f"未获取到数据(key:{case_key})")
    logging.info(result)
    return result


def get_converted_data(data):
    """
    获取转换过的数据
    :return:
    """
    # result = get_sql_data(data_key,table)
    # result["data"] = json.loads(variable_convert(result.get("data")))
    return json.loads(variable_convert(data))


def converted_data(data):
    """
    获取转换过的数据
    :return:
    """
    # result = get_sql_data(data_key,table)
    # result["data"] = json.loads(variable_convert(result.get("data")))
    return json.loads(variable_convert(data))


# 连接数据库
class MysqlObjV2(metaclass=SingletonMeta):
    def __init__(self):
        mysql_config = automated_test_framework.load_config.GlobalConfig().MySqlConfig
        print(mysql_config.username, mysql_config.host)
        self.__mysql_db_obj = MySQLDatabase(mysql_config.database, user=mysql_config.username,
                                            password=mysql_config.password,
                                            host=mysql_config.host, port=mysql_config.port)

    def close(self):
        self.__mysql_db_obj.close()

if __name__ == '__main__':
    # get_sql_data("xlza.camera.getCameraInfo1")
    print(id(MysqlObjV2()))
    print(id(MysqlObjV2()))
