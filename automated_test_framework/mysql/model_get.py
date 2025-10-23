#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/23 22:23
# Author:zhouxiaochuan
# Description:
from automated_test_framework.mysql.model_v1.page_locate_model import MysqlLocateDataModel
from automated_test_framework.mysql.model_v2.data_model import MysqlDataModel, MysqlJsonPathDataModel, \
    MysqlJsonPathTimeRangeModel, MysqlDataLoginModel


class MysqlModelGet:
    @staticmethod
    def get_data_model(key):
        return MysqlDataModel.get(MysqlDataModel.key == key)

    @staticmethod
    def get_json_path_data_model(key):
        return MysqlJsonPathDataModel.get(MysqlJsonPathDataModel.key == key)

    @staticmethod
    def get_json_path_time_range_model(key):
        return MysqlJsonPathTimeRangeModel.get(MysqlJsonPathTimeRangeModel.key == key)

    @staticmethod
    def get_login_model(key):
        return MysqlDataLoginModel.get(MysqlDataLoginModel.key == key)

    @staticmethod
    def get_location_data_model(key):
        return MysqlLocateDataModel.get(MysqlLocateDataModel.key == key)

