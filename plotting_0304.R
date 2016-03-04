#plotting for the blog
# what we learned today
# par(mar=c(5.1,4.1,4.1,2.1)
#http://www.r-bloggers.com/setting-graph-margins-in-r-using-the-par-function-and-lots-of-cow-milk/


#basic settings
setwd("/Users/ps22344/Desktop")
fontsize=2


#plottiplot: density plot
# png("test.png", width=960, height=960);
# par(mar=c(5.1,5.1,4.1, 2.1));
# plot(density(t), cex.main=fontsize+1, cex.axis=fontsize-fontsize/2, cex.lab=fontsize, col='red', lwd=3);
# dev.off()


#barplot
#http://www.ats.ucla.edu/stat/r/faq/barplotplus.htm
png("wordlength.png", width=960, height=960);
par(mar=c(5.1,5.1,4.1, 2.1));
barplot(sort(debate$averagewordlength, decreasing=T), 
cex.main=fontsize+1, cex.axis=fontsize, cex.lab=fontsize, cex.names=fontsize+1,
ylim=c(0,5),
main="Average word length", 
ylab="Mean word length in characters",
names=debate$name,
col='red', lwd=3);
dev.off()

###ayayaya
