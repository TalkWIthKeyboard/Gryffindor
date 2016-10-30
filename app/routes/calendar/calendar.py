# coding=utf-8

from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app.task.calendar.calendar import (ready_getActivities,
                                        create_dates_by_first_last)
import sys
import datetime

DEFAULT_PAGE_SIZE = 10

reload(sys)

sys.setdefaultencoding('utf8')

@app.route('/calendar/getCalendar',methods=['GET'])
def get_calendar():
    '''
    获取日历页面
    :return:
    '''

    return render_template('calendar/calendar.html')

@app.route('/calendar/getActivities',methods=['POST'])
def get_activities():
    '''
    获取日历一页的所有活动
    :param firstDay: 日历一页的起始日期
    :param lastDay: 日历一页的结束日期
    :return: 活动list
    '''
    if request.method == 'POST':
        firstDay = datetime.datetime.strptime(str(request.form['firstDay']),'%Y-%m-%d')
        lastDay = datetime.datetime.strptime(str(request.form['lastDay']),'%Y-%m-%d')
        userid = '1'

        info = ready_getActivities(userid,firstDay,lastDay)
        dateDict = create_dates_by_first_last(firstDay, lastDay)
        for each in info:
            dateDict[each['date']] += 1

        return jsonify({'dateDict': dateDict, 'event': info})


