#!/usr/bin/env python
# coding: utf-8

# Monte Carlo Simulation for Random Walk
# 
# Objective: We have another random walk with a 60% chance of +1 and a 40% chance of -1. We are starting from 0. What is the probability of reaching 5 before reaching -3?

# In[ ]:





# In[48]:


#one simulation

start=0
position=[start]

#define probability matrix of +1 and -1

prob=[0.6,0.4]

rand=np.random.random(100)
up=rand > prob[1]
down=rand < prob[1]

for i in rand:
    if i > prob[1]:
        start += 1 
    else:
        start -=1
    position.append(start)

plt.plot(position)
plt.show()


# In[42]:


#multiple simulations

import random
import numpy as np
import matplotlib.pyplot as plt

five=0
before3=0

for j in range(1000):
    start=0
    position=[start]
#define probability matrix of +1 and -1
    prob=[0.6,0.4]
    rand=np.random.random(1000)
    for i in rand:
        if i > prob[1]:
            start += 1 
        else:
            start -= 1
        position.append(start)
    if -3 in position and 5 in position:
        if position.index(-3)>position.index(5):
            before3=before3+1
    if 5 in position and -3 not in position:
            five=five+1
    count=before3+five
    plt.plot(position)
plt.show()
print(count)

#plt.plot(position)
#plt.show()


# In[ ]:





# In[43]:


probability=count/1000
probability

