# coding=utf-8

from flask import render_template, request, jsonify, redirect
from flask_login import current_user, login_required
from app import app
from app.task.movie.movie import (ready_for_SelectMovieByName,
                                  ready_for_SelectMovieById,
                                  click_for_user_movie_save,
                                  user_movie_impression,
                                  user_movie_one_impression,
                                  movie_detail_info)
import sys

reload(sys)
sys.setdefaultencoding('utf8')


@app.route('/movies/<string:name>/<string:num>', methods=['GET'])
@login_required
def select_movie_by_name(name, num):
    '''
    通过电影名字输入，模糊匹配所有可能的电影
    :param name: 电影名字片段
    :param num: 跳过前多少个
    :return:
    '''
    list = ready_for_SelectMovieByName(str(name), int(num))
    return jsonify({'movieList': list, 'movieNum': str(int(num) + 1)})


@app.route('/movies/<int:id>', methods=['GET'])
@login_required
def select_movie_by_id(id):
    '''
    通过电影id，查找这个电影的信息
    :param id: 电影的id
    :return:
    '''
    userid = current_user.myid
    movie = ready_for_SelectMovieById(userid, id)
    detail = movie_detail_info(id)
    return render_template('movie/postMovie.html', movie=movie, detail=detail)


@app.route('/movies', methods=['POST', 'GET'])
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
        except Exception, e:
            return jsonify(dict(message='fail'))
    else:
        # 获取电影搜索页面
        return render_template('movie/searchMovie.html')


@app.route('/movies/impressions/<string:id>', methods=['GET'])
# @login_required
def get_all_impression(id):
    '''
    获取用户对于这个电影的所有感想
    :return:
    '''
    user = current_user
    info = user_movie_one_impression(str(id))
    movieid = str(info['movieId'])
    info = user_movie_impression(str(user.myid), movieid, str(id))
    movie = ready_for_SelectMovieById(str(user.myid), int(movieid))
    detail = movie_detail_info(int(movieid))
    return render_template('movie/detailInfo.html',
                           impression=info['out'],
                           this=info['this'],
                           movie=movie,
                           detail=detail)
