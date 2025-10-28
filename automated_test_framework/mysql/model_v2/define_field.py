#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 18:47
# Author:zhouxiaochuan
# Description:
import json
from typing import Union

from peewee import TextField, CharField
from pydantic import BaseModel
from selenium.webdriver.common.by import By


class LocateBy:
    ID = By.ID
    XPATH = By.XPATH
    LINK_TEXT = By.LINK_TEXT
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    NAME = By.NAME
    TAG_NAME = By.TAG_NAME
    CLASS_NAME = By.CLASS_NAME
    CSS_SELECTOR = By.CSS_SELECTOR


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)
        return None


class JsonPathField(TextField):
    class JsonPathFiledModel(BaseModel):
        expect_data: Union[dict, list, str]
        jsonpath_exp: str

        def get_list_expect_data(self):
            return list(self.expect_data)

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return JsonPathField.JsonPathFiledModel(**json.loads(value))
        return None


class TimeRangeField(TextField):
    class JsonPathTimeRangeModel(BaseModel):
        class TimeRangeModel(BaseModel):
            start_time: str
            end_time: str

        expect_data: TimeRangeModel
        jsonpath_exp: str

        def get_list_expect_data(self):
            return list(self.expect_data)

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return TimeRangeField.JsonPathTimeRangeModel(**json.loads(value))
        return None


class LoginField(TextField):
    class LoginModel(BaseModel):
        username: str
        password: str
        name: str

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return LoginField.LoginModel(**json.loads(value))
        return None


class SeleniumBYField(CharField):

    def db_value(self, value):
        return value

    def python_value(self, value):
        if value is not None:
            return getattr(LocateBy, value)
        return None
