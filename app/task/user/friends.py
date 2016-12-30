# coding=utf-8

from app import User, Friends
from app.core.user.user import (select_user_by_name_blur)


def ready_for_MakeFriends(name, num):

    out = []
    user_list = select_user_by_name_blur(name, num)
    if user_list is not None:
        for each in user_list.items:
            info = each.to_dict()
            info.pop('account')
            info.pop('password')
            info.pop('state')
            out.append(info)
        return out
    else:
        return None