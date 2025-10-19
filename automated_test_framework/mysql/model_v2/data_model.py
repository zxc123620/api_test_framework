#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 18:34
# Author:zhouxiaochuan
# Description:
from peewee import Model, CharField, AutoField

from automated_test_framework.mysql.model_v2.define_field import JSONField


class DataModel(Model):
    key = CharField()
    title = CharField()
    description= CharField()
    project = AutoField()
    module= CharField()
    data = JSONField()
    interfaceName = CharField()