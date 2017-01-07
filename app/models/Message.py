# -*- coding: utf-8 -*-
from app import db
from Basic import Basic


class Message(db.Document, Basic):
    '''
        朋友关系类
    '''

    _id = db.ObjectIdField()
    # 关联的感谢对应的电影事件的id
    movieEventId = db.StringField(required=True)
    # 留言者的id
    myid = db.IntField(required=True)
    # 留言的内容
    message = db.StringField(required=True)

    def to_dict(self):
        return dict(
            _id=str(self._id),
            movieEventId=self.movieEventId,
            myid=self.myid,
            message=self.message,
            createTime=self.createTime,
            updateTime=self.updateTime
        )
