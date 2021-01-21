#!/usr/bin/env python
# coding: utf-8

# ## Complete List Tasks

# In[ ]:


#List is collection of an ordered collection of valid python values.
#list can be Empty, mutable, cn be nested


# In[18]:


g = [1,2,2,2,3,4,5,6,7,8,9] #Integer List
emp_list = [] #Empty List
print(emp_list)
str_list = ['Ahmed', 'Hassan', 'Yousaf', 'Rashad'] #String_List
mix_list = [1, 2.356, 'Ahmed', 'Hassan'] # Mixed_List
nested_list = [4,5,6,7,8,9,['Yousaf', 'Rashad'], 10, 786, 2000]
print(str_list)
print(mix_list)
print(nested_list)
print(g)
print(g[6])
print(type(g))
print(type(str_list))
print(type(mix_list))
print(type(nested_list))


# In[6]:


x = y = [7,8,9]
print(x, y)
#modify an element of list
x = [13, 8, 9]
print(x, y)
#modify an element of list
x[1] = 786
print(x, y)


# In[28]:


#List Operations
names = ['Alice', 'Bob', 'Craig', 'Eric']
print(names)
print(names[-1])
print(names[-3])

#Change values iin list
names[0] = 'Micheal'
print(names)

#Append Operation L.append(object)
names.append('Sia')
print(names)

#Insert Operation L.insert(index, object)
names.insert(1,'John')
print(names)

#Remove Operation L.remove(Value)
names.remove('Bob')
print(names)


# In[35]:


#Finding Index in the list
names.index('Craig')

#Length of the list
len(names)

#count occurances of any item
g.count(2)

#List Reversal
g.reverse()
print(g)

