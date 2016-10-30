# coding=utf-8

import datetime
from app.core.calendar.calendar import select_event_by_user_date
from app import MovieRecordEvent,MovieFeatureEvent


def ready_getActivities(userid, firstDay, lastDay):
    '''
    为get_activities准备数据
    :param userid:
    :param firstDay:
    :param lastDay:
    :return:
    '''
    recordList = select_event_by_user_date(MovieRecordEvent, userid, firstDay, lastDay)
    featrueList = select_event_by_user_date(MovieFeatureEvent, userid, firstDay, lastDay)
    out = []
    if recordList is not None:
        out.extend(ready_date(recordList))
    if featrueList is not None:
        out.extend(ready_date(featrueList))
    return out


def ready_date(list):
    out = []
    for each in list:
        dict = each.to_dict()
        info = {}
        info['date'] = dict['date'].strftime("%Y-%m-%d")
        info['id'] = str(each.id)
        info['movieId'] = dict['movieId']
        info['impression'] = dict['impression'] if dict.has_key('impression') else ''
        out.append(info)
    return out


def create_dates_by_first_last(firstDate, lastDate):
    '''
    根据起始日期和结束日期生成日期数组
    :param firstDay:
    :param lastDay:
    :return:
    '''
    dateDict = {}
    while (firstDate <= lastDate):
        dateDict[firstDate.strftime("%Y-%m-%d")] = 0
        firstDate = firstDate + datetime.timedelta(days = 1)
    return dateDict


