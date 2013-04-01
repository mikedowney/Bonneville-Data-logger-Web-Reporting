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
print "<center><img src=maintenance.jpg><BR><BR><BR>"
print "Are you sure you want to delete all datasetss? <BR><BR>" 

print "WARNING - This will delete all data on the data collection system!<BR><BR>"
print "<a href=delete_all2.py?dataset=%s>Yes</a>" % dataset
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
print "<a href=maintenance.py>No</a><BR>"


