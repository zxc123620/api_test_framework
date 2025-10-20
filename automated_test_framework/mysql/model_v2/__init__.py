#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 18:33
# Author:zhouxiaochuan
# Description:
from peewee import MySQLDatabase

from automated_test_framework.load_config import GlobalConfig

db = MySQLDatabase(GlobalConfig().MySqlConfig.database, user=GlobalConfig().MySqlConfig.username,
                   password=GlobalConfig().MySqlConfig.password,
                   host=GlobalConfig().MySqlConfig.host, port=GlobalConfig().MySqlConfig.port)
