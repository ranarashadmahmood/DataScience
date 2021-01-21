#!/usr/bin/env python
# coding: utf-8

# # Variables used to reserve memory to store values
# #Data Types
# 
# #Integer

# # in Python, no need to declare datatypes like this
# int a = 0
# string a = 0
# float a = 0
# double a = 0
# 

# In[7]:


# Integers
age = 26
print(age)


# In[8]:


# Float, String, Bool
pi = 3.14159
c = 'c'
s = 'Rashad Mahmood'
q = not 'True'
print(age)
print(pi)
print(c)
print(s)
print(q)
_y = True
print(_y)
# Note Variable Assignment--->Left to Right---No need to declare its data type in python
print(type(age))
print(type(pi))
print(type(c))
print(type(s))
print(type(q))
print(type(_y))


# In[11]:


# a,b,c are different names given to the same object. However, assigning aa different object to one of 
#them will not affect others. variable always holds latest values assigned.
a, b, _ = 1, 2, 3
print(a, b)


# In[10]:


a = b = c = 10
print(a, b, c)


# In[13]:


b = 2000
print(a, b, c)


# # Complex

# In[28]:


x = 45+57j
print(x)
print(type(x))


# In[ ]:




