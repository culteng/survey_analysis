# run analysis on cleaned survey results (csv output from cleaning.py)
# python imports 
import os
import glob
import pandas as pd
import time


def populate_df(filenames: list, seperator: str =',', encoding: str = 'cp1252', quote_char: str = '"', quoting_lev: int =0):
    """populate DataFrame for hand-off to load_data()
    Parameters
    ----------
    filenames : list
        A list of files to be imported, output of utils.getfilesfromdir() can be used
    seperator : string
        define seperator used in .txt when not csv
    Returns
    ----------
    staging_df: pd.DataFrame 
        dataframe populated with content from imported files
    """
    
    start_time = time.time()
    
    file_count = 0
    total_files = len(filenames)
    inp_cols = []
        
    for filename in filenames:
        file_count += 1
        engine = 'c'
        if len(seperator) > 1: engine = 'python'
        read_df = pd.read_csv(r"{}".format(filename), sep=seperator, encoding=encoding, engine=engine, quotechar=quote_char, quoting=quoting_lev)
    
        # setup column list & df
        if file_count == 1:
            inp_cols = list(read_df.columns.values)
            staging_df = read_df.copy()
            read_df = None
    
        # check for new columns
        else:
            for col in read_df.columns:
                if col not in inp_cols:
                    inp_cols.append(col)
            staging_df = staging_df.append(read_df, ignore_index=True)
            read_df = None
                
    return staging_df


def main(args):
    filenames = glob.glob("data/cleaned/*.csv")
    df = populate_df(filenames)


if __name__ == '__main__':
    main(sys.argv[1:])


''' pp report
from pandas_profiling import ProfileReport
import numpy as np

filenames = glob.glob("data/cleaned/*.csv")
df = populate_df(filenames)
for i in range(100):
    randos = [2,np.NaN,np.random.random_integers(8,12),np.random.random_integers(0,1),np.random.choice(['b','w','l','a']),np.random.random_integers(1,5)]
    randos.extend(np.random.random_integers(1,5,19))
    randos.extend([np.NaN]*12)
    df.loc[len(df)] = randos

profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("your_report.html")

'''

''' waffle chart
import matplotlib.pyplot as plt
from pywaffle import Waffle

# randomized
data = dict(zip(['Asian', 'Latino', 'Black', 'White'],df.ethnicity.value_counts().values))
fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=data, 
    colors=("#dfed64", "#736464", "#000000", "#ffffff"),
    title={'label': 'Ethnicity Breakdown', 'loc': 'left'},
    labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
    icons='child', icon_size=18, 
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.savefig('./imgs/foo.png')

# pretend actual
data = dict(zip(['Asian', 'Latino', 'Black', 'White'],[3,32,51,15]))
fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=data, 
    colors=("#dfed64", "#736464", "#000000", "#ffffff"),
    title={'label': 'Ethnicity Breakdown', 'loc': 'left'},
    labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
    icons='child', icon_size=18, 
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.savefig('./imgs/foo2.png')

'''