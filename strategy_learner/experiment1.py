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
import util as ut
from util import get_data, plot_data
import random

from marketsimcode import compute_portvals, compute_portvals_stats
import StrategyLearner as sl
from ManualStrategy import testPolicy, Benchmark

def author():                                                               
    return 'zfu66' #Change this to your user ID

def main(symbol="JPM", start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31)):

    np.random.seed(3 ** 9) 
    random.seed(3 ** 9)      

    print "Random seed is: ", 3**9, "\n\n"                                                                                        

    # Manual Strategy

    (df_trades, indicators_manual) = testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    #df_trades.to_csv("manual.csv")
    Manual_trade_dates = df_trades[symbol].nonzero()
    #print SL_trade_dates[0][0]
    print "\nFirst trading date of Manual Strategy: ", df_trades.index.values[Manual_trade_dates[0][0]]
    print "Trading times of Manual Strategy: ", len(Manual_trade_dates[0]), "\n"
    Manual_portval = compute_portvals(df_trades, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    Manual_portval_stats = compute_portvals_stats(Manual_portval)

    # Learning Strategy

    strategy_learner = sl.StrategyLearner(verbose = False, impact=0.0)
    strategy_learner.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL = strategy_learner.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL_trade_dates = df_SL[symbol].nonzero()
    #print SL_trade_dates[0][0]
    print "\nFirst trading date of Strategy Learner: ", df_SL.index.values[SL_trade_dates[0][0]]
    print "Trading times of Strategy Learner: ", len(SL_trade_dates[0]), "\n"
    SL_portval = compute_portvals(df_SL, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    SL_portval_stats = compute_portvals_stats(SL_portval)

    # Benchmark

    df_benchmark = Benchmark(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    BM_trade_dates = df_benchmark[symbol].nonzero()
    #print df_benchmark
    print "\nFirst trading date of Benchmark: ", df_benchmark.index.values[BM_trade_dates[0][0]]
    print "Trading times of Benchmark: ", len(BM_trade_dates[0]), "\n"
    Benchmark_portval = compute_portvals(df_benchmark, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    Benchmark_portval_stats = compute_portvals_stats(Benchmark_portval)


    ############################
    #
    # Print Stats
    #
    ############################

                                                                                              
    print "Date Range: {} to {}".format(start_date, end_date)                                                                                             
    print                                                                                             
    print "Sharpe Ratio of Manual: {}".format(Manual_portval_stats[0])       
    print "Sharpe Ratio of SL: {}".format(SL_portval_stats[0])                                                                                        
    print "Sharpe Ratio of Benchmark: {}".format(Benchmark_portval_stats[0])                                                                                              
    print                                                                                             
    print "Cumulative Return of Manual: {}".format(Manual_portval_stats[1])      
    print "Cumulative Return of SL: {}".format(SL_portval_stats[1])                                                                                         
    print "Cumulative Return of Benchmark: {}".format(Benchmark_portval_stats[1])                                                                                             
    print
    print "Average Daily Return of Manual: {}".format(Manual_portval_stats[2])          
    print "Average Daily Return of SL: {}".format(SL_portval_stats[2])                                                                                       
    print "Average Daily Return of Benchmark: {}".format(Benchmark_portval_stats[2])                                                                                              
    print                                                                                                     
    print "Standard Deviation of Manual: {}".format(Manual_portval_stats[3])  
    print "Standard Deviation of SL: {}".format(SL_portval_stats[3])                                                                                              
    print "Standard Deviation of Benchmark: {}".format(Benchmark_portval_stats[3])                                                                                                
    print                                                                                                                                                                             
    print "Final Portfolio Value Manual: {}".format(Manual_portval[-1]) 
    print "Final Portfolio Value SL: {}".format(SL_portval[-1]) 
    print "Final Portfolio Value Benchmark: {}".format(Benchmark_portval[-1])   

    portfolio_df = pd.DataFrame(index=Benchmark_portval.index, columns=['Manual Strategy', 'Strategy Learner', 'Benchmark'])
    
    portfolio_df['Manual Strategy'] = Manual_portval / Manual_portval[0]
    portfolio_df['Strategy Learner'] = SL_portval / SL_portval[0]
    portfolio_df['Benchmark'] = Benchmark_portval / Benchmark_portval[0]

    #manual_buy = indicators_manual[indicators_manual['Final_Signal'] == 1]
    #print manual_buy.index
    #manual_sell = indicators_manual[indicators_manual['Final_Signal'] == -1]
    #print manual_sell.index

    ax = portfolio_df.plot(fontsize=16, color = ["blue", "red", "black"])                                                                                                
    ax.set_xlabel("Dates", fontsize=16)                                                                                             
    ax.set_ylabel("Normalized Portfolio Values", fontsize=16)
    #ymin, ymax = ax.get_ylim()
    #plt.vlines(manual_buy.index,ymin,ymax,color='g')
    #plt.vlines(manual_sell.index,ymin,ymax,color='r')
    #filename = "Figure2.png"
    #plt.savefig(filename)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(8, 6)
    figure.suptitle("Manual Strategy Vs. Strategy Learner Vs. Benchmark", fontsize=16)
    # when saving, specify the DPI
    figure.savefig("Figure1.png")

if __name__ == "__main__":

    #sd = [int(m) for m in sys.argv[1].split(",")]
    #ed = [int(n) for n in sys.argv[2].split(",")]

    #print "sd: ", sd
    #print "ed: ", ed

    main(symbol="JPM", start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31))
