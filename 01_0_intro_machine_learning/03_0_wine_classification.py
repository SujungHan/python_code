
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# In[2]:

wine_df = pd.read_csv('data/winequality-white.csv', sep=';')


# In[3]:

y = wine_df['quality']
x = wine_df.drop('quality', axis=1)


# In[4]:

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[5]:

model = RandomForestClassifier()
model.fit(x_train, y_train)


# In[6]:

prediction = model.predict(x_test)


# In[7]:

print(classification_report(y_test, prediction))
print('정답률 = ', accuracy_score(y_test, prediction))


# In[ ]:



