#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :json_path_model.py
# @Time      :2025-05-27 22:14
# @Author    :zhouxiaochuan
# @description:
from typing import Union

from pydantic import BaseModel

from automated_test_framework.mysql.model.case_data_model import MysqlDataModel


class JsonPathDataModel(MysqlDataModel):
    class DataModel(BaseModel):
        expect_data: Union[dict, list]
        jsonpath_exp: str

    data: DataModel
