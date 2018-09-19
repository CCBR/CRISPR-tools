import sys
import regex

#input file is the parsed blat response.
#calculates number of multimaps, counts fractions for multimap
#returns count file, multimapped reads and frequency file, and start position frequency

header = sys.argv[2]

lineCount = 0
readCount = dict()
sgrnaCount = dict()
positionCount = dict()

#first open to determine multimaps
with open(sys.argv[1],'r') as fileIn1:
	for line in fileIn1:
		# print (line[0].isdigit())
		if (line[0].isdigit() == False): #skip header
			continue
		line = line.strip("\n")
		lineArray = line.split("\t")
		readId = lineArray[1]
		# print readId
		if ((readId in readCount) == False):
			readCount[readId] = 0
		readCount[readId] += 1
		lineCount += 1
fileIn1.close()

print ("{} unique read IDs found in {} lines".format(len(readCount),lineCount))
# exit()

lineCount2 = 0
#second read through to generate sgrna counts
with open (sys.argv[1],'r') as fileIn2:
	for line in fileIn2:
		lineCount2 +=1
		if line[0].isdigit() == False: #skip header
			continue
		line = line.strip("\n")
		lineArray = line.split("\t")
		
		sgrna = lineArray[0]
		readId = lineArray[1]
		
		if ((sgrna in sgrnaCount) == False):
			sgrnaCount[sgrna] = 0
		if ((readId in readCount) == False):
			print ("Missing read: {} at line {}\n".format(readId,lineCount2))
			exit()
		sgrnaCount[sgrna] += float(1)/(readCount[readId])
		positionStart = lineArray[3]
		if ((positionStart in positionCount) == False):
			positionCount[positionStart] = 0
		positionCount[positionStart] += 1
		
fileIn2.close()

countOut = open("{}_positionCount.txt".format(header),'w')
sgrnaOut = open("{}_sgrnaCount.txt".format(header),'w')
multimapOut = open("{}_multimapCount.txt".format(header),'w')



for sgrna in sgrnaCount:
	sgrnaOut.write("{}\t{}\n".format(sgrna,round(sgrnaCount[sgrna],2)))

for position in sorted(positionCount, key = lambda x: int(x)):
	countOut.write ("{}\t{}\n".format(position,positionCount[position]))

for readId in readCount:
	if ((int(readCount[readId]))>1):
		multimapOut.write("{}\t{}\n".format(readId,readCount[readId]))

countOut.close()
sgrnaOut.close()
multimapOut.close()