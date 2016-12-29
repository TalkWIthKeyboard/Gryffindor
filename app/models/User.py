# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin


class User(db.Document, UserMixin):
    '''
        用户信息类
    '''
    myid = db.IntField(required=True)
    # 账号
    account = db.StringField(max_length=60)
    # 密码（md5加密）
    password = db.StringField(max_length=60)
    # 用户类型(0为管理员、1为用户)
    state = db.IntField(required=True)

    # 微信平台openId
    openId = db.StringField(max_length=60)
    # 头像
    headImgUrl = db.StringField(max_length=2400)
    # 用户名
    nickName = db.StringField(max_length=60)
    # 省份
    province = db.StringField(max_length=60)
    # 城市
    city = db.StringField(max_lengtg=60)
    # 性别
    sex = db.IntField()

    meta = {
        'ordering': ['-myid']
    }

    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return dict(
            myid=self.myid,
            account=self.account,
            password=self.password,
            state=self.state,
            openId=self.openId,
            headImgUrl=self.headImgUrl,
            nickName=self.nickName,
            province=self.province,
            city=self.city,
            sex=self.sex
        )
