''' This file contains necessary custom built functions '''
from random imoprt sample
import streamlit as st

def recommend(df, category):
    ''' Filter for Fund Recommendation '''
    categorized = df.loc[df['category']==category]
    sortinized = categorized.loc[df['sortino'] > 0.9 ]
    beta = sortinized.loc[(df['beta'] < 1)]
    sharpe = beta.loc[df['sharpe'] > 1 ]
    alpha = sharpe.loc[df['alpha'] > 0 ]
    alpha = alpha.sort_values(by='alpha', ascending=False)
    return alpha.head(15)

def options(df, category):
    ''' Function displays 3 randomly choosen rows from the dataset '''
    df1 = recommend(df, category)
    row_numbers = df1.index.to_list()
    try:
        random_rows = sample(row_numbers, 3)
    except:
        random_rows = row_numbers
    df2 = df.loc[random_rows]
    return df2

def options2(df, category):
    ''' Function displays 3 randomly choosen rows from the dataset '''
    df2 = df.loc[df['category'] == category]
    return df2
