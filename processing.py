#Peter Bates
#CIS 245 Assignemtn 9.1

import os

def checkInput(toCheck):
	while toCheck == '':
		toCheck = input("Please enter something: ")
	return toCheck

def checkDir(dirCheck):
	if os.path.isdir(dirCheck) == False:
		print ("this is false")
		return False
	else:
		return True

#main block of code
isDir = False
filelist = os.listdir()
print (filelist)
while isDir == False:
	directory = input("Please enter the name of the directory you would like to use: ")
	directory = checkInput(directory)
	isDir = checkDir(directory)
	print(repr(directory))
	if isDir == False:
		print ("Please enter a valid directory.")

