import numpy as np
import pandas as pd 

def convertage(row):
    
    if row['Age'] == '[0-10)':
        return 10
    
    if row['Age'] == '[10-20)':
        return 20
    
    if row['Age'] == '[20-30)':
        return 30
    
    if row['Age'] == '[30-40)':
        return 40
    
    if row['Age'] == '[40-50)':
        return 50
    
    if row['Age'] == '[50-60)':
        return 60
    
    if row['Age'] == '[60-70)':
        return 70
    
    if row['Age'] == '[70-80)':
        return 80
    
    if row['Age'] == '[80-90)':
        return 90
    
    if row['Age'] == '[90-100)':
        return 100
    
    
    