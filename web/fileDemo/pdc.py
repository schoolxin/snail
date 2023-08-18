import pymysql


def connect_db():
    '''
    通过pymsql连接数据库
    :return:
    '''
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute('select version()')  # 指定要执行的sql语句 查询出来的结果直接保存在cursor对象中
    data = cursor.fetchone()
    print('数据库版本{d}'.format(d=data))
    cursor.close()
    db.close()
    # return cursor


def create_db():
    '''
    创建新的数据库
    :return:
    '''
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute('create database if not exists woniudb')  # 指定要执行的sql语句 创建数据库的语句没有返回值
    cursor.close()
    db.close()


def create_table():
    '''
    创建一张表
    :return:
    '''
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute("use woniudb")
    cursor.execute('create table if not exists student(id int,name varchar(256))')  # 指定要执行的sql语句 创建数据库的语句没有返回值
    db.close()


def insert_db():
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute("use woniudb")
    rows = cursor.execute("insert into student(id,name) values (%d,'%s')" % (100, 'liss'))  # 指定要执行的sql语句 创建数据库的语句没有返回值
    print(rows)
    db.commit()  # 提交数据库事务
    db.close()


def data_search():
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute("use woniudb")
    sql = "select * from student where id = %s" % 100
    cursor.execute(sql)
    result = cursor.fetchall()  # result 是一个元组对象
    print(type(result))
    # print(result)
    for row in result:
        id = row[0]
        name = row[1]
        # name1 = row['name']
        print("name", name)
    cursor.close()
    db.close()


def data_update():
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute("use woniudb")

    sql = "update  student set name = '%s' where id = %s" % ('wangwu', 100)
    rows = cursor.execute(sql)
    print("影响的行数", rows)
    db.commit()
    db.close()


def data_delete():
    '''
    删除数据
    :return:
    '''
    db = pymysql.connect(host="hadoop102", user="root", password="000000", charset='utf8')
    cursor = db.cursor()  # 返回数据库操作对象
    cursor.execute("use woniudb")

    sql = "delete from  student where id = %s" % (100)
    rows = cursor.execute(sql)
    print("影响的行数", rows)
    db.commit()
    db.close()


if __name__ == '__main__':
    data_search()
    data_delete()
    print("更新后")
    data_search()
