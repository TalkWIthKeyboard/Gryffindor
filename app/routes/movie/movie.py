# coding=utf-8

from flask import render_template, request, jsonify
from flask_login import current_user,login_required
from app import app
from app.task.movie.movie import (ready_for_SelectMovieByName,
                                  ready_for_SelectMovieById,
                                  click_for_user_movie_save,
                                  user_movie_impression)
import sys

reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/selectMovieByName/<string:name>/<string:num>', methods=['GET'])
@login_required
def select_movie_by_name(name,num):
    '''
    通过电影名字输入，模糊匹配所有可能的电影
    :param name: 电影名字片段
    :param num: 跳过前多少个
    :return:
    '''
    list = ready_for_SelectMovieByName(str(name), int(num))
    return jsonify({'movieList' : list, 'movieNum': str(int(num) + 1)})


@app.route('/selectMovieById/<int:id>', methods=['GET'])
@login_required
def select_movie_by_id(id):
    '''
    通过电影id，查找这个电影的信息
    :param id: 电影的id
    :return:
    '''
    userid = current_user.myid
    movie = ready_for_SelectMovieById(userid,id)
    return render_template('movie/postMovie.html',movie=movie)


@app.route('/postMovieInfo', methods=['POST'])
@login_required
def post_movie_info():
    '''
    将表单信息存入数据库
    :return:
    '''
    if request.method == 'POST':
        try:
            form = {}
            form['userId'] = str(current_user.myid)
            for (key, value) in request.form.items():
                form[key] = str(value)
            click_for_user_movie_save(form)
            return jsonify(dict(message='success'))
        except Exception,e:
            return jsonify(dict(message='fail'))


@app.route('/searchPage',methods=['GET'])
@login_required
def get_search_page():
    '''
    获取电影搜索页面
    :return:
    '''
    return render_template('movie/searchMovie.html')


@app.route('/movie/getAllImpression/<int:id>',methods=['GET'])
@login_required
def get_all_impression(id):
    '''
    获取用户对于这个电影的所有感想
    :return:
    '''
    user = current_user
    info = user_movie_impression(user.myid,id)
    return jsonify(dict({'impression':info}))