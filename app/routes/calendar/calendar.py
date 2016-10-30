# coding=utf-8

from flask import render_template, request, jsonify, redirect, url_for
from app import app, BasicInfo
import sys

DEFAULT_PAGE_SIZE = 10

reload(sys)

sys.setdefaultencoding('utf8')

@app.route('/',methods=['GET'])
def getCalendar():
    '''
    获取日历页面
    :return:
    '''
    return render_template('calendar/calendar.html')