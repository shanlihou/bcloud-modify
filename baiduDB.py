# -*- coding: utf-8 -*-     
#mysqldb    
import MySQLdb    
#连接    
class baiduDB(object):
	def __init__(self):
		self.conn=MySQLdb.connect(host="localhost",user="root",passwd="1",db="baiduyun",charset="utf8")  
		self.cursor = self.conn.cursor()    
	def close(self):
		self.conn.commit()
		self.conn.close()
	def insert(self, table, attr, value):
		sql = "insert into " + table + "(attr,value) values(%s,%s)"   
		param = (attr, value)    
		n = self.cursor.execute(sql,param)    
	def query(self, table):		
		n = self.cursor.execute("select * from " + table)    
		ret = self.cursor.fetchall()    
		print(ret) 
		return ret
#写入 
#更新    
'''
sql = "update user set name=%s where id=3"   
param = ("bbb")    
n = cursor.execute(sql,param)    
print n    
   '''
#查询    
   
#删除    
'''
sql = "delete from user where name=%s"   
param =("aaa")    
n = cursor.execute(sql,param)    
print n    
cursor.close()    
   '''
#关闭 
