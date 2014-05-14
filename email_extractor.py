# this script will open a file with email addresses in it, then extract 
# those address and write them to a new file

import os
import re

# vars for filenames
filename = 'emaillist.txt'
newfilename = 'emaillist-rev.txt'

# read file
if os.path.exists(filename):
	data = open(filename,'r')
	bulkemails = data.read()
else:
	print "File not found."
	raise SystemExit

# regex = whoEver@wHerever.xxx
# r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
# r = re.compile(r'(\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b)')
r = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
results = r.findall(bulkemails)    

emails = ""   
for x in results:
	emails += str(x)+"\n"	

# function to write file
def writefile():
	f = open(newfilename, 'w')
	f.write(emails)
	f.close()
	print "File written."

# function to handle overwrite question
def overwrite_ok():
	response = raw_input("Are you sure you want to overwrite "+str(newfilename)+"? Yes or No\n")
	if response == "Yes":
		writefile()
	elif response == "No":
		print "Aborted."
	else:
		print "Please enter Yes or No."
		overwrite_ok()

# write/overwrite
if os.path.exists(newfilename):
	overwrite_ok()		
else: 
	writefile()
