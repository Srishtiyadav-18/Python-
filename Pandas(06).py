#!/usr/bin/env python
# coding: utf-8

# PANDAS

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s=pd.Series([1,2,3, np.nan, 5,6])
print(s)


# In[3]:


#creating a series with a custom index
s=pd.Series([1,2,3],index=['a','b','c'])
print(s)


# In[4]:


s.iloc[1]


# In[5]:


s.loc['b']


# #Dataframe
# 

# In[6]:


data={
    'A':[1,3,5,6],
    'B':[7,8,9,6],
    'C':[1,4,5,6]
}
df= pd.DataFrame(data)
print(df)


# #Viewing Data

# In[7]:


#display the first rows
print(df.head)
print(df.tail)


# In[8]:


df.info()


# In[9]:


#display summary statistics
print(df.describe())


# In[10]:


#Display the dataframe's index
print(df.index)


# In[11]:


print(df.values)


# In[12]:


print(df.columns)


# SELECTING DATA

# In[13]:


#selecting a sinle column
print(df['A'])


# In[14]:


#selecting a multiple column
print(df[['A','B']])


# In[15]:


df


# In[16]:


print(df.loc[0])
print(df.iloc[0:2,0:2])  


# In[17]:


df['A'][0]=10
df


# In[18]:


df['B'][0]=9
df


# In[19]:


df.iloc[0][1]=7
df


# In[20]:


df1=df.copy()


# In[21]:


df1.iloc[0,1]=np.nan
print(df1)


# In[28]:


df_with_nan=df.copy()


# In[34]:


print(df_with_nan.dropna())  #drop rows with missing values


# In[35]:


#setting values by position
df.iat[0,1]=20
print(df)


# In[31]:


df_with_nan


# In[32]:


df_with_nan.iloc[0,1]=np.nan
df_with_nan


# In[33]:


print(df_with_nan.isna()) #check the missing values


# Handling duplicates

# In[44]:


#Creating DataFrame with duplicates
df_dup=pd.DataFrame({
    'A':['1','2','3','5'],
    'B':['a','b','c','d']
})
print(df_dup)
print()


# In[45]:


#dropping duplicates
df_no_dup=df_dup.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_dup)


# In[51]:


#Creating DataFrame with duplicates
df_dup=pd.DataFrame({
    'A':['1','2','3','3'],          #duplicate data
    'B':['a','b','c','c']
})
print(df_dup)
print()


# In[52]:


#dropping duplicates
df_no_dup=df_dup.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_dup)   


# String operation

# In[58]:


df_str=pd.DataFrame ({
    'A':['1','2','3','4'],         
    'B':['a','b','c','d']
})
df_str


# In[ ]:




