# coding=utf-8

from flask import render_template, request, jsonify
from flask_login import current_user
from app import app
from app.task.movie.movie import (ready_for_SelectMovieByName,
                                  ready_for_SelectMovieById,
                                  click_for_user_movie_save)
import sys
from app.task.tools import makeDate

DEFAULT_PAGE_SIZE = 10
reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/selectMovieByName/<string:name>', methods=['GET'])
def select_movie_by_name(name):
    '''
    通过电影名字输入，模糊匹配所有可能的电影
    :param name: 电影名字片段
    :return:
    '''
    list = ready_for_SelectMovieByName(str(name))
    return jsonify({'movieList' : list})


@app.route('/selectMovieById/<int:id>', methods=['GET'])
def select_movie_by_id(id):
    '''
    通过电影id，查找这个电影的信息
    :param id: 电影的id
    :return:
    '''
    userid = '1'
    movie = ready_for_SelectMovieById(userid,id)
    return render_template('movie/postMovie.html',movie=movie)


@app.route('/postMovieInfo', methods=['POST'])
def post_movie_info():
    '''
    将表单信息存入数据库
    :return:
    '''
    if request.method == 'POST':
        form = {}
        form['userId'] = current_user.myid
        for (key, value) in request.form.items():
            form[key] = str(value)
        click_for_user_movie_save(form)


@app.route('/searchPage',methods=['GET'])
def get_search_page():
    '''
    获取电影搜索页面
    :return:
    '''
    return render_template('movie/searchMovie.html')