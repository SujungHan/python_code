
# coding: utf-8

# In[2]:

import pandas as pd
from sklearn.utils.testing import all_estimators
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


# In[3]:

# 붓꽃 데이터 읽어 들이기
iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")


# In[4]:

# 붓꽃 데이터를 레이블과 입력 데이터로 분리하기 
y = iris_data.loc[:,'class']
x = iris_data.loc[:,['sepal_length','sepal_width','petal_length','petal_width']]


# In[5]:

# classifier 알고리즘 모두 추출하기--- (*1)
allAlgorithms = all_estimators(type_filter='classifier')


# In[6]:

# K-분할 크로스 밸리데이션 전용 객체 --- (*1)
kfold_cv = KFold(n_splits=5, shuffle=True)


# In[10]:

for(name, algorithm) in allAlgorithms:
    try:
        # 각 알고리즘 객체 생성하기
        clf = algorithm()

        # score 메서드를 가진 클래스를 대상으로 하기--- (*2)
        if hasattr(clf,"score"):
            # 크로스 밸리데이션--- (*3)
            scores = cross_val_score(clf, x, y, cv=kfold_cv)
            print(name,"의 정답률=")
            print(scores)
    except:
        pass


# In[ ]:



