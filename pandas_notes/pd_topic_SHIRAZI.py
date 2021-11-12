#!/usr/bin/env python
# coding: utf-8

# ## Provided by:
# 
# __Ahmad Shirazi__<br>
# __Shirazi@umich.edu__
# 

# ## Topic:
# 
# Using <font color=red>glob module</font> to create a data frame from multiple files, row wise:

# In[1]:


import pandas as pd
from glob import glob


# - We can read each dataframe from its own CSV file, combine them together and delet the original dataframes. <br>
# - This will need a lot of code and will be memory and time consuming.<br>
# - A better solution is to use the built in glob module.<br>
# - Lets make example dataframes in the next cell.<br>

# In[2]:


# making 3 dataframes as inputs for our example
data_age1 = pd.DataFrame({'Name':['Tom', 'Nick', 'Krish', 'Jack'],
        'Age':[17, 31, 28, 42]})

data_age2 = pd.DataFrame({'Name':['Kenn', 'Adam', 'Joe', 'Alex'],
        'Age':[20, 21, 19, 18]})

data_age3 = pd.DataFrame({'Name':['Martin', 'Jenifer', 'Roy', 'Mike'],
        'Age':[51, 30, 38, 25]})

# Saving dataframes as CSV files to be used as inputs for next example
data_age1.to_csv('data_age1.csv', index=False)
data_age2.to_csv('data_age2.csv', index=False)
data_age3.to_csv('data_age3.csv', index=False)


# - We pass a patern to the glob (including wildcard characters)
# - It will return the name of all files that match that pattern in the data subdirectory.
# - We can then use a generator expression to read each file and pass the results to the concat function.
# - It will concatenate the rows for us to a single dataframe.

# In[3]:


students_age_files = glob('data_age*.csv')
students_age_files


# In[4]:


pd.concat((pd.read_csv(file) for file in students_age_files), ignore_index=True)

