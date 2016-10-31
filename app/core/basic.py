# coding=utf-8

def query_by_id(db, id):
    '''
    通过mongodb生成的id查询
    :param db: 表
    :param id: id
    :return:
    '''
    try:
        info = db.objects(_id=id).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception,e:
        print e.message
        return None