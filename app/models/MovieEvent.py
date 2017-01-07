# -*- coding: utf-8 -*-
from app import db


class MovieBasic(object):
    '''
        电影事件基础类
    '''

    _id = db.ObjectIdField()
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
    # 类型(0 是曾经观看，1是将要观看)
    state = db.IntField()

    meta = {
        'ordering': ['-createTime']
    }

    def to_dict(self):
        return dict(
            _id=str(self._id),
            userId=self.userId,
            movieId=self.movieId,
            date=self.date,
            num=self.num,
            address=self.address,
            impression=self.impression,
            createTime=self.createTime,
            updateTime=self.updateTime,
            state=self.state
        )
