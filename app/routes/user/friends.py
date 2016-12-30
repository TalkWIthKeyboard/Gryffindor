# coding=utf-8

from app import app, User
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app.task.user.friends import (ready_for_MakeFriends,
                                   change_friend_ship)
from app.core.user.user import (check_friend)


@app.route('/friends', methods=['GET'])
@login_required
def get_friends_page():
    '''
    进入朋友圈页面
    :return:
    '''

    return render_template('user/friends.html')


@app.route('/friends/<string:name>/<string:num>', methods=['GET'])
@login_required
def search_user(name, num):
    '''
    通过用户名字输入，模糊匹配所有可能的用户
    :param name:
    :param num:
    :return:
    '''
    list = ready_for_MakeFriends(str(name), int(num))
    return jsonify({'userList': list, 'userNum': str(int(num) + 1)})


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
    except Exception,e:
        return jsonify(dict(message='error',err=e.message))

