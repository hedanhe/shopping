from flask import Flask,session,redirect,url_for,request,make_response
import datetime
import pymysql
import os
import configparser #读取配置文件

app = Flask(__name__, static_url_path='/static')


class Query(object):
    def conn(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        host = self.config['db']['host']
        user = self.config['db']['user']
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

        port = self.config.getint('db','port')  #端口是整数,上面读出来是字符串

        self.db = pymysql.connect(host=host,
                                    user=user,
                                    port=port,
                                    password=password,
                                    database = database,
                                    charset=charset)

        return self.db

    def close(self):
        """关闭数据库连接"""
        self.db.close()