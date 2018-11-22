# RHadoopML-Project

This project is an introduction to using the Hadoop platform, R programming language, and the application of MapReduce. Once the data required is queried and processed, machine learning will be used to analyze the data. 

RHadoop Code: This was the code used to import, filter, and save the data using R and Hadoop. All the data regarding patients who would be classified as having respiratory diseases based on 'diag_1' tests were extracted. That data was split into two based on where they were discharged to go home or not. 

dataAnalysis.py: This was the code used to primarily analyze the data straight from the CSV file prior to using MapReduce(0 with R & Hadoop. The purpose of this project was to learn R + Hadoop implementation to process data, however, in this script, the data is queiried and analyzed without the data being processed using RHadoop. This is not really a majoy factor since the query is simple and the resulting data would all the same. The other data analysis script is the one used to analyze the data after being processed using MapReduce with RHadoop. 


