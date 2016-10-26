# coding=utf-8

from app.core.movie.movie import (select_basic_info_by_name_blur,
                                  select_by_id)
from app import BasicInfo,Score,Details


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

            # 查找电影分数
            score = select_by_id(Score,id).to_dict()
            if score is not None:
                info = dict(info, **score)

            # 查找上映时间（默认取第一个上映时间）
            detail = select_by_id(Details,id)
            if detail is not None:
                info['date'] = str(detail['release'][0]['date'])
            else:
                info['date'] = "暂无上映时间"
            out.append(info)
        return out
    else:
        return None


def ready_for_SelectMovieById(id):
    '''
    为SelectMovieById做数据准备
    :param id:
    :return:
    '''
    out = select_by_id(BasicInfo,id).to_dict()
    score = select_by_id(Score,id).to_dict()
    if score is not None:
        out = dict(out,**score)
    return out

