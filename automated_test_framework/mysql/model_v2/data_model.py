#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 18:34
# Author:zhouxiaochuan
# Description:
from peewee import Model, CharField, ForeignKeyField

from automated_test_framework.mysql.model_v2 import db
from automated_test_framework.mysql.model_v2.define_field import JSONField, JsonPathField, TimeRangeField
from automated_test_framework.mysql.model_v2.project_model import ProjectModel


class DataModel(Model):
    key = CharField(primary_key=True)
    title = CharField()
    description = CharField()
    project = ForeignKeyField(ProjectModel, on_delete='CASCADE', column_name='project')
    module = CharField()
    data = JSONField()
    interfaceName = CharField()

    class Meta:
        database =db
        table_name = 'data'


class JsonPathDataModel(Model):
    key = CharField(primary_key=True)
    title = CharField()
    description = CharField()
    project = ForeignKeyField(ProjectModel, on_delete='CASCADE',column_name='project')
    module = CharField()
    data = JsonPathField()
    interfaceName = CharField()


    class Meta:
        database =db
        table_name = 'data'


class JsonPathTimeRangeModel(DataModel):
    data = TimeRangeField()
