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

print "Content-type: text/plain\n"
print "dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT"


db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
#print sql_string

c.execute(sql_string)
i=0
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
  print "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (dataset, date_time_string, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, cht)

db.close()
c.close()
