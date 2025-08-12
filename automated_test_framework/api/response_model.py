#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :response_model.py
# @Time      :2025/8/3 22:55
# @Author    :zhouxiaochuan
# @Description:
from typing import Optional

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status_code: int
    headers: dict
    json_body: Optional[dict]
    content: Optional[bytes]
    text: Optional[str]

# ResponseModel().model_dump_json()