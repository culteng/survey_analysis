# subprocess.check_call([sys.executable, "-m", "pip", "install", 'seaborn'])
# python imports 
import os
import glob
import pandas as pd
import numpy as np
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
