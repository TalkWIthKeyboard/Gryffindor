# coding=utf-8

from app import User, Friends, MovieRecordEvent
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


def query_user_by_myid(myid):
    '''
    通过用户myid查询
    :param db:
    :return:
    '''
    try:
        info = User.objects(myid=myid).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception, e:
        print e.message
        return None


def select_user_by_name_blur(name):
    '''
    通过名字片段查找用户基本信息
    :param name: 名字片段
    :return:
    '''
    search = \
        {'__raw__':
            {'$and':
                [
                    {'nickName': re.compile(name)},
                    {'state': 1}
                ]
            }
        }
    try:
        basic = User.objects(**search).all()
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


def get_all_friends(myid):
    '''
    获取一个人的所有朋友
    :param myid:
    :return:
    '''
    try:
        friends_list = Friends.objects(userFrom=myid).all()
        if friends_list:
            return friends_list
        else:
            return None
    except Exception, e:
        print e.message
        return None


def get_all_timeline_info(myid, num):
    '''
    分页获取朋友圈消息
    :param myid:
    :param num:
    :return:
    '''
    try:
        friends_list = get_all_friends(myid)
        # 拿出所有朋友的myid
        list = []
        for each in friends_list:
            each = each.to_dict()
            list.append(str(each['userTo']))
        # 构造查找函数
        search = \
            {'__raw__':
                 {'userId':
                      {'$in': list}
                  }
             }
        basic = MovieRecordEvent.objects(**search).paginate(page=num, per_page=3)
        if basic:
            return basic
        else:
            return None
    except Exception, e:
        print e.message
        return None
