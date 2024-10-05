#!/usr/bin/env python
# coding: utf-8

# ### Calculator

# In[37]:


def get_number(number):
    
  while True:
    operand = input('Number ' + str(number) + ': ')
    try:
        return float(operand)
    except:
        print('Math Error')


# In[38]:


operand1 = get_number(1)


# In[39]:


operand2 = get_number(2)


# In[40]:


sign = input('Sign :')


# In[41]:


print(str(operand1) +" "+sign+" "+ str(operand2))


# In[45]:


result = 0

if sign == '+':
    result = float(operand1) + float(operand2)
elif sign == '-':
    result = float(operand1) - float(operand2)
elif sign == '*':
    result = float(operand1) * float(operand2)
elif sign == '/':
    if float(operand2) != 0:
        result = float(operand1) / float(operand2)
    else:
        print('Math Error')
print(str(operand1) +" "+sign+" "+ str(operand2)+" "+'='+" "+str(result))


# In[ ]:




