#plotting for the blog
# what we learned today
# par(mar=c(5.1,4.1,4.1,2.1)
#http://www.r-bloggers.com/setting-graph-margins-in-r-using-the-par-function-and-lots-of-cow-milk/
#mar – A numeric vector of length 4, which sets the margin sizes in the following order: bottom, left, top, and right. The #default is c(5.1, 4.1, 4.1, 2.1).

#basic settings
setwd("/Users/ps22344/Desktop")
fontsize=2


#plottiplot: density plot
# png("test.png", width=960, height=960);
# par(mar=c(5.1,5.1,4.1, 2.1));
# plot(density(t), cex.main=fontsize+1, cex.axis=fontsize-fontsize/2, cex.lab=fontsize, col='red', lwd=3);
# dev.off()


#barplot wordlength
# #http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
# png("wordlength.png", width=960, height=960);
# par(mar=c(6.1,5.1,4.1, 2.1));
# barplot(sort(debate$averagewordlength, decreasing=T), 
# names=debate[order(debate$averagewordlength, decreasing=T),]$name,
# cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize,
# ylim=c(0,5),
# main="Average word length", 
# ylab="Mean word length in characters",
# col='red', lwd=3);
# dev.off()



#barplot sentlength
#http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
png("sentlength.png", width=960, height=960);
par(mar=c(6.1,5.1,4.1, 2.1));
barplot(sort(debate$averagesentlength, decreasing=T), 
names=debate[order(debate$averagesentlength, decreasing=T),]$name,
cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize,
ylim=c(0,20),
main="Average sentence length", 
ylab="Mean sentence length in words",
col='red', lwd=3);
dev.off()
###ayayaya


# #barplot questfreq
# #http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
# png("questfreq.png", width=960, height=960);
# par(mar=c(6.1,5.1,4.1, 2.1));
# barplot(sort(debate$questionfreq*1000, decreasing=T), 
# names=debate[order(debate$questionfreq, decreasing=T),]$name,
# cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize,
# ylim=c(0,6),
# main="Questions asked", 
# ylab="Number of questions per 1,000 words",
# col='red', lwd=3);
# dev.off()
# ###ayayaya


# # #we want a function that takes the colname
# barplot negemotion
# http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
# png("negative.png", width=960, height=960);
# par(mar=c(6.1,5.1,4.1, 2.1));
# barplot(sort(debate$negativefreq*1000, decreasing=T), 
# names=debate[order(debate$negativefreq, decreasing=T),]$name,
# cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize,
# ylim=c(0,40),
# main="Negative vocabulary", 
# ylab="Number of negative opinion words per 1,000 words",
# col='red', lwd=3);
# dev.off()
# # #ayayaya''





#we want a function that takes the colname
# #barplot posemotion
# #http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
# png("positive.png", width=960, height=960);
# par(mar=c(6.1,5.1,4.1, 2.1));
# barplot(sort(debate$positivefreq*1000, decreasing=T), 
# names=debate[order(debate$positivefreq, decreasing=T),]$name,
# cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize,
# ylim=c(0,40),
# main="Positive vocabulary", 
# ylab="Number of positive opinion words per 1,000 words",
# col='red', lwd=3);
# dev.off()
# ###ayayaya


# #barplot thinkingverbs
# #http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
# png("think.png", width=960, height=960);
# par(mar=c(6.1,5.1,4.1, 2.1));
# barplot(sort(debate$thinkingfreq*1000, decreasing=T), 
# names=debate[order(debate$thinkingfreq, decreasing=T),]$name,
# cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize-0.25, cex.names=fontsize,
# ylim=c(0,10),
# main="Thinking verbs", 
# ylab="Number of 'think', ,'wonder', 'know' and 'believe' per 1,000 words",
# #ylab=expression(Number ~of~ italic(believe ~ know ~ think) ~ per ~1000~words),
# col='red', lwd=3);
# dev.off()
# ###ayayaya

