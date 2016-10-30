# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class MtimeMixin(object):
    '''
        时光网上电影的id
    '''
    movieid = db.IntField(required=True)


class YearFinished(db.Document):
    '''
        完成电影的年份
    '''
    year = db.IntField(required=True)
    meta = {
        'indexes' : ['-year'],
        'ordering' : ['-year']
    }


class IdFinished(db.Document):
    '''
        按年份爬虫列表完成后保存电影的id
    '''
    year = db.IntField(required=True)
    ids = db.ListField(required=True)
    meta = {
        'indexes' : ['-year']
    }

class AliasName(db.Document):
    '''
        数据库中存在的名字和别名
    '''
    name = db.StringField(max_lenghth=60, required=True) # 数据库中存在的名字
    alias = db.ListField(db.StringField(max_length=60, required=True)) # 这个人的别名

class Actor(db.EmbeddedDocument):
    '''
        演员信息
    '''
    mid = db.IntField(default=0, required=True) # 演员链接的唯一ID
    poster = db.StringField(max_length=100) # 海报缩略图
    name = db.StringField(max_length=60, required=True) # 演员的名字
    play = db.StringField(max_length=60, required=True) #剧中人物

class Director(db.EmbeddedDocument):
    '''
        导演信息
    '''
    mid = db.IntField(default=0)  # 演员链接的唯一ID
    name = db.StringField(max_length=60)  # 导演名字
    cnname = db.StringField(max_length=60)  # 可能有中文翻译过来的名字
    poster =db. StringField(max_length=100)  # 海报缩略图

class Fullcredits(db.Document, MtimeMixin):
    '''
        演职员表
    '''
    director = db.ListField(db.EmbeddedDocumentField(Director))  # 导演
    writer = db.ListField(db.StringField(max_length=30, required=True))  # 编剧
    actor = db.ListField(db.EmbeddedDocumentField(Actor))  # 演员
    produced = db.ListField(db.StringField(max_length=60, required=True))  # 制作人
    originalmusic = db.ListField(
        db.StringField(max_length=60, required=True))  # 原创音乐
    cinematography = db.ListField(db.StringField(max_length=60, required=True))  # 摄影
    filmediting = db.ListField(db.StringField(max_length=60, required=True))  # 剪辑
    artdirection = db.ListField(db.StringField(max_length=60, required=True))  # 美术设计
    costumedesign = db.ListField(
        db.StringField(max_length=60, required=True))  # 服装设计
    assistantdirector = db.ListField(
        db.StringField(max_length=60, required=True))  # 副导演/助理导演
    def to_dict(self):
        return dict(
            director=self.director,
            writer=self.writer,
            actor=self.actor
        )


class EmbeddedReleaseInfo(db.EmbeddedDocument):
    encountry = db.StringField(max_length=30, required=True)  # 英文国家名
    cncountry = db.StringField(max_length=30, required=True)  # 中文国家名
    releasetime = db.DateTimeField(default=datetime.now(), required=True)  # 上映时间

class Movie(db.Document, MtimeMixin):
    '''
        电影信息
    '''
    rating = db.FloatField(required=True)  # 评分
    ratingcount = db.IntField(default=0, required=True)  # 评分人数
    want = db.IntField(default=0, required=True)  # 想看
    favorited = db.IntField(default=0, required=True)  # 收藏数

class Plot(db.Document, MtimeMixin):

    '''
        电影剧情
    '''
    content = db.ListField(db.StringField())  # 剧情片段

class EmbeddedScenes(db.EmbeddedDocument):
    title = db.StringField(max_length=30, required=True)  # 主题
    content = db.ListField(db.StringField())

class Scenes(db.Document, MtimeMixin):
    '''
        幕后揭秘
    '''
    scene = db.ListField(db.EmbeddedDocumentField(EmbeddedScenes))  # 花絮

class Company(db.EmbeddedDocument):
    '''
        制作/发行信息
    '''
    name = db.StringField(max_length=60, required=True)  # 公司名字
    country = db.StringField(max_length=30)  # 公司所在国家

class MovieInfo(db.EmbeddedDocument):
    '''
        更多的名字信息和时长
    '''
    enalias = db.ListField(db.StringField())  # 中文片名
    cnalias = db.ListField(db.StringField())  # 外文片名
    time = db.StringField(max_length=60)  # 片长

class Release(db.EmbeddedDocument):
    '''
        上映地区和时间
    '''
    encountry = db.StringField()  # 地区英文名
    cncountry = db.StringField()  # 地区中文名
    date = db.DateTimeField()  # 上映日期

class MovieDetail(db.EmbeddedDocument):
    '''
        制作公司、发行商等细节
    '''
    publish = db.ListField(db.EmbeddedDocumentField(Company))  # 发行公司
    make = db.ListField(db.EmbeddedDocumentField(Company))  # 制作公司

class Details(db.Document, MtimeMixin):
    '''
        详细信息
    '''
    movieinfo = db.EmbeddedDocumentField(MovieInfo)
    release = db.ListField(db.EmbeddedDocumentField(Release))
    detail = db.EmbeddedDocumentField(MovieDetail)
    def to_dict(self):
        return dict(
            movieinfo = self.movieinfo,
            release = self.release,
            detail = self.detail
        )

class Awardsinfo(db.EmbeddedDocument):
    type = db.StringField(max_length=30, required=True)  # 提名或者获奖
    peoples = db.ListField(db.ListField(required=True))  # 获奖的人, 但不是必选,有些奖项是整个电影的成就

class Oneawards(db.EmbeddedDocument):
    name = db.StringField(max_length=30, required=True)  # 奖项名, 比如 奥斯卡金像奖
    period = db.IntField(required=True)  # 届
    year = db.IntField(required=True)  # 年份
    awards = db.ListField(db.EmbeddedDocumentField(Awardsinfo))  # 获奖的具体情况: 奖项-人物

class Awards(db.Document, MtimeMixin):
    '''
        获奖记录
    '''
    awards = db.ListField(db.EmbeddedDocumentField(Oneawards))

class EmbeddedContent(db.EmbeddedDocument):
    type = db.StringField(max_length=10, required=True)  # 比如文本,视频,图片, 内嵌
    content = db.StringField()  # 内容

class EmbeddedComment(db.EmbeddedDocument):
    name = db.StringField(max_length=30, required=True)  # 发评论人
    commenter_url = db.StringField(max_length=100)  # 评论人的url
    ac = db.IntField(default=0, required=True)  # 点赞数
    rc = db.IntField(default=0, required=True)  # 转发数
    cc = db.IntField(default=0, required=True)  # 评论数
    url = db.StringField(max_length=100, required=True)  # 原文url
    poster = db.StringField(max_length=100)  # 原文的海报图
    image = db.StringField(max_length=120, required=True)  # 评论人图片url
    title = db.StringField(max_length=60)  # 标题
    score = db.FloatField()  # 评分, 只是看过的人会评分,但不评分
    content = db.ListField(db.EmbeddedDocumentField(EmbeddedContent))  # 评论内容
    shortcontent = db.StringField(default='')  # 评论内容的简略, 也就是mtime直接显示的那部分
    publishdate = db.DateTimeField(default=datetime.now())  # 发表时间

    meta = {'allow_inheritance': True}


class EmbeddedMicroComment(EmbeddedComment):
    content = db.StringField()  # 评论内容格式不同


class Comment(db.Document, MtimeMixin):
    comments = db.ListField(db.EmbeddedDocumentField(EmbeddedComment))  # 长评


class MicroComment(db.Document, MtimeMixin):
    microcomments = db.ListField(db.EmbeddedDocumentField(EmbeddedMicroComment))  # 微评

class Score(db.Document, MtimeMixin):
    '''
        电影评分
    '''
    favorited = db.IntField()  # 喜欢的人数
    rating = db.IntField()  # 得分 满分10分
    ratingcount = db.IntField()  # 参与评分的人数
    want = db.IntField()  # 想观看的人数

    def to_dict(self):
        return dict(
            movieid = self.movieid,
            favorited = self.favorited,
            rating = self.rating,
            ratingcount = self.ratingcount,
            want = self.want
        )

class EmbeddedBasicInfo(db.EmbeddedDocument):
    '''
        电影基本信息
    '''
    cnname = db.StringField()  # 主要的中文名字
    enname = db.StringField()  # 主要的英文名字
    img = db.StringField() # 宣传图url

class BasicInfo(db.Document, MtimeMixin):
    '''
        封装电影基本信息
    '''
    info = db.EmbeddedDocumentField(EmbeddedBasicInfo) # 基本信息列表

    def to_dict(self):
        info = self.info
        return dict(
            movieid = self.movieid,
            cnname = info.cnname,
            enname = info.enname,
            img = info.img
        )