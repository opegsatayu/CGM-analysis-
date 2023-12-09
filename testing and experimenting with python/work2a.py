import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob  # Import glob to list CSV files


#import diabetic 
folder_path = 'data_for_diabetes/'
diabetic = glob.glob(folder_path + 'case *.csv') 

#df is for diabetic datas
for file in diabetic:

    df = pd.read_csv(file)

  
    print(f"Data from {file}:")
    print(df.head())

#do mean of every row of diabetic cases files



#import nondiabetic 
nondiabetic = pd.read_csv('data for no diabetes.csv')
nondiabetic

#mean diabetic 
df_diabetic = df.iloc[134:225, 2]
mean_diabetic = df_diabetic.mean()
print("mean diabetic:", mean_diabetic)

#mean nondiabetic 
nondiabetic = pd.read_csv('data for no diabetes.csv')
nondiabetic

#df_nondiabetic = nondiabetic.iloc[:, 3]
df_nondiabetic = pd.to_numeric(nondiabetic.iloc[:, 3], errors='coerce') #from stackoverflow, this ignores the non-numeric number 
mean_nondiabetic = df_nondiabetic.mean()
print("mean nondiabetic:", mean_nondiabetic)

#mean diabetic = 92.382
#mean nondiabetic = 102.972

#graph BG vs time for both (do time interval of 3 hours)




# graph diabetic vs time [row 170 to 205] [column 3 for value, column 2 for time]
plt.figure(figsize=(10, 6))
x = df.iloc[134:225 , 1]
y = df.iloc[134:225 , 2]

plt.scatter(x, y)

plt.title('BG vs time of diabetic')
plt.xlabel('time')
plt.ylabel('Blood Glucose')

max_y = y.max()  
max_x = x[y.idxmax()]  

# Highlighting the highest point
plt.plot(max_x, max_y, "x", color='red')

plt.show()


# plot nondiabetic vs time 
plt.clf()
plt.figure(figsize=(10, 6))
x = nondiabetic.iloc[2:38, 2]
y = nondiabetic.iloc[2:38, 3]
plt.scatter(x, y)

plt.title('BG vs time of nondiabetic')
plt.xlabel('time')
plt.ylabel('Blood Glucose')

\

sorted_y = np.sort(y.unique())
plt.yticks(sorted_y)

max_y = y.max()  
max_x = x[y.idxmax()]  


plt.plot(max_x, max_y, "x", color='red')




#graph mean vs time  