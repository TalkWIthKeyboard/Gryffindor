# coding=utf-8

from app import User
import re

def query_first(db):
    '''
    返回数据库默认第一个（按照myid排序）
    :param db:
    :return:
    '''
    try:
        info = db.objects.first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception, e:
        print e.message
        return None


def query_user_by_account(account):
    '''
    通过用户账号查询
    :param db:
    :return:
    '''
    try:
        info = User.objects(account=account).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception, e:
        print e.message
        return None


def select_user_by_name_blur(name, num):
    '''
    通过名字片段查找用户基本信息
    :param name: 名字片段
    :return:
    '''
    search = {'__raw__': {'nickName': re.compile(name)}, 'state': 1}
    try:
        basic = User.objects(**search).paginate(page=num, per_page=5)
        if basic:
            return basic
        else:
            return None
    except Exception, e:
        print e.message
        return None

