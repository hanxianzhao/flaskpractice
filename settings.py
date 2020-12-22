# -*- coding: utf-8 -*-
"""
@author:韩先钊
@file: settings.py
@time: 2020/12/22  22:34
"""


class Config(object):
    DEBUG = True
    SECRET_KEY = "qwertyuiosdfghj"


class ProductionConfig(object):
    DEBUG = True


class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = "qwertyuiosdfghj"

class TestingConfig(object):
    Testing = True
