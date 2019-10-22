
# coding: utf-8

# ### 필요 라이브러리 임포트

# In[3]:

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


# ### 학습데이터와 레이블 만들기

# In[5]:

train_data = [[0,0], [0,1], [1,0], [1,1]]
train_label = [0, 0, 0, 1]


# ### 알고리즘 선택

# In[6]:

model = LinearSVC()


# ### 학습, Train

# In[7]:

model.fit(train_data, train_label)


# ### 테스트 데이터로 예측하기

# In[11]:

test_data = [[1,0]]
prediction = model.predict(test_data)
prediction


# ### 예측 결과 평가

# In[12]:

print(test_data, '의 예측결과:', prediction)
print('정답률 = ', accuracy_score([0], prediction))


# In[ ]:



