# coding=utf-8

from app import User, Friends
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

def check_friend(userMyid, friendMyid):
    '''
    检查两个人之间的关系 (0 是陌生人，1 是我关注了他， 2是他关注了我， 3是互相关注了)
    :param userMyid:
    :param friendMyid:
    :return:
    '''
    try:
        user_to_friend = Friends.objects(userFrom=userMyid, userTo=friendMyid).count()
        friends_to_user = Friends.objects(userFrom=friendMyid, userTo=userMyid).count()
        if user_to_friend + friends_to_user == 2:
            return 3
        elif user_to_friend == 1 and friends_to_user == 0:
            return 1
        elif user_to_friend == 0 and friends_to_user == 1:
            return 2
        else:
            return 0
    except Exception, e:
        print e.message
        return 0
