# -*- coding: utf-8 -*-
from app import db
from Basic import Basic


class MovieBasic(object):
    '''
        电影事件基础类
    '''

    # 用户Id
    userId = db.StringField(max_length=60, required=True)
    # 电影Id
    movieId = db.StringField(max_length=60, required=True)
    # 创建日期
    createTime = db.DateTimeField(required=True)
    # 更新日期
    updateTime = db.DateTimeField(required=True)


class MovieRecordEvent(db.Document, MovieBasic):
    '''
        日历中的电影观看记录事件
    '''

    # 观看次数
    num = db.IntField(required=True)
    # 观看感想
    impression = db.ListField(db.StringField(max_length=2048))
    # 未来观看日期
    featureDate = db.StringField(max_length=64)
    # 观看地址
    address = db.ListField(db.StringField(max_length=2048))
    # 观看日期
    date = db.ListField(db.StringField(max_length=64))

    def to_dict(self):
        return dict(
            userId = self.userId,
            movieId = self.movieId,
            date = self.date,
            num = self.num,
            featureDate = self.featureDate,
            address = self.address,
            impression = self.impression,
            createTime = self.createTime,
            updateTime = self.updateTime
        )
