
# coding: utf-8

# In[17]:

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# In[18]:

wine_df = pd.read_csv('data/winequality-white.csv', sep=';')


# In[19]:

y = wine_df['quality']
x = wine_df.drop('quality', axis=1)


# ### 레이블 변경하기

# In[20]:

def categorize_label(x):
    if x <= 4:
        return 0
    elif x <= 7:
        return 1
    else:
        return 2


# In[21]:

y = y.apply(categorize_label)


# In[22]:

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[23]:

model = RandomForestClassifier()
model.fit(x_train, y_train)


# In[24]:

prediction = model.predict(x_test)


# In[25]:

print(classification_report(y_test, prediction))
print('정답률 = ', accuracy_score(y_test, prediction))


# In[ ]:



