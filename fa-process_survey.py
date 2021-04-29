# python imports
import pandas as pd
import numpy as np
import glob
from scipy.stats import mannwhitneyu, kruskal

# project imports
import utils
import dictionaries

# use R for Horn's Parallel Analysis - https://w1ndy.medium.com/calling-r-libraries-from-python-5ffbf3c3e5a8
# def determine_factor_num( # https://github.com/yuany-pku/2017_CSIC5011/blob/master/slides/paran.R

    

def mann_whit(set1, set2):
    # https://machinelearningmastery.com/nonparametric-statistical-significance-tests-in-python/
    # mann-whitney is nonparametric statistical significance test for determining whether two independent samples were drawn from a population with the same distribution 
    stat_val, p_val = mannwhitneyu(set1, set2)
    print(stat_val, p_val)
    if p_val < .05:
        return stat_val, p_val
    else: return 0, 0
    

def krus_kal(*sets):
    # used to determine whether more than two independent samples have a different distribution. It can be thought of as the generalization of the Mann-Whitney U test
    # returns 1 if variance between samples is significant
    h_val, p_val = kruskal(*[set.values.ravel() for set in sets])
    print(h_val, p_val)
    if p_val < .05:
        return h_val, p_val
    else: return 0, 0


def main(args):
    filenames = glob.glob("data/cleaned/fake-gender.csv")
    df = utils.populate_df(filenames)

    df_likerts = df.loc[:, df.columns.str.startswith('lik_')]
    df_counts = pd.get_dummies(df_likerts.stack()).groupby(level=1).sum()
    
    mann_whit_res = pd.DataFrame()
    krus_kal_res = pd.DataFrame()
    
    for construct_n in range(1,7):  
        cols = [c for c in df_likerts.columns if c.startswith('lik_{}'.format(construct_n))]
        
        # test for difference across gender
        stat_val, p_val = mann_whit(
                df_likerts[cols].where(df.gender==0).values.ravel(), 
                df_likerts[cols].where(df.gender==1).values.ravel()
            )
        mann_whit_res = mann_whit_res.append({
            'construct_n': construct_n, 
            'stat_val': stat_val,
            'p_val': p_val}, ignore_index=True)
        
        # test for difference across ethnicity
        list_df_eth = [pd.DataFrame(v)[cols] # (2) turn each group by back into a DF & keep only likert columns
                        for k, v in 
                        df.groupby('ethnicity')] # (1) split df by 4 possible column values
        h_val, p_val = krus_kal(*list_df_eth)
        krus_kal_res = krus_kal_res.append({
            'construct_n': construct_n,
            'h_val': h_val,
            'p_val': p_val }, ignore_index=True)
    
    if (mann_whit_res.p_val > 0).any():
        mann_whit_min_idx = mann_whit_res[mann_whit_res.p_val > 0].p_val.idxmin()
        mann_sig = dictionaries.construct_dict[mann_whit_min_idx]
    else: mann_sig = 'None Found'
    
    if (krus_kal_res.h_val > 0).any():
        krus_kal_min_idx = krus_kal_res[krus_kal_res.h_val > 0].h_val.idxmin()
        krus_sig = dictionaries.construct_dict[krus_kal_min_idx]
    else: krus_sig = 'None Found'
    
    print('mann_whit results\n\t', mann_whit_res)
    print(
        'the construct with the most significant difference observed across gender by the Mann-Whitney U Test is:\n\t',
        mann_sig
        )
    print('krus results\n\t', krus_kal_res)
    print(
        'the construct with the most significant difference observed across ethnicities by the Kruskal-Wallis H-test is:\n\t',
        krus_sig
        )

    
if __name__ == '__main__':
    main(None)

