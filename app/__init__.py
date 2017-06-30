#coding=utf-8
"""filename:app/__init__.py
Created 2017-06-30
Author: by anaf
note:初始化函数
"""

from flask import Flask,render_template
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap

mail = Mail()
moment = Moment()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
#session_protection属性可以设置None，basic，strong提供不同的安全等级防止用户会话遭篡改
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u"请登录后访问该页面."

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	bootstrap.init_app(app)

	#添加蓝图main,auth
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/auth')


	login_manager.init_app(app)

	return app

"""
python manage.py shell 
from app import db 
db.create_all()
from app.models import Role,User
admin_role = Role(name = 'admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')
user_admin = User(username='admins',password='admins',role=admin_role)
user_mod = User(username='moderator',password='moderator',role=mod_role)
user_user = User(username='use',password='use',role=user_role)
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add_all([user_admin,user_mod,user_user])
db.session.commit()
"""