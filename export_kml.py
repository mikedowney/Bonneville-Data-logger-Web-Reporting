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
print "<center><img src=bonneville.jpg><BR><BR><BR>"



text_file  = open('/var/www/py/dataset.kml', 'w')

#text_file.write("dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT"

text_file.write("<?xml version='1.0' encoding='UTF-8'?>")
text_file.write("<kml xmlns='http://www.opengis.net/kml/2.2' xmlns:gx='http://www.google.com/kml/ext/2.2'>")
text_file.write("  <Document>")
text_file.write("    <name>Dataset %s</name>" % dataset)
text_file.write("    <Snippet>Created %s</Snippet>" % datetime.now())
text_file.write("    <!-- Normal multiTrack style -->")
text_file.write("    <Style id='multiTrack_n'>")
text_file.write("      <IconStyle>")
text_file.write("        <Icon>")
text_file.write("          <href>http://earth.google.com/images/kml-icons/track-directional/track-0.png</href>")
text_file.write("        </Icon>")
text_file.write("      </IconStyle>")
text_file.write("      <LineStyle>")
text_file.write("        <color>ff0000ff</color>")
text_file.write("        <width>6</width>")
text_file.write("      </LineStyle>")
text_file.write("    </Style>")
text_file.write("    <!-- Highlighted multiTrack style -->")
text_file.write("    <Style id='multiTrack_h'>")
text_file.write("      <IconStyle>")
text_file.write("        <scale>1.2</scale>")
text_file.write("        <Icon>")
text_file.write("          <href>http://earth.google.com/images/kml-icons/track-directional/track-0.png</href>")
text_file.write("        </Icon>")
text_file.write("      </IconStyle>")
text_file.write("      <LineStyle>")
text_file.write("        <color>ff0000ff</color>")
text_file.write("        <width>8</width>")
text_file.write("      </LineStyle>")
text_file.write("    </Style>")
text_file.write("    <StyleMap id='multiTrack'>")
text_file.write("      <Pair>")
text_file.write("        <key>normal</key>")
text_file.write("        <styleUrl>#multiTrack_n</styleUrl>")
text_file.write("      </Pair>")
text_file.write("      <Pair>")
text_file.write("        <key>highlight</key>")
text_file.write("        <styleUrl>#multiTrack_h</styleUrl>")
text_file.write("      </Pair>")
text_file.write("    </StyleMap>")
text_file.write("    <Schema id='schema'>")
text_file.write("      <gx:SimpleArrayField name='Speed' type='int'>")
text_file.write("        <displayName>Speed</displayName>")
text_file.write("      </gx:SimpleArrayField>")
text_file.write("    </Schema>")
text_file.write("    <Folder>")
text_file.write("      <name>Tracks</name>")
text_file.write("      <Placemark>")
text_file.write("        <name>Dataset %s</name>" % dataset)
text_file.write("        <styleUrl>#multiTrack</styleUrl>")
text_file.write("        <gx:Track>")

db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset

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
  date_time_string =  date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
  text_file.write("             <when>%s</when>" %  date_time_string)
db.close()
c.close()


db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
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
  date_time_string =  date_time.strftime('%Y-%m-%d %H:%M:%S')
  text_file.write("             <gx:coord>%s %s %s</gx:coord>" %  (longitude, latitude, altitude/3.28084))
db.close()
c.close()




text_file.write("          <ExtendedData>")
text_file.write("             <SchemaData schemaUrl='#schema'>")




text_file.write("               <gx:SimpleArrayData name='speed'>")

db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
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
  date_time_string =  date_time.strftime('%Y-%m-%d %H:%M:%S')
  text_file.write("                  <gx:value>%s</gx:value>" %  speed)
db.close()
c.close()

text_file.write("       </gx:SimpleArrayData>")









text_file.write("               <gx:SimpleArrayData name='RPM'>")

db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
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
  date_time_string =  date_time.strftime('%Y-%m-%d %H:%M:%S')
  text_file.write("                  <gx:value>%s</gx:value>" %  engine_rpm)
db.close()
c.close()

text_file.write("       </gx:SimpleArrayData>")








text_file.write("               <gx:SimpleArrayData name='EGT'>")

db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
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
  date_time_string =  date_time.strftime('%Y-%m-%d %H:%M:%S')
  text_file.write("                  <gx:value>%s</gx:value>" %  egt)
db.close()
c.close()

text_file.write("       </gx:SimpleArrayData>")











text_file.write("               <gx:SimpleArrayData name='CHT'>")

db=MySQLdb.connect(user="root",passwd="aviator",db="speed_tracker")
c=db.cursor(MySQLdb.cursors.DictCursor)
sql_string = "SELECT dataset_num, date_time, latitude, longitude, speed, altitude, GPS_status, engine_rpm, egt, CHT FROM datapoints where dataset_num = %s order by date_time" % dataset
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
  date_time_string =  date_time.strftime('%Y-%m-%d %H:%M:%S')
  text_file.write("                  <gx:value>%s</gx:value>" %  cht)
db.close()
c.close()

text_file.write("       </gx:SimpleArrayData>")








text_file.write("            </SchemaData>")
text_file.write("          </ExtendedData>")
text_file.write("        </gx:Track>")
text_file.write("      </Placemark>")
text_file.write("    </Folder>")
text_file.write("  </Document>")
text_file.write("</kml>")

print "Click here to open <a href=dataset.kml?temp=%d>dataset %s</a> in Google Earth" % (time.mktime(time.localtime()), dataset)

print "<BR><BR>Google Earth can be downloaded free at <a href=http://www.google.com/earth/download/ge/agree.html>This location</a>"

print "<BR><BR><a href=bonneville.py>Back To the Main Graphing Page</a></center><BR>"

