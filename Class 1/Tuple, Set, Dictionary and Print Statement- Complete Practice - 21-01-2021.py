#!/usr/bin/env python
# coding: utf-8

# ## Tuple

# ##### Tuples - Commonly used for small collections of values that will not need to change. Tuple must have one member at least.

# In[8]:


a = (1, 2, 3, 4, 5)
c = (1,)
c1 = 1,
c2 = tuple(['one member'])
print(a)
print(a[1])
print(a[-1])
print(type(a))
print(type(c))
print(type(c1))
print(type(c2))


# ## Set

# In[ ]:


# A set is collection of ordered elements with No-Repitition, without insertion 
# order but sorted. For larger data, its much faster to do search in SET instead of LIST


# In[12]:


set_one = {1,2,3,4,5,6,5,6,5,6,5}
print(set_one)
print(type(set_one))


# In[20]:


#Already defined List can also be used for Set
my_list = [1,2,3,4,5,6,67]
my_new_set = set(my_list)
number = input("Enter Number ::")
if number in my_new_set:
    print(number)
#print(my_list)
#print(my_new_set)


# In[23]:


first_names = {'Adam', 'Bob', 'Charlie'}
name = input("Enter Name ::")
if name in first_names:
    print(name)


# ## Dictionary

# In[24]:


# In python, it is key-value pair, while each pair is separated using comma 
# and key-value pair using colon

state_capitals = {'Arkansas':'Little Rock',
                 'Colorado':'Denver',
                 'California':'Sacramento',
                 'Georgia':'Atlanta'
                 }
ca_capitals = state_capitals ['California']
print(ca_capitals)


# In[27]:


#use of iteration

for k in state_capitals.keys():
    print('{} is the Capital of {}'.format(state_capitals[k], k))


# ## Print Statements

# In[32]:


Name = "Rashad Mahmood Khan"
Age = 30
Weight = 87.00
print("My Name is {} and my age {} while my weight is {}".format(Name,Age,Weight))

print("My Name is %s and my age %d while my weight is %f" %(Name,Age,Weight))

print(f"My Name is {Name} and my age {Age} while my weight is {Weight}")


# In[ ]:




