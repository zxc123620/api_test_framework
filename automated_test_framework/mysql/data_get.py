#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :data_get.py
# @Time      :2025/8/3 23:14
# @Author    :zhouxiaochuan
# @Description:
import logging

from pydantic import ValidationError, BaseModel

from automated_test_framework.mysql.model.case_data_model import MysqlDataModel
from automated_test_framework.mysql.model.page_locate_model import MysqlLocateDataModel
from automated_test_framework.mysql.mysql_conn import MysqlObj, converted_data


class MysqlDataGet:
    cursor = MysqlObj.get_conn().cursor()

    @classmethod
    def __get_sql_data(cls, sql, params):
        """
        获取原始数据
        :param sql:
        :param params:
        :return:
        """
        # sql = f"-- SELECT * FROM data WHERE `key`=%s"
        cls.cursor.execute(sql, params)
        result = cls.cursor.fetchone()
        if result is None:
            raise Exception(f"未获取到数据(sql:{sql})")

    @classmethod
    def __model_match(cls, model_class, data):
        """
        模型匹配
        :return:
        """
        model = model_class(**data)
        for sub_class in model_class.__subclasses__():
            try:
                model = sub_class(**data)
                logging.info(f"{sub_class}模型匹配")
                break
            except ValidationError as e:
                logging.info(f"{sub_class}模型不匹配")
                # logging.debug(f"{sub_class} 模型不匹配,理由:{e.errors()}")
        return model

    @classmethod
    def get_data(cls, case_key, model_cls=None):
        """
        从数据库中找数据并变成一个模型
        :return:
        """
        sql = f"SELECT * FROM data WHERE `key`=%s"
        result = cls.__get_sql_data(sql, (case_key,))
        result["data"] = converted_data(result["data"])
        logging.info(f"获取数据库数据:{result}")
        if model_cls is not None:
            return model_cls(**result)
        model = cls.__model_match(MysqlDataModel, result)
        # logging.info(f"自定义子类:{MysqlDataModel.__subclasses__()}")
        # model = MysqlDataModel(**result)
        # for sub_class in MysqlDataModel.__subclasses__():
        #     try:
        #         model = sub_class(**result)
        #         logging.info(f"{sub_class}模型匹配")
        #         break
        #     except ValidationError as e:
        #         logging.info(f"{sub_class}模型不匹配")
        #         # logging.debug(f"{sub_class} 模型不匹配,理由:{e.errors()}")
        return model

    @classmethod
    def get_page_locate_data(cls, key):
        """
        获取页面定位数据
        :param key:
        :return:
        """
        sql = f"SELECT * FROM page_locate WHERE `key`=%s"
        result = cls.__get_sql_data(sql, (key,))
        logging.info(f"获取数据库数据:{result}")
        model = cls.__model_match(MysqlLocateDataModel, result)
        return model


if __name__ == '__main__':
    print(type(BaseModel))
