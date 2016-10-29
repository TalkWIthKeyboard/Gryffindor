# coding=utf-8

from flask_mongoengine import MongoEngine
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
app.secret_key = 'GryffindorProject'
db = MongoEngine(app)


# loginManager = LoginManager()
# loginManager.init_app(app)
# loginManager.login_view='admin_login'

# models
from app.models.Movie import BasicInfo # 电影基本信息
from app.models.Movie import Details # 电影细节信息
from app.models.Movie import Score # 电影分数信息
from app.models.Movie import Fullcredits # 电影演职人员
from app.models.MovieEvent import MovieRecordEvent # 电影记录事件

# router
from app.routes.calendar import calendar
from app.routes.movie import movie

#
# @loginManager.user_loader
# def load_user(id):
#     if str(id) == 'None':
#         return None
#     return User.objects(myid=int(id)).first()