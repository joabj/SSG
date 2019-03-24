#This program collects all the .jpg images in a folder and makes a directory page for them, 
#including the links to the source page. 
#The Working Directory and year is defined as a command line arguments:
#i.e. "python Listing-Create.py 1902-FA-Richard_Kalina 2019 0"
#Optional Flags for third argument (otherwise it must be a "0"):
#   -L  = landscape mode  (If you want the photos to be placed in landscape mode (450 x 253):
#         usage: "python Listing-Create.py 1902-FA-Richard_Kalina 2019 -L"
#   -D  = Directory mode  (This assumes each photo has an accompanying HTML page:
#         usage: "python Listing-Create.py [Filler value doesn't matter what you use] 2019 -D"
#It assumes the source page is the same name as the
#photo, except with an .html suffix instead of a .jpg one.
#The working directory is defined, for now, in the GalleryDirectory variable below.
#It creates a simple text page, with no intro or outro or metadata at this point
#It is meant to run in the folder with the photos. The photo links are all in the single directory.
#All the photos must be square
#To operate, this program requires the mako template library.
#Note, when controlled over the Web, the working directory must be writeable to all 

#ToDo: Make it run from the Web
#Richer metadata from PhotoPage
#Automate it on a routine (with NewPhoto-Add scripted to auto dump)

import glob
import os.path
import sys
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO


 

#Passing the name of the directory to the program:
DirectoryName = sys.argv[1]
DirectoryYear = sys.argv[2]

GalleryDirectory = "/var/www/Photos/"+DirectoryYear+"/"+DirectoryName+"/"
Gallery = GalleryDirectory + "PhotoList.txt"
#For standard entry web location
GalleryDirectoryWeb = "/Photos/"+DirectoryYear+"/"+DirectoryName+"/"



#Parsing the system arguments 
#need to figure out later how to vary the number of arguments
if sys.argv[3] == "-L": Mode = 1
elif sys.argv[3] == "-D": Mode = 2
else: Mode = 0

if Mode == 1:
	DirectoryEntry = Template(filename='/var/www/Photos/code/Listing-Create/ListingEntryTemplate-Landscape.txt') 
elif Mode == 2: 
	DirectoryEntry = Template(filename='/var/www/Photos/code/Listing-Create/ListingEntryTemplate-Directory.txt') 
	#This is a hack right now below, just to assume that the directory is a year folder. To fix later
	GalleryDirectory = "/var/www/Photos/"+DirectoryYear+"/"
	Gallery = GalleryDirectory + "PhotoList.txt"
else: 
	DirectoryEntry = Template(filename='/var/www/Photos/code/Listing-Create/ListingEntryTemplate.txt') 


#Open file:
f = open(Gallery,"w") 

#This collects all the photos in the current directory...
ParseDirectory = GalleryDirectory + "*.jpg"
Photos = glob.glob(ParseDirectory)
Photos.sort()

#From here on out this operation works on each photo found, 
#this operation This pulls the info from the photos
for Photo in Photos:
	PhotoFile = Photo
	PhotoFile = os.path.basename(PhotoFile)
	
	ExtensionRemover = PhotoFile.split('.')
	
	#Make name of HTML photo page, photo name and title from file name (for now)
	PhotoLink = ExtensionRemover[0] + ".html"
	PhotoTitle=ExtensionRemover[0] 
	PhotoName=ExtensionRemover[0]

#Add the Photo to the Photo Directory
	buf = StringIO()
	ctx = Context(buf,GalleryDirectoryWeb=GalleryDirectoryWeb, PhotoLink=PhotoLink, PhotoFile=PhotoFile, PhotoTitle=PhotoTitle, PhotoName=PhotoName)
	DirectoryEntry.render_context(ctx)
	f.write(buf.getvalue())

f.close()


#https://www.pythonforbeginners.com/system/python-sys-argv
