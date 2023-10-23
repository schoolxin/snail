import pymysql

# 作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。
pymysql.install_as_MySQLdb()