# coding=utf-8

from flask import render_template, request, jsonify, redirect, url_for
from app import app, BasicInfo
import sys

DEFAULT_PAGE_SIZE = 10

reload(sys)

sys.setdefaultencoding('utf8')

@app.route('/',methods=['GET'])
def getCalendar():

    try:
        basic = BasicInfo.objects(movieid=22506).first()
        basic = basic.to_dict()
    except Exception,e:
        print e.message

    return render_template('calendar/calendar.html')


