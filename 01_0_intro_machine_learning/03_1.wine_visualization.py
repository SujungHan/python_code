
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:

wine_df = pd.read_csv('data/winequality-white.csv', sep=';')


# In[3]:

wine_df.head()


# In[8]:

count_data = wine_df.groupby('quality')['quality'].count()
count_data


# In[9]:

count_data.plot()


# In[ ]:



