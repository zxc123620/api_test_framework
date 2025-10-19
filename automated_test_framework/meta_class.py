#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time:2025/10/19 17:41
# Author:zhouxiaochuan
# Description:

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = type.__call__(cls, *args, **kwargs)
        return cls._instances[cls]