#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :url_save_model.py
# @Time      :2025/10/27 19:47
# @Author    :zhouxiaochuan
# @Description:
from automated_test_framework.mysql.model_v2 import db
from peewee import Model, CharField, AutoField


class UrlSaveModel(Model):
    key = CharField(max_length=100, primary_key=True)
    protocol = CharField(max_length=100)
    host = CharField(max_length=100)
    port = AutoField()
    path = CharField(max_length=255)
    desc = CharField(max_length=255)

    class Meta:
        database = db
        table_name = 'url_save'

    def get_full_path(self):
        if self.path.startswith("/"):
            path = self.path[1:]
        else:
            path = self.path
        return f"{self.protocol}://{self.host}:{self.port}/{path}"
