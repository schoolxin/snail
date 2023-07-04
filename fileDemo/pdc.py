import pymysql


def connect_db():
    '''
    通过pymsql连接数据库
    :return:
    '''
    pymysql.connect(host="hadoop102",user="root",password="000000")
