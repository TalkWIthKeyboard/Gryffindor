# coding=utf-8

from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app.task.movie.movie import ready_for_SelectMovie
import sys

DEFAULT_PAGE_SIZE = 10
reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/selectMovie/<string:name>', methods=['GET'])
def select_movie(name):
    '''
    通过电影名字输入，模糊匹配所有可能的电影
    :param name: 电影名字片段
    :return:
    '''
    list = ready_for_SelectMovie(str(name))
    return render_template('movie/loadMovie.html',list=list)