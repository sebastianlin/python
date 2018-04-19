#!/usr/bin/python3

import mysql.connector 
import sys,getopt


config = {
	'user': '',
	'password': '',
	'host': '',
	'database': '',
#	'raise_on_warnings': True,
}

table_name=''

opts, args = getopt.getopt(sys.argv[1:], "u:p:h:d:t:", ["help"])
for o, a in opts:
	if o == "-u":
		config['user']=a
	elif o == "-p":
		config['password']=a
	elif o == "-h":
		config['host']=a
	elif o == "-d":
		config['database']=a
	elif o == "-t":
		table_name=a
	elif o == "--help":
		print("Usage: {} -u [user] -p [password] -h [ip] -d [db] -t [table]".format(sys.argv[0]))
		sys.exit()
	else:
		print("{} {}".format(o,a))


try:
#	db = mysql.connector.connect(user=user, password=pwd, host=host, database=db_name)
	db = mysql.connector.connect(**config)

	dbc = db.cursor()

	#dbc.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{}'".format(table_name))
	dbc.execute("SELECT * from {}".format(table_name))
	db_results = dbc.fetchall()
	print(len(db_results))

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Access denied!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	db.close()



