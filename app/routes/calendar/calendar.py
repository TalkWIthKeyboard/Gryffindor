# coding=utf-8

from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app import app
from app.task.calendar.calendar import (ready_getActivities,
                                        create_dates_by_first_last,
                                        ready_out_date)
import sys
import datetime

DEFAULT_PAGE_SIZE = 10

reload(sys)

sys.setdefaultencoding('utf8')


@app.route('/calendar', methods=['GET', 'POST'])
@login_required
def get_calendar():
    '''
    获取日历页面
    :return:
    '''
    if request.method == 'GET':
        user = current_user
        if user.is_active:
            return render_template('calendar/calendar.html')
        else:
            return render_template('user/login.html')
    else:
        '''
        获取日历一页的所有活动
        :param firstDay: 日历一页的起始日期
        :param lastDay: 日历一页的结束日期
        :return: 活动list
        '''
        firstDay = datetime.datetime.strptime(str(request.form['firstDay']), '%Y-%m-%d')
        lastDay = datetime.datetime.strptime(str(request.form['lastDay']), '%Y-%m-%d')
        userid = str(current_user.myid)

        info = ready_out_date(ready_getActivities(userid, firstDay, lastDay))
        dateDict = create_dates_by_first_last(firstDay, lastDay)
        for each in info:
            if each['state'] == 0:
                dateDict[each['date']]['history'] += 1
            else:
                dateDict[each['date']]['feature'] += 1

        return jsonify({'dateDict': dateDict, 'event': info})
