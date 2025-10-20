#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/20 20:44
# Author:zhouxiaochuan
# Description:
from peewee import Model

from automated_test_framework.load_config import GlobalConfig


class MysqlBaseModel(Model):
    class Meta:
        database = GlobalConfig().MySqlConfig.mysql_db()