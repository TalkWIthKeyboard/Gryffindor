# coding=utf-8

import datetime

def makeDate(dateString):
    '''
    字符串转date
    :param dateString: date字符串
    :return:
    '''
    dateList = dateString.split('-')
    return datetime.date(int(dateList[0]),int(dateList[1]),int(dateList[2]))