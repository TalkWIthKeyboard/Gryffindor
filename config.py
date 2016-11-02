# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_SETTINGS = {'db': 'Gryffindor-task','hosts': 'localhost','port': 27017}

UPLOAD_FOLDER = os.path.join(basedir, 'app/static/image/head-image')

ALLOWED_EXTENSIONS = ['img', 'jpeg', 'png', 'gif', 'jpg']