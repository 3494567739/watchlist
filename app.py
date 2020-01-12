# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 07:37:07 2020

@author: Nicolas Xiong
"""

from flask import Flask
from flask import url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
import os
import click



app=Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

# @app.route('/') 
# @app.route('/index') 
# @app.route('/home')
# def hello():   
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# @app.route('/static/favicon.ico')
# def get_fav():
#     print(__name__)
#     return app.send_static_file('favicon.ico')

# @app.route('/user/<name>') 
# def user_page(name):    
#     return 'User: %s' % name

# @app.route('/test') 
# def test_url_for():    
#     # 下面是一些调用示例：    
#     print(url_for('index'))  # 输出：/    
#     # 注意下面两个调用是如何生成包含 URL 变量的 URL 的    
#     print(url_for('user_page', name='nicolasxiong'))  # 输出：/user/nicolasxoing    
#     print(url_for('test_url_for'))  # 输出：/test    
#     # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。    
#     print(url_for('test_url_for', num=2))  # 输出：/test?num=2    
#     return 'Test page'

@app.context_processor 
def inject_user():           #这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用
    user = User.query.first()    
    return dict(user=user)

@app.route('/') 
def index():     
    movies = Movie.query.all()  # 读取所有电影记录
    return render_template('index.html', movies=movies)

@app.errorhandler(404)  # 传入要处理的错误代码 
def page_not_found(e):  # 接受异常对象作为参数      
    return render_template('404.html'), 404  # 返回模板和状态码

@app.cli.command() 
def forge():    
    """Generate fake data."""    
    db.create_all()
    
    name = 'Nicolas Xiong'
    movies = [
                           {'title': 'My Neighbor Totoro', 'year': '1988'},
                           {'title': 'Dead Poets Society', 'year': '1989'},    
                           {'title': 'A Perfect World', 'year': '1993'},    
                           {'title': 'Leon', 'year': '1994'},    
                           {'title': 'Mahjong', 'year': '1996'},    
                           {'title': 'Swallowtail Butterfly', 'year': '1996'},    
                           {'title': 'King of Comedy', 'year': '1999'},    
                           {'title': 'Devils on the Doorstep', 'year': '1999'},    
                           {'title': 'WALL-E', 'year': '2008'},
                           {'title': 'The Pork of Music', 'year': '2012'}
                           ]
    
    user = User(name=name)    
    db.session.add(user)    
    for m in movies:        
         movie = Movie(title=m['title'], year=m['year'])        
         db.session.add(movie)
         
    db.session.commit()    
    click.echo('Done.')


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）    
    id = db.Column(db.Integer, primary_key=True)  # 主键    
    name = db.Column(db.String(20))  # 名字
    
class Movie(db.Model):  # 表名将会是 movie    
    id = db.Column(db.Integer, primary_key=True)  # 主键    
    title = db.Column(db.String(60))  # 电影标题    
    year = db.Column(db.String(4))  # 电影年份
























