#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import linear_model
import pandas as pd 
import math


# In[15]:


def predictingusingsklearn ( ):
    df = pd.read_csv("C:\\Users\\shaurya rakesh\\Desktop\\pythonML\\testscores")
    r = linearRegression()
    r.fit(df[['math']],df.cs)
    return r.coef_, r.intercept_

    


# In[21]:


def gradientdescent(x,y):
    learningrate=0.001
    iterations = 1000
    mcurr = bcurr = 0
    n = len(x)
    costprev= 0
    for i in range(itertions):
        ypredicted = mcurr*x + bcurr
        md=(2/n)*sum(x*(y-ypredicted))
        #to check how we are doing lets print cost it should be miniumum
        cost = (1/n)*sum([val**2 for val in (y-ypredicted)])
        
        bd=md=(2/n)*sum(x*(y-ypredicted))
        mcurr = mcurr - learningrate * md
        bcurr = bcurr - learningrate * bd
        costprev = cost
        print ("m {}, b {}, cost {}, iteration {}".format(mcurr,bcurr,cost, i))
        return mcurr, bcurr 
if mcurr == 0 :
    
        
    df = pd.read_csv("C:\\Users\\shaurya rakesh\\Desktop\\pythonML\\testscores")
    x = np.array(df.math)
    y = np.array(df.cs)
    m, b = gradient_descent(x,y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn = predict_using_sklean()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))


# In[ ]:




