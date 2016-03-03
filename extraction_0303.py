###extracting text from transcript
# 
# (APPLAUSE)
# 
# BLITZER: Governor Kasich?
# 
# KASICH: Well, you know, on the way over here, even getting ready earlier and sitting in the green r
import re, os

#Our regexes and functions
# we can identify speakers cause theyre capitalized
speakerregex='\s[A-Z]{4,}:'

def speechextractor(name,inputtext):
	regex=re.compile(name+'\:(.*?)(?='+speakerregex+')', re.DOTALL)
	result=regex.findall(transcript)
	print name, "has {} chunks".format(len(result))
	return result

print "start"
inputfilename="transcript.txt"
os.chdir("/Users/ps22344/Documents")
transcript=open(inputfilename, "r").read()
print "file is {} characters long".format(len(transcript))


#remember to whitestrip those speakers
speakers=re.findall(speakerregex,transcript)




print "identified speakers", ",".join(set(speakers))
#print "{} text chunks".format(len(text))
f=speechextractor('TRUMP', transcript)

for item in f:
	print item

#(CHEERING)
#
#UNIDENTIFIED MALE: I tell the truth, I tell the truth.
print "finished"
