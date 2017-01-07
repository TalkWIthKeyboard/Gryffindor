# coding=utf-8

from flask import render_template, request, jsonify
from flask_login import current_user, login_required
from app import app
from app.task.movie.movie import (ready_for_SelectMovieByName,
                                  ready_for_SelectMovieById,
                                  click_for_user_movie_save,
                                  user_movie_impression,
                                  movie_detail_info,
                                  query_event_message,
                                  save_message_info,
                                  query_by_movie_record_event_id)
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
    return render_template('movie/postMovie.html',
                           movie=movie,
                           detail=detail)


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


@app.route('/movies/impressions/<string:movieId>', methods=['GET'])
@login_required
def get_all_impression(movieId):
    '''
    获取用户对于这个电影的所有感想
    :return:
    '''
    user = current_user
    movieid = str(movieId)
    info = user_movie_impression(str(user.myid), movieid)
    movie = ready_for_SelectMovieById(str(user.myid), movieid)
    detail = movie_detail_info(int(movieid))
    return render_template('movie/detailInfo.html',
                           impression=info['out'],
                           num=info['num'],
                           movie=movie,
                           detail=detail)


@app.route('/movies/friends/<string:userId>/impressions/<string:movieId>', methods=['GET'])
@login_required
def get_friend_impression(userId, movieId):
    '''
    获取好友对于这个电影的所有感想
    :param userId:
    :param movieId:
    :return:
    '''
    info = user_movie_impression(userId, movieId)
    movie = ready_for_SelectMovieById(userId, movieId)
    detail = movie_detail_info(int(movieId))
    impression = info['out'] if info else None
    num = info['num'] if info else None
    return render_template('movie/detailInfo.html',
                           impression=impression,
                           num=num,
                           movie=movie,
                           detail=detail)


@app.route('/test', methods=['GET'])
def test():
    return render_template('movie/message.html')


@app.route('/movies/message/<string:eventId>', methods=['GET', 'POST'])
@login_required
def get_event_message(eventId):
    '''
    GET: 获取一个感想事件的所有留言
    POST: 提交感想事件的留言
    :param eventId:
    :return:
    '''
    if request.method == 'GET':
        event = query_by_movie_record_event_id(eventId)
        message = query_event_message(eventId)
        return render_template('movie/message.html',
                               event=event,
                               message=message,
                               num=len(message))
    elif request.method == 'POST':
        info = save_message_info(current_user.myid, eventId, str(request.form['message']))
        return jsonify(dict({'message': info}))
