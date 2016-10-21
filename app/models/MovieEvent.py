# -*- coding: utf-8 -*-
from app import db
from Basic import Basic


class MovieBasic(db.Document, Basic):
    '''
        电影事件基础类
    '''

    # 用户Id
    userId = db.StringField(max_length=60, required=True)
    # 电影Id
    movieId = db.StringField(max_length=60, required=True)
    # 对应日期
    date = db.DateTimeField(required=True)


class MovieRecordEvent(db.Document, MovieBasic):
    '''
        日历中的电影观看记录事件
    '''

    # 观看次数
    num = db.IntField(required=True)
    # 观看时间
    time = db.ListField(db.StringField(max_length=60))
    # 观看感想
    impression = db.ListField(db.StringField(max_length=2048))

    def to_dict(self):
        return dict(
            userId = self.userId,
            movieId = self.movieId,
            date = self.date,
            num = self.num,
            time = self.time,
            impression = self.impression
        )

class MovieExpectEvent(db.Document, MovieBasic):
    '''
        日历中的未来电影观看安排事件
    '''

    # 观看原因
    reason = db.StringField(db.StringField(max_length=2048))

    def to_dict(self):
        return dict(
            userId=self.userId,
            movieId=self.movieId,
            date=self.date,
            reason = self.reason
        )