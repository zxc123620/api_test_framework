#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/20 21:56
# Author:zhouxiaochuan
# Description:
from peewee import Model, AutoField, CharField

from automated_test_framework.mysql.model_v2 import db


class ProjectModel(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    description = CharField()

    class Meta:
        database =db
        table_name = 'project'

if __name__ == '__main__':
   pass