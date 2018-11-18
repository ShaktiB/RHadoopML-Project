import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

theData = pd.read_csv("diabetic_data_V2.csv")
idMapping = pd.read_csv("IDs_mapping.csv")

#print(theData.head())
#print(theData.dtypes)

# Add another column while is the numeric version of the 'diag_1' column whic hwas originally an object (read as str)
theData['new_diag_1'] = pd.to_numeric(theData['diag_1'],errors='coerce') # 'coerce' replaces non-numeric values with NaN

# Extracting all samples belonging to the group "Respiratory" 
respiratory = theData.loc[(theData['new_diag_1'] >= 460) & (theData['new_diag_1'] <= 519) | (theData['new_diag_1'] == 786)]

###### Exporting new CSV Files ###########
respiratory.to_csv('respiratory_samples.csv')


