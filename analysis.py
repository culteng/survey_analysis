# run analysis on cleaned survey results (csv output from cleaning.py)
# subprocess.check_call([sys.executable, "-m", "pip", "install", 'seaborn'])
# python imports 
import os
import glob
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
from pywaffle import Waffle
import plot_likert


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


def chart_waffle(df_ser, labels = None):
    '''
    Parameters
    ----------
    df_ser : pandas series
        data to be grouped; should have ser.name intact from df
    labels : list of strings
        labels to be used for groups. if None, values in series will be used
    
    Returns
    ----------
    fig object to be saved or displayed
    
    
    Example usage
    -------------
    fig = chart_waffle(df.column_name, ['First Item', 'Second Item'])
    plt.savefig('./imgs/foo.png')
    '''
    df_ser = df_ser.sort_values()
    if labels is None:
        labels = list(df_ser.value_counts().index)
    
    data = dict(zip(labels, df_ser.value_counts().values))
    fig = plt.figure(
        FigureClass=Waffle, 
        rows=5, 
        values=data, 
        colors=("#dfed64", "#736464", "#000000", "#ffffff"),
        title={'label': '{} Breakdown'.format(df_ser.name).format, 'loc': 'left'},
        labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
        icons='child', icon_size=18, 
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
    )
    fig.gca().set_facecolor('#EEEEEE')
    fig.set_facecolor('#EEEEEE')
    
    return fig
    

def chart_likert(df_likerts):
    # likert_colors = ['white', 'firebrick','lightcoral','gainsboro','cornflowerblue', 'darkblue']
    df_counts = pd.get_dummies(df_likerts.stack()).groupby(level=1).sum()
    df_counts.columns = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
    fig = plot_likert.plot_counts(df_counts, plot_likert.scales.agree)
    
    return fig


def main(args):
    filenames = glob.glob("data/cleaned/*.csv")
    df = populate_df(filenames)
    
    #create single likert plot. split by section? summary stats?
    df_likerts = df.loc[:, df.columns.str.startswith('scl')]
    ax = chart_likert(df_likerts)
    plt.savefig('likert1.png', bbox_inches='tight')


if __name__ == '__main__':
    main(sys.argv[1:])

