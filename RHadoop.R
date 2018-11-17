
library(rmr2) # Map reduce package 
library(rhdfs) #The library package rhdfs provides commands for file manipulation in terms of reading, writing and moving files

setwd("C:/Users/Shakti/Desktop/5th Year/777/Project") # initialize with the path to your working directory.

databme777<-read.csv("diabetic_data_V2.csv")  # study the read.csv command parameters and read the dataset csv file.

head(databme777, n = 3) # Retreive the first 3 rows of data 

hdfs.init() # Initialize 

databme777.values <- to.dfs(databme777) # puts the data into HDFS, where the bulk of the data has to reside for mapreduce to operate on
