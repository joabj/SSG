

#Run in the directory that needs organizing
#Photo names MUST be in the format of YYMM-Keyword1-Keyword2-Keyword3.jpg for however many keywords
#The first keyword may be 2-letter abbreviations for categories 
#Initially it is "SA" for "Street Art", See other a dictionary of categories under the PhotoCategory var 
#Additional metadata can be added in the PhotoPagesData.py page
#Note .jpg files must have lower case suffixes (not .JPG)

import glob
import os.path
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO

PhotoTitle = ""
PhotoKeywords = " "
PhotoDate = " "
PhotoDescription = " "
PhotoLocation = " "
PhotoFile = " "
PhotoPage = " "

PhotoFrame = Template(filename='[YOUR DIRECTORY PATH]/NewPhoto-Add/PhotoPagesTemplate.txt')
#This you vary to set the working directory
FilePath = '[YOUR DIRECTORY PATH] /NewPhoto-Add/Delivery/'


#Fill In Your Own decoders...
PhotoCategory = {"SA": "Street Art",
		            "PP" : "People",
                "RR" : "Railroad",
		            "MU" : "Music",
                "FD" : "Food and Drink",
                "FA" : "Fine Art",
                "VE" : "Vehicles",
                "PL" : "Place",
                "EV" : "Event",
		            "NA" : "Nature",
                "Tech" : "Technology",
		            "CL" : "Clothing",
		            "Misc" : "Miscellaneous",
		            "Folk" : "Folk Art"
			}
		
#This collects all the photos in the specified directory...
Photos = glob.glob("[YOUR DIRECTORY PATH]/NewPhoto-Add/Delivery/*.jpg")
#Note here that glob returns the full path name
Photos.sort()

#From here on out this operation works on each photo found, 
#this operation This pulls the info from the photos
for Photo in Photos:
	#Here you use os.path to shed the path info...
	Photo = os.path.basename(Photo)

	#Remove Extension first
	ExtensionRemover = Photo.split('.')
	
	#Make name of HTML photo page
	PhotoPage = ExtensionRemover[0] + ".html"

	#This part grabs keywords from file name	
	PhotoTitle = ExtensionRemover[0]
	KeywordExtractor = ExtensionRemover[0].split('-');
	dater = KeywordExtractor[0]
	count = len(KeywordExtractor)
	if KeywordExtractor[1] in PhotoCategory:
		KeywordExtractor[1] = PhotoCategory[KeywordExtractor[1]]

#Starts a list of keywords
	PhotoKeywords = [KeywordExtractor[1]]
	
#Some Broad Categories are extracted here 
	tally = 2
	while tally < count:
		PhotoKeywords.append(KeywordExtractor[tally])		
		tally = tally + 1
	
	PhotoKeywords.append("Photograph")		
	
#Now we turn the list of keywords into a string
	PhotoKeywords = ', '.join(PhotoKeywords)
			
#Here we parse the year and month from file name
	year = dater[0] + dater[1]
	YearNum = int(year)	
	if YearNum > 65:
		year = "19" + year
	else:
		year = "20" + year
	
	month = dater[2] + dater[3]
	Months = {"01": "January",
                "02" : "February",
                "03" : "March",
                "04" : "April",
                "05" : "May",
                "06" : "June",
                "07" : "July",
                "08" : "August",
		            "09" : "September",
                "10" : "October",
                "11" : "November",
                "12" : "December",
				        "00" : " "
			}
				
	PhotoDate = Months[month] + " " + year

#Write the file	
#Put the file path and name back together
	PhotoPage = FilePath + PhotoPage
	PhotoFile = Photo


	buf = StringIO()
	ctx = Context(buf, PhotoTitle=PhotoTitle, PhotoDate=PhotoDate, PhotoFile=PhotoFile, PhotoDescription=PhotoDescription, PhotoLocation=PhotoLocation, PhotoKeywords=PhotoKeywords)
	PhotoFrame.render_context(ctx)
	f = open(PhotoPage,"w") 
	f.write(buf.getvalue())
	f.close()
