# coding=utf-8

from app import app
from app.task.user.user import (query_user_by_account,
                                save_user_info,
                                check_user_info)
from flask import render_template, request, jsonify, redirect, url_for


@app.route('/',methods=['GET'])
def default_url():
    '''
    默认路由
    :return:
    '''
    return redirect(url_for('get_user_login'))


@app.route('/user/register',methods=['GET'])
def get_user_register():
    '''
    注册页面
    :return:
    '''
    return render_template('user/register.html')


@app.route('/user/register',methods=['POST'])
def post_user_register():
    '''
    用户注册
    :return:
    '''
    if request.method == 'POST':
        info = {}
        try:
            info['account'] = str(request.form['account'])
            # 检测账号是否重复
            if query_user_by_account(info['account']):
                return jsonify(dict(message='repeat'))
            else:
                save_user_info(request.form,info)
                return jsonify(dict(message='success'))
        except Exception,e:
            return jsonify(dict(message='fail'))


@app.route('/user/login',methods=['GET'])
def get_user_login():
    '''
    登陆页面
    :return:
    '''
    return render_template('user/login.html')


@app.route('/user/login',methods=['POST'])
def post_user_login():
    '''
    用户登陆
    :return:
    '''
    if request.method == 'POST':
        try:
            if check_user_info(request.form):
                return jsonify(dict(message='success'))
            else:
                return jsonify(dict(message='fail'))
        except Exception,e:
            return jsonify(dict(message='error'))



