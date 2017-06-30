#coding=utf-8
"""filename:app/main/__init__.py
Created 2017-06-30
Author: by anaf
note:main/__init__.py  Blueprint蓝图
""" 

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,forms


