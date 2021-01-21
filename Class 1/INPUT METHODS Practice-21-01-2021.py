#!/usr/bin/env python
# coding: utf-8

# # Input Methods

# In[3]:


a = 4
b = 3
print(a + b)


# ## By default, Python took input as string...so we need to convert them as per requirements

# In[ ]:


First_Number = input("Enter First Number ::")
Second_Number = input("Enter Second Number ::")
print(First_Number + Second_Number)
print(type(First_Number + Second_Number))


# In[6]:


# As we are taking integers, so we have to convert string into integers

First_Number = int(input("Enter First Number ::"))
Second_Number = int(input("Enter Second Number ::"))
print(First_Number + Second_Number)
print(type(First_Number + Second_Number))


# In[7]:


# for decimal input, we would change into float or double
First_Number = float(input("Enter First Number ::"))
Second_Number = float(input("Enter Second Number ::"))
print(First_Number + Second_Number)
print(type(First_Number + Second_Number))


# In[ ]:




