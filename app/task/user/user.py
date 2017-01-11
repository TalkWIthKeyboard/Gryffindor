# coding=utf-8

from app.core.user.user import query_first, query_user_by_account
from app import User
from app.core.basic import get_md5
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, UPLOADS_DEFAULT_URL
import os


def ready_myid():
    '''
    myid自增器
    :return:
    '''
    old = query_first(User)
    if old is not None:
        return old['myid'] + 1
    else:
        return 1


def save_user_info(image, form, info):
    '''
    保存用户账号信息
    :param form: 表单
    :param info: 中转dict
    :return:
    '''
    try:
        info['password'] = get_md5(str(form['password']))
        info['nickName'] = str(form['username'])
        info['myid'] = ready_myid()
        info['state'] = 1
        # 头像保存
        if image != None:
            path = save_image(image, info['myid'])
            info['headImgUrl'] = path if path != 'fail' and path != 'error' else ''
        else:
            info['headImgUrl'] = ''

        User(**info).save()
    except Exception, e:
        print e.message


def save_wechat_user_info(json, open_id, info):
    '''
    保存微信端过来的用户账号信息
    :param json:
    :param info:
    :return:
    '''
    try:
        info['headImgUrl'] = json[u'headimgurl']
        info['nickName'] = json[u'nickname'].decode('utf-8')
        info['province'] = json[u'province']
        info['city'] = json[u'city']
        info['myid'] = ready_myid()
        info['sex'] = int(json[u'sex'])
        info['state'] = 1
        info['account'] = 'myAccount:' + open_id
        info['password'] = get_md5('123456')

        User(**info).save()
    except Exception, e:
        print e.message


def check_user_info(form):
    '''
    检测账号密码是否正确
    :param form: 表单
    :return:
    '''
    account = str(form['account'])
    user = query_user_by_account(str(account))
    if user is None:
        return False
    else:
        password = str(user['password'])
        re_password = get_md5(str(form['password']))
        return (password == re_password and user['state'] == 1)


def save_image(file, account):
    '''
    保存图片
    :param file: 文件
    :param id:
    :return:
    '''
    try:
        fileName = file.filename
        if file and allowed_file(fileName):
            save_name = str(account + '.' + fileName.rsplit('.', 1)[1])
            path = os.path.join(UPLOAD_FOLDER, save_name)
            file.save(path)
            return os.path.join(UPLOADS_DEFAULT_URL, save_name)
        else:
            return 'fail'
    except Exception, e:
        print e.message
        return 'error'


def allowed_file(filename):
    '''
    验证上传文件的格式是否合法
    :param filename: 文件名字
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def query_user_by_openId(openId):
    '''
    通过openid查询
    :param id:
    :return:
    '''
    try:
        info = User.objects(openId=openId).first()
        if info:
            return info.to_dict()
        else:
            return None
    except Exception, e:
        print e.message
        return None
