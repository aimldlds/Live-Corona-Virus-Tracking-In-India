#!/usr/bin/env python
# coding: utf-8

# # Corona Virus Live Tracking For India
# 

# In[18]:


import pandas as pd
df = pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
df


# In[19]:


df=df.iloc[:-1,1:]


# In[20]:


df.head()


# In[21]:


df.tail()


# In[22]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
total_states = np.arange(len(df['state_name']))


# In[23]:


total_states


# In[24]:


df['active']


# In[25]:


max(df['positive'])


# # Total Positive Cases Based On States In India

# In[26]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['positive'], align='center', alpha=0.5,  
                 color=(1,0,0),  
                 edgecolor=(0.5,0.2,0.8))
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['positive'])+100) 
plt.xlabel('Positive Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# # Active Number Of Cases Based On States 

# In[27]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['new_active'], align='center', alpha=0.5,  
                 color=(1,0.5,0),  
                 edgecolor=(0.5,0.4,0.8)  )
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['new_active'])+10) 
plt.xlabel('Active Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# # Death Number Of Cases Based On States

# In[28]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['death'], align='center', alpha=0.5,  
                 color=(0,0,1),  
                 edgecolor=(0.5,0.4,0.8)  )
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['death'])+10) 
plt.xlabel('Death Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# # Stack All The  Columns In The Bar Chart 

# In[29]:


df.columns


# In[30]:


df=df.set_index('state_name',drop=True)


# In[31]:


df.head()


# In[32]:


df.tail()


# In[33]:


### Plotting Based on Stacking
df.plot.barh(stacked=True,figsize=(10,10)) 


# In[34]:


df1=df.iloc[:,1:3]
df1.plot.barh(color={"cured": "red", "positive": "green"},figsize=(10,10))


# In[ ]:




