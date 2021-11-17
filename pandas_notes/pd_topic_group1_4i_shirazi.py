# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# + [Create a df from multiple files](#Create-a-df-from-multiple-files) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Create a df from multiple files
# __Provided by: Ahmad Shirazi__ <br>
# __Email: Shirazi@umich.edu__

# import required libraries
import pandas as pd
from glob import glob

# - We can read each dataframe from its own CSV file, combine them together and delet the original dataframes. <br>
# - This will need a lot of code and will be memory and time consuming.<br>
# - A better solution is to use the built in glob module.<br>
# - Lets make example dataframes in the next cell.<br>


# +
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
# -

# - We pass a patern to the glob (including wildcard characters)
# - It will return the name of all files that match that pattern in the data subdirectory.
# - We can then use a generator expression to read each file and pass the results to the concat function.
# - It will concatenate the rows for us to a single dataframe.

students_age_files = glob('data_age*.csv')
pd.concat((pd.read_csv(file) for file in students_age_files), ignore_index=True)
