#This is an offshot of the ListingCreate program that only does directory listings of all the .jpg files in a folder, without any
#HTML templates, so the resulting listing can be inserted into a directory page through a SSI, as a file called "PhotoList.txt."
#usage:   python ListingCreate-Directory.py [Name of Directory under the /Photos tree]

import glob
import os.path
import sys
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO

 
#Passing the name of the directory to the program [Must be a relative directory following /Photos/"]
DirectoryName = sys.argv[1]


GalleryDirectory = "/var/www/Photos/"+DirectoryName+"/"
Gallery = GalleryDirectory + "PhotoList.txt"
#For standard entry web location
GalleryDirectoryWeb = "/var/www/Photos/"+DirectoryName+"/"

DirectoryEntry = Template(filename='/var/www/Photos/code/ListingCreate-Directory/DirectoryListingEntryTemplate.txt') 
GalleryDirectory = "/var/www/Photos/"+DirectoryName+"/"
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
	PhotoLink =ExtensionRemover[0] + ".html"
	PhotoTitle=ExtensionRemover[0] 
	PhotoName=ExtensionRemover[0] 

#Add the Photo to the Photo Directory
	buf = StringIO()
	ctx = Context(buf,PhotoLink=PhotoLink,PhotoFile=PhotoFile,PhotoTitle=PhotoTitle,PhotoName=PhotoName)
	DirectoryEntry.render_context(ctx)
	f.write(buf.getvalue())


f.close()
