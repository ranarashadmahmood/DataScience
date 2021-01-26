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


# In[2]:


set_one = {1,2,3,4,5,6,7,8,9,11,12,13,13,13,14,14}
set_two = {2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,8,8,9,9,9,10,1,1,11,11,12,12}
print(set_one)
print(set_two)
print(type(set_one))


# ### SET OPERATIONS

# In[9]:


set_one = {1,2,3,4,5,6,7,8,9,11,12,13,13,13,14,14}
set_two = {2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,8,8,10,1,1,11,11,12,12}

print(set_one.difference(set_two))
print(set_one.union(set_two))
print(set_one.intersection(set_two))
set_one.discard(14)
print(set_one)
set_one.remove(13)
print(set_one)


# In[ ]:




