# -*- coding: utf-8 -*-
from app import db
from datetime import datetime

class Basic(db.Document):
    '''
        数据库的基本共有属性
    '''

    # 创建时间
    createAt = db.DateTimeField(required=True)
    # 更新时间
    updateAt = db.DateTimeField(required=True)
