import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

respData = pd.read_csv("respiratory_samples.csv")
respData = respData.rename(index=str, columns={"Unnamed: 0": "Original Data Index"})

# Extracting all samples belonging to the group "Respiratory" such that they were discharged to home: dischargeID = 1 
respHome = respData.loc[respData['discharge_disposition_id'] == 1] 

# Extracting all samples belonging to the group "Respiratory" such that they were NOT discharged to home 
respOther = respData.loc[respData['discharge_disposition_id'] != 1] 


columns = ["Original Data Index","admission_type_id","discharge_disposition_id","diag_1"]

homeStats = respHome.describe()
homeStats = homeStats.drop(columns,axis=1)

otherStats = respOther.describe()
otherStats = otherStats.drop(columns,axis=1)
