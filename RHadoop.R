
library(rmr2)
library(rhdfs)

setwd('/home/student1/anavival/Desktop/hello' ) # initialize with the path to your working directory.

databme777<-read.csv("new_diabetic_data_V2.csv")  # study the read.csv command parameters and read the dataset csv file.

#head(databme777)

hdfs.init()
databme777.values <- to.dfs(databme777)

# write your own map() and reduce() functions based on your assigned queries.
databme777.map.fn <- function(k,v) {
	p <- which((as.numeric(v[,1]) == 1) & ((as.numeric(v[,8]) >= 460) & (as.numeric(v[,8]) <= 519)) | (as.numeric(v[,8]) == 786))
keyval(p, v[p,])
}
databme777.reduce.fn <- function(k,v) {
keyval(k,(unlist(v)))
}

databme777.map.fns <- function(k,v) {
	p <- which((as.numeric(v[,1]) == 2) & ((as.numeric(v[,8]) >= 460) & (as.numeric(v[,8]) <= 519)) | (as.numeric(v[,8]) == 786))
keyval(p, v[p,])
}
databme777.reduce.fns <- function(k,v) {
keyval(k,(unlist(v)))
}
# study mapreduce function and pass appropriate inputs and ouputs.

dataex <- mapreduce(input= databme777.values ,
                   map = databme777.map.fn,
                   reduce = databme777.reduce.fn)

dataexs <- mapreduce(input=databme777.values ,
                   map =databme777.map.fns ,
                   reduce = databme777.reduce.fns)

new_var<-from.dfs(dataex)
o<- unlist(new_var[2])
l <- length(o)/2


new_vars<-from.dfs(dataexs)
q<- unlist(new_var[2])
ll <- length(q)/2

# write appropriate code to format the data matrix you want to write to a csv file.
#k <- unlist(new_var)
#l <- length(k)/2
#y<-matrix(k,nrow=l,ncol=2,byrow=TRUE)

# write appropriate code to format the data matrix you want to write to a csv file.

#k <- rbind(as.data.frame(new_var[2]))
#j <- as.data.frame(k[!duplicated(as.data.frame(k)),])

#q <- rbind(as.data.frame(new_vars[2]))
#i <- as.data.frame(q[!duplicated(as.data.frame(q)),])

y<-matrix(k,nrow=l,ncol=10,byrow=FALSE)
w<-matrix(q,nrow=ll,ncol=2,byrow=FALSE)
write.csv(y,'BME777_BigData_Extract_class1.csv')
write.csv(w,'BME777_BigData_Extract_class2.csv')
