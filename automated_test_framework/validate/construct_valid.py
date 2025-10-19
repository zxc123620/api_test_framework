#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :construct_valid.py
# @Time      :2025/4/9 22:00
# @Author    :zhouxiaochuan
# @Description: 结构验证器
# import copy
# import logging
#
# import yaml
from pydantic import BaseModel, ValidationError
#
#
# def yml_load(yml_file_path):
#     with open(yml_file_path, 'r', encoding="utf-8") as f:
#         data = yaml.load(f.read(), Loader=yaml.FullLoader)
#         return data
#
#
# def construct_valid(expect_cons: dict, actual_data: dict):
#     """
#     结构验证器
#     :param expect_cons: 预期结构
#     :param actual_data: 实际结构
#     :return:
#     """
#     expect_cons = copy.deepcopy(expect_cons)
#     for key in expect_cons.keys():
#         item_data = expect_cons.get(key)
#         need = item_data.pop("py_need")  # 是否必须项
#         data_type = item_data.pop("py_type")  # 数据类型
#         if need:
#             # 如果是必须,就要进行验证
#             logging.debug(f"{key}为必须项,需要进行验证")
#             assert key in actual_data.keys(), f"结构验证不通过, {key}为必须项,但不存在与{list(actual_data.keys())}中"
#         # 查看是否有子项
#         if data_type == "dict" and key in actual_data.keys():
#             # 如果为字典,就进入到里面继续验证
#             construct_valid(item_data, actual_data.get(key))
#         if data_type == "list" and key in actual_data.keys() and isinstance(actual_data.get(key), list) and len(
#                 actual_data.get(key)) > 1:
#             for in_data in actual_data.get(key):
#                 construct_valid(item_data.get("py_sub_list")[0], in_data)


#
# def api_response_construct_valid_decorator(yml_file_path: str):
#     """
#     api返回数据结构验证装饰器
#     :param yml_file_path:
#     :return:
#     """
#     logging.info("装饰器生效")
#     expect_data = yml_load(yml_file_path)
#
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             response_obj = func(*args, **kwargs)
#             if response_obj.has_resp_body():
#                 # 验证
#                 construct_valid(expect_cons=expect_data, actual_data=response_obj.res_body)
#             return response_obj
#
#         return inner
#
#     return wrapper
#
# def api_response_construct_valid_decorator(validate_model):
#     """
#     api返回数据结构验证装饰器
#     :param validate_model:
#     :return:
#     """
#
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             response_obj = func(*args, **kwargs)
#             if response_obj.has_resp_body():
#                 logging.info("验证结构")
#                 try:
#                     response_obj.model_v1 = validate_model(**response_obj.res_body)
#                     logging.info("结构验证通过")
#                 except ValidationError as e:
#                     logging.exception(e.errors())
#                     assert False, f"结构验证不通过,理由:{e.errors()}"
#             return response_obj
#
#         return inner
#
#     return wrapper
