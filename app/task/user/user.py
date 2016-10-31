# coding=utf-8

from app.core.user.user import query_first,query_user_by_account
from app import UserInfo
from app.core.basic import get_md5


def ready_myid():
    '''
    myid自增器
    :return:
    '''
    old = query_first(UserInfo)
    if old is not None:
        return old['myid'] + 1
    else:
        return 1


def save_user_info(form,info):
    '''
    保存用户账号信息
    :param form: 表单
    :param info: 中转dict
    :return:
    '''
    info['password'] = get_md5(str(form['password']))
    info['username'] = str(form['username'])
    info['myid'] = ready_myid()
    UserInfo(**info).save()


def check_user_info(form):
    '''
    检测账号密码是否正确
    :param form: 表单
    :return:
    '''
    account = str(form['account'])
    password = str(query_user_by_account(str(account))['password'])
    re_password = get_md5(str(form['password']))
    return (password == re_password)
