#!/usr/bin/env python
# coding: utf-8

# ## Dictionary Practice with Dynamic Input

# In[12]:


phonebook = {"Ahmed":33324647879,"Rashad":3007866833}
print(phonebook)


# In[17]:


name = input('Enter your Name:..!')
Cell_number = input('Enter your Cell Number:..!')
#alternate_number = input('Enter your Alternate Number:..!')

phonebook[name] = Cell_number
#phonebook[name] = alternate_number
phonebook


# #### How to handle if i want to assign multiple numbers to one key? Please Answer

# In[18]:


print(phonebook)


# In[19]:


print(len(phonebook))


# In[20]:


type(phonebook)


# In[26]:


phonebook.keys()


# In[25]:


phonebook.values()


# In[28]:


phonebook.items()


# In[29]:


print(phonebook)


# In[ ]:




