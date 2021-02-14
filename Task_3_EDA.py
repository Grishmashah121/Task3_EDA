#!/usr/bin/env python
# coding: utf-8

# # Task 3- Exploratory Data Analysis -Retail
# 
# # Grishma Shah

# In[1]:


#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#Import the data
data=pd.read_csv("C:\Python\Data\SampleSuperstore.csv")
data.head(5)


# In[8]:


#Checking data types
data.dtypes


# In[5]:


#Checking information of data
data.info()


# In[10]:


#Checking number of rows and column
data.shape


# In[11]:


#Checking description of data
data.describe()


# In[16]:


#checking the null values
data.isnull()


# In[17]:


duplicate_rows_data=data[data.duplicated()] # checking duplicated rows
duplicate_rows_data.shape


# In[18]:


#Dropping the duoplicate data
data=data.drop_duplicates()
data.head()


# In[20]:


data.shape


# # Outliers

# In[21]:


#Plotting boxplot for Profit
sns.boxplot(x=data['Profit'])


# In[22]:


#Plotting boxplot for Sales
sns.boxplot(x=data['Sales'])


# In[23]:


#Plotting boxplot for Quantity
sns.boxplot(x=data['Quantity'])


# In[24]:


#Plotting boxplot for Discount
sns.boxplot(x=data['Discount'])


# In[25]:


# finding Interquartile range(IQR)
Q1=data.quantile(0.25)
Q3=data.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[26]:


# Removing Outliers
data=data[~((data<(Q1-1.5*IQR))|(data>(Q3+1.5*IQR))).any(axis=1)]
data.shape


# In[27]:


data.describe()


# In[28]:


data.max()


# In[29]:


data.min()


# In[30]:


# finding correlation
c_1 = data["Sales"]
c_2 = data["Discount"]
correl = c_1.corr(c_2)
print(correl)


# In[31]:


c_1=data["Discount"]
c_2=data["Profit"]
correl=c_2.corr(c_1)
print(correl)


# In[32]:


c_1 = data["Sales"]
c_2 = data["Quantity"]
correl = c_1.corr(c_2)
print(correl)


# In[34]:


f,ax=plt.subplots(figsize=(11,11))
sns.heatmap(data.corr(),annot=True)
plt.show()

From Above correlation between sales and profit is 0.4 and is positive or good,followed by Quantity and profit that os 0.23
# In[36]:


plt.figure(figsize=(6,6))
plt.pie(data['Category'].value_counts(),labels=data['Category'].value_counts().index,autopct='%1.1f%%')
plt.show()


# In[37]:


plt.figure(figsize=(6,6))
plt.pie(data['Sub-Category'].value_counts(),labels=data['Sub-Category'].value_counts().index,autopct='%1.1f%%')
plt.show()


# In[38]:


fig,ax=plt.subplots(figsize=(15,8))

ax.bar(data['Sub-Category'],data['Quantity'])


# In[39]:


#Counterplot
plt.figure(figsize=(15,10))
sns.countplot(x=data['State'],hue=data['Sub-Category'],palette='Set3',saturation=1,linewidth=30)
plt.xticks(rotation=90)
plt.show()


# In[40]:



plt.figure(figsize=(15,10))
sns.countplot(x=data['Region'],hue=data['Sub-Category'],palette='Set1',saturation=1,linewidth=30)
plt.xticks(rotation=90)
plt.show()


# In[41]:



plt.figure(figsize=(15,10))
sns.countplot(x=data['Segment'],hue=data['Sub-Category'],palette='Set1',saturation=1,linewidth=30)
plt.xticks(rotation=90)
plt.show()


# In[42]:


fig,ax=plt.subplots(figsize=(15,8))

ax.bar(data['Sub-Category'],data['Sales'])


# In[43]:


fig,ax=plt.subplots(figsize=(15,8))

ax=fig.add_axes([0,0,1,1])
x=data['Sub-Category']
ax.bar(x,data['Profit'],color='green',width=0.25)
ax.bar(x,data['Sales'],color='yellow',width=0.25)


# # Insights
# * There is maximum demand of office supplies followed by technology and furniture
# * There is noticable positive correlation between a)Sales & Profit b)Quantity & Profit
# * quantity of items (Book cases,machines and Tables) are less in number,copiers are least in number
# * maximum number of purchases are made from States of California,Newyork and Texas followed by noticable number of purchases done in states of Washington,Pennsylvania and Illionis.But number of purchases in other States are very less
# * We also see the n.o of purchases per region and per segment, We see Consumer segment makes more purchases
# * We see from sales and Profit sacked bar Graph that though Sales are much more profit is really less for some items likes Appliances and Copiers though Sales is very high there is negligible profit which is point of concern
# * Seeing that there is vast difference between Sales and Profit Company must analyse and try to minimize expenses on over heads,shipment,they can build their sub centres so that at one they can ship product in a bulk to a subcentre and subcentres can deliver to customers in their region than individually shipping

# In[ ]:




