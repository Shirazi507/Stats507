#!/usr/bin/env python
# coding: utf-8

# # NOTE:
# The latest version of python 3.9 is used for this homework

# In[1]:


#pip install numpy


# In[2]:


#pip install tabulate


# # Answer to Question 0

# <span style="font-family:High Tower Text"> 
# 
# This is _question 0_ for <font color=red>problem set 1</font> of <font color=red>Stats 507</font>.
#     
# > <font size="4">Question 0 is about Markdown.</font>
# 
# The next question is about the __Fibonnaci sequence__, Fn=Fn−2+Fn−1. In part __a__ we will define a Python function <code>fib_rec()</code>.
# 
# Below is a …
# </span>
# 
# ### Level 3 Header
# <span style="font-family:High Tower Text"> 
# Next, we can make a bulleted list:
# 
# - Item 1
# 
#    - detail 1
#    - detail 2
# - Item 2
# 
# Finally, we can make an enumerated list:
# 
# 1. Item 1
# 2. Item 2
# 3. Item 3
#     
# </span>

# In[3]:


import math
import numpy as np
from tabulate import tabulate


# # Answer to Question 1

# In[4]:


def fib_rec(a,b,n):
    if n < 0:
        print("Plese enter a positive integer")
    else:
        if n==0:
            return a
        if n==1:
            return b
        else:
            return fib_rec(a,b,n-2)+fib_rec(a,b,n-1)


# In[5]:


fib_rec(0,1,25)


# In[6]:


def fib_for(a,b,n):
    if n < 0:
        print("Plese enter a positive integer")
    if n==0:
        fib= a
    if n==1:
        fib= b
    else:
        for i in range(2,n+1):
            fib = a+b
            a=b
            b=fib
            
    return(fib)            


# In[7]:


# %%time
# fib_for(0,1,1000)


# In[8]:


def fib_whl(a,b,n):
    if n < 0:
        print("Plese enter a positive integer")
    if n==0:
        fib= a
    if n==1:
        fib= b
    else:
        i=2
        while i <n+1:
            fib = a+b
            a=b
            b=fib
            i=i+1
            
    return(fib)


# In[9]:


# %%time
# fib_whl(0,1,1000)


# In[10]:


def fib_rnd(n):
    if n < 0:
        print("Plese enter a positive integer")
    return(round((1.6180339887**n)/(5**0.5)))


# In[11]:


# %%time
# fib_rnd(1000)


# In[12]:


def fib_flr(n):
    if n < 0:
        print("Plese enter a positive integer")
    return(math.floor((1.6180339887**n+0.5)/(5**0.5)))


# In[13]:


# %%time
# fib_flr(1000)


# In[14]:


import timeit


# In[15]:


from datetime import datetime
funcs= ["Recursive","Forloop","While loop","Round","Floor"]
a=0
b=1
n_fibo=1000
numit=5
for i in funcs:
#     if i=="Recursive":
#         b1=[i]
#         for j in range(numit):
#             start_time = datetime.now()
#             fib_rec(a,b,n_fibo)
#             end_time = datetime.now()
#             b1=np.hstack((b1,str(end_time - start_time)))
            
    
    
    if i=="Forloop":
        b2=[i]
        for j in range(numit):
            start_time = timeit.default_timer()
            fib_for(a,b,n_fibo)
            end_time = timeit.default_timer()
            b2=np.hstack((b2,str((end_time - start_time))))
    
    
    if i=="While loop":
        b3=[i]
        for j in range(numit):
            start_time = timeit.default_timer()
            fib_whl(a,b,n_fibo)
            end_time = timeit.default_timer()
            b3=np.hstack((b3,str(end_time - start_time)))
    
    
    if i=="Round":
        b4=[i]
        for j in range(numit):
            start_time = timeit.default_timer()
            fib_rnd(n_fibo)
            end_time = timeit.default_timer()
            b4=np.hstack((b4,str(end_time - start_time)))
    
    
    if i=="Floor":
        b5=[i]
        for j in range(numit):
            start_time = timeit.default_timer()
            fib_flr(n_fibo)
            end_time = timeit.default_timer()
            b5=np.hstack((b5,str(end_time - start_time)))


Time= np.vstack((b2,b3,b4,b5))
print(tabulate(Time.tolist(), headers=["1st iter", "2nd iter","3rd iter","4th iter","5th iter"]))


# ### Note:
# - The recursive process it took too much time beyond 100 ierations. <br>
#   For loop and while loop take significantly larger time than round and floor methods. <br>
#   Medianwise, looks like Forloop takes less time than Whileloop and Floor takes less time than Round.

# # Answer to Question 2

# In[16]:


def PascalsTriangleRow(n):
    print('Row '+str(n)+" of Pascal's triangle is:")
    print(1.0,end='')
    if n>0:
        pas0=1
        for k in range(1,n+1):
            pas=pas0*(n+1-k)/k
            pas0=pas
            print(end=', '+str(pas))


# In[17]:


PascalsTriangleRow(3)


# In[18]:


def PascalsTriangleRow(n):
    print((3*n)*" ",end='')
    print(1.0,end='')
    if n>0:
        for i in range(1,n+1):
            print("\n")
            print(3*(n-i)*" ",end='')
            print(1.0,end='')
            pas0=1
            for k in range(1,i+1):
                pas=pas0*(i+1-k)/k
                pas0=pas
                print(end=' , '+str(pas))
            


# In[19]:


PascalsTriangleRow(10)


# # Answer to Question 3

# In[21]:


pip install scipy  


# In[22]:


from scipy import stats


# In[23]:


# the format has to iclude EST,LWR,UPR and LVL for estimated value, lower and upper confidence 
# intervals and the confidence level, respectively. For example θ^ [XX%CI:(θ^L,θ^U)] must be written
# as EST[LVL%CI:(LWR,UPR)]

def Q4A(Array, CL, Format) :
    try:
        A=np.array(Array)
    except Exception:
        print("Array myst be a 1D Numpy array or convertable to a 1D Numpy array using np.array")
        
    est=np.mean(A)
    serr=np.std(A)/np.sqrt(len(A))
    alpha=(1-CL/100)/2
    zee=abs(stats.distributions.norm.ppf(alpha))
    lwr,upr=est-zee*serr , est+zee*serr
    d = dict();
    d['est'] = est
    d['lwr'] = lwr
    d['upr'] = upr
    d['level'] = CL
    
    if Format == None:
        return d
    else:
        if not all(x in Format for x in ["EST","LWR","UPR","LVL"]):
            print("Please refer to the format style mentioned above")
        else:
            Format=Format.replace("EST",str(est))
            Format=Format.replace("LWR",str(lwr))
            Format=Format.replace("UPR",str(upr))
            Format=Format.replace("LVL",str(CL))
            print(Format)
        
        


# In[24]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])
Q4A(Array,95,"the estimated value is EST with a LVL% confidence level of (LWR , UPR) ")


# In[25]:


Q4A(Array,95,None)


# In[26]:


Q4A(Array,95,None)["est"]


# In[27]:


# the format has to iclude EST,LWR,UPR and LVL for estimated value, lower and upper confidence 
# intervals and the confidence level, respectively. For example θ^ [XX%CI:(θ^L,θ^U)] must be written
# as EST[LVL%CI:(LWR,UPR)]

def Q4bi(Array, CL, Format) :
    try:
        A=np.array(Array)
    except Exception:
        print("Array myst be a 1D Numpy array or convertable to a 1D Numpy array using np.array")
    n=len(A)   
    est=np.mean(A)
    if np.min([est*n,(1-est)*n])<12 :
        print("the approximation is not adequate \n (either n*phat or (1-phat)*n is <= 12)")
    else:    
        serr=np.sqrt((est*(1-est))/n)
        alpha=(1-CL/100)/2
        zee=abs(stats.distributions.norm.ppf(alpha))
        lwr,upr=est-zee*serr , est+zee*serr
        d = dict();
        d['est'] = est
        d['lwr'] = lwr
        d['upr'] = upr
        d['level'] = CL

        if Format == None:
            return d
        else:
            if not all(x in Format for x in ["EST","LWR","UPR","LVL"]):
                print("Please refer to the format style mentioned above")
            else:
                Format=Format.replace("EST",str(est))
                Format=Format.replace("LWR",str(lwr))
                Format=Format.replace("UPR",str(upr))
                Format=Format.replace("LVL",str(CL))
                print(Format)
        


# In[28]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])
Q4bi(Array, 95, None)


# In[29]:


from scipy.stats import beta


# In[30]:


# the format has to iclude LWR,UPR and LVL for lower and upper confidence 
# intervals and the confidence level, respectively. For example θ^ [XX%CI:(θ^L,θ^U)] must be written
# as EST[LVL%CI:(LWR,UPR)]

def Q4bii(Array, CL, Format) :
    try:
        A=np.array(Array)
    except Exception:
        print("Array myst be a 1D Numpy array or convertable to a 1D Numpy array using np.array")
    n=len(A)   
    est=np.mean(A)
    x=np.sum(A)
    if np.min([est*n,(1-est)*n])<12 :
        print("the approximation is not adequate \n (either n*phat or (1-phat)*n is <= 12)")
    else:    
    #    serr=np.sqrt((est*(1-est))/n)
        alpha=(1-CL/100)
        zee=abs(stats.distributions.norm.ppf(alpha))
        lwr,upr=beta.ppf(alpha/2,x,n-x+1) , beta.ppf(1-alpha/2,x+1,n-x)
        d = dict();
        d['lwr'] = lwr
        d['upr'] = upr
        d['level'] = CL

        if Format == None:
            return d
        else:
            if not all(x in Format for x in ["LWR","UPR","LVL"]):
                print("Please refer to the format style mentioned above")
            else:
    #            Format=Format.replace("EST",str(est))
                Format=Format.replace("LWR",str(lwr))
                Format=Format.replace("UPR",str(upr))
                Format=Format.replace("LVL",str(CL))
                print(Format)


# In[31]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])
Q4bii(Array,95,None)


# In[32]:


# the format has to iclude LWR,UPR and LVL for lower and upper confidence 
# intervals and the confidence level, respectively. For example θ^ [XX%CI:(θ^L,θ^U)] must be written
# as EST[LVL%CI:(LWR,UPR)]

def Q4biii(Array, CL, Format) :
    try:
        A=np.array(Array)
    except Exception:
        print("Array myst be a 1D Numpy array or convertable to a 1D Numpy array using np.array")
    n=len(A) 
    est=np.mean(A)
    x=np.sum(A)
    if np.min([est*n,(1-est)*n])<12 :
        print("the approximation is not adequate \n (either n*phat or (1-phat)*n is <= 12)")
    else:    
    #    serr=np.sqrt((est*(1-est))/n)
        alpha=(1-CL/100)
    #    zee=abs(stats.distributions.norm.ppf(alpha))

        lwr=np.max([0,beta.ppf(alpha/2,x+0.5,n-x+0.5)])
        upr=np.min([beta.ppf(1-alpha/2,x+0.5,n-x+0.5),1])
        
        d = dict();
        d['lwr'] = lwr
        d['upr'] = upr
        d['level'] = CL

        if Format == None:
            return d
        else:
            if not all(x in Format for x in ["LWR","UPR","LVL"]):
                print("Please refer to the format style mentioned above")
            else:
    #            Format=Format.replace("EST",str(est))
                Format=Format.replace("LWR",str(lwr))
                Format=Format.replace("UPR",str(upr))
                Format=Format.replace("LVL",str(CL))
                print(Format)


# In[33]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])
Q4biii(Array,95,None)


# In[34]:


# the format has to iclude LWR,UPR and LVL for lower and upper confidence 
# intervals and the confidence level, respectively. For example θ^ [XX%CI:(θ^L,θ^U)] must be written
# as EST[LVL%CI:(LWR,UPR)]

def Q4biv(Array, CL, Format) :
    try:
        A=np.array(Array)
    except Exception:
        print("Array myst be a 1D Numpy array or convertable to a 1D Numpy array using np.array")
    n=len(A)   
    est=np.mean(A)
    x=np.sum(A)
    if np.min([est*n,(1-est)*n])<12 :
        print("the approximation is not adequate \n (either n*phat or (1-phat)*n is <= 12)")
    else:    
#        serr=np.sqrt((est*(1-est))/n)
        alpha=(1-CL/100)
        zee=abs(stats.distributions.norm.ppf(alpha))
        n_bar=n+zee**2
        p_bar=(x+zee**2/2)/n_bar

        lwr=p_bar-zee*np.sqrt(p_bar*(1-p_bar)/n_bar)
        upr=p_bar+zee*np.sqrt(p_bar*(1-p_bar)/n_bar)

        d = dict();
        d['lwr'] = lwr
        d['upr'] = upr
        d['level'] = CL
        
        if Format == None:
            return d
        else:
            if not all(x in Format for x in ["LWR","UPR","LVL"]):
                print("Please refer to the format style mentioned above")
            else:
    #            Format=Format.replace("EST",str(est))
                Format=Format.replace("LWR",str(lwr))
                Format=Format.replace("UPR",str(upr))
                Format=Format.replace("LVL",str(CL))
                print(Format)


# In[35]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])
Q4biv(Array,95,None)


# In[36]:


A=np.ones(42)
B=np.zeros(48)
Array=np.concatenate([A,B])

CL= [90,95,99]

Methods=["Standard Normal Dist","Binomial Normal Approx","Clopper-Pearson interval","Jeffrey’s interval","Agresti-Coull interval"]
ConfInt = np.zeros((5,6));

r=3

for i in Methods:
    
    if i=="Standard Normal Dist":
        c1=[i]
        for j in CL:
            d=Q4A(Array, j, None)
            c1=np.hstack((c1,"   ("+str(np.round(d["lwr"],r))+" , "+str(np.round(d["upr"],r))+" )   "))
        
    if i=="Binomial Normal Approx":
        c2=[i]
        for j in CL:
            d=Q4bi(Array, j, None)
            c2=np.hstack((c2,"   ("+str(np.round(d["lwr"],r))+" , "+str(np.round(d["upr"],r))+" )   "))

    if i=="Clopper-Pearson interval":
        c3=[i]
        for j in CL:
            d=Q4bii(Array, j, None)
            c3=np.hstack((c3,"   ("+str(np.round(d["lwr"],r))+" , "+str(np.round(d["upr"],r))+" )   "))

    if i=="Jeffrey’s interval":
        c4=[i]
        for j in CL:
            d=Q4biii(Array, j, None)
            c4=np.hstack((c4,"   ("+str(np.round(d["lwr"],r))+" , "+str(np.round(d["upr"],r))+" )   "))

    if i=="Agresti-Coull interval":
        c5=[i]
        for j in CL:
            d=Q4biv(Array, j, None)
            c5=np.hstack((c5,"   ("+str(np.round(d["lwr"],r))+" , "+str(np.round(d["upr"],r))+" )   "))
            
            
ConfInt= np.vstack((c1, c2,c3,c4,c5))
#print(ConfInt)
print(tabulate(ConfInt.tolist(), headers=["Methods", str(CL[0])+"% CI",str(CL[1])+"% CI",str(CL[2])+"% CI"]))


# - __Agresti-Coull interval is the narrowest and the most conservative for all three confidence levels.__

# In[ ]:




