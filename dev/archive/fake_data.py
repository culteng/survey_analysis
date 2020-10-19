import numpy as np
import glob
import pandas as pd
from pandas_profiling import ProfileReport

filenames = glob.glob("data/cleaned/*.csv")
df = populate_df(filenames)
for i in range(100):
    randos = [2,np.NaN,np.random.randint(8,12+1),np.random.randint(0,1+1),np.random.choice(['b','w','l','a']),np.random.randint(1,5+1)]
    randos.extend(np.random.randint(1,5+1,19))
    randos.extend([np.NaN]*12)
    df.loc[len(df)] = randos

df.to_csv('data/cleaned/fake.csv')

profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("your_report.html")

# visual for empties 
sns.heatmap(df.isnull(), cmap='viridis')
