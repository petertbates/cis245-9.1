#Peter Bates
#CIS 245 Assignemtn 9.1

import os

def checkInput(toCheck):
	while toCheck == '':
		toCheck = input("Please enter something: ")
	return toCheck

def checkDir(dirCheck):
	if os.path.isdir(dirCheck) == False:
		return False
	else:
		return True

def checkFile(fileCheck):
	if os.path.isfile(fileCheck):
		return True
	else:
		return False

def getInfo():
	userName = input("Please enter your name: ")
	userName = checkInput(userName)
	userAddress = input("Please enter your address: ")
	userAddress = checkInput(userAddress)
	userPhone = input("Please enter your phone number: ")
	userPhone = checkInput(userPhone)
	csv = userName + "," + userAddress + "," + userPhone
	return csv

#Main block of code
isDir = False
isFile = True
#This will check and reprompt for input if the directory doesn't exist
while isDir == False:
	directory = input("Please enter the name of the directory you would like to use: ")
	directory = checkInput(directory)
	isDir = checkDir(directory)
	if isDir == False:
		print ("Please enter a valid directory.")
#This will check and reprompt for input if the file already exists
while isFile:
	fileName = input("Please enter a name for your file: ")
	fileName = checkInput(fileName)
	fileName = directory + "/" + fileName + ".txt"
	isFile = checkFile(fileName)
	if isFile:
		print ("Please enter a new filename.")

#Another function to build the csv for the txt file
userInfo = getInfo()

#Opening file to write
with open(fileName, 'w') as toWrite:
	toWrite.write(userInfo)

#Opening file to read
with open(fileName, 'r') as toRead:
	fileInfo = toRead.read()

print ("Thank you, your information has been stored here: " + fileName)
print ("This file contains: " + fileInfo)