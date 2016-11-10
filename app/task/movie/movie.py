# coding=utf-8

from app.core.movie.movie import (select_basic_info_by_name_blur,
                                  select_by_id,
                                  select_by_userid_movieid,
                                  select_by_userid_movieid_all,
                                  select_by_objectid,
                                  select_by_enname)
from app import BasicInfo,Score,Details,Fullcredits,MovieRecordEvent,MovieFeatureEvent,Awards,Comment,Plot,Scenes
import datetime
from app import db

def ready_for_SelectMovieByName(name, num):
    '''
    为SelectMovieByName做数据准备
    :param name:
    :param num:
    :return:
    '''
    out = []
    movie_list = select_basic_info_by_name_blur(name, num)
    if movie_list is not None:
        for each in movie_list.items:
            id = each['movieid']
            info = each.to_dict()
            score = select_by_id(Score,id)
            detail = select_by_id(Details,id)
            fullcredits = select_by_id(Fullcredits, id)

            # 电影分数
            if score is not None:
                info = dict(info, **score)
            # 上映时间（默认取第一个上映时间）
            info['date'] = str(detail['release'][0]['date']) if detail is not None and len(detail['release']) > 0 is not None else '-'
            # 导演
            info['director'] = fullcredits['director'][0]['name'] if fullcredits is not None and fullcredits['director'][0]['name'] else '-'
            # 主演
            info['actor'] = fullcredits['actor'][0]['name'] if fullcredits is not None and fullcredits['actor'][0]['name'] else '-'

            out.append(info)
        return out
    else:
        return None

def ready_for_SelectMovieById(userid, id):
    '''
    为SelectMovieById做数据准备
    :param id:
    :return:
    '''
    out = select_by_id(BasicInfo,id)
    score = select_by_id(Score,id)
    detail = select_by_id(Details,id)
    fullcredits = select_by_id(Fullcredits,id)
    feature = select_by_userid_movieid(MovieFeatureEvent,userid,str(id))
    history = select_by_userid_movieid(MovieRecordEvent,userid,str(id))

    # 再刷的日期
    out['featureDate'] = str(history.to_dict()['date']) if history is not None else None
    out['num'] = str(history.to_dict()['num']) if feature is not None else None

    #  上映年份
    date = detail['release'][0]['date'].year if detail is not None and len(detail['release']) > 0 else '-'
    out['cnname'] = '{}({})'.format(out['cnname'],date)
    # 导演
    out['director'] = fullcredits['director'][0]['name'] if fullcredits is not None and fullcredits['director'][0]['name'] else '-'
    # 主演
    out['actor'] = fullcredits['actor'][0]['name'] if fullcredits is not None and fullcredits['actor'][0]['name'] else '-'

    # 电影得分
    if score is not None:
        out = dict(out,**score)
    return out

def click_for_user_movie_save(info):
    '''
    通过用户id、电影id检查是否存在记录,并存入数据库
    :param userid: 用户id
    :param movieid: 电影id
    :return:
    '''
    record = select_by_userid_movieid(MovieRecordEvent,info['userId'],info['movieId'])
    feature = select_by_userid_movieid(MovieFeatureEvent,info['userId'],info['movieId'])
    info['createTime'] = datetime.datetime.now()
    info['updateTime'] = datetime.datetime.now()
    info['date'] = datetime.datetime.strptime(info['date'],'%Y-%m-%d')

    # 电影记录事件
    if record is not None:
        recordDict = record.to_dict()
        info['num'] = int(recordDict['num']) + 1
    else:
        info['num'] = 1
    date = datetime.datetime.strptime(info['featureDate'],'%Y-%m-%d')
    info.pop('featureDate')
    MovieRecordEvent(**info).save()

    # 电影未来观看事件
    if date != '':
        if feature is not None:
            feature.date = info['featureDate']
            feature.save()
        else:
            info['date'] = date
            info.pop('num')
            info.pop('impression')
            info.pop('address')
            MovieFeatureEvent(**info).save()

def user_movie_impression(userid,movieid,id):
    '''
    返回用户对于一个电影的所有评论
    :param userid: 用户id
    :param moiveid: 电影id
    :return:
    '''
    this = -1
    out = []
    num = 0
    info = select_by_userid_movieid_all(MovieRecordEvent, userid, movieid)
    if info is not None:
        for each in info:
            if str(each.id) == id:
                this = num
            num += 1
            out.append(each.to_dict())
        return dict({'out':out,'this':this})
    else:
        return None


def movie_detail_info(movieid):
    '''
    获取一个电影的详细信息
    :param movieid:
    :return:
    '''
    out = {}
    awards = select_by_id(Awards,movieid)       # 获奖信息
    comment = select_by_id(Comment,movieid)     # 评论
    plot = select_by_id(Plot,movieid)           # 简介
    scenes = select_by_id(Scenes,movieid)       # 揭秘
    fullcredits = getCnname(select_by_id(Fullcredits,movieid))  # 演职人员信息

    out['awards'] = awards['awards'] if awards and len(awards['awards']) > 0 else None
    out['plot'] = plot['content'] if plot and len(plot['content']) > 0 else None
    out['fullcredits'] = fullcredits
    db_to_dict(comment,'comments',out)
    db_to_dict(scenes,'scene',out)

    plot_str = ''
    for each in out['plot']:
        plot_str += each

    out['plot_str'] = plot_str

    return out


def db_to_dict(db,key,out):
    '''
    转换一下数据格式
    :param db: 表名
    :param key: 字段名
    :param out: 结果数组
    :return:
    '''
    if db and len(db[key]) > 0:
        list = []
        for each in db[key]:
            list.append(each.to_dict())
        out[key] = list
    else:
        out[key] = None


def user_movie_one_impression(impressionid):
    '''
    通过默认id获取电影记录
    :param impressionid:
    :return:
    '''
    info = select_by_objectid(MovieRecordEvent,impressionid)
    return info

def getCnname(list):
    '''
    获取相对应的中文名字
    :param list:
    :return:
    '''
    for (key,value) in list.items():
        if (key == 'actor'):
            for each in value:
                alias = select_by_enname(str(each['name']))
                each['cnname'] = alias['alias'][0] if alias is not None and len(alias['alias']) > 0 else None
        elif (key != 'director'):
            for each in value:
                enname = str(each)
                alias = select_by_enname(enname)
                each = alias['alias'][0] if alias is not None and len(alias['alias']) > 0 else None

    return list








