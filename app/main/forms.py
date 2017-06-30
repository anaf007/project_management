#coding=utf-8
"""filename:app/main/forms.py
Created 2017-05-30
Author: by anaf
"""
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,\
	SubmitField,TextAreaField,FileField,SelectField
from wtforms.validators import Required,Length,Email
from app.models import Navcat,Page_system,Service

class NavcatForm(Form):
	title = StringField(u'导航名称',validators=[Required(),Length(1,30)])
	submit = SubmitField(u'提交')

class PageForm(Form):
	number = StringField(u'项目编号',validators=[Required(),Length(1,30)])
	service = SelectField(u'服务器',validators=[Required()])
	navcat = SelectField(u'栏目',validators=[Required()])
	note = StringField(u'备注',validators=[Required(),Length(1,200)])
	url = StringField(u'访问路径',validators=[Required(),Length(1,200)])
	thumbnail = FileField(u'缩略图',validators=[Required()])
	submit = SubmitField(u'添加')



class ServiceForm(Form):
	name = StringField(u'服务器名称',validators=[Required(),Length(1,30)])
	username = StringField(u'用户名',validators=[Required(),Length(1,30)])
	password = StringField(u'密码',validators=[Required(),Length(1,30)])
	ip = StringField(u'IP地址',validators=[Required(),Length(1,30)])
	submit = SubmitField(u'添加')


