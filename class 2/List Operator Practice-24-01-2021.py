#!/usr/bin/env python
# coding: utf-8

# ## LIST OPERATOR

# In[13]:


list_one = [1, 2, 3, 8.5, 9.5, 'Four', "Rana Rashad", 100]

print(list_one)
print(":.............")
print(list_one[0])
print(list_one[4])
print(list_one[5])
print(list_one[6])
print(list_one[0:5])
print(list_one[:])
print(list_one[1:7])
print(list_one[-3])


# ### Finding Index of List

# In[50]:


vowel_letters = ['a', 'e', 'i', 'o', 'u']
print(vowel_letters.index('a'))
print(vowel_letters.index('i'))
print(vowel_letters.index('u'))


# ### Nested List and List Operations

# In[16]:


integer_list = [0, 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
print(integer_list)


# In[35]:


integer_list.append(30)
print(integer_list)


# In[37]:


integer_list.insert(0,100)
print(integer_list)


# In[38]:


integer_list.remove(10)
print(integer_list)


# In[40]:


integer_list.extend([200,300,400])
print(integer_list)


# In[41]:


integer_list.reverse()
print(integer_list)


# In[42]:


integer_list.sort()
print(integer_list)


# In[45]:


print(len(integer_list))
print(max(integer_list))
print(min(integer_list))


# In[49]:


nested_list = [1,1,1,2,2,2,2,3,4,5,[6,7,8,8,9],10,11,12]
print(nested_list)
print(nested_list[10])
print(nested_list[10][2:4])


# In[ ]:




