#coding=utf-8

from flask import render_template,redirect,url_for,request,flash,current_app
from . import main
from .forms import *
from app.models import Navcat,Page_system,Service
from app import db
import datetime,random
import os
from werkzeug import secure_filename
try:
	import Image
except Exception, e:
	from PIL import Image

@main.route('/')
@main.route('/200')
def index():
	page = request.args.get('page', 1, type=int)
	page = Page_system.query.order_by(Page_system.view.desc()).paginate(page,12,error_out=False)
	return render_template('main/index.html',page=page)

#添加服务器
@main.route('/add_service',methods=['GET'])
def add_service():
	return render_template('main/add_service.html',form=ServiceForm())

@main.route('/add_service',methods=['POST'])
def add_service_post():
	form = ServiceForm()
	if form.validate_on_submit():
		service = Service()
		service.name = form.name.data
		service.username = form.username.data
		service.password = form.password.data
		service.ip = form.ip.data
		db.session.add(service)
		db.session.commit()
		flash(u'添加服务器完成')
	else:
		flash(u'数据校验失败')
	return redirect(url_for('.add_service'))

#添加项目
@main.route('/add_project',methods=['GET'])
def add_project():
	form = PageForm()
	form.service.choices = [(g.id, g.name) for g in Service.query.all()]
	form.navcat.choices = [(g.id, g.title) for g in Navcat.query.all()]
	return render_template('main/add_project.html',form = form)
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))
@main.route('/add_project',methods=['POST'])
def add_project_post():
	form = PageForm()
	
	form.service.choices = [(form.service.data,'')]
	form.navcat.choices = [(form.service.data,'')]
	print form.navcat.choices[0][0]
	if form.validate_on_submit():
		fname, fext = os.path.splitext(form.thumbnail.data.filename)
		rnd_name = '%s%s' % (gen_rnd_filename(), fext)
		im = Image.open(form.thumbnail.data)
		im.thumbnail((200, 300))
		filepath = os.path.join(current_app.static_folder, 'uploads/static_html_thumbnail', rnd_name)
		im.save(filepath)

		ps = Page_system()
		ps.number = form.number.data
		ps.note = form.note.data
		ps.url = form.url.data
		try:
			service = Service.query.get_or_404(int(form.service.choices[0][0]))
			navcat = Navcat.query.get_or_404(int(form.navcat.choices[0][0]))
			ps.service = service
			ps.Navcat = navcat
		except Exception, e:
			flash(u'数据校验失败:%s'%str(e))
			return redirect(url_for('.add_project'))
		ps.thumbnail = '/static/uploads/static_html_thumbnail/'+rnd_name
		try:
			db.session.add(ps)
			db.session.commit()
			flash(u'添加页面内容完成')
		except Exception, e:
			db.session.rollback()
			flash(u'添加页面内容失败：%s'%str(e))
		
	else:
		flash(u'数据校验失败')
	return redirect(url_for('.add_project'))

#添加导航
@main.route('/add_navcat',methods=['GET'])
def add_navcat():
	return render_template('main/add_navcat.html',form=NavcatForm())

@main.route('/add_navcat',methods=['POST'])
def add_navcat_post():
	form = NavcatForm()
	if form.validate_on_submit():
		navcat = Navcat()
		navcat.title = form.title.data
		db.session.add(navcat)
		db.session.commit()
		flash(u'添加导航完成')
	return redirect(url_for('.add_navcat'))


@main.route('/show/<int:id>')
def show(id):
	page = Page_system.query.get_or_404(id)
	page.view +=1
	db.session.add(page)
	db.session.commit()
	return redirect(page.url)


