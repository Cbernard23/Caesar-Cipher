###########################
###Author: Chris Bernard###
###########################

def readFile():
	fileName = input("What is the name of the file that you would like to encrypt?")
	inFile = open(fileName, "r")
	inputString = inFile.read()
	inFile.close();
	print(inputString)
	return inputString

def encrypt(iString):
	shifter = int(input("How much would you like to shift by?(0-26)"))
	value = 0
	nval = 0
	nString = ""
	for i in range(0, (len(iString)-1)):
		value = ord(iString[i])
		nval = value + shifter
		if(value > 64 and value < 91):
			if(nval > 90):
				nval = nval - 26
		elif(value> 96 and value < 123):
			if(nval > 122):
				nval = nval - 26
		else:
			nval = nval - shifter
		nString += chr(nval)
	print(nString)

def main():
	inputString = readFile()
	encrypt(inputString)


if __name__ == "__main__":
	main()