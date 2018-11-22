
library(rmr2) # Map reduce package 
library(rhdfs) #The library package rhdfs provides commands for file manipulation in terms of reading, writing and moving files

setwd("/home/student2/sbhati/Desktop/BME 777/Project") # initialize with the path to your working directory.

databme777 <-read.csv("diabetic_data_V2.csv", header=T, stringsAsFactors=FALSE) # study the read.csv command parameters and read the dataset csv file

head(databme777, n = 3) # Retreive the first 3 rows of data 

hdfs.init() # Initialize 

databme777.values <- to.dfs(databme777) # puts the data into HDFS, where the bulk of the data has to reside for mapreduce to operate on

databme777.map.fn <- function(k,v) {
	p <- which((as.numeric(v[,4]) == 1) & (((as.numeric(v[,8]) >= 460) & (as.numeric(v[,8]) <= 519)) | (as.numeric(v[,8]) == 786)))
keyval(p, v[p,])
}
databme777.reduce.fn <- function(k,v) {
keyval(k,(unlist(v)))
}

databme777.map.fns <- function(k,v) {
	p <- which( (as.numeric(v[,4]) != 1) & (((as.numeric(v[,8]) >= 460) & (as.numeric(v[,8]) <= 519)) | (as.numeric(v[,8]) == 786)))
keyval(p, v[p,])
}
databme777.reduce.fns <- function(k,v) {
keyval(k,(unlist(v)))
}

dataex <- mapreduce(input= databme777.values ,
                   map = databme777.map.fn,
                   reduce = databme777.reduce.fn)

dataexs <- mapreduce(input=databme777.values ,
                   map =databme777.map.fns ,
                   reduce = databme777.reduce.fns)

new_var<-from.dfs(dataex)
k<- unlist(new_var[2])
l <- length(k)/10
#k <- rbind(as.data.frame(new_var[2]))
#j <- as.data.frame(k[!duplicated(as.data.frame(k)),])

new_vars<-from.dfs(dataexs)
q<- unlist(new_vars[2])
ll <- length(q)/10
#q <- rbind(as.data.frame(new_vars[2]))
#i <- as.data.frame(q[!duplicated(as.data.frame(q)),])

y<-matrix(k,nrow=l,ncol=10,byrow=TRUE)
w<-matrix(q,nrow=ll,ncol=10,byrow=TRUE)
write.csv(y,'BME777_BigData_Extract_class1.csv')
write.csv(w,'BME777_BigData_Extract_class2.csv')
