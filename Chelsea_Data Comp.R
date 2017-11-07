rm(list=ls())

location = "C:/Users/Chelsea/Documents/Data_Competition/DEMO.csv"
data.demo <- read.csv(location)

demo.kids = subset(data.demo, ridageyr = c("5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"))

demo.kids <- data.demo[which(data.demo$ridageyr > 4 & data.demo$ridageyr < 19),]

location1 = "C:/Users/Chelsea/Documents/Data_Competition/DR1IFF.csv"
data.diet1<- read.csv(location1)
location2 = "C:/Users/Chelsea/Documents/Data_Competition/DR2IFF.csv"
data.diet2<- read.csv(location2)

data.diet = merge(data.diet1, data.diet2)
kids.diet <- data.diet[which(demo.kids$seqn == data.diet$seqn),]
demo.diet = merge(kids.diet, demo.kids)
lunch.diet <- demo.diet[which(demo.diet$dr1.030z == "2" | demo.diet$dr1.030z == "11" | demo.diet$dr2.030z == "2" | demo.diet$dr2.030z == "11"),]
myvars <- lunch.diet[c(1, 10, 15:17, 48, 89, 94, 95,  127, 170, 207, 209)]
filtered.lunch.diet<- na.omit(myvars)
pc.kids = princomp(filtered.lunch.diet[2:42,2:13], COR = TRUE)
summary(pc.kids)
pc.kids$loadings

screeplot(pc.kids, type = "lines", main = 'Screeplot for Diet Data of Children')
abline(1,0,col='red',lty=2)

biplot(pc.kids,choices = 1:2, scale = 0, pc.biplot = FALSE,cex=0.65)
