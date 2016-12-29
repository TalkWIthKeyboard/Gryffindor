# -*- coding: utf-8 -*-
from app import db


class MovieBasic(object):
    '''
        电影事件基础类
    '''

    # 用户Id
    userId = db.StringField(max_length=60, required=True)
    # 电影Id
    movieId = db.StringField(max_length=60, required=True)
    # 创建时间
    createTime = db.DateTimeField(required=True)
    # 更新时间
    updateTime = db.DateTimeField(required=True)


class MovieRecordEvent(db.Document, MovieBasic):
    '''
        日历中的电影观看记录事件
    '''

    # 观看次数
    num = db.IntField(required=True)
    # 观看感想
    impression = db.StringField(max_length=2048)
    # 观看地址
    address = db.StringField(max_length=2048)
    # 观看日期
    date = db.DateTimeField(required=True)

    meta = {
        'ordering': ['-num']
    }

    def to_dict(self):
        return dict(
            userId=self.userId,
            movieId=self.movieId,
            date=self.date,
            num=self.num,
            address=self.address,
            impression=self.impression,
            createTime=self.createTime,
            updateTime=self.updateTime
        )


class MovieFeatureEvent(db.Document, MovieBasic):
    '''
        日历中的未来观影事件
    '''
    # 未来观看日期
    date = db.DateTimeField(required=True)

    def to_dict(self):
        return dict(
            userId=self.userId,
            movieId=self.movieId,
            date=self.date,
            createTime=self.createTime,
            updateTime=self.updateTime
        )
