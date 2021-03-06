#!/usr/bin/python
# -*- coding: utf-8 -*-

#This program prints a listing of the blog entries on the site 
#puts them in a file marked "StoryListing.txt" in that directory
#using the Mako-based templates
#Still experimental

import sys
import MySQLdb as mdb
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from datetime import date, datetime

#For the command line input:

StoryFile = '/var/www/Writing/Technique/StoryListing.txt'
#NOTE: as of now, StorlyListing.txt must be writeable by public

con = mdb.connect('localhost', '[USERNAME]', '[PASSWORD]', 'site', use_unicode=True, charset='utf8');


with con:
	StoryListing = Template(filename='/StoryListing/StoryListing-Entry-Template.txt')
	dbCommand = "SELECT FileName, FileLocation, Subject, Headline, Description, Published, Art FROM SiteStories where Publication='Blog' order by Published desc limit 10"

	#The tr/except construction ensures DB is o.k. If not, it exits
	try:
		cur = con.cursor(mdb.cursors.DictCursor)
		cur.execute(dbCommand)
	except:
		print "Something ain't right with the db, program exiting"
		sys.exit(0)
	
	print "database o.k. Onward!"

	#Only after db is shown to work do we rewrite the file
	f = open(StoryFile,"w") 

	for i in range(cur.rowcount):
		row = cur.fetchone()
		Link = "[BASE URL]" + row["FileLocation"] + row["FileName"] + ".html"
		Description = row["Description"]
		Headline = row["Headline"]
		Art = row["Art"]
		Published = row["Published"]
		Subject = row["Subject"]
		#Parsing the date
		Published = Published.strftime("%a, %d %b %Y")
		buf = StringIO()
		ctx = Context(buf, Headline=Headline, Link=Link, Description=Description, Published=Published, Art=Art, Subject=Subject)
		StoryListing.render_context(ctx)
		f.write(buf.getvalue())
	f.close() 

#DB connectivity code from http://zetcode.com/db/mysqlpython/
#Date format http://www.faqs.org/rfcs/rfc822.html

