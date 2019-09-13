#!/usr/bin/env python
# coding: utf-8

# ## Import
# 

# In[2]:


#import all the libraries 
#Pandas :  for data analysis
#numpy : for Scientific Computing.
#matplotlib and seaborn : for data visualization
#scikit-learn : ML library for classical ML algorithms
#math :for mathematical functions

import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')

#Load the data from the CSV
crime_stats= pd.read_csv('/Desktop/crime.csv',engine='python')





# # Data Analysis
# 

# In[3]:


#Return the first 5 rows of data 
crime_stats.head(5)


# In[4]:


# Get the column labels of the data

crime_stats.columns


# In[5]:


# To view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values.
crime_stats.describe()


# In[6]:


# To get data from specific columns

crime_stats[['OFFENSE_DESCRIPTION','STREET']]


# In[17]:


# To get data from specific columns based on a condition 


crime_stats[crime_stats.OFFENSE_DESCRIPTION =="INVESTIGATE PROPERTY"]


# In[24]:


# To get top 5 rows from specific columns


crime_stats[["OFFENSE_CODE_GROUP", "YEAR"]].head(5)


# In[25]:


##List unique values in the df['name'] column

crime_stats["OFFENSE_CODE_GROUP"].unique()


# In[26]:


# To get data from specific columns based on a condition ( top rows of the data)


crime_stats[crime_stats.OFFENSE_CODE_GROUP=='Verbal Disputes'][['DAY_OF_WEEK','HOUR','STREET']].head()


# In[29]:


# To get data count for each columns based on a condition 


crime_stats[crime_stats.OFFENSE_CODE_GROUP=='Verbal Disputes'].count()


# In[30]:


# To get total data count for each columns 

crime_stats.count()


# In[33]:


#To get a concise summary of the data 

crime_stats.info()


# In[91]:


#Group by one column and count the values of another column per this column value using count

crime_stats.groupby("OFFENSE_CODE_GROUP").count()


# In[89]:


#Group by multiple columns and count the values of another column per these column value using count 
#( show top rows using head)

crime_stats[crime_stats.OFFENSE_CODE_GROUP=='Verbal Disputes'].groupby(['DAY_OF_WEEK','HOUR','STREET']).count().head()


# In[90]:


crime_stats.sort_values("OFFENSE_CODE_GROUP").head()


# In[6]:


#Print a sample of your dataframe from the tail

crime_stats.sort_values("OFFENSE_CODE_GROUP").tail(5)


# In[7]:


#sort the data in Ascending or Descending order of passed Columns

crime_stats.sort_values(by=["OFFENSE_CODE_GROUP","STREET"])


# In[8]:


#sort the data in Descending order of passed Columns


crime_stats.sort_values(by=["OFFENSE_CODE_GROUP","STREET"], ascending=False)


# In[9]:


#sort the data in Descending order of passed Columns and Reset the index

crime_stats.sort_values(by=["OFFENSE_CODE_GROUP","STREET"], ascending=False).reset_index()


# In[10]:


#sort the data in Descending order of passed Columns and Reset the index and remove the old index by making drop=True

crime_stats.sort_values(by=["OFFENSE_CODE_GROUP","STREET"], ascending=False).reset_index(drop=True)


# # Data Visualization

# In[26]:


#Histogram : use plt.hist() function of matplotlib 
# and pass in the data along with the number of bins and a few optional parameters.

fig,ax=plt.subplots()
ax.hist(crime_stats["HOUR"],bins=10,edgecolor='black', linewidth=1.2)
ax.set_title("Crime by Hour")
ax.set_xlabel("Hour")
ax.set_ylabel("Frequency")


# In[38]:


# show the relationship between a numerical and one or more categorical variables using catplot. 

sns.set(style="ticks", color_codes=True)
sns.catplot(x="MONTH", y="OFFENSE_CODE_GROUP", data=crime_stats, jitter=False,height=15,hue="UCR_PART");



# In[41]:


# show the relationship between a numerical and one or more categorical variables using catplot and kind=violin 

sns.catplot(x="MONTH", y="OFFENSE_CODE_GROUP", data=crime_stats, split=True,kind="violin",height=15,colour="Blue");


# In[44]:


#Group By count based on some condition

crme=crime_stats.groupby(crime_stats["OFFENSE_CODE_GROUP"]=="Warrant Arrests").count()
crme


# In[85]:


#countplot is used to show the counts of observations in each categorical bin using bars.

sns.set(style="whitegrid")
sns.countplot(x="DAY_OF_WEEK",data=crime_stats,edgecolor=sns.color_palette('dark',3))#,facecolor=(0, 0, 0, 0));



# In[84]:


# show the relationship between a numerical and one or more categorical variables using catplot and set col. 

sns.set(style="whitegrid")
sns.catplot(x="DAY_OF_WEEK",col="UCR_PART",kind="count",data=crime_stats,height=9, aspect=.7);



# In[ ]:




