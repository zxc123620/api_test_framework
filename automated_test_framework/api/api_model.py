#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pims_api.py
# @Time      :2025-05-25 10:04
# @Author    :zhouxiaochuan
# @description:
import logging

import requests
from automated_test_framework.api.response_model import ResponseModel

from automated_test_framework.load_config import GlobalConfig
from automated_test_framework.temp_data import TempData


class ApiModel:
    @staticmethod
    def api_inject(url, method, response_model_cls=None, log=False):
        """
        Api注册
        :param log:
        :param url: 地址
        :param method: 方法
        :param response_model_cls: 响应模型
        :return:
        """

        def inner_function(func):
            def inner(params: dict = None, json: dict = None, *args, **kwargs):
                headers = TempData.HEADER if TempData.HEADER else None
                protocol = GlobalConfig().ServerConfig.protocol
                host = GlobalConfig().ServerConfig.host
                port = GlobalConfig().ServerConfig.port
                new_url = url
                if "http" not in url:
                    new_url = f"{protocol}://{host}:{port}/{url}"
                logging.info(f"请求url:{url}, 方法:{method}, 头部信息:{headers}")
                response = requests.request(method=method, url=new_url, json=json, params=params, headers=headers, timeout=10,verify=False)
                logging.info(f"响应码:{response.status_code}")
                res_json = response.json()
                res_text = response.text
                res_content = response.content
                logging.info(f"响应头:{response.headers}, 响应内容:{res_json}, 响应文本:{res_text}, 响应二进制数据:{res_content}") if log else None
                response_model_cls_new = ResponseModel if response_model_cls is None else response_model_cls
                res_model = response_model_cls_new(**{"status_code": response.status_code, "headers": response.headers,
                                                      "json_body": response.json(), "content": response.content,
                                                      "text": response.text})
                logging.info("响应模型生成完毕")
                func_result = func(params, json, *args, **kwargs)
                logging.info("函数执行完毕")
                if func_result is None:
                    return res_model
                else:
                    return res_model, func_result

            return inner

        return inner_function


if __name__ == '__main__':
    log = False
    logging.info("123") if log else None
