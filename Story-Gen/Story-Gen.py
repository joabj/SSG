#!/usr/bin/python
# -*- coding: utf-8 -*-

#This program requires 1 input, the filename, which must correspond to the database filename

import sys
import MySQLdb as mdb
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from datetime import date, datetime

#For the command line input:

FileName = str(sys.argv[1])

#Fetch data from database. Fill in the filename

con = mdb.connect('localhost', '[USER NAME}', '[PASSWORD]', 'site');

#Prep SQL Query
SQLQuery = "SELECT * FROM SiteStories where FileName='"+FileName+"'"

with con:
	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute(SQLQuery)
	row = cur.fetchone()
	Link = row["FileLocation"] + row["FileName"] + ".html"
	Topic = row["Topic"]
	Subtopics = row["Subtopic1"] + ", " + row["Subtopic2"] + ", " + row["Subtopic3"]
	Subject = row["Subject"]
	Headline = row["Headline"]
	Description = row["Description"]
	Published = row["Published"]
	Type = row["Type"]
	Art = row["Art"]
	
	
	#Parsing the date
	#BlogPublished must execute before Published is reassigned
	BlogPublished = Published.strftime("%m%d")
	Published = Published.strftime("%B %d, %Y")
	#Parsing Artwork
	ArtHomePage = Art[:-3]+"html"
	
	
	

#Rendering the HTML frame
StoryHTMLFrame = Template(filename='0000-Mako-Template.html')

buf = StringIO()
ctx = Context(buf, Headline=Headline, Subject=Subject, Subtopics=Subtopics, Topic=Topic, Type=Type, Published=Published, ArtHomePage=ArtHomePage, Art=Art, Link=Link, Description=Description)

StoryHTMLFrame.render_context(ctx)

f = open("Delivery/" + FileName + ".html", "w") 
f.write(buf.getvalue())
f.close() 

#vestigial Function
#Rendering the Intro text for the blog
#First, rework the filename to include the day instead:
#FileNameList = list(FileName)
#del(FileNameList[0:4])
#FileNameTruncated = "".join(FileNameList)
#FileNameBlog = BlogPublished + FileNameTruncated + ".txt"


#StoryBody = Template(filename='0000-Mako-Template.txt')
#buf = StringIO()
#ctx = Context(buf, Link=Link, Headline=Headline, Published=Published, Art=Art, Subject=Subject, Description=Description)
#StoryBody.render_context(ctx)
#f = open("Delivery/" + FileNameBlog,"w") 
#f.write(buf.getvalue())
#f.close() 

#Manual cleanup:  change art link in .html to .htm from .jpg. Also clean up file locations
