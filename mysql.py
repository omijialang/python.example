#!/usr/bin/env python2.6

import MySQLdb

class light_SQL:
	
	def __init__(self, database, host='localhost', user='root', passwd="", port=3306):

		self.conn_host = host
		self.conn_user = user
		self.conn_passwd = passwd
		self.conn_port = port
		self.conn_database = database

	def connect_mysql_S(self):

		try:
			self.conn = MySQLdb.connect(host=self.conn_host, user=self.conn_user, \
									passwd=self.conn_passwd, port=self.conn_port)
			self.cur=self.conn.cursor()
			self.conn.select_db(self.conn_database)
				
			return True
		except MySQLdb.Error:
			return False

	def exec_sql(self, sql, arg=None, commit=False):
		
		try:
			if arg:
				self.cur.execute(sql, arg)
			else:
				self.cur.execute(sql)
			
			if commit:
				self.cur.commit()
			return True
		except MySQLdb.Error as e:
			print e
			return False
	
	def conn_close(self):

		self.conn.commit()
		self.cur.close()
		self.conn.close()


