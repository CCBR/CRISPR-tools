import sys
import regex
import numpy

#Purpose - separate multimapped library sequences by dividing counts. Rewrites to tab delimited of sgrna,target,count
#v1: Can do the separation by itself

#Import file
#Obtain counts for multiples
#Array[0], separate to obtain divisor in position 2
#Array[0], everything after separator becomes its own id. split at double period to create each pair of sgRNA and target
#Array[1], total count. hit with divisor and generate new value
#output. foreach value of array 0, print id, target, new count
#should be able to cat the outputs for MAGeCK

fileIn = sys.argv[1]
fileOut = open(sys.argv[2],'w')

with open("{}".format(fileIn),'r') as fileIn:
	for line in fileIn:
		if (line[1].isdigit() == False): #skip header
			continue
		line = line.strip ("\n")
		lineArray = line.split("\t")
		ids = lineArray[0]
		count = float(lineArray[1])
		idArray = ids.split("|")
		# print (ids)
		# print idArray[0]
		divisor = int(idArray[1])
		# print count
		# print divisor
		dividedCount = count/divisor
		
		# if (divisor > 1):
		# 	print count
		# 	print divisor
		# 	print dividedCount
		# 	exit()
		for idCombined in idArray[2:]:
			idComboArray = idCombined.split("..")
			fileOut.write("{}\t{}\t{}\n".format(idComboArray[0],idComboArray[1],dividedCount))

fileIn.close()
fileOut.close()
		
