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
if "dataset" in form:
  dataset = form["dataset"].value
else:
  dataset = 0

print "Content-type: text/html\n"
print "<html>"
print "<head>"
print "<title>Raspberry Pi Bonneville Data Logger</title>"
print "</head>"
print "<center><img src=maintenance.jpg><BR>"



db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c2=db2.cursor(MySQLdb.cursors.DictCursor)
sql_string = "delete FROM dataset where id = %s" % dataset
#print sql_string
c2.execute(sql_string)
db2.commit()
#print "<BR>"
sql_string = "delete FROM datapoints where dataset_num = %s" % dataset
#print sql_string

c2.execute(sql_string)
db2.commit()

db2.close()
c2.close()


print "<BR><BR>Dataset %s Deleted Sucessfully<BR><BR>" % dataset

print "<BR><BR><a href=maintenance.py>Back To Database Maintenance</a><BR>"

