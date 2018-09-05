import sys
import regex

#fileIn is csv
#fileOut is fasta

fastaOut = open(sys.argv[2],'w')
lineCount = 0
targetDict = dict()

with(open(sys.argv[1],'r')) as fileIn:
	for line in fileIn:
		line = line.strip("\n")
		lineArray = line.split(",")
		lineCount+=1
		target = lineArray[0]
		# print (lineArray[0])
		if ((target in targetDict) == False):
			targetDict[target] = 1
		else:
			targetDict[target] += 1
			# print(target)
			# print (targetDict[target])
		fastaOut.write(">{}|{}|{}\n{}\n".format(lineCount,target,targetDict[target],lineArray[1]))
fileIn.close()
fastaOut.close()
