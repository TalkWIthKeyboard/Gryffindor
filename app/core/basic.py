# coding=utf-8
import hashlib
import datetime


def query_by_id(db, id):
    '''
    通过mongodb生成的id查询
    :param db: 表
    :param id: id
    :return:
    '''
    try:
        info = db.objects(_id=id).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception, e:
        print e.message
        return None


def get_md5(str1=None):
    '''
        md5加密
    '''
    md5 = hashlib.md5()
    md5.update(str1)
    return md5.hexdigest()


def calculation_time(date):
    '''
    计算和现在相差多少时间
    :param date:
    :return:
    '''
    now = datetime.datetime.now()
    old = date
    now_old_second = (now - old).seconds
    now_old_day = (now - old).days
    if now_old_day == 0:
        type = 'minute'
        ans = now_old_second / 60
        if ans >= 60:
            type = 'hour'
            ans /= 60
        elif ans == 0:
            ans = 1
    else:
        ans = now_old_day
        type = 'day'

    if type == 'minute':
        ans_str = str(ans) + '分钟前'
    elif type == 'hour':
        ans_str = str(ans) + '小时前'
    elif type == 'day':
        ans_str = str(ans) + '天前'
    return ans_str
