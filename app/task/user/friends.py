# coding=utf-8

from app import User, Friends
from app.core.user.user import (select_user_by_name_blur,
                                check_friend)


def ready_for_MakeFriends(name, num, myid):
    '''
    为makefriends函数准备数据
    :param name:
    :param num:
    :param myid:
    :return:
    '''
    out = []
    user_list = select_user_by_name_blur(name, num)
    if user_list is not None:
        for each in user_list.items:
            info = each.to_dict()
            userId = info.myid
            info['isFriend'] = check_friend(myid, userId)
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
            Friends(**info).save()
    except Exception,e:
        print e.message


# def search_friend_list(myid):
#     '''
#     为朋友圈准备数据
#     :param myid:
#     :return:
#     '''
#     try:
#
#     except Exception,e:
#         print e.message