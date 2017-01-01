# coding=utf-8

from app import app
from flask import render_template, jsonify
from flask_login import login_required, current_user
from app.task.user.friends import (ready_for_MakeFriends,
                                   change_friend_ship,
                                   ready_for_get_friends_page)
from app.core.user.user import (check_friend)
from app.core.movie.movie import (user_movie_history_count)


@app.route('/friends', methods=['GET'])
@login_required
def search_friends_page():
    '''
    进入朋友搜索页面
    :return:
    '''
    return render_template('user/searchFriends.html')


@app.route('/timeline', methods=['GET'])
@login_required
def get_friends_page():
    '''
    进入朋友圈页面
    :param num: 页数
    :return:
    '''
    user = current_user
    list = ready_for_get_friends_page(user.myid, 1)
    movie_count = user_movie_history_count(user.myid)
    return render_template('user/friends.html',
                           list=list,
                           count=movie_count,
                           user_img=user.headImgUrl,
                           user_name=user.nickName,
                           list_num=len(list))


@app.route('/timeline/more/<int:num>', methods=['GET'])
@login_required
def get_friends_more_page(num):
    '''
    获得更多的朋友圈信息
    :param num:
    :return:
    '''
    user = current_user
    list = ready_for_get_friends_page(user.myid, num)
    return jsonify(dict(list=list))


@app.route('/friends/friend/<string:name>', methods=['GET'])
@login_required
def search_user(name):
    '''
    通过用户名字输入，模糊匹配所有可能的用户
    :param name:
    :param num:
    :return:
    '''
    user = current_user
    list = ready_for_MakeFriends(str(name), user.myid)
    return jsonify({'userList': list})


@app.route('/friends/one/<int:myid>', methods=['GET'])
@login_required
def make_friends(myid):
    '''
    修改朋友关系（交朋友，删除朋友）
    :param myid:
    :return:
    '''
    try:
        user = current_user
        friend_ship = check_friend(user.myid, myid)
        if friend_ship == 1 or friend_ship == 3:
            change_friend_ship(user.myid, myid, 0)
        else:
            change_friend_ship(user.myid, myid, 1)
        return jsonify(dict(message='success'))
    except Exception, e:
        return jsonify(dict(message='error', err=e.message))
