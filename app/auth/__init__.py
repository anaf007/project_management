#coding=utf-8
"""filename:app/auth/__init__.py
Created 2017-05-30
Author: by anaf
note:auth初始化函数
"""

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views 