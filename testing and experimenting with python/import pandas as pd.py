import pandas as pd
import numpy as np

import matplotlib 
import matplotlib.pyplot as pp

#finding the mean of the MARD from Enlite (Medtronic)
fig1 = pd.read_csv('Enlitedata.csv')
fig1

MARD_En = fig1.mean()
print("MARD_En:", MARD_En)

data = [20.756667, 13.606667, 15.623333]
data_series = pd.Series(data)
MARD_all = data_series.mean()
print("MARD of all_En:", MARD_all)


#MARD of Guardian (Medtronic)
MARD_G = 20.3 

data = {'X': ['Freestyle libre 2', 'Dexcom 7', 'Guardian 3'], 'Y':[11.8, 8.2, 9.6]}
    
df = pd.DataFrame(data)
ax = df.plot(kind='bar', x='X', y='Y', color='b') 
ax.set_title('MARD of each company')
ax.set_xlabel('Company')
ax.set_ylabel('MARD value in percentage')

pp.show()

#price of each brand
datap = {'X': ['Freestyle libre 2', 'Dexcom 7', 'Guardian 3'], 'Y':[47.95, 46.6, 68.85]}
df = pd.DataFrame(datap)
ax = df.plot(kind='bar', x='X', y='Y', color='g') 
ax.set_title('Price of each CGM from different company')
ax.set_xlabel('Company')
ax.set_ylabel('Price(£)')

pp.show()

#price vs MARD
datavs = {'X': ['11.8', '8.2', '9.6'], 'Y':[47.95, 46.6, 68.85],'Color': ['red', 'blue', 'green']}
df = pd.DataFrame(datavs)
scatter = df.plot(kind='scatter', x='X', y='Y', c=df['Color'], label='Scatter Plot', colormap='viridis', s=50)
ax.set_title('Price vs MARD')
ax.set_xlabel('MARD')
ax.set_ylabel('Price(£)')

pp.show()
print("Red=Freestyle libre2 , Blue = Dexcom 7 , green = Guardian3")