
# coding: utf-8

# In[1]:

def Fibonacci(n):

# n is required to be an integer equal to or greater than one

    if n<=0:
        print 'Alert: n cannot be negative.'
    elif n==1:
        s=[0]*n    
        s[0]=1
        return s[n-1]
    elif n ==2:
        s=[0]*n    
        s[0]=1
        s[1]=1
        return s[n-1]
    else:
        s=[0]*n    
        s[0]=1
        s[1]=1
        for x in range(3,n+1):
            s[x-1]=s[x-2]+s[x-3]
        return s[n-1]


# In[2]:

Fibonacci(100)


# In[3]:

Fibonacci(10)


# In[4]:

Fibonacci(-5)


# In[ ]:



