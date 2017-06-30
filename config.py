#coding=utf-8
"""filename:config.py
Created 2017-05-29
Author: by anaf
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	#保护字段，必须设置  
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'strings'
	#sql自动提交
	SQLALCHEMY_COMMIT_ONTRARDOWN = True
	#####
	SQLALCHEMY_TRACK_MODIFICATIONS  = False

	@staticmethod
	def init_app(app):
		pass

#开发配置
class DevelopmentConfig(Config):
	DEBUG = True
	SUPERADMIN_NAME = os.environ.get('SUPERADMIN_NAME') or 'admin'
	#配置数据库路径从系统变量读取没有就根据字符串中的读取 mysql为例子
	SQLALCHEMY_DATABASE_URI = os.environ.get('dev_database_url') or \
		'mysql://root:@127.0.0.1:3306/project_management'

#测试配置
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('dev_database_url') or \
		'mysql://root:@127.0.0.1:3306/project_management'


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('dev_database_url') or \
		'mysql://root:@localhost:3306/project_management'


config = {
	'development' : DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}

