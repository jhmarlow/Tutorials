#%%
# First time using Interactive Shell in VScode

#%%
# Install a pip package in the current Jupyter kernel

# import sys
# !{sys.executable} -m pip install matplotlib

#%%
# Load data 
import pandas as pd
df = pd.read_csv('/Users/jacobmarlow/Documents/Data Analytics/SampleData/business-price-indexes-march-2019-quarter-csv.csv')
df.head()

#%%
import matplotlib.pyplot as plt
plt.plot(df['Period'].values[0:100], df['Data_value'].values[0:100], 'x')
plt.title('NZ Business Data')
plt.xlabel('Period')
plt.ylabel('Data Value')

#%%
