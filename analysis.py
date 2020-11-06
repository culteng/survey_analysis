# run analysis on cleaned survey results (csv output from cleaning.py)
# subprocess.check_call([sys.executable, "-m", "pip", "install", 'seaborn'])
# python imports 
import os
import glob
import pandas as pd
import numpy as np
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
    

def chart_likert(df):
    # likert_colors = ['white', 'firebrick','lightcoral','gainsboro','cornflowerblue', 'darkblue']
    fig = plot_likert.plot_counts(df, plot_likert.scales.agree)
    
    return fig


def chart_kde(df_kde):
    fig = sns.kdeplot(x=['scl_happy', 'scl_speakup', 'scl_mission_diverse', 'scl_ldrshp'], y='gender', kind="violin", data=df_kde)
    
    return fig


def chart_donut(df, col, color_lol):
    # https://towardsdatascience.com/donut-plot-with-matplotlib-python-be3451f22704
    df_percs = pd.DataFrame((df.groupby((col)).size())).reset_index()
    df_percs['percs'] = df_percs[0] / len(df)
    
    fig, axs = plt.subplots(1, len(df_percs))
        
    for index, row in df_percs.iterrows():
        print(row["percs"], index)
        scenario = row[col]
        percentage = int(round(row["percs"] * 100, 0))
        textLabel = scenario + ': ' + str(percentage) + '%'
        donut_sizes = [100 - percentage, percentage] # 
        axs[index].text(0.01, .8, textLabel, horizontalalignment='center', verticalalignment='center')
        axs[index].pie(donut_sizes, radius=.7, startangle=90, colors=color_lol[index],
                wedgeprops={"edgecolor": "white", 'linewidth': 1})
                
        circle = plt.Circle(xy=(0, 0), radius=0.35, facecolor='white')
        axs[index].add_patch(circle)
    
    return axs
    


def chart_box(df):
    fig, ax = plt.subplots(figsize=(10,5))
    sns.boxplot(x="variable", y="value", data=pd.melt(df))
    

def table_heat(df):
    dfstats = df[['mean', 'std']].sort_values(by=['mean'])
    mask = np.zeros((len(df), 2))
    mask[:,0] = True
    fig = sns.heatmap(dfstats, vmin=min(dfstats['std']), vmax=max(dfstats['std']), mask=mask, cmap='RdYlGn_r', linewidths=0.5, annot=True)
    
    for (j,i), label in np.ndenumerate(dfstats.values):
        if i == 0:
            fig.text(i+0.5, j+0.5, round(label, 1), 
                    fontdict=dict(ha='center',  va='center',
                                             color='black', fontsize=20))
                                             
    return fig


def main(args):
    filenames = glob.glob("data/cleaned/*.csv")
    df = populate_df(filenames)
    
    df_likerts = df.loc[:, df.columns.str.startswith('scl')]
    df_counts = pd.get_dummies(df_likerts.stack()).groupby(level=1).sum()
    df_counts.columns = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
    df_likert_stats = df_likerts.join(df_likerts.mean(1).rename('mean')).join(df_likerts.std(1).rename('std'))
    
    # heat table
    plt.clf()
    ax = table_heat(df_likert_stats.iloc[:5])
    plt.savefig('./output/heattable1.png', bbox_inches='tight')
    
    # create single likert plot. split by section? summary stats?
    plt.clf()
    ax = chart_likert(df_counts)
    plt.savefig('./output/plt_likert.png', bbox_inches='tight')
    
    # heatplot
    plt.clf()
    ax = chart_kde(df)
    ax.set_xticklabels(['male','female'])
    plt.savefig('./output/plt_violin.png', bbox_inches='tight')
    
    # gender donut plots
    plt.clf()
    ax = chart_donut(df, 'gender', [['#d5f6da', '#5cdb6f'], ['#BED6DD', '#11ADDB']])
    plt.savefig('./output/plt_donut_genders.jpg', bbox_inches='tight')


if __name__ == '__main__':
    main(sys.argv[1:])

