# -*- coding: utf-8 -*-
from app import db
from Basic import Basic

class Friends(db.Document, Basic):
    '''
        朋友关系类
    '''
    # 关注者
    userFrom = db.IntField(required=True)
    # 被关注者
    userTo = db.IntField(required=True)

    def to_dict(self):
        return dict(
            userFrom=self.userFrom,
            userTo=self.userTo
        )
