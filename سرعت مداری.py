#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("!سلام ،جهان")
#Numerical Python in Astronomy and Astrophysics A Practical Guide to Astrophysical Problem Solving (Undergraduate Lecture Notes in Physics) by Wolfram Schmidt, Marcel Völschow 


# In[4]:


radius = 1.496e8# شعاع مداری کیلومتر
period = 3.156e7# s دوره مداری
# محاسبه سرعت مداری
velocity = 2*3.14159*radius/period
print(velocity)


# In[10]:


print("سرعت مداری =", velocity, "km/s")


# In[8]:


print("سرعت مداری = {:5.2f} km/s".format(velocity))


# In[9]:


radius = 10*radius
print("سرعت مداری جدید = {:.3e} km".format(radius))


# In[11]:


# calculate period in s from radius in km (Kepler’s third law)
period = 2*3.14159 * (6.674e-11*1.989e30)**(-1/2) * (1e3*radius)**(3/2)
# print period in yr
print("new orbital period = {:.1f} yr".format(period/3.156e7))
velocity = 2*3.14159*radius/period
print("new orbital velocity = {:.2f} km/s".format(velocity))


# In[13]:


sum = 0 # initialization
n = 100 # number of iterations
for k in range(1,n+1): # k running from 1 to n
    sum = sum + k
# iteration of sum
print("Sum =", sum)


# In[19]:


# how many numbers are computed
n_max = 10
# initialize variables
F_prev = 0 # 0. number
F = 1
# 1. number
# compute sequence of Fibonacci numbers
for n in range(1,n_max+1):
    print("{:d}. Fibonacci number = {:d}".format(n,F))
# next number is sum of F and the previous number
    F_next = F + F_prev
    # prepare next iteration
    F_prev = F # first reset F_prev
    F = F_next # then assign next number to F


# In[21]:


# initialize variables
F_prev = 0 # 0. number
n,F = 1,1 # 1. number
# compute sequence of Fibonacci numbers smaller than 1000
while F < 1000:
    print("{:d}. Fibonacci number = {:d}".format(n,F))
    # next number is sum of F and the previous number
    F_next = F + F_prev
    # prepare next iteration
    F_prev = F # first reset F_prev
    F = F_next # then assign next number to F
    n += 1
    # increment counter


# In[25]:


# initialize variables
F_prev = 0 # 0. number
F = 1
# 1. number
n_even = 0
n_odd = 0
# compute sequence of Fibonacci numbers smaller than 1000
while F < 1000:
    # next number is sum of F and the previous number
    F_next = F + F_prev
    # prepare next iteration
    F_prev = F # first reset F_prev
    F = F_next # then assign next number to F
    # test if F is even (divisible by two) or odd
    if F%2 == 0:
        n_even += 1
    else:
        n_odd += 1
print("Found {:d} even and {:d} odd Fibonacci numbers".    format(n_even,n_odd))


# In[26]:


import scipy.constants
print(scipy.constants.gravitational_constant)


# In[ ]:




