#This program collects all the .jpg images in a folder and makes a directory page for them.
#It creates a simple text page, with no intro or outro or metadata that then can 
#be inserted into a web page. One  could be created using the story daturbase
#It is meant to run in the folder with the photos. The photo links are all in the single directory.
#All the photos must be square
#Put metadata in the GalleryCreateData.py file
#To operate, this program requires the mako template library.
#Note, when controlled over the Web, the working directory must be writeable to all 

import glob
import os.path
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from GalleryCreateData import *

DirectoryEntry = Template(filename='GalleryEntryTemplate.txt') 

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
#Add the Photo to the Photo Directory
	buf = StringIO()
	ctx = Context(buf,PhotoFile=PhotoFile, PhotoTitle=GalleryDescription)
	DirectoryEntry.render_context(ctx)
	f.write(buf.getvalue())

f.close()
