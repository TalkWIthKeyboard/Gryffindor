# -*- coding: utf-8 -*-
from app import db

class UserInfo(db.Document):
    '''
        用户信息类
    '''
    myid = db.IntField(required=True)
    # 账号
    account = db.StringField(max_length=60,required=True)
    # 密码（md5加密）
    password = db.StringField(max_length=60,required=True)
    # 用户名
    username = db.StringField(max_length=60,required=True)
    # 头像路径
    userimage = db.StringField

    meta = {
        'ordering': ['-myid']
    }

    def to_dict(self):
        return dict(
            myid = self.myid,
            account = self.account,
            password = self.password,
            username = self.username,
            userimage = self.userimage
        )