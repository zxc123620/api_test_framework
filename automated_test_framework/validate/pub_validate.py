#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pub_validate.py
# @Time      :2025-05-25 15:35
# @Author    :zhouxiaochuan
# @description:
import logging
from enum import Enum

import jsonpath

from automated_test_framework.enum import AssertType
from automated_test_framework.framework_error import ParamConvertError
from automated_test_framework.mysql.data_get import MysqlDataGet


class PubValidate:

    @staticmethod
    def __json_path_extrack(json_path_exp: str, expect_data, actual_data):
        """
        jsonPath验证
        :param json_path_exp: json_path语法
        :param expect_data: 预期验证数据
        :param actual_data: 实际验证数据
        :return:
        """
        logging.info(f"jsonpath语法:{json_path_exp},从实际结果中提取数据...")
        result = jsonpath.jsonpath(actual_data, json_path_exp)
        assert result, f"jsonpath解析失败,未从数据中提取到{json_path_exp}数据"
        logging.info("提取成功,开始验证")
        return expect_data, result
        # valid_method(expect_data, result)


    @classmethod
    def json_path_data_in_assert(cls, json_path_exp: str, expect_data, actual_data):
        """
        data_in验证
        :param json_path_exp:
        :param expect_data:
        :param actual_data:
        :return:
        """
        expect_data, result = cls.__json_path_extrack(json_path_exp, expect_data, actual_data)
        cls.assert_data_in(expect_data, result)

    @classmethod
    def json_path_data_in_validate(cls, data_id:str, res_model):
        """
        data_in验证
        :param data_id:
        :param res_model:
        :return:
        """
        model = MysqlDataGet.get_data(data_id)
        PubValidate.json_path_data_in_assert(model.data.jsonpath_exp, model.data.expect_data, res_model.json_body.model_dump())

    @classmethod
    def json_path_data_in_loop_validate(cls, data_id_list:list, res_model):
        """
        data_in多验证
        :param data_id_list:
        :param res_model:
        :return:
        """
        for data_id in data_id_list:
            model = MysqlDataGet.get_data(data_id)
            PubValidate.json_path_data_in_assert(model.data.jsonpath_exp, model.data.expect_data, res_model.json_body.model_dump())

    @classmethod
    def json_path_list_equal_validate(cls, data_id:str, res_model):
        """
        列表相等验证
        :param data_id:
        :param res_model:
        :return:
        """
        model = MysqlDataGet.get_data(data_id)
        expect_data, result = cls.__json_path_extrack(model.data.jsonpath_exp, model.data.expect_data, res_model.json_body.model_dump())
        cls.assert_list_equal(expect_data, result)

    @classmethod
    def json_path_list_equal_loop_validate(cls, data_id_list:list, res_model):
        """
        多验证
        :param res_model:
        :param data_id_list:
        :return:
        """
        for data_id in data_id_list:
            model = MysqlDataGet.get_data(data_id)
            expect_data, result = cls.__json_path_extrack(model.data.jsonpath_exp, model.data.expect_data, res_model.json_body.model_dump())
            cls.assert_list_equal(expect_data, result)


    @classmethod
    def json_path_list_in_loop_validate(cls, data_id_list:list, res_model):
        """
        多验证
        :param res_model:
        :param data_id_list:
        :return:
        """
        for data_id in data_id_list:
            model = MysqlDataGet.get_data(data_id)
            expect_data, result = cls.__json_path_extrack(model.data.jsonpath_exp, model.data.expect_data, res_model.json_body.model_dump())
            cls.assert_list_in(expect_data, result)

    @classmethod
    def json_path_list_equal_assert(cls, json_path_exp: str, expect_data, actual_data):
        """
        列表相等验证
        :param json_path_exp:
        :param expect_data:
        :param actual_data:
        :return:
        """
        expect_data, result = cls.__json_path_extrack(json_path_exp, expect_data, actual_data)
        cls.assert_list_equal(expect_data, result)

    @staticmethod
    def assert_data_in(expect_data: dict, actual_data_list: list):
        """
        验证预期的字典是否在实际字典的里面
        :param expect_data:
        :param actual_data_list:
        :return:
        """
        test_pass = False
        logging.info(f"预期结果:{expect_data}, 实际结果:{actual_data_list}")
        for index, actual_data in enumerate(actual_data_list):
            for expect_key, expect_value in expect_data.items():
                actual_value = actual_data.get(expect_key, None)
                logging.info(f"从实际结果中提取到[{expect_key}],数据:[{actual_value}]")
                try:
                    assert actual_value == expect_value, \
                        f"{expect_key}预期结果与实际结果不一致,预期:[{expect_value}],类型：{type(expect_value)},实际:[{actual_value}],类型:{type(actual_value)}"
                    test_pass = True
                    break
                except AssertionError as e:
                    logging.info(e)
        assert test_pass

    @staticmethod
    def assert_data_equal(expect_data, actual_data):
        """
        验证两个值是否相等
        :param expect_data:
        :param actual_data:
        :return:
        """
        logging.info(f"值相等验证,预期值:{expect_data}, 实际值:{actual_data}")
        assert expect_data == actual_data, f"预期结果[{expect_data}]与实际结果[{actual_data}]不一致"

    @staticmethod
    def convert_to_list(data):
        raw = data
        if not isinstance(data, list):
            data = eval(data)
        if not isinstance(data, list):
            raise ParamConvertError(f"将{raw}转换为列表失败")
        return data

    @classmethod
    def assert_list_equal(cls,expect_data, actual_data:list):
        """
        验证实际结果列表数据是否相等
        :param expect_data:
        :param actual_data:
        :return:
        """
        expect_data = cls.convert_to_list(expect_data)
        assert set(actual_data) == set(expect_data), f"预期列表与实际列表不一致,预期{expect_data},类型：{type(expect_data)}, 实际:{actual_data},类型:{type(actual_data)}"

    @classmethod
    def assert_list_in(cls, expect_data, actual_data):
        """
        验证列表包含
        """
        expect_data = cls.convert_to_list(expect_data)
        assert set(expect_data) == set(actual_data) & set(expect_data),f"预期列表与实际列表不一致,预期{expect_data},类型：{type(expect_data)}, 实际:{actual_data},类型:{type(actual_data)}"

    @staticmethod
    def loop_verify_for_jsonpath(case_key_list, api_res_model, assert_type: AssertType):
        """
        从case_id获取数据并进行jsonpath验证
        :param assert_type:
        :param case_key_list:
        :param api_res_model:
        :return:
        """
        for key in case_key_list:
            model = MysqlDataGet.get_data(key)
            jsonpath_exp = model.data.jsonpath_exp
            expect_data = model.data.expect_data
            if assert_type == AssertType.DATA_IN:
                PubValidate.json_path_data_in_assert(jsonpath_exp, expect_data, api_res_model)
            elif assert_type == AssertType.LIST_EQUAL:
                PubValidate.json_path_list_equal_assert(jsonpath_exp, expect_data, api_res_model)
