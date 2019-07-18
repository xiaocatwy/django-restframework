#coding=utf-8
import pymysql as  MySQLdb
from DBUtils.PooledDB import PooledDB
import common.mydb as mydb
from common.mydb import DB

mydb = DB()
SQL = "select * from test"
data=mydb.query(SQL)
print(data)

