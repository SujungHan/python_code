
# coding: utf-8

# In[2]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd


# In[8]:

# CSV 파일 읽어 들이기 ---(*1)
df = pd.read_csv("data/tem10y.csv", encoding="utf-8")


# In[9]:

# 월별 평균 구하기 ---(*2)
g = df.groupby('월')['기온']
gg = g.sum() / g.count()


# In[10]:

# 결과 출력하기 ---(*3)
print(gg)
gg.plot()


# In[ ]:



