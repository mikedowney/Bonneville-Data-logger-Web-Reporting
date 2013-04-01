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
print "<center><img src=maintenance.jpg><BR>"



db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c2=db2.cursor(MySQLdb.cursors.DictCursor)
sql_string = "delete FROM dataset"
#print sql_string
c2.execute(sql_string)
db2.commit()
sql_string = "delete FROM datapoints"
#print sql_string

c2.execute(sql_string)
db2.commit()

db2.close()
c2.close()


print "<BR><BR>All Datasets Deleted Sucessfully. Your data collection system is now blank<BR><BR>" % dataset

print "<BR><BR><a href=bonneville.py>Back To Database Maintenance</a><BR>"

