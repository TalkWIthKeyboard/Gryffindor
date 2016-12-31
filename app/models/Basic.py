# -*- coding: utf-8 -*-
from app import db
from datetime import datetime


class Basic(object):
    '''
        数据库的基本共有属性
    '''

    # 创建时间
    createTime = db.DateTimeField(required=True)
    # 更新时间
    updateTime = db.DateTimeField(required=True)
