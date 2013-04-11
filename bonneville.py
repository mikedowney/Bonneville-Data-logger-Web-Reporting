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
print "<center><img src=bonneville.jpg><BR>"


if dataset == 0:
  db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
  c2=db2.cursor(MySQLdb.cursors.DictCursor)
  sql_string = "SELECT id, starttime FROM dataset order by id desc limit 1"
  c2.execute(sql_string)
  for row in c2.fetchall() :
    dataset = row["id"]
    starttime = row["starttime"]
  db2.close()
  c2.close()
else:
  db2=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
  c2=db2.cursor(MySQLdb.cursors.DictCursor)
  sql_string = "SELECT id, starttime FROM dataset where id = %s" % dataset
  c2.execute(sql_string)
  for row in c2.fetchall() :
    dataset = row["id"]
    starttime = row["starttime"]
  db2.close()
  c2.close()




db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
#print sql_string

c.execute(sql_string)
i=0
text_file  = open('/var/www/py/speed_data.txt', 'w')
for row in c.fetchall() :
  i=i+1
  latitude = row["latitude"]
  longitude = row["longitude"]
  speed = row["speed"]
  altitude = row["altitude"]
  GPS_status = row["GPS_status"]
  engine_rpm = row["engine_rpm"]
  egt = row["egt"]
  cht = row["CHT"]
  date_time = row["date_time"]
  date_time_string =  date_time.strftime('%Y-%m-%d-%H:%M:%S')
  file_data = "%s %s %s %s %s\n" % (date_time_string, cht, egt, speed, engine_rpm)
  text_file.write(file_data)

db.close()
c.close()
text_file.close()
p = subprocess.Popen("gnuplot /var/www/py/speed.txt", shell = True)
os.waitpid(p.pid, 0)

print "<font size=+2>Graphing DataSet %s " % (dataset)
print "Collected at %s </font><BR>" % (starttime)
print "<img src=speed.png?temp=%d><BR>" % time.mktime(time.localtime())




print "<BR><BR><font size=+2>Other Actions</font><BR><BR><table border = 0><tr>"

print "<td width=200><center><a href=export_csv.py?dataset=%s>Export this dataset to a CSV file</a><BR><BR>" % dataset

print "<a href=export_kml.py?dataset=%s>Open this Dataset in Google Earth</a></center></td>" % dataset

print "<td width=200><center>Graph A Different Dataset <BR><form action=bonneville.py method=get>"
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
#print "<BR>"
print "<input type=submit value=Show_New_Dataset>"
print "</form></center></td>"

print "<td width=200><center><a href=maintenance.py>Perform Database Maintenance</a></center></td>"

print"</tr></table>"
