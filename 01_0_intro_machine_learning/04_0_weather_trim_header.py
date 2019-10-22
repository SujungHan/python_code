
# coding: utf-8

# ### CSV 파일을 한줄 씩 읽어들이기

# In[1]:

with open('data/weather-data.csv', encoding='EUC-KR') as file:
    lines = file.readlines()


# In[3]:

# 기존의 데이터를 분리해서 가공하기 ---(*2)
lines = ["연,월,일,기온,품질,균질\n"] + lines[5:]
lines = map(lambda v: v.replace('/', ','), lines)
result = "".join(lines).strip()
print(result)


# In[7]:

# 결과를 파일에 출력하기 ---(*3)
with open('data/tem10y.csv', "w", encoding="utf-8") as file:
    file.write(result)
    print("saved.")


# In[ ]:



