#!/usr/bin/env python
# coding: utf-8

# Note: Pnadas started on thursday sept 16th <br>
# Talked about it on sept 21st

# ## Q0

# In[1]:


import numpy as np
import pandas as pd
from collections import defaultdict


# In[2]:


import timeit
from timeit import Timer


# In[3]:


def rnd():
    return np.random.randint(1, 9)


# In[4]:


sample_list=[]
for i in range (2000):
    sample_list.append(tuple(sorted((rnd(),rnd(),rnd()))))
np.shape(sample_list)


# In[5]:


op = []
for m in range(len(sample_list)):
    li = [sample_list[m]]
    for n in range(len(sample_list)):
        if (sample_list[m][0] == sample_list[n][0] and
                sample_list[m][2] != sample_list[n][2]):
            li.append(sample_list[n])
    op.append(sorted(li, key=lambda dd: dd[2], reverse=True)[0])
res = list(set(op))


# In[6]:


np.shape(res)


# #### Conclusion: 
# This code, among tuples with different 3rd element and similar first element, keeps the ones with largest 3rd element.  

# #### Possible improvements:
# 1. Iterate over values instead of iterating over indicies.
# 2. Use more meaningful variables, possibly with a comment to be more descriptive
# 3. Use consistent indatation
# 4. Run the code and make sure it is working (proofing)

# ## Q1

# In[7]:


def rnd(lw,hi):
    return np.random.randint(lw, hi)


def creat_tuple(n,k,lw,hi):
    sample=[]
    for i in range (n):
        sample.append(tuple(sorted([rnd(lw,hi) for j in range(k)])))
    return sample
    


# In[8]:


assert creat_tuple(1000,3,1,9)


# ## Q2
# Since the function finds the tuples with the top 3rd element, it is called "tops".

# In[9]:


def tops(idx1,idx2,sample_list):
    op = []
    for m in range(len(sample_list)):
        li = [sample_list[m]]
        for n in range(len(sample_list)):
            if (sample_list[m][idx1] == sample_list[n][idx1] and
                    sample_list[m][idx2] != sample_list[n][idx2]):
                li.append(sample_list[n])
        op.append(sorted(li, key=lambda dd: dd[idx2], reverse=True)[0])
    res = list(set(op))
    return res


# In[10]:


sample_list=creat_tuple(1000,3,1,10)


# In[11]:


res=tops(0,2,sample_list)
print(res[1:5])
np.shape(res)


# ## Q2-b
# The improved version of the previous code

# In[12]:


def tops_improved(idx1,idx2,sample_list):
    op = []
    for m in sample_list:
        li = [m]
        for n in sample_list:
            if (m[idx1] == n[idx1]) and (m[idx2] != n [idx2]):
                li.append(n)
        op.append(sorted(li, key=lambda dd: dd[idx2], reverse=True)[0])
    res3 = list(set(op))
    return res3


# In[13]:


res2=tops_improved(0,2,sample_list)
print(res2[1:5])
np.shape(res2)


# ## Q2-c
# Making some more fundumental changes:

# In[14]:



def tops_from_scratch(idx1,idx2,sample_list):
    op = []
    while sample_list!=[]:
        m = sample_list[0]
        li = [m]
        aa=m[idx2]
        for n in sample_list:
            if (m[idx1] == n[idx1]):
                aa=max(aa,n[idx2])
                li.append(n)
        li_tops=[x for x in li if x[idx2]==aa]    
        op=op+li_tops
        sample_list=[xx for xx in sample_list if not xx in li]
    return list(set(op))


# 
# __Note__: this code selects all elements with a certain tuple value (named list li, defined by idx1), <br>
# selects the ones with the topest tupple element definded by idx2 and then removes all elements <br>
# in li from the main list. So, it loops over each element twixce.
# 

# In[15]:


res3=tops_from_scratch (0,2,sample_list)
print(res3[1:5])
np.shape(res3)


# ## Q2d

# In[16]:


# min 15 of sept 16
  
print("size of sample_list is:" , np.shape(sample_list))

idx1=0
idx2=2


time_nda=defaultdict(list)
      
for f in [tops,tops_improved,tops_from_scratch]:
    t=Timer('f(idx1,idx2,sample_list)',globals={'f':f,'idx1':idx1,'idx2':idx2,'sample_list':sample_list})
    tm=t.repeat(repeat=10,number=10)
    time_nda['Function'].append(f.__name__)
    time_nda['min, s'].append(np.min(tm))
    time_nda['median, s'].append(np.median(tm))
    time_nda['mean, s'].append(np.mean(tm))


# In[17]:


time_nda=pd.DataFrame(time_nda)
for c, d in zip(time_nda.columns,time_nda.dtypes):
    if d==np.dtype('float64'):
        time_nda[c] = time_nda[c].map(lambda x: '%5.3f' %x)
print("For a sample size of ",str(np.shape(sample_list)),', the calculation time is:')
        
time_nda


# ## Q3
# 
# __Note:__ in this question, cohorts 1 to 4 belong to the years 2011-2012, 2013-2014, 2015-2016 and 2017-2018, respectively. <br>
# 
# The code for first dataset is intentionally left to be different from the one for the second data set. It is showing the flow of my work. However, the code for the second datset (for_loop) is preferred due to using less variables.

# In[18]:


cols = ['SEQN','RIDAGEYR','RIDRETH3','DMDEDUC2','DMDMARTL','RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']

col_names=['unique ids','age','race and ethnicity','education','marital status',
           'examination status','masked variance pseudo', 'masked variance pseudo-stratum','2 year MEC exam weight',
           '2 year interview weight']

df_1 = pd.read_sas(r'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT')[cols]
df_1.columns = col_names
df_1 ["cohort"] = np.ones(len(df_1))
df_1=df_1.convert_dtypes()

df_2 = pd.read_sas(r'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT')[cols]
df_2.columns = col_names
df_2 ["cohort"] = np.ones(len(df_2))*2
df_2=df_2.convert_dtypes()

df_3 = pd.read_sas(r'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT')[cols]
df_3.columns = col_names
df_3 ["cohort"] = np.ones(len(df_3))*3
df_3=df_3.convert_dtypes()

df_4 = pd.read_sas(r'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT')[cols]
df_4.columns = col_names
df_4 ["cohort"] = np.ones(len(df_4))*4
df_4=df_4.convert_dtypes()


# In[19]:


df_1.to_pickle(r"E:\UM\Hamechi\Stats507\Jupyter\HW2\DEMO_G.pkl")
df_2.to_pickle(r"E:\UM\Hamechi\Stats507\Jupyter\HW2\DEMO_H.pkl")
df_3.to_pickle(r"E:\UM\Hamechi\Stats507\Jupyter\HW2\DEMO_I.pkl")
df_4.to_pickle(r"E:\UM\Hamechi\Stats507\Jupyter\HW2\DEMO_J.pkl")


# In[20]:


num_cases1=[str(len(df_1)),str(len(df_2)),str(len(df_3)),str(len(df_4))]
sum_cases1=len(df_1)+len(df_2)+len(df_3)+len(df_4)
str1='The number of cases in each of the cohorts 1 to 4 for \n demographic data are:'
print(str1,num_cases1,', respectively')
print('\n total number of cases for demographic data are:',sum_cases1)


# In[22]:


cols=['OHX0'+str(i)+'TC' for i in range(1,10)]+['OHX'+str(i)+'TC' for i in range(10,33)]
cols=cols+['OHX0'+str(i)+'CTC' for i in range(2,10)]+['OHX'+str(i)+'CTC' for i in range(10,32)]
cols.remove('OHX16CTC')
cols.remove('OHX17CTC')

col_names=['tooth Count #'+str(i) for i in range(1,10)]+['tooth Count: #'+str(i) for i in range(10,33)]
col_names=col_names+[
    'coronal cavities #'+str(i) for i in range(2,10)]+['coronal cavities #'+str(i) for i in range(10,32)]

col_names.remove('coronal cavities #16')
col_names.remove('coronal cavities #17')

files=['G','H','I','J']
num_cases2=[]
sum_cases2=0

for i in range(1,5):
    read_path=r'https://wwwn.cdc.gov/Nchs/Nhanes/'+str(2010+(2*i-1))+'-'+str(2010+2*i)+'/OHXDEN_'+files[i-1]+'.XPT'
    df = pd.read_sas(read_path)[cols]
    df.columns = col_names
    df["cohort"] = np.ones(len(df))*i
    df=df.convert_dtypes()
    num_cases2.append(len(df))
    sum_cases2=sum_cases2+len(df)
    save_path=r"E:\UM\Hamechi\Stats507\Jupyter\HW2\OHXDEN_"+files[i-1]+".pkl"
    df.to_pickle(save_path)
str2='The number of cases in each of the cohorts 1 to 4 for \n oral health and dentition data are:'
print(str2,num_cases2,', respectively')
print('\n total number of cases for oral health and dentition data are:',sum_cases2)


# 
