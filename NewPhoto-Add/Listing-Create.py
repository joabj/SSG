#This program collects all the .jpg images in a folder and makes a directory page for them, 
#including the li nks to the source page. It assumes the source page is the same name as the
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
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO


DirectoryEntry = Template(filename='/var/www/Photos/code/Listing-Create/ListingEntryTemplate.txt') 

GalleryDirectory = "/var/www/Photos/2016/"

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