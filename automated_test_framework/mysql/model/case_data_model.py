#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :case_data_model.py
# @Time      :2025-05-27 22:13
# @Author    :zhouxiaochuan
# @description:
from typing import Optional

from pydantic import BaseModel


class MysqlDataModel(BaseModel):
    key: str
    title: str
    description: str
    project: int
    module: str
    data: dict
    interfaceName: Optional[str]


if __name__ == '__main__':
    MysqlDataModel(**{'project': 1, 'module': '角色管理', 'title': '获取角色下的监测点、雷达列表信息', 'key': 'xlza.role.getStationIds',
                      'data': {'role_name': 'api_test'}, 'description': '获取角色下的监测点信息', 'interfaceName': None})
