#!/usr/bin/env python
# coding: utf-8

# 1. Write a program that prints "Hello, World!" to the console

# In[3]:


'Hello,World!'


# **Variables and Data Types**

# Declare a variable named is_true and assign it a boolean value.

# In[13]:


is_true=True
type(is_true)


# Create a variable named my_list and assign it a list of your favorite colors.

# In[15]:


my_list = ['pink','orange','white','black']
type(my_list) 


# **Basic Operations**

# Declare two variables, x and y, with values 10 and 3. Perform the following operations:
# Addition of x and y.
# Subtraction of y from x.
# Multiplication of x and y.
# Division of x by y.
# Exponentiation of x to the power of y.

# In[28]:


x=10
y=3
#Addition of x,y
z=x+y
print('Addition of 10,3 = ',z)
#Subtraction of y from x
c=x-y
print('Subtraction of 3 from 10 = ',c)
#Multiplication of x and y
a=x*y
print('Multiplication of 10 and 3 = ',a)
#Division of x by y
b=x/y
print('Division of 10 by 3 = ',b)
#Exponentiation of x to the power of y
d=x**y
print('Exponentiation of 10 to the power of 3 = ',d)


# **User Input and Operations**

# Take user input for two numbers and perform addition on them.

# In[31]:


a=int(input("Enter first Number = "))
b=int(input("Enter Second Number = "))
c=a+b
print(f'{a} + {b} = {c}')


# Take user input for a floating-point number and round it to the nearest integer.

# In[9]:


a=input("Enter Floating-Point Number = ")
a=float(a)
round_of_a =round(a)
print(f'Round of {a} is {round_of_a}')



# **Type Conversion**

# Convert the variable x (previously declared) to a string and print its type

# In[13]:


x=10
converting_to_string = str(x)
type(converting_to_string)


# Convert the string "25" to an integer and print its type.

# In[15]:


string="25"
converting_to_int = int(string)
type(converting_to_int)


# Convert the float pi to an integer.

# In[18]:


pi=2.4
converting_to_int = int(pi)
type(converting_to_int)


# **Combining Strings**

# Declare two string variables, first_name and last_name, and concatenate them to form a full name.

# In[27]:


first_name=input("First Name : ")
last_name=input("Last Name : ")
Full_Name=first_name+' '+last_name
print("Full Name : ",Full_Name)


# Create a string that includes a variable in the middle of a sentence (e.g., "I am {} years old").

# In[29]:


a=input("Enter Your Name : ")
print(f'My Name is {a}')


# **Increment and Decrement**

# 1.Declare a variable count and initialize it to 0.
# 
# 2.Increment the value of count by 1.
# 
# 3.Decrement the value of count by 2.

# In[31]:


count=0
count+=1
count-=2
print(count)


# **Math Module**

# Import the math module.

# In[32]:


import math


# Use the math.sqrt() function to find the square root of a number.

# In[35]:


Number=int(input("Enter Number for square root = "))
square_root=math.sqrt(Number)
print(f'Square root of given number is {square_root}')
    
    


# **Comparisons**

# Compare two variables and print whether they are equal.

# In[38]:


a=10
b=10
if a==b:
    print("Both Variables as same")
else:
    print("Different Variables")
    


# Compare two variables and print whether one is greater than the other.

# In[41]:


a=int(input('Enter First Number = '))
b=int(input('Enter second Number = '))
if a>b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is less than {b}')



# **Compound Assignment Operators**

# Use compound assignment operators to increment a variable by 5 and then multiply it by 2.

# In[43]:


num=2
num+=5
b=num*2
b


# In[ ]:




