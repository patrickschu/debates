#!/usr/bin/env python

#####extracting features

import re, os, string, nltk, numpy

# moving parts
dir="/Users/ps22344/Documents/debatefiles/"
outputfilename="debates_0304"
print "start"

#getting files etc
files=[f for f in os.listdir(dir) if not f.startswith(".")]
print "files we're working with: {}".format(",".join(files))
annotations=['(CROSSTALK)', '(LAUGHTER)', '(BELL RINGS)', '(APPLAUSE)']
#negative and positive words
#cite this: https://www.cs.uic.edu/~liub/publications/www05-p536.pdf
#https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html
negative=[w for w in open("negative-words.txt", "r").read().split("\n")]
positive=[w for w in open("positive-words.txt", "r").read().split("\n")]


#featureextracter takes the inputstring and the search term; in this case an ontological
#verb
def verbextracter(inputtext, search_term, fili):
	regexstring=r" "+search_term+" "
	regexfinder=re.compile(regexstring)
	result=regexfinder.findall(inputtext)
	return result
	
def wordextracter(inputtext, search_term, fili):
	regexstring=r" ("+search_term+"s?(?:ed)?)\W"
	regexfinder=re.compile(regexstring)
	result=regexfinder.findall(inputtext)
	return result

#set up files
spreadsheet=open(outputfilename+".csv", "a")

spreadsheet.write(
"name, wordcount, sentcount, averagewordlength, averagesentlength, questionfreq, thinkingfreq, positivefreq, negativefreq\n"
)

#main
for fili in files:
	inputfile=open(dir+fili, "r").read()
	print "working on", fili
	inputlowered=inputfile.lower()
	#basic stats: wordcount, sentence count
	words=[w for w in nltk.word_tokenize(inputfile) if w not in string.punctuation+'APPLAUSE'+'LAUGHTER'+'CROSSTALK']
	sentprep=re.sub("[\n+]", " ", inputfile)	
	sents=nltk.sent_tokenize(sentprep)
	print "words {}, sentences {}".format(len(words), len(sents))
	
	#mean word length, sent length
	wordlength=numpy.mean([len(w) for w in words])
	sentlength=numpy.mean([len(s.split()) for s in sents])
	print "wordlength {}, sentencelength {}".format(wordlength, sentlength)

	#think verbs
	think=verbextracter(inputlowered, "(think|thought)", fili)
	believe=verbextracter(inputlowered, "(believe|believed)", fili)
	wonder=verbextracter(inputlowered, "(wonder|wondered)", fili)
	know=verbextracter(inputlowered, "(know|knew|known)", fili)
	thinkingverbs=sum([len(think), len(believe), len(wonder), len(know)])
	print "thinkingverbs", thinkingverbs
	
	#emotion words
	positiveemos=sum([len(wordextracter(inputlowered, p, fili)) for p in positive])
	negativeemos=sum([len(wordextracter(inputlowered, n, fili)) for n in negative])
	print "positive: {}, negative: {}".format(positiveemos, negativeemos)
	
	#questions
	questions=len(re.findall("\?", inputfile))
	print "questions: ", questions

	#what do we want to output?
	#name, wordcount, sentcount, averagewordlength, averagesentlength, questionfreq, positivefreq, negativefreq
	stats=[fili.rstrip(".txt"), 
	len(words), 
	len(sents), 
	wordlength, 
	sentlength, 
	float(questions)/len(words),
	float(thinkingverbs)/len(words),
	float(positiveemos)/len(words), 
	float(negativeemos)/len(words)]
	
	#spreadsheet.write(",".join([str(i) for i in stats])+"\n")
	print fili, "extracted"
	print "\n\n----\n\n"
	
	
spreadsheet.close()
	
print "finish"
