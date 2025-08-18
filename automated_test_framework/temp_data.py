#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :temp_data.py
# @Time      :2025/8/3 22:30
# @Author    :zhouxiaochuan
# @Description:
from automated_test_framework.framework_error import TempDataNotFindError


class TempData:
    HEADER = {}
    __TEMP_DATA = {}

    @classmethod
    def set_temp_data(cls, key, value):
        cls.__TEMP_DATA[key] = value

    @classmethod
    def get_temp_data(cls, key):
        value = cls.__TEMP_DATA.get(key)
        if value is None:
            raise TempDataNotFindError(f"没找到数据:{key}")
        return value
