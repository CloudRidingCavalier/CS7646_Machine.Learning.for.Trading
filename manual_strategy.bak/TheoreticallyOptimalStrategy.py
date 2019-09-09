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
import sys
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from util import get_data, plot_data
from marketsimcode import compute_portvals, compute_portvals_stats

def testPolicy(symbol="JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv=100000):

    prices = get_data([symbol], pd.date_range(sd, ed), True)
    prices = prices.drop(['SPY'], axis=1)
        
    prices['daily_diff'] = prices.shift(-1) - prices
    prices['daily_diff'] = prices['daily_diff'] / abs(prices['daily_diff']) 
    prices.fillna(method='bfill', inplace=True) 

    #print prices.head(10)
    
    trades = pd.DataFrame(data = 0, index = prices.index, columns = {symbol})
    trades[symbol] = prices.ix[0,-1] * 1000

    previous_position = prices.ix[0,-1]
    
    for i,j in prices[1:].iterrows():
        if j['daily_diff'] == previous_position:
            trades.loc[i] = 0
        else:
            trades.loc[i] = previous_position * -2000
            previous_position = j['daily_diff']
    
    trades.ix[-1] = 0

    return(trades)

def Benchmark(symbol="JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv=100000):

    prices = get_data([symbol], pd.date_range(sd, ed), True)
    prices = prices.drop(['SPY'], axis=1)
    share = [1000,-1000]
    dates = [prices.index[0], prices.index[-1]]
    benchmark_df = pd.DataFrame(data = share, index = dates, columns = {symbol})
    return benchmark_df

def author():                                                               
    return 'zfu66' #Change this to your user ID    

def main(start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31)):
    
    df_trades = testPolicy(symbol="JPM", sd=start_date, ed=end_date, sv=100000)
    #print df_trades.head(10)
    TOS_portval = compute_portvals(df_trades, start_val = 100000, commission=0.0, impact=0.0, symbol="JPM")
    TOS_portval_stats = compute_portvals_stats(TOS_portval)

    df_benchmark = Benchmark(symbol="JPM", sd=start_date, ed=end_date, sv=100000)
    
    Benchmark_portval = compute_portvals(df_benchmark, start_val = 100000, commission=0.0, impact=0.0, symbol="JPM")
    #print Benchmark_portval
    Benchmark_portval_stats = compute_portvals_stats(Benchmark_portval)
    #print df_benchmark

                                                                                              
    print "Date Range: {} to {}".format(start_date, end_date)                                                                                             
    print                                                                                             
    print "Sharpe Ratio of TOS: {}".format(TOS_portval_stats[0])                                                                                              
    print "Sharpe Ratio of Benchmark: {}".format(Benchmark_portval_stats[0])                                                                                              
    print                                                                                             
    print "Cumulative Return of TOS: {}".format(TOS_portval_stats[1])                                                                                             
    print "Cumulative Return of Benchmark: {}".format(Benchmark_portval_stats[1])                                                                                             
    print
    print "Average Daily Return of TOS: {}".format(TOS_portval_stats[2])                                                                                              
    print "Average Daily Return of Benchmark: {}".format(Benchmark_portval_stats[2])                                                                                              
    print                                                                                                     
    print "Standard Deviation of TOS: {}".format(TOS_portval_stats[3])                                                                                                
    print "Standard Deviation of Benchmark: {}".format(Benchmark_portval_stats[3])                                                                                                
    print                                                                                                                                                                             
    print "Final Portfolio Value TOS: {}".format(TOS_portval[-1]) 
    print "Final Portfolio Value Benchmark: {}".format(Benchmark_portval[-1])   

    portfolio_df = pd.DataFrame(index=TOS_portval.index, columns=['Theoretically Optimal Strategy', 'Benchmark'])
    
    portfolio_df['Theoretically Optimal Strategy'] = TOS_portval / TOS_portval[0]
    portfolio_df['Benchmark'] = Benchmark_portval / Benchmark_portval[0]

    plt.figure(figsize=(12,8))
    ax = portfolio_df.plot(title="Theoretically Optimal Strategy Vs. Benchmark", fontsize=12, color = ["black", "blue"])                                                                                                
    ax.set_xlabel("Dates")                                                                                             
    ax.set_ylabel("Normalized Portfolio Values")
    filename = "TOS.Vs.Benchmark" + "_" + str(start_date) + "_" + str(end_date) + ".png"
    plt.savefig(filename)

if __name__ == "__main__":

    sd = [int(m) for m in sys.argv[1].split(",")]
    ed = [int(n) for n in sys.argv[2].split(",")]

    print "sd: ", sd
    print "ed: ", ed

    main(start_date=dt.datetime(sd[0], sd[1], sd[2]), end_date=dt.datetime(ed[0], ed[1], ed[2]))
