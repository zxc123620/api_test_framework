#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/9/10 21:43
# Author:zhouxiaochuan
# Description:
from pydantic import BaseModel

from automated_test_framework.mysql.model_v1.case_data_model import MysqlDataModel

class TimeRangeModel(BaseModel):
    start_time: str
    end_time: str

class JsonPathTimeRangeModel(MysqlDataModel):
    class DataModel(BaseModel):
        expect_data: TimeRangeModel
        jsonpath_exp: str

    data: DataModel