
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

# 기온 데이터 읽어 들이기
df = pd.read_csv('data/tem10y.csv', encoding="utf-8")


# In[3]:

# 데이터를 학습 전용과 테스트 전용으로 분리하기 ---(*1)
train_year = (df["연"] <= 2015)
test_year = (df["연"] >= 2016)
interval = 6


# In[4]:

# 과거 6일의 데이터를 기반으로 학습할 데이터 만들기 ---(*2)
def make_data(data):
    x = [] # 학습 데이터
    y = [] # 결과
    temps = list(data["기온"])
    for i in range(len(temps)):
        if i < interval: continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return (x, y)


# In[5]:

train_x, train_y = make_data(df[train_year])
test_x, test_y = make_data(df[test_year])


# In[6]:

# 직선 회귀 분석하기 ---(*3)
lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y) # 학습하기
pre_y = lr.predict(test_x) # 예측하기


# In[7]:

# 결과를 그래프로 그리기 ---(*4)
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')


# In[9]:

# 평가하기
sum(abs(pre_y - test_y) / len(pre_y))


# In[10]:

max(pre_y - test_y)


# In[ ]:



