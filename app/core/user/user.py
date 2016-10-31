# coding=utf-8

from app import UserInfo

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
    except Exception,e:
        print e.message
        return None

def query_user_by_account(account):
    '''
    通过用户账号查询
    :param db:
    :return:
    '''
    try:
        info = UserInfo.objects(account=account).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception,e:
        print e.message
        return None