#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pims_logger.py
# @Time      :2025/2/23 18:50
# @Author    :zhouxiaochuan
# @Description: 
import logging.config
import os
log_dir = os.path.join(os.getcwd(), "log")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": log_dir + "/info.log",
            "maxBytes": 1024*1024*100,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": log_dir + "/errors.log",
            "maxBytes": 1024*1024*100,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "debug_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": log_dir + "/debug.log",
            "maxBytes": 1024*1024*100,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "info_file_handler", "error_file_handler","debug_file_handler"]
    }
}
logging.config.dictConfig(log_config)
