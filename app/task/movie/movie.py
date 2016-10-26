# coding=utf-8

from app.core.movie.movie import (select_basic_info_by_name_blur,
                                  select_detail_by_id)


def ready_for_SelectMovie(name):

    out = []
    movie_list = select_basic_info_by_name_blur(name)
    if movie_list is not None:
        for each in movie_list:
            info = {}
            id = each['movieid']
            info['id'] = id
            info['image'] = each['info']['img']
            info['cnname'] = each['info']['cnname']
            info['enname'] = each['info']['enname']

            # 查找上映时间（默认取第一个上映时间）
            detail = select_detail_by_id(id)
            if detail is not None:
                info['date'] = str(detail['release'][0]['date'])
            else:
                info['date'] = "暂无上映时间"
            out.append(info)
        return out
    else:
        return None
