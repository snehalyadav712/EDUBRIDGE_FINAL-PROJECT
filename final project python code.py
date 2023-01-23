#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import the pandas library
import pandas as pd


# In[5]:


#Data cleaning
Data=pd.read_csv('python file.csv')
print(Data)


# In[6]:


#use of isnull
Data.isnull()


# In[7]:


Data['age']=Data['age'].fillna(0)
print(Data)


# In[9]:


#removing the duplicates rows and columns in the data
Data.drop_duplicates()


# In[10]:


#Data processing
#displaing specific records from dataset 
print(Data.loc[0:10])


# In[11]:


#displaying sepcific row with specific column
print(Data.loc[[0,5],['gender','bloodpressure','diabetic']])


# In[13]:


print(Data[0:3]['bloodpressure'])


# In[14]:


#DATA WRANGLING
df=pd.DataFrame(Data)
grouped = df.groupby('gender')
print (grouped.get_group('male'))


# In[17]:


#STATSTICAL FUNCTION
import statistics
x=Data.claim
mean=statistics.mean(x)
print(mean)
from statistics import median
y=Data.age
print(median(y))
z=Data.bloodpressure
print(statistics.mode(z))
print(statistics.variance(z))


# In[8]:


#DATA VISULIZATION
import matplotlib.pyplot as plt
import numpy as np


# In[11]:


#line chart
x=np.array([2017, 2018,2019,2020,2021,2022])
y=np.array([10,15,23,25,35,45])
plt.plot(x,y,linestyle="dotted", color="red",marker="*")
plt.xlabel('Year')
plt.ylabel('Profit')
plt.title("Profit By Year")
plt.grid()
plt.show()


# In[12]:


#scatterplot
#compairing 2 values in single plot
x= np.array([20,34,25,43,50])
y=np.array([42,15,46,31,20])
plt.scatter(x,y)
x= np.array([40,34,45,23,12])
y=np.array([36,50,32,10,25])
plt.scatter(x,y)
plt.show()


# In[13]:


#pie chart
x=np.array([56,67,80,46])
my_labels = ["east", "west", "north", "south"]
plt.title('region wise sale')
plt.pie(x,labels=my_labels)
plt.show()


# In[18]:


#bar chart
x= np.array(["mumbai","pune","nasik"])
y=np.array([50000,30000,10000])
plt.title('Population')
plt.bar(x,y,color="red",width=0.2)
plt.show()


# In[19]:


y=np.random.normal(100,5,50)
print(y)


# In[17]:


plt.hist(y)
plt.show()


# In[ ]:




