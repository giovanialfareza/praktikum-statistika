#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data_reza = pd.read_csv('C:/Users/Lenovo/Downloads/titanic.csv')
print(data_reza)


# In[2]:


#mengambil data pada kolom tertentu
data1 = data_reza.loc[:,['Age','Pclass','Survived']]
print(data1)


# In[3]:


#memvisualisasikan data titanic
data2 = data_reza[['Age', 'Pclass', 'Survived']]
data2.plot(title='Persebaran Data', x='Age', y='Pclass', kind='scatter', c='Survived', colormap='Paired')


# In[4]:


#memanipulasi data jumlah penumpang berdasarkan group Pclass
data3 = data_reza[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Pclass')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)


# In[5]:


#memfilter data penumpang yang selamat berdasarkan pclass
data4 = data_reza[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Pclass'].loc[data_reza['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Pclass'].loc[data_reza['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())


# In[6]:


#memanipulasi data jumlah penumpang berdasarkan group Sex
data3 = data_reza[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
penumpang=data3.groupby('Sex')['Name'].nunique()
print('Jumlah Penumpang:\n', penumpang)


# In[7]:


#memfilter data penumpang yang selamat berdasarkan sex
data4 = data_reza[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]
notsurvivedpassanger=data4['Sex'].loc[data_reza['Survived']==0]
print('Penumpang yang tidak survived:\n', notsurvivedpassanger.value_counts())
survivedpassanger=data4['Sex'].loc[data_reza['Survived']==1]
print('\nPenumpang yang survived:\n', survivedpassanger.value_counts())


# In[ ]:




