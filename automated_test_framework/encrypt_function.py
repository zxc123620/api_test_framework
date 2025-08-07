#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :encrypt_function.py
# @Time      :2025/8/5 18:19
# @Author    :zhouxiaochuan
# @Description: 

import json

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS_cipher
import base64


def encrypt_data(data: dict, public_key_str):
    """
    RSA加密
    :param public_key_str:
    :param data:
    :return:
    """
    # public_key_str = """-----BEGIN PUBLIC KEY-----
    # MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoAWjg0r6UQ3fih4EZK8Sz4tIcRdM3LPFQEXwBJSKBsKiker89olABv7UM7NRQn0+OQ6Mz7gYbig+h1vK+RHtcwuJ/Ub7crz50NFuo+L+jxhR0mBNC0Sf9nAqUH/Q95715rRKiiwA5U5c9cF70ZCxFGcWZqJvQVUPiHVFwWbWZswIDAQAB
    # -----END PUBLIC KEY-----"""
    public_key = RSA.import_key(public_key_str)
    cipher = PKCS_cipher.new(public_key)
    data_str = json.dumps(data).replace(" ", '').encode("utf-8")
    encrypted_data = cipher.encrypt(bytes(data_str))
    return base64.b64encode(encrypted_data).decode("utf-8")
