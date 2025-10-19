#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_locate_model.py
# @Time      :2025/10/15 11:58
# @Author    :zhouxiaochuan
# @Description:
from typing import Optional

from pydantic import BaseModel


class MysqlLocateDataModel(BaseModel):
    key: str
    locate_type: str
    desc: Optional[str]
    locate_value: int
    page: Optional[str]
