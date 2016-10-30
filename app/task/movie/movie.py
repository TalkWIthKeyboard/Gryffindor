# coding=utf-8

from app.core.movie.movie import (select_basic_info_by_name_blur,
                                  select_by_id,
                                  select_by_userid_movieid)
from app import BasicInfo,Score,Details,Fullcredits,MovieRecordEvent
import datetime

def ready_for_SelectMovieByName(name):
    '''
    为SelectMovieByName做数据准备
    :param name:
    :return:
    '''
    out = []
    movie_list = select_basic_info_by_name_blur(name)
    if movie_list is not None:
        for each in movie_list:
            id = each['movieid']
            info = each.to_dict()
            score = select_by_id(Score,id)
            detail = select_by_id(Details,id)
            fullcredits = select_by_id(Fullcredits, id)

            # 电影分数
            if score is not None:
                info = dict(info, **score)
            # 上映时间（默认取第一个上映时间）
            info['date'] = str(detail['release'][0]['date']) if detail is not None else '-'
            # 导演
            info['director'] = fullcredits['director'][0]['name'] if fullcredits['director'][0]['name'] else '-'
            # 主演
            info['actor'] = fullcredits['actor'][0]['name'] if fullcredits['actor'][0]['name'] else '-'

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
    history = select_by_userid_movieid(MovieRecordEvent,userid,str(id))

    # 再刷的日期
    out['featureDate'] = str(history.to_dict()['featureDate']) if history is not None else None

    #  上映年份
    date = detail['release'][0]['date'].year if len(detail['release']) > 0 else '-'
    out['cnname'] = '{}({})'.format(out['cnname'],date)
    # 导演
    out['director'] = fullcredits['director'][0]['name'] if fullcredits['director'][0]['name'] else '-'
    # 主演
    out['actor'] = fullcredits['actor'][0]['name'] if fullcredits['actor'][0]['name'] else '-'

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
    out = select_by_userid_movieid(MovieRecordEvent,info['userId'],info['movieId'])
    if out is not None:
        outDict = out.to_dict()

        out.num = int(outDict['num']) + 1
        out.impression = workList(list(outDict['impression']),info['impression'])
        out.address = workList(list(outDict['address']),info['address'])
        out.date = workList(list(outDict['date']),info['date'])
        out.featureDate = info['featureDate']
        out.updateTime = datetime.datetime.now()
        out.save()
    else:
        info['num'] = 1
        info['createTime'] = datetime.datetime.now()
        info['updateTime'] = datetime.datetime.now()
        info['date'] = [info['date']]
        info['address'] = [info['address']]
        info['impression'] = [info['impression']]
        MovieRecordEvent(**info).save()

def workList(list,addObj):
    for i in range(0,len(list) - 1):
        list[i] = str(list[i])
    list.append(addObj)
    return list



