#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_locate_model.py
# @Time      :2025/10/15 11:58
# @Author    :zhouxiaochuan
# @Description:
from typing import Optional

from peewee import Model, CharField, ForeignKeyField, AutoField

from automated_test_framework.mysql.model_v2 import db
from automated_test_framework.mysql.model_v2.define_field import SeleniumBYField


class MysqlLocateTypeModel(Model):
    id = AutoField(primary_key=True)
    loc_type = SeleniumBYField()

    class Meta:
        database = db
        table_name = 'locate_type'


class MysqlLocateDataModel(Model):
    key = CharField(primary_key=True)
    locate_type = ForeignKeyField(MysqlLocateTypeModel, column_name="locate_type", on_delete="CASCADE",
                                  on_update="CASCADE")
    desc = CharField()
    locate_value = CharField(null=False)
    page = CharField()

    class Meta:
        database = db
        table_name = 'page_locate'
