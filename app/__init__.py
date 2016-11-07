# coding=utf-8

from flask_mongoengine import MongoEngine
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
app.secret_key = 'GryffindorProject'
db = MongoEngine(app)
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view='get_user_login'

# models
from app.models.Movie import BasicInfo # 电影基本信息
from app.models.Movie import Details # 电影细节信息
from app.models.Movie import Score # 电影分数信息
from app.models.Movie import Fullcredits # 电影演职人员
from app.models.Movie import Awards # 电影得奖信息
from app.models.Movie import Comment # 电影评论信息
from app.models.Movie import Plot # 电影简介信息
from app.models.Movie import Scenes # 电影幕后解密
from app.models.MovieEvent import MovieRecordEvent # 电影记录事件
from app.models.MovieEvent import MovieFeatureEvent # 电影未来观看事件
from app.models.User import User

# router
from app.routes.calendar import calendar
from app.routes.movie import movie
from app.routes.user import user


@loginManager.user_loader
def load_user(id):
    return User.objects(id=(str(id))).first()