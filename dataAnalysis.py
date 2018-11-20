import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


idMapping = pd.read_csv("IDs_mapping.csv")
respData = pd.read_csv("respiratory_samples.csv")
respData = respData.rename(index=str, columns={"Unnamed: 0": "Original Data Index"})

# Extracting all samples belonging to the group "Respiratory" such that they were discharged to home: dischargeID = 1 
respHome = respData.loc[respData['discharge_disposition_id'] == 1] 

# Extracting all samples belonging to the group "Respiratory" such that they were NOT discharged to home 
respOther = respData.loc[respData['discharge_disposition_id'] != 1] 

# To focus on factors leading to early readmission, only measuring the data which with readmission <30 
#home30 = respHome.loc[respHome['readmitted'] == '<30']
#other30 = respOther.loc[respOther['readmitted'] == '<30']

# Summary statistics of the numerical data correspondign to patients discharged home and discharged to other than home 
columns = ["Original Data Index","admission_type_id","discharge_disposition_id","diag_1"]

homeStats = respHome.describe()
homeStats = homeStats.drop(columns,axis=1)

otherStats = respOther.describe()
otherStats = otherStats.drop(columns,axis=1)

################## Comparing A1Cresults with early readmission in HOME patients ########

# A1Cresult = norm and readmitted early (HOME PATIENTS)
norm_early_home = ((respHome['A1Cresult']=='Norm') & (respHome['readmitted']=='<30'))
NEH = norm_early_home.value_counts()

# A1Cresult = none and readmitted early (HOME PATIENTS)
none_early_home = ((respHome['A1Cresult']=='None') & (respHome['readmitted']=='<30'))
NoneEH = none_early_home.value_counts()

# A1Cresult = '>7' (no change in medication) and readmitted early (HOME PATIENTS)
noChange_early_home = ((respHome['A1Cresult']=='>7') & (respHome['readmitted']=='<30'))
NCEH = noChange_early_home.value_counts()

# A1Cresult = '>8' (change in medication) and readmitted early (HOME PATIENTS)
change_early_home = ((respHome['A1Cresult']=='>8') & (respHome['readmitted']=='<30'))
CEH = change_early_home.value_counts()

# Bar graph visualization 
theLabels = ('Norm','None','No Change in Medication','Change in Medication')
y_pos = np.arange(len(theLabels))
earlyReadmissions = [NEH[1],NoneEH[1],NCEH[1],CEH[1]]

plt.figure()
plt.bar(y_pos, earlyReadmissions, align='center', alpha=0.5,color = 'b')
plt.xticks(y_pos, theLabels)
plt.ylabel('Number of Early Readmissions (Patients discharged home)')
plt.title('HbA1c Test Results')
plt.show()

"""The graph shows that when the patients are discharged home without conducting any HbA1c tests, their likeihood of 
being readmitted early (readmission in less than 30 days of charge) is significantly higher compared to when an HbA1c is conducted)"""


################## Comparing A1Cresults with early readmission in OTHER patients ########

# A1Cresult = none and readmitted early (OTHER PATIENTS)
norm_early_other = ((respOther['A1Cresult']=='Norm') & (respOther['readmitted']=='<30'))
NEO = norm_early_other.value_counts()

# A1Cresult = none and readmitted early (OTHER PATIENTS)
none_early_other = ((respOther['A1Cresult']=='None') & (respOther['readmitted']=='<30'))
NoneEO = none_early_other.value_counts()

# A1Cresult = '>7' (no change in medication) and readmitted early (Other PATIENTS)
noChange_early_other = ((respOther['A1Cresult']=='>7') & (respOther['readmitted']=='<30'))
NCEO = noChange_early_other.value_counts()

# A1Cresult = '>8' (change in medication) and readmitted early (Other PATIENTS)
change_early_other = ((respOther['A1Cresult']=='>8') & (respOther['readmitted']=='<30'))
CEO = change_early_other.value_counts()

# Bar graph visualization 
theLabels2 = ('Norm','None','No Change in Medication','Change in Medication')
y_pos2 = np.arange(len(theLabels))
earlyReadmissions2 = [NEO[1],NoneEO[1],NCEO[1],CEO[1]]

plt.figure()
plt.bar(y_pos2, earlyReadmissions2, align='center', alpha=0.5,color = 'b')
plt.xticks(y_pos2, theLabels2)
plt.ylabel('Number of Early Readmissions (Patients no discharged home)')
plt.title('HbA1c Test Results')
plt.show()

""" Similar to previous analysis, the lack of HbA1c tests reults in great increase in early readmissions even for patients 
who were discharged to 'other' facilities/treatments """ 


##### Comparison of the male and female data ###############
maleHome = respHome.loc[respHome['gender']=='Male']
femaleHome = respHome.loc[respHome['gender']=='Female']

maleOther = respOther.loc[respOther['gender'] == 'Male']
femaleOther = respOther.loc[respOther['gender']=='Female']

maleHomeStats = maleHome.describe()
maleHomeStats = maleHomeStats.drop(columns,axis=1)

femaleHomeStats = femaleHome.describe()
femaleHomeStats = femaleHomeStats.drop(columns,axis=1)

maleOtherStats = maleOther.describe()
maleOtherStats = maleOtherStats.drop(columns,axis=1)

femaleOtherStats = femaleOther.describe()
femaleOtherStats = femaleOtherStats.drop(columns,axis=1)

"""This split of data also shows that there is little variance between the males and females in their attributes in their 
respective classification of either being discharged home or other"""

##### Observing the effects of age on the probability of patients being discharged home
ageHome1 = respHome.groupby(['age','discharge_disposition_id']).size()

xlabels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
y_age = np.arange(len(xlabels))

plt.figure()
plt.plot(y_age,ageHome1)
plt.xticks(y_age, xlabels)
plt.ylabel('Number of Home Discharges')
plt.xlabel('Age')
plt.title('Home Discharges Based on Age')
plt.show()

"""As the age increases, there an increased the number of patients discharged to go home; a good feature that can help 
classify the data leadign to being discharged to home or other" """




