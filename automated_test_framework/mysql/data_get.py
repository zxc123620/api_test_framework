#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :data_get.py
# @Time      :2025/8/3 23:14
# @Author    :zhouxiaochuan
# @Description:
import logging

from pydantic import ValidationError

from automated_test_framework.mysql.model.case_data_model import MysqlDataModel
from automated_test_framework.mysql.mysql_conn import get_converted_data


class MysqlDataGet:
    @staticmethod
    def get_data(case_key, model_cls=None):
        """
        从数据库中找数据并变成一个模型
        :return:
        """
        result = get_converted_data(case_key)
        logging.info(f"获取数据库数据:{result}")
        if model_cls is not None:
            return model_cls(**result)
        logging.info(f"自定义子类:{MysqlDataModel.__subclasses__()}")
        model = MysqlDataModel(**result)
        for sub_class in MysqlDataModel.__subclasses__():
            try:
                model = sub_class(**result)
                logging.info(f"{sub_class}模型匹配")
                break
            except ValidationError as e:
                logging.info(f"{sub_class}模型不匹配")
                logging.debug(f"{sub_class} 模型不匹配,理由:{e.errors()}")
        return model
    # @staticmethod
    # def get_jsonpath_data(case_key):
    #     """
    #     从数据库中找数据并变成一个模型
    #     :return:
    #     """
    #     result = get_converted_data(case_key)
    #     return JsonPathDataModel(**result)
