import numpy as np
def gradient_descent(x,y):
    iterations = 1000
    n = len(x)
    mcurr=bcurr=0
    learningrate=0.001


    for i in range(iterations):
        ypredicted = mcurr*x + bcurr
        md=(2/n)*sum(x*(y-ypredicted))
        #to check how we are doing lets print cost it should be miniumum
        cost = (1/n)*sum([val**2 for val in (y-ypredicted)])
        
        bd=md=(2/n)*sum(x*(y-ypredicted))
        mcurr = mcurr - learningrate * md
        bcurr = bcurr - learningrate * bd
        print("m{},  b  {}, iteratio  {},cost {} ".format(mcurr,bcurr,i,cost))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)
