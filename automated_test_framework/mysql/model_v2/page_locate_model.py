#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_locate_model.py
# @Time      :2025/10/15 11:58
# @Author    :zhouxiaochuan
# @Description:
from typing import Optional

from peewee import Model, CharField, ForeignKeyField

from automated_test_framework.mysql.model_v2 import db


class MysqlLocateTypeModel(Model):
    id = CharField(primary_key=True)

    class Meta:
        database = db
        table_name = 'locate_type'

class MysqlLocateDataModel(Model):
    key = CharField(primary_key=True)
    locate_type = ForeignKeyField(MysqlLocateTypeModel, column_name="locate_type", on_delete="RESTRICT", on_update="RESTRICT")
    desc = CharField()
    locate_value = CharField(null=False)
    page = CharField()

    class Meta:
        database = db
        table_name = 'page_locate'