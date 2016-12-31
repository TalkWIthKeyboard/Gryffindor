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
    old = datetime.datetime(date)
    type = 'minute'
    ans = (now - old).minute
    if ans >= 60:
        ans = (now - old).hour
        type = 'hour'
        if ans >= 24:
            ans = (now - old).days
            type = 'day'
    return {'date': ans, 'type': type}
