#!/usr/bin/env bash
pip install virtualenv
virtualenv flask
flask/bin/pip install --upgrade pip
flask/bin/pip install setuptools --no-use-wheel --upgrade
flask/bin/pip install flask==0.9
flask/bin/pip install flask-wtf==0.8.4
flask/bin/pip install pymongo
flask/bin/pip install requests
flask/bin/pip install mongoengine
flask/bin/pip install flask-mongoengine