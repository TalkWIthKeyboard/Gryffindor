from flask_mongoengine import MongoEngine
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
app.secret_key = 'GryffindorProject'
db = MongoEngine(app)


# loginManager = LoginManager()
# loginManager.init_app(app)
# loginManager.login_view='admin_login'


# router
from app.routes.calendar import calendar

#
# @loginManager.user_loader
# def load_user(id):
#     if str(id) == 'None':
#         return None
#     return User.objects(myid=int(id)).first()