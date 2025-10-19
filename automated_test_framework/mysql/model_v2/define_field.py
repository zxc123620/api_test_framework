#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 18:47
# Author:zhouxiaochuan
# Description:
import json

from peewee import TextField


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)
