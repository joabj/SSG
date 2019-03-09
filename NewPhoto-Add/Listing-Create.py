#Richer metadata from PhotoPage
#Automate it on a routine (with NewPhoto-Add scripted to auto dump)

import glob
import os.path
import sys
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO


DirectoryEntry = Template(filename='/var/www/Photos/code/Listing-Create/ListingEntryTemplate.txt') 



#Passing the name of the directory to the program:
DirectoryName = sys.argv[1]
DirectoryYear = sys.argv[2]

GalleryDirectory = "/var/www/Photos/"+DirectoryYear+"/"+DirectoryName+"/"

Gallery = GalleryDirectory + "PhotoList.txt"

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
	ctx = Context(buf,PhotoLink=PhotoLink, PhotoFile=PhotoFile, PhotoTitle=PhotoTitle, PhotoName=PhotoName)
	DirectoryEntry.render_context(ctx)
	f.write(buf.getvalue())

f.close()


#https://www.pythonforbeginners.com/system/python-sys-argv
