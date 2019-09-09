"""Project: Manual Strategy.                                                                                              
                                                                                              
Copyright 2018, Georgia Institute of Technology (Georgia Tech)                                                                                                
Atlanta, Georgia 30332                                                                                                
All Rights Reserved                                                                                               
                                                                                              
Template code for CS 4646/7646                                                                                                
                                                                                              
Georgia Tech asserts copyright ownership of this template and all derivative                                                                                              
works, including solutions to the projects assigned in this course. Students                                                                                              
and other users of this template code are advised not to share it with others                                                                                             
or to make it available on publicly viewable websites including repositories                                                                                              
such as github and gitlab.  This copyright statement should not be removed                                                                                                
or edited.                                                                                                
                                                                                              
We do grant permission to share solutions privately with non-students such                                                                                                
as potential employers. However, sharing with other current or future                                                                                             
students of CS 7646 is prohibited and subject to being investigated as a                                                                                              
GT honor code violation.                                                                                              
                                                                                              
-----do not edit anything above this line---                                                                
                                                                
  Student Name: ZHENG FU
  GT User ID: zfu66
  GT ID: 903369876                                                              
"""   

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from util import get_data, plot_data

def author():                                                               
    return 'zfu66' #Change this to your user ID 

def SMA(df, symbol, windows):
    return df[symbol].rolling(windows).mean()

def EMA(df, symbol, windows):
    return df[symbol].ewm(com=windows).mean()

def BollingerBands(df, symbol, windows, width):

    SMA_mean = df[symbol].rolling(windows).mean()
    SMA_std  = df[symbol].rolling(windows).std()
    SMA_std  = SMA_std.fillna(method='bfill')

    BB_upper_band = SMA_mean + width * SMA_std
    BB_lower_band = SMA_mean - width * SMA_std
    BB_value = (df[symbol] - SMA_mean) / (2 * SMA_std)

    return [SMA_mean, SMA_std, BB_upper_band, BB_lower_band, BB_value]

def Momentum(df, symbol, windows):
    return (df[symbol] / df[symbol].shift(windows)) - 1

def main():

    ############################
    #
    # Define parameters
    #
    ############################

    start_date = '2008-1-1'
    end_date = '2009-12-31'
    dates = pd.date_range(start_date,end_date)
    symbol = 'JPM'

    ############################
    #
    # Loading Stock Data
    #
    ############################
    
    loading_stock = get_data([symbol], dates, True)
    loading_stock  = loading_stock[[symbol]]
    loading_stock_noNA = loading_stock.fillna(method='ffill')
    loading_stock_noNA = loading_stock_noNA.fillna(method='bfill')
    loading_stock_noNA_normalized = loading_stock_noNA / loading_stock_noNA.ix[0,] 

    #print loading_stock_noNA_normalized
    
    ############################
    #
    # 20, 50, 200-days SMA
    #
    ############################

    SMA_20 = SMA(loading_stock_noNA_normalized, symbol, 20)
    SMA_50 = SMA(loading_stock_noNA_normalized, symbol, 50)
    SMA_200 = SMA(loading_stock_noNA_normalized, symbol, 200)

    #SMA_20 = SMA_20.fillna(method='bfill')
    #SMA_50 = SMA_50.fillna(method='bfill')
    #SMA_200 = SMA_200.fillna(method='bfill')

    #SMA_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'SMA_20days', 'SMA_50days', 'SMA_200days'])
    SMA_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'SMA_20days', 'SMA_50days'])

    SMA_df['JPM'] = loading_stock_noNA_normalized[symbol]
    SMA_df['SMA_20days'] = SMA_20
    SMA_df['SMA_50days'] = SMA_50
    #SMA_df['SMA_200days'] = SMA_200

    plt.figure(figsize=(12,8))
    ax = SMA_df.plot(title="Simple Moving Average of JPM Historical Data \n Dates = 2008-1-1 to 2009-12-31", fontsize=12)                                                                                                
    ax.set_xlabel("Dates")                                                                                             
    ax.set_ylabel("Normalized Price")
    plt.savefig("SMA.png")


    ############################
    #
    # 20, 50, 200-days EMA
    #
    ############################

    EMA_20 = EMA(loading_stock_noNA_normalized, symbol, 20)
    EMA_50 = EMA(loading_stock_noNA_normalized, symbol, 50)
    EMA_200 = EMA(loading_stock_noNA_normalized, symbol, 200)

    #EMA_20 = EMA_20.fillna(method='bfill')
    #EMA_50 = EMA_50.fillna(method='bfill')
    #EMA_200 = EMA_200.fillna(method='bfill')

    #EMA_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'EMA_20days', 'EMA_50days', 'EMA_200days'])
    EMA_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'EMA_20days', 'EMA_50days'])
    
    EMA_df['JPM'] = loading_stock_noNA_normalized[symbol]
    EMA_df['EMA_20days'] = EMA_20
    EMA_df['EMA_50days'] = EMA_50
    #EMA_df['EMA_200days'] = EMA_200

    plt.figure(figsize=(12,8))
    ax = EMA_df.plot(title="Exponential Moving Average of JPM Historical Data \n Dates = 2008-1-1 to 2009-12-31", fontsize=12)                                                                                                
    ax.set_xlabel("Dates")                                                                                             
    ax.set_ylabel("Normalized Price")
    plt.savefig("EMA.png")

    ############################
    #
    # 20-days Bollinger Bands
    #
    ############################

    [SMA_20, SMA_20_std, BB_upper_band, BB_lower_band, BB_value] = BollingerBands(loading_stock_noNA_normalized, symbol, 20, 2)

    #BB_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'SMA_20days', 'BB_value', 'BB_upper_band', 'BB_lower_band'])
    BB_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'SMA_20days', 'BB_upper_band', 'BB_lower_band'])
    
    BB_df['JPM'] = loading_stock_noNA_normalized[symbol]
    BB_df['SMA_20days'] = SMA_20
    #BB_df['BB_value']   = BB_value
    BB_df['BB_upper_band'] = BB_upper_band
    BB_df['BB_lower_band'] = BB_lower_band

    plt.figure(figsize=(12,8))
    ax = BB_df.plot(title="20-days Simple Moving Average with Bollinger Bands of JPM Historical Data \n Dates = 2008-1-1 to 2009-12-31", fontsize=12)                                                                                                
    ax.set_xlabel("Dates")                                                                                             
    ax.set_ylabel("Normalized Price")
    plt.savefig("BB.png")

    ############################
    #
    # 20-days Momentum
    #
    ############################

    momentum_20 = Momentum(loading_stock_noNA_normalized, symbol, 20)
    #momentum_20 = momentum_20.fillna(method='bfill')

    momentum_df = pd.DataFrame(index=loading_stock_noNA_normalized.index, columns=['JPM', 'SMA_20days', 'Momentum_20days'])
    
    momentum_df['JPM'] = loading_stock_noNA_normalized[symbol]
    momentum_df['SMA_20days'] = SMA_20
    momentum_df['Momentum_20days'] = momentum_20

    plt.figure(figsize=(12,8))
    ax = momentum_df.plot(title="20-days Simple Moving Average with Momentum of JPM Historical Data \n Dates = 2008-1-1 to 2009-12-31", fontsize=12)                                                                                                
    ax.set_xlabel("Dates")                                                                                             
    ax.set_ylabel("Normalized Price")
    plt.savefig("Momentum.png")

if __name__ == "__main__":
    main()