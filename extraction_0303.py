###extracting text from transcript, write to file
#works with transcripts as published by the washington post

import re, os, string

#our regexes and functions
# we can identify speakers cause theyre capitalized
speakerregex='\s[A-Z]{4,}:'


#this function extracts the text following the speaker name given from the text given as
#inputtext
#writes to file if reqrd
def speechextractor(name,inputtext, write="no"):
	regex=re.compile(name+'\:(.*?)(?='+speakerregex+')', re.DOTALL)
	result=regex.findall(transcript)
	print name, "has {} chunks, {} words".format(len(result), sum([len(i.split()) for i in result]))
	if write=="yes":
		outputfile=open(name+".txt", "w")
		outputfile.write(" ".join(result))
		print "file {} written".format(outputfile)
		outputfile.close()
	return result

print "start"
#files are read
inputfilename="transcript.txt"
os.chdir("/Users/ps22344/Documents")
transcript=open(inputfilename, "r").read()
print "file is {} characters long".format(len(transcript)),  "\n----\n"


#speakers are identified and whitestripped
speakers=re.findall(speakerregex,transcript)
speakerset=set([i.strip(string.punctuation+'\n ') for i in speakers])
print "identified speakers:", ",".join(speakerset), "\n----\n"


#run speech extraction for each speaker
for speaker in speakerset:
	speechextractor(speaker, transcript, write="yes")



#(CHEERING)
#
#UNIDENTIFIED MALE: I tell the truth, I tell the truth.
print "finished"



# 
# (APPLAUSE)
# 
# BLITZER: Governor Kasich?
# 
# KASICH: Well, you know, on the way over here, even getting ready earlier and sitting in the green r