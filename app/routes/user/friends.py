# coding=utf-8

from app import app, User
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app.task.user.friends import (ready_for_MakeFriends)


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

#
# @app.route('/friends/one/<int:myid>', methods=['GET'])
# @login_required
# def make_friends(myid):