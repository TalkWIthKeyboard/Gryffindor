# coding=utf-8


def select_event_by_user_date(db, userid, firstDay, lastDay):
    '''
    通过用户id，起始日期，结束日期检索活动(适用于电影记录事件、未来观看事件)
    :param userid:
    :param firstDay:
    :param lastDay:
    :return:
    '''

    try:
        info = db.objects(userId=userid, date__gte=firstDay, date__lte=lastDay).all()
        if info:
            return info
        else:
            return None
    except Exception, e:
        print e.message
        return None
