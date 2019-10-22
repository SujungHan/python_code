
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# ### 붓꽃 데이터 읽기

# In[2]:

df = pd.read_csv('data/iris.csv')


# In[3]:

df.head()


# ### 입력데이터와 레이블로 분리

# In[6]:

x = df[['sepal_length', 'sepal_width','petal_length','petal_width']]
y = df['class']


# ### 학습데이터와 테스트 데이터로 분리 (8:2)

# In[11]:

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)


# ### 학습하기

# In[56]:

model = SVC()


# In[57]:

model.fit(x_train, y_train)


# ### 평가하기

# In[58]:

prediction = model.predict(x_test)


# In[59]:

print('정답률 = ', accuracy_score(y_test, prediction))


# In[ ]:



