import sys
import regex

#Uses current sgRNA fasta file and creates a unique sgRNA fasta file

fastaIn = sys.argv[1]
fastaOut = open(sys.argv[2],'w')

seq2Ids = dict()
idLine = 0
sequenceLine = ""
idCounter = 0
seqCounter = 0
identifier = ""
sequence = ""
with open ('{}'.format(fastaIn), 'r') as fastaIn:
	for line in fastaIn:
		# print line[0]
		if (line[0]==">"):
			idCounter+=1
			if (len(identifier)>0):
				if ((sequence in seq2Ids) == False):
					seq2Ids[sequence] = list()
				seq2Ids[sequence].append(identifier)
				#set ID to the next value
				identifier = line[1:].strip("\n")
				identifier = regex.sub("\|"," ",identifier)
				#reset the sequence
				sequence = ""
				# print line
				# print (identifier)
			else:
				identifier = line[1:].strip("\n")
				identifier = regex.sub("\|"," ",identifier)

		else:
			sequence += line.strip("\n")
			seqCounter += 1
			# print sequenceLine
			# break
		
if ((sequence in seq2Ids) == False):
	seq2Ids[sequence] = list()
seq2Ids[sequence].append(identifier)

print ("{} IDs associated with {} sequences".format(idCounter,len(seq2Ids)))

newId = 0
for seq in seq2Ids:
	idCount = len(seq2Ids[seq])
	newId +=1
	sgRNA_string = "|".join(seq2Ids[seq])
	fastaOut.write(">{}|{}|{}\n{}\n".format(newId,idCount,sgRNA_string,seq))

fastaIn.close()
fastaOut.close()
