# -*- coding: utf-8 -*-
from app import db
from Basic import Basic

class MovieEvent(db.Document, Basic):
    '''
        日历中的电影事件
    '''

    # 用户Id
    userId = db.StringField(max_length=60, required=True)
    # 电影Id
    movieId = db.StringField(max_length=60, required=True)
    # 观看时间
    time = db.StringField(max_length=60)
    # 观看感想
    impression = db.StringField(max_length=2048)

    def to_dict(self):
        return dict(
            userId = self.userId,
            movieId = self.movieId,
            time = self.time,
            impression = self.impression
        )