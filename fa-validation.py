# pip install factor_analyzer==0.2.3 

# python imports
import pandas as pd
import numpy as np
import glob
import prince  # https://github.com/MaxHalford/prince#multiple-factor-analysis-mfa
from factor_analyzer import FactorAnalyzer  # https://github.com/EducationalTestingService/factor_analyzer
from scipy.stats import mannwhitneyu, kruskal

# project imports
import utils

# use R for Horn's Parallel Analysis - https://w1ndy.medium.com/calling-r-libraries-from-python-5ffbf3c3e5a8
# def determine_factor_num( # https://github.com/yuany-pku/2017_CSIC5011/blob/master/slides/paran.R

gender_dict = {
    0:'male',
    1:'female'
    }



def analyze_factors(df):
    fa = FactorAnalyzer(n_factors=6, rotation=None)
    fa.fit(df)
    return np.round(fa.loadings_, 3)


def multi_fa(df, df_likerts):
    groups = {
            'Construct #{}'.format(no+1): [c for c in df_likerts.columns if c.startswith('lik_{}'.format(no+1))]
            for no in range(6)
            }

    mfa = prince.MFA(
         groups=groups,
         n_components=6, 
         n_iter=3,
         copy=True,
         check_input=True,
         engine='auto',
         random_state=42
     )
    mfa = mfa.fit(df_likerts)
    
    for name, fa in sorted(mfa.partial_factor_analysis_.items()):
        print('{} eigenvalues: {}'.format(name, fa.eigenvalues_))
        
    # print(mfa.partial_row_coordinates(df_likerts))
    
    ax = mfa.plot_row_coordinates(
         df_likerts,
         ax=None,
         figsize=(6, 6),
         x_component=0,
         y_component=1,
         labels=df_likerts.index,
         color_labels=[gender_dict[t] for t in df['gender']],
         ellipse_outline=False,
         ellipse_fill=True,
         show_points=True
    )
    ax.get_figure().savefig('mfa_row_coordinates.svg')


def main(args):
    filenames = glob.glob("data/cleaned/fake-gender.csv")
    df = utils.populate_df(filenames)

    df_likerts = df.loc[:, df.columns.str.startswith('lik_')]
    df_counts = pd.get_dummies(df_likerts.stack()).groupby(level=1).sum()
    
    af_res = analyze_factors(df_likerts)
    print(af_res)
    
if __name__ == '__main__':
    main(None)

