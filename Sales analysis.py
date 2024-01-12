#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import iplot


# In[2]:


all_data=pd.read_csv("C:\\Users\\PC\\Downloads\\Project 1 - Sales Data Analysis-20240110T200611Z-001\\Project 1 - Sales Data Analysis\\Dataset MeriSKILL\\Sales Data.csv")
all_data.head()


# In[3]:


all_data.dtypes


# In[4]:


all_data.isnull().sum()


# In[5]:


all_data.head()


# In[6]:


all_data=all_data.dropna(how='all')
all_data.shape


# In[7]:


'04/19/2019 08:46'.split('/')[0]


# In[8]:


def month(x):
    return x.split('/')[0]


# In[9]:


all_data.dtypes


# In[10]:


all_data['Months']=all_data['Order Date'].apply(month)


# In[11]:


all_data.dtypes


# In[12]:


all_data['Month'].unique()


# In[13]:


Filter = all_data['Month'] == 'Order Date'
len(all_data[~Filter])


# In[14]:


all_data = all_data[~Filter]


# In[15]:


all_data.shape


# In[16]:


all_data.head()


# In[17]:


all_data["Month"]


# In[18]:


all_data.dtypes


# In[19]:


all_data['price Each'] = all_data['Price Each'].astype(float)


# In[20]:


all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(float)


# In[21]:


all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
all_data.head()


# In[22]:


all_data.groupby('Month')['Sales'].sum()


# In[23]:


'917 1st St, Dallas, TX 75001'.split(',')[1]


# In[24]:


def City(x):
    return x.split(',')[1]


# In[27]:


all_data['City'] = all_data['Purchase Address'].apply(City)


# In[28]:


all_data.groupby('City')['City'].count()


# In[36]:


city_counts = all_data.groupby('City')['City'].count()


# In[37]:


plt.bar(city_counts.index, city_counts)
plt.xticks(rotation='vertical')
plt.ylabel('Received Orders')
plt.xlabel('City Names')
plt.title('Orders Count by City')
plt.show()


# In[38]:


# all_data['Order Date'][0].dtype


# In[40]:


all_data['Hour'] = pd.to_datetime(all_data['Order Date']).dt.hour


# In[42]:


keys = []
hour = []


# In[43]:


for key, hour_df in all_data.groupby('Hour'):
    keys.append(key)
    hour.append(len(hour_df))


# In[44]:


all_data['Hour'] = pd.to_datetime(all_data['Order Date']).dt.hour


# In[45]:


plt.grid()
plt.plot(keys,hour)


# In[47]:


all_data.groupby('Product')['Quantity Ordered'].sum().plot(kind='bar')


# In[49]:


all_data.groupby('Product')['Price Each'].mean()


# In[50]:


products=all_data.groupby('Product')['Quantity Ordered'].sum().index


# In[53]:


quantity = all_data.groupby('Product')['Quantity Ordered'].sum()


# In[54]:


prices = all_data.groupby('Product')['Quantity Ordered'].mean()


# In[62]:


fig, ax1 = plt.subplots(figsize=(15, 8))
ax1.bar(products, quantity, color='g')
ax1.set_xlabel('Product', size=12)
ax1.set_ylabel('Quantity Ordered', color='g', size=12)
ax2 = ax1.twinx()
ax2.plot(products, prices, 'b-')
ax2.set_ylabel('Price Each', color='b', size=12)
ax1.set_xticks(products)
ax1.set_xticklabels(products, rotation='vertical', size=10)
plt.show()


# In[60]:


ax1.set_xticks(products)
ax1.set_xticklabels(products, rotation='vertical', size=10)


# In[64]:


all_data.shape


# In[66]:


df = all_data[all_data['Order ID'].duplicated(keep=False)]
df.head(15)


# In[68]:


df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))


# In[70]:


df.shape


# In[72]:


# Let's drop all duplicate Order ID
df2 = df.drop_duplicates(subset=['Order ID'])


# In[74]:


df2['Grouped'].value_counts().iloc[0:5].plot.pie(autopct='%1.1f%%', startangle=90)


# In[97]:


values = df2['Grouped'].value_counts().iloc[0]
labels = df2['Grouped'].value_counts().index[0]


# In[99]:


import plotly.graph_objects as go


# In[103]:


labels = df2['Grouped'].str.split(',')


# In[104]:


labels = [item for sublist in labels.dropna() for item in sublist]


# In[105]:


label_counts = pd.Series(labels).value_counts()


# In[106]:


trace = go.Pie(labels=label_counts.index, values=label_counts.values,
               hoverinfo='label+percent', textinfo='value',
               textfont=dict(size=25),
               pull=[0, 0, 0, 0.2, 0])


# In[107]:


layout = go.Layout(title='Pie Chart')


# In[108]:


fig = go.Figure(data=[trace], layout=layout)


# In[109]:


fig.show()


# In[ ]:




