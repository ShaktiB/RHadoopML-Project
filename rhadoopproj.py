import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

theData = pd.read_csv("respiratory_samples.csv")
theData = theData.rename(index=str, columns={"Unnamed: 0": "Original Data Index"})

respHome = theData.loc[theData['discharge_disposition_id'] == 1] 

respOther = theData.loc[theData['discharge_disposition_id'] != 1] 





