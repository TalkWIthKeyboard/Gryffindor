# coding=utf-8

from app import BasicInfo
import re

def select_basic_info_by_name_blur(name):
    '''
    通过名字片段查找电影基本信息
    （中文名字和英文名字都参加匹配）
    :param name: 名字片段
    :return:
    '''
    search = { '__raw__' :
                   { '$or': [{'info.cnname': re.compile(name)},
                             {'info.enname': re.compile(name)}] }}
    try:
        basic = BasicInfo.objects(**search).all()
        return basic
    except Exception,e:
        print e.message
        return None

def select_by_id(db,id):
    '''
    通过id查找电影的某种信息
    :param db: 表
    :param id: 电影的id
    :return:
    '''
    try:
        info = db.objects(movieid=id).first()
        return info
    except Exception,e:
        print e.message
        return None