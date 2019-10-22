
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:

# 파일 읽어 들이기
df = pd.read_csv('data/tem10y.csv', encoding="utf-8")


# In[3]:

# 온도가 30도를 넘는 데이터 확인하기 ---(*1)
df.loc[df['기온'] > 30]


# In[4]:

# 연별로 세기 ---(*3)
df.loc[df['기온'] > 30].groupby(["연"])["연"].count()


# In[5]:

# 출력하기
df.loc[df['기온'] > 30].groupby(["연"])["연"].count().plot()


# In[ ]:



