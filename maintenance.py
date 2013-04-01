#!/usr/bin/python
# -*- coding: UTF-8 -*-
# enable debugging
import cgi
import cgitb
import MySQLdb
from datetime import datetime
import os
import subprocess
import time
import Gnuplot, Gnuplot.funcutils
cgitb.enable()

form = cgi.FieldStorage()

print "Content-type: text/html\n"
print "<html>"
print "<head>"
print "<title>Raspberry Pi Bonneville Data Logger</title>"
print "</head>"
print "<center><img src=maintenance.jpg><BR><BR><BR>"
print "<table border=0><tr>"


print "<td width=200><center>Delete one particular dataset from the database<BR><form action=delete_dataset.py method=get>"
print "<select NAME=dataset>"
db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c2=db2.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT id, starttime FROM dataset order by id desc"
#print sql_string
c2.execute(sql_string)
for row in c2.fetchall() :
  print "<option value=%s >[%s] %s</option>" % (row["id"],row["id"], row["starttime"])
db2.close()
c2.close()
print "</select>"
print "<BR>"
print "<input type=submit value=Delete_Dataset>"
print "</form><center></td>"

print "<td width=200><center><a href=delete_all.py>Delete All Datasets from the Database</a><BR><BR>WARNING - this will erase everything from the Data collection system</center></td>"

print "<td width=200><center><a href=bonneville.py>Back To the Main Graphing Page</a></center><BR>"

print "</tr></table><BR><BR>"

db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c2=db2.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT sum( data_length + index_length ) / 1024 / 1024 AS 'db_size' FROM information_schema.TABLES where table_schema = 'speed_tracker' GROUP BY table_schema"
#print sql_string
c2.execute(sql_string)
for row in c2.fetchall() :
  print "Current Database size: %06.2f MB" % ( row["db_size"])
db2.close()
c2.close()

