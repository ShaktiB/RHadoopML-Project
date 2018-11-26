import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from respfunctions import convertage
from respfunctions import normalize
import math

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
respO['Age2']= respO.apply (lambda row: convertage(row),axis=1)

############### Convert Data Types #####################
#Converting 'admission type', 'diagnosis', 'medications', 'discharge disposition' data to numeric data instead of string

aTypeH = np.array(pd.to_numeric(respH['Admission_Type'])) # Admission type data (HOME)
diagH = np.array(pd.to_numeric(respH['Diagnosis'])) # Diagnosis data (HOME)
respH['AdmissionType'] = aTypeH
respH['Diagnosis1'] = diagH

aTypeO = np.array(pd.to_numeric(respO['Admission_Type'])) # Admission type data (OTHER)
diagO = np.array(pd.to_numeric(respO['Diagnosis'])) # Diagnosis data (OTHER)
respO['AdmissionType'] = aTypeO
respO['Diagnosis1'] = diagO

respH['Medications'] = pd.to_numeric(respH['Num_of_Medications'])
respO['Medications'] = pd.to_numeric(respO['Num_of_Medications'])

respH['Discharge'] = pd.to_numeric(respH['Discharge_Disposition'])
respO['Discharge'] = pd.to_numeric(respO['Discharge_Disposition'])

dataTypesH = respH.dtypes 
dataTypesO = respO.dtypes

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

# Age Data 
ageCountH = respH['Age2'].value_counts(sort=False) # Count the number of people in each age group 
ageCountH=ageCountH.sort_index() # Sort the age index to go from 10 to 100 

ageCountO = respO['Age2'].value_counts(sort=False) 
ageCountO=ageCountO.sort_index()

x_axis = np.arange(0,len(ageCountH)/2)
x_labels = ['10-20','30-40','50-60','70-80','90-100']

## Plot of age distribution in class Home  --> BAR GRAPHS
#plt.figure()
#plt.bar(x_axis,ageCountH)
#plt.xticks(x_axis, x_labels)
#plt.ylabel('Count')
#plt.xlabel('Age')
#plt.title('Distribution of Age of People Discharged Home')
#plt.show()
#
## Plot of age distribution in class Other --> BAR GRAPHS
#plt.figure()
#plt.bar(x_axis,ageCountO)
#plt.xticks(x_axis, x_labels)
#plt.ylabel('Count')
#plt.xlabel('Age')
#plt.title('Distribution of Age of People Discharged to Ohter Facilities')
#plt.show()

### Histograms #####

theLegend = ['Discharged Home', 'Discharged Other']

plt.figure()
plt.hist([respH['Age2'],respO['Age2']],bins=10,color = ['orange','green'])
plt.ylabel('Count')
plt.xlabel('Age')
plt.title('Distribution of Age')
plt.legend(theLegend)
plt.show()

# Analysis of the Admission Types in both classes
uniqueH, countsH = np.unique(aTypeH, return_counts=True) # Returns the occurences of each admission type 
admissionH = dict(zip(uniqueH, countsH)) # Puts the information into a dict 

uniqueO, countsO = np.unique(aTypeO, return_counts=True) # Returns the occurences of each admission type 
admissionO = dict(zip(uniqueO, countsO)) # Puts the information into a dict

plt.figure()
plt.hist([aTypeH,aTypeO],bins=8,color = ['orange','green'])
plt.ylabel('Count')
plt.xlabel('Admission Type')
plt.title('Distribution of Admission Types')
plt.legend(theLegend)
plt.show()

# A1C Result Analysis 

a1cCountH = respH['A1CResult'].value_counts()
a1cCountO = respO['A1CResult'].value_counts()

avgA1cH = (a1cCountH/len(respH))*100
avgA1cO = (a1cCountO/len(respO))*100
print('Average A1C Results in class Home:', avgA1cH)
print()
print('Average A1C Results in class Other:', avgA1cO)

# Redadmitted data analysis 

readmCountH = respH['Readmitted'].value_counts()
readmCountO = respO['Readmitted'].value_counts()

avgReadmH = (readmCountH/len(respH))*100
avgReadmO = (readmCountO/len(respO))*100

############################# Set up data for Neural Network  #########################################

lenO = len(respO) # Number of samples in class Other

class1 = np.array(respH[['Age2', 'Time_in_Hospital','Num_of_Lab_Procedures','Medications','Discharge']].sample(n=lenO))
class2 = np.array(respO[['Age2', 'Time_in_Hospital','Num_of_Lab_Procedures','Medications','Discharge']])
classes = np.append(class1,class2,axis=0)
np.random.shuffle(classes) # Randomize the array 

### Creating normalized feature arrays ######
x1 = normalize(classes[:,0]) # Age
x2 = normalize(classes[:,1]) # Time in Hospital 
x3 = normalize(classes[:,2]) # Number of lab procecures 
x4 = normalize(classes[:,3]) # Number of medications 

target = np.where(classes[:,4]==1,1,(-1)) # classification targets 

############## Neural Network ###############################
# 4-3-1 Neural network 

# Initialization 

eta = 0.1
theta = 0.001
maxIterations = 300

# Random initial weight vectors 
wih1 = np.array([0.69, 0.10, 0.75, 0.39, 0.41]) # Weight vector --> input to hidden node 1 
wih2 = np.array([0.65, 0.83, 0.37, 0.15, 0.32]) # Weight vector --> input to hidden node 2
wih3 = np.array([0.35, 0.95, 0.25, 0.62, 0.45]) # Weight vector --> input to hidden node 3 
who1 = np.array([0.42, 0.59, 0.56, 0.75]) # Weight vector --> hidden layer to output node 

j = np.zeros(len(x1)) # Cost 

right = 0
wrong = 0

r = 0;

while(r<len(x1)):
      
    deltaWih1 = np.array([0, 0, 0, 0, 0]) # Inputs of bias, x1,x2,x3,x4 to hidden neuron 1
    deltaWih2 = np.array([0, 0, 0, 0, 0]) # Inputs of bias, x1,x2,x3,x4 to hidden neuron 2
    deltaWih3 = np.array([0, 0, 0, 0, 0]) # Inputs of bias, x1,x2,x3,x4 to hidden neuron 3
    deltaWho1 = np.array([0, 0, 0, 0]) # Inputs of bias, y1, y2, y3 to output neuron 1
    
    # Initialize training sample order and predicted output.
    
    m = 0;
    Z = np.zeros(1,len(x1))
    
    # Initializaing training data 
    x11 = x1
    x22 = x2
    x33 = x3
    x44 = x4
    t = target
    
    # Initializaing test point for Leave-One-Out Method 
    testx1 = x11[r]
    testx2 = x22[r]
    testx3 = x33[r]
    testx4 = x44[r]
    testTar = t[r]
    
    x11 = np.delete(x11,r)
    x22 = np.delete(x22,r)
    x33 = np.delete(x33,r)
    x44 = np.delete(x44,r)        
    t = np.delete(t,r)
    
    r = r+1 # Incrementing the epoch 
            
    while(m<lengthX11):
        
        Xm = np.array([1, x11[m], x22[m], x33[m], x44[m]]) # Input features 
        
        y1 = np.dot(wih1, Xm)
        y2 = np.dot(wih2, Xm)
        y3 = np.dot(wih3, Xm)
        
        # sigmoid = a*tanh(b*xm) where a=b=1 
        
        Ym = np.array([1, np.tanh(y1), np.tanh(y2), np.tanh(y3)]) # applying activation function on the hidden layer 
        netk_1 = np.dot(Ym,who1)
        Z[m] = np.tanh(netk_1)
        
        # Calculate the sensitivity value of each hidden neuron and the output neuron
        
        deltaO1 = np.dot( (t[m] - Z[m]), (1 - (np.tanh(netk_1))**2) ) # Sensitivity value of the output neuron
        deltaH1 = (1-(np.tanh(y1))**2)*who1[1]*deltaO1 # Sensitivity value of hidden neuron 1
        deltaH2 = (1-(np.tanh(y2))**2)*who1[2]*deltaO1 # Sensitivity value of hidden neuron 2
        deltaH3 = (1-(np.tanh(y3))**2)*who1[3]*deltaO1 # Sensitivity value of hidden neuron 3
        
        # Update the gradient
        
        deltaWih1 = deltaWih1 + eta*deltaH1*Xm 
        deltaWih2 = deltaWih2 + eta*deltaH2*Xm
        deltaWih3 = deltaWih3 + eta*deltaH3*Xm 
        deltaWho1 = deltaWho1 + eta*deltaO1*Ym
        
        m = m + 1
        
    # Update the weight vectors
    
    wih1 = wih1 + deltaWih1 # Weight vector input to hidden unit no.1
    wih2 = wih2 + deltaWih2 # Weight vector input to hidden unit no.2
    wih3 = wih3 + deltaWih3 # Weight vector input to hidden unit no.3
    who1 = who1 + deltaWho1 # Weight vector hidden to output unit
    
    # Cost 
    j[r] = 0.5*(math.sqrt(sum((t-Z)**2)))
    
    # testing ---> the feed forward network from above 
    
    testPoint = np.array([1, testx1, testx2, testx3, testx4])
    
    test_y1 = np.dot(wih1, testPoint)
    test_y2 = np.dot(wih2, testPoint)
    test_y3 = np.dot(wih3, testPoint)
    
    test_Ym = np.array([1, np.tanh(test_y1), np.tanh(test_y2), np.tanh(test_y3)])
    test_netk_1 = np.dot(test_Ym,who1)
    testZ = np.tanh(test_netk_1)
    
    if ((testZ > 0) & (t>0)):
        right = right + 1
    elif ((testZ < 0) & (t<0)):
        right = right + 1
    else:
        wrong = wrong + 1
        
    accuracy = (right/len(x1))*100


