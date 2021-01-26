#!/usr/bin/env python
# coding: utf-8

# ## TUPLE 

# In[1]:


tple_one = (3.0, 5, 6.5, 75, 'Sixty Seven', 2, 3)
print(tple_one)


# ### Fetching

# In[18]:


print(tple_one[2])
print(tple_one[0:5])
print(tple_one[:6])
print(tple_one[-4])
print(tple_one[0])
print(type(tple_one[0]))
tple_one[0] = 30.45
print(tple_one[0])
print(tple_one + tple_one)


# ### index

# In[9]:


print(tple_one.index(75))
print(tple_one.index('Sixty Seven'))


# In[20]:


print(tple_one + tple_one)
print(max(tple_one))


# In[ ]:




