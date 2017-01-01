# coding=utf-8

from app import Friends, BasicInfo, Fullcredits
from app.core.user.user import (select_user_by_name_blur,
                                check_friend,
                                get_all_timeline_info,
                                query_user_by_myid)
from app.core.movie.movie import (select_by_id)
from app.core.basic import (calculation_time)
import datetime


def ready_for_MakeFriends(name, myid):
    '''
    为makefriends函数准备数据
    :param name:
    :param num:
    :param myid:
    :return:
    '''
    out = []
    user_list = select_user_by_name_blur(name)
    if user_list is not None:
        for each in user_list:
            info = each.to_dict()
            userId = info['myid']
            info['isFriend'] = check_friend(myid, userId)
            info['isMy'] = 0 if myid == userId else 1
            info.pop('account')
            info.pop('password')
            info.pop('state')
            out.append(info)
        return out
    else:
        return None


def change_friend_ship(myid, friendid, state):
    '''
    修改朋友关系
    :param myid:
    :param friendid:
    :param state: 关系参数，0是解除朋友关系，1是添加朋友关系
    :return:
    '''
    try:
        if state == 0:
            Friends.objects(userFrom=myid, userTo=friendid).delete()
        else:
            info = {}
            info['userFrom'] = myid
            info['userTo'] = friendid
            info['createTime'] = datetime.datetime.now()
            info['updateTime'] = datetime.datetime.now()
            Friends(**info).save()
    except Exception, e:
        print e.message


def ready_for_get_friends_page(myid, num):
    '''
    为朋友圈准备数据
    :param myid:
    :return:
    '''
    try:
        info = get_all_timeline_info(myid, num)
        list = []
        if info is not None:
            for each in info.items:
                # 重新把数据拿出来
                obj = {}
                each = each.to_dict()
                obj['userId'] = each['userId']
                obj['movieId'] = each['movieId']
                obj['date'] = each['date']
                obj['state'] = each['state']
                # 准备用户数据
                obj['user_info'] = query_user_by_myid(each['userId'])
                # 准备电影数据
                obj['movie_info'] = select_by_id(BasicInfo, each['movieId'])
                # 准备时间数据
                obj['date'] = calculation_time(each['date'])
                # 导演编剧数据
                fullcredits = select_by_id(Fullcredits, obj['movieId'])
                obj['director'] = fullcredits['director'][0]['name'] if fullcredits is not None and \
                                                                     fullcredits['director'][0]['name'] else '-'
                obj['writer'] = fullcredits['writer'][0] if fullcredits is not None and \
                                                                     fullcredits['writer'][0] else '-'

                list.append(obj)
        return list
    except Exception, e:
        print e.message
