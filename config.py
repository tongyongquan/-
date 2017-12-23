#encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)


DIALECT='mysql'
DRIVER='mysqldb'
USRNAME='root'
PASSWORD='happy100'
HOST='127.0.0.1'
PORT='3306'
DATABASE='wendapingtai'
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USRNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS= False