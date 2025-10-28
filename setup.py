#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :setup.py
# @Time      :2025-06-11 21:45
# @Author    :zhouxiaochuan
# @description:
from setuptools import setup, find_packages

setup(
    name='AutomatedTestFramework',  # 包名
    version='0.0.2',  # 版本号
    description='自动化测试框架(初版)',  # 简短描述
    long_description=open('README.md', "r", encoding="utf-8").read(),  # 从 README.md 读取长描述
    long_description_content_type='text/markdown',  # 长描述的格式
    author='zhouxiaochuan',  # 作者
    author_email='3067188237@qq.com',  # 作者邮箱
    packages=find_packages(),  # 自动查找所有包
    install_requires=[  # 依赖列表
        'pycryptodome',
        'PyYAML',
        'Requests',
        'PyMySQL',
        'pydantic',
        "jsonpath",
        "peewee",
        "selenium"
    ],
    python_requires='>=3.9',  # Python 版本要求
)
