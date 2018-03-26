
# coding: utf-8

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def caculator(a,*args): 
    if a=="加":
        return add(*args)
    elif a=="減":
        return subtract(*args)
    elif a=="乘":
        return multiply(*args)
    elif a=="除":
        return divide(*args)

