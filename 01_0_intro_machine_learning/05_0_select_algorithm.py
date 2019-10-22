
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils.testing import all_estimators


# In[2]:

# 붓꽃 데이터 읽어 들이기
iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")


# In[3]:

iris_data.head()


# In[4]:

# 붓꽃 데이터를 레이블과 입력 데이터로 분리하기 
y = iris_data.loc[:,'class']
x = iris_data.loc[:,['sepal_length','sepal_width','petal_length','petal_width']]


# In[6]:

# 학습 전용과 테스트 전용 분리하기 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)


# In[11]:

# classifier 알고리즘 모두 추출하기--- (*1)
allAlgorithms = all_estimators(type_filter='classifier')


# In[14]:

for(name, algorithm) in allAlgorithms:
    try:
        # 각 알고리즘 객체 생성하기 --- (*2)
        clf = algorithm()

        # 학습하고 평가하기 --- (*3)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        print(name,"의 정답률 = " , accuracy_score(y_test, y_pred))
    except:
        pass


# In[ ]:



