# coding=utf-8

from app import app, User
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_user
import requests, json


@app.route('/friends', methods=['GET'])
def get_friends_page():
    '''
    进入朋友圈页面
    :return:
    '''
    return render_template('user/friends.html')