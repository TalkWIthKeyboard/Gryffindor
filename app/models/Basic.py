# -*- coding: utf-8 -*-
from app import db

class Basic(db.Document):
    '''
        数据库的基本共有属性
    '''

    # 创建时间
    createAt = db.StringField(max_length=60, required=True)
    # 更新时间
    updateAt = db.StringField(max_length=60, required=True)