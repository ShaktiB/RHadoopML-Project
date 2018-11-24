import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from respfunctions import convertage 

################# Load data and store in a new variable #################

idMapping = pd.read_csv("IDs_mapping.csv")

# Respiratory disease patients discharged home (class 1)
respH_ = pd.read_csv("BME777_BigData_Extract_class1.csv",index_col=0) 
respH = respH_
# Respiratory disease patients NOT discharged home (class 2)
respO_ = pd.read_csv("BME777_BigData_Extract_class2.csv",index_col=0)
respO = respO_

# Rename Column Labels 
colNames = {'V1':'Gender','V3':'Admission_Type','V4':'Discharge_Disposition',
            'V5':'Time_in_Hospital','V6':'Num_of_Lab_Procedures',
            'V7':'Num_of_Medications','V8':'Diagnosis',
            'V9':'A1CResult','V10':'Readmitted','V2':'Age'}

respH = respH.rename(index=str, columns = colNames)
respO = respO.rename(index=str, columns = colNames)

################## Clean data ###########################

respH = respH[(respH['Gender'] == 'Male')|(respH['Gender'] == 'Female')]
respO = respO[(respO['Gender'] == 'Male')|(respO['Gender'] == 'Female')]

respH = respH[(respH['Age'] != 'Male') & (respH['Age'] != 'Female')]
respO = respO[(respO['Age'] != 'Male') & (respO['Age'] != 'Female')]

# Creating numeric version of the 'Age' data which is currently an object and cannot be functionaly changed to numerics
respH['Age2']= respH.apply (lambda row: convertage(row),axis=1)
respO['Age2']= respH.apply (lambda row: convertage(row),axis=1)

############### Convert Data Types #####################
#Converting 'admission type' and 'diagnosis' data to numeric data instead of string

dataTypesH = respH.dtypes 
dataTypesO = respO.dtypes 

aTypeH = np.array(pd.to_numeric(respH['Admission_Type'])) # Admission type data (HOME)
diagH = np.array(pd.to_numeric(respH['Diagnosis'])) # Diagnosis data (HOME)

aTypeO = np.array(pd.to_numeric(respO['Admission_Type'])) # Admission type data (OTHER)
diagO = np.array(pd.to_numeric(respO['Diagnosis'])) # Diagnosis data (OTHER)

############ Data Analysis #########################

# Summary of statistics for both classes (Home and Other)
statsH = respH.describe() 
statsO = respO.describe()
#Provides statistical summary of the NUMERIC data --time in hospital and # of procedures
print('Class Home stats')
print(statsH)
print()
print('Class Other stats')
print(statsO)

genderCountH = respH['Gender'].value_counts()
genderCountO = respO['Gender'].value_counts()

avgMaleH = (genderCountH[1]/len(respH)) * 100
avgFemaleH = (genderCountH[0]/len(respH)) * 100
avgMaleO = (genderCountO[1]/len(respO)) * 100
avgFemaleO = (genderCountO[0]/len(respO)) * 100

print('Male % (Home):', format(avgMaleH, '.2f'))
print('Female % (Home):', format(avgFemaleH, '.2f'))
print('Male % (Other):', format(avgMaleO, '.2f'))
print('Female % (Other):', format(avgFemaleO, '.2f'))





