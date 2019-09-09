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

    # Learning Strategy: (impact = 0.0)                                                                                          

    strategy_learner1 = sl.StrategyLearner(verbose = False, impact=0.0)
    strategy_learner1.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL1 = strategy_learner1.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL1_portval = compute_portvals(df_SL1, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    SL1_portval_stats = compute_portvals_stats(SL1_portval)

    SL_trade_dates = df_SL1[symbol].nonzero()
    #print SL_trade_dates[0][0]
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.0): ", df_SL1.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.0): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.0): ", 0
        print "Trading times of Strategy Learner (impact=0.0): ", "No trading"


    # Learning Strategy: (impact = 0.005)

    strategy_learner2 = sl.StrategyLearner(verbose = False, impact=0.005)
    strategy_learner2.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL2 = strategy_learner2.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL2_portval = compute_portvals(df_SL2, start_val = 100000, commission=0.0, impact=0.005, symbol=symbol)
    SL2_portval_stats = compute_portvals_stats(SL2_portval)

    SL_trade_dates = df_SL2[symbol].nonzero()
    #print SL_trade_dates[0][0]
    #print len(SL_trade_dates[0])
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.005): ", df_SL2.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.005): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.005): ", 0
        print "Trading times of Strategy Learner (impact=0.005): ", "No trading"

    # Learning Strategy: (impact = 0.05)

    strategy_learner3 = sl.StrategyLearner(verbose = False, impact=0.05)
    strategy_learner3.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL3 = strategy_learner3.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL3_portval = compute_portvals(df_SL3, start_val = 100000, commission=0.0, impact=0.05, symbol=symbol)
    SL3_portval_stats = compute_portvals_stats(SL3_portval)

    SL_trade_dates = df_SL3[symbol].nonzero()
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.05): ", df_SL3.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.05): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.05): ", 0
        print "Trading times of Strategy Learner (impact=0.05): ", "No trading"

    # Learning Strategy: (impact = 0.5)

    strategy_learner4 = sl.StrategyLearner(verbose = False, impact=0.5)
    strategy_learner4.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL4 = strategy_learner4.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL4_portval = compute_portvals(df_SL4, start_val = 100000, commission=0.0, impact=0.5, symbol=symbol)
    SL4_portval_stats = compute_portvals_stats(SL4_portval)

    SL_trade_dates = df_SL4[symbol].nonzero()
    #print SL_trade_dates[0][0]
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.5): ", df_SL4.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.5): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.5): ", 0
        print "Trading times of Strategy Learner (impact=0.5): ", "No trading"

    # Benchmark

    df_benchmark = Benchmark(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    Benchmark_portval = compute_portvals(df_benchmark, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    Benchmark_portval_stats = compute_portvals_stats(Benchmark_portval)

    BM_trade_dates = df_benchmark[symbol].nonzero()
    #print df_benchmark
    print "\nFirst trading date of Benchmark: ", df_benchmark.index.values[BM_trade_dates[0][0]]
    print "Trading times of Benchmark: ", len(BM_trade_dates[0]), "\n"


    ############################
    #
    # Print Stats
    #
    ############################

                                                                                              
    print "Date Range: {} to {}".format(start_date, end_date)                                                                                             
    print                                                                                             
    print "Sharpe Ratio of SL1: {}".format(SL1_portval_stats[0])          
    print "Sharpe Ratio of SL2: {}".format(SL2_portval_stats[0])    
    print "Sharpe Ratio of SL3: {}".format(SL3_portval_stats[0])    
    print "Sharpe Ratio of SL4: {}".format(SL4_portval_stats[0])                                                                                  
    print "Sharpe Ratio of Benchmark: {}".format(Benchmark_portval_stats[0])                                                                                              
    print                                                                                             
    print "Cumulative Return of SL1: {}".format(SL1_portval_stats[1])          
    print "Cumulative Return of SL2: {}".format(SL2_portval_stats[1])    
    print "Cumulative Return of SL3: {}".format(SL3_portval_stats[1])    
    print "Cumulative Return of SL4: {}".format(SL4_portval_stats[1])                                                                                          
    print "Cumulative Return of Benchmark: {}".format(Benchmark_portval_stats[1])                                                                                             
    print
    print "Average Daily Return of SL1: {}".format(SL1_portval_stats[2])          
    print "Average Daily Return of SL2: {}".format(SL2_portval_stats[2])     
    print "Average Daily Return of SL3: {}".format(SL3_portval_stats[2])          
    print "Average Daily Return of SL4: {}".format(SL4_portval_stats[2])                                                                                   
    print "Average Daily Return of Benchmark: {}".format(Benchmark_portval_stats[2])                                                                                              
    print                                                                                                     
    print "Standard Deviation of SL1: {}".format(SL1_portval_stats[3]) 
    print "Standard Deviation of SL2: {}".format(SL2_portval_stats[3])   
    print "Standard Deviation of SL3: {}".format(SL3_portval_stats[3]) 
    print "Standard Deviation of SL4: {}".format(SL4_portval_stats[3])                                                                                            
    print "Standard Deviation of Benchmark: {}".format(Benchmark_portval_stats[3])                                                                                                
    print                                                                                                                                                                             
    print "Final Portfolio Value SL1: {}".format(SL1_portval[-1]) 
    print "Final Portfolio Value SL2: {}".format(SL2_portval[-1]) 
    print "Final Portfolio Value SL3: {}".format(SL3_portval[-1]) 
    print "Final Portfolio Value SL4: {}".format(SL4_portval[-1])
    print "Final Portfolio Value Benchmark: {}".format(Benchmark_portval[-1])   

    portfolio_df = pd.DataFrame(index=Benchmark_portval.index, columns=['Strategy Learner (impact=0.0)', \
                                                                     'Strategy Learner (impact=0.005)', \
                                                                     'Strategy Learner (impact=0.05)', \
                                                                     'Strategy Learner (impact=0.5)', 'Benchmark'])
    
    portfolio_df['Strategy Learner (impact=0.0)']   = SL1_portval / SL1_portval[0]
    portfolio_df['Strategy Learner (impact=0.005)'] = SL2_portval / SL2_portval[0]
    portfolio_df['Strategy Learner (impact=0.05)']  = SL3_portval / SL3_portval[0]
    portfolio_df['Strategy Learner (impact=0.5)']   = SL4_portval / SL4_portval[0]
    portfolio_df['Benchmark'] = Benchmark_portval / Benchmark_portval[0]

    #manual_buy = indicators_manual[indicators_manual['Final_Signal'] == 1]
    #print manual_buy.index
    #manual_sell = indicators_manual[indicators_manual['Final_Signal'] == -1]
    #print manual_sell.index

    ax = portfolio_df.plot(fontsize=16, color = ["red", "orange", "green", "navy", "black"])                                                                                                
    ax.set_xlabel("Dates", fontsize=16)                                                                                             
    ax.set_ylabel("Normalized Portfolio Values", fontsize=16)
    #ymin, ymax = ax.get_ylim()
    #plt.vlines(manual_buy.index,ymin,ymax,color='g')
    #plt.vlines(manual_sell.index,ymin,ymax,color='r')
    #filename = "Figure2.png"
    #plt.savefig(filename)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(9, 6)
    figure.suptitle("Strategy Learner with various impact factors Vs. Benchmark", fontsize=16)
    # when saving, specify the DPI
    figure.savefig("Figure2.png")

def alt(symbol="JPM", start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31)):

    np.random.seed(3 ** 9 - 100) 
    random.seed(3 ** 9 - 100)          

    print "Random seed is: ", 3**9 - 100, "\n\n"                                                                                    

    # Learning Strategy: (impact = 0.0)                                                                                          

    strategy_learner1 = sl.StrategyLearner(verbose = False, impact=0.0)
    strategy_learner1.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL1 = strategy_learner1.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL1_portval = compute_portvals(df_SL1, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    SL1_portval_stats = compute_portvals_stats(SL1_portval)

    SL_trade_dates = df_SL1[symbol].nonzero()
    #print SL_trade_dates[0][0]
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.0): ", df_SL1.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.0): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.0): ", 0
        print "Trading times of Strategy Learner (impact=0.0): ", "No trading"


    # Learning Strategy: (impact = 0.005)

    strategy_learner2 = sl.StrategyLearner(verbose = False, impact=0.005)
    strategy_learner2.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL2 = strategy_learner2.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL2_portval = compute_portvals(df_SL2, start_val = 100000, commission=0.0, impact=0.005, symbol=symbol)
    SL2_portval_stats = compute_portvals_stats(SL2_portval)

    SL_trade_dates = df_SL2[symbol].nonzero()
    #print SL_trade_dates[0][0]
    #print len(SL_trade_dates[0])
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.005): ", df_SL2.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.005): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.005): ", 0
        print "Trading times of Strategy Learner (impact=0.005): ", "No trading"

    # Learning Strategy: (impact = 0.05)

    strategy_learner3 = sl.StrategyLearner(verbose = False, impact=0.05)
    strategy_learner3.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL3 = strategy_learner3.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL3_portval = compute_portvals(df_SL3, start_val = 100000, commission=0.0, impact=0.05, symbol=symbol)
    SL3_portval_stats = compute_portvals_stats(SL3_portval)

    SL_trade_dates = df_SL3[symbol].nonzero()
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.05): ", df_SL3.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.05): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.05): ", 0
        print "Trading times of Strategy Learner (impact=0.05): ", "No trading"

    # Learning Strategy: (impact = 0.5)

    strategy_learner4 = sl.StrategyLearner(verbose = False, impact=0.5)
    strategy_learner4.addEvidence(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    df_SL4 = strategy_learner4.testPolicy(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    SL4_portval = compute_portvals(df_SL4, start_val = 100000, commission=0.0, impact=0.5, symbol=symbol)
    SL4_portval_stats = compute_portvals_stats(SL4_portval)

    SL_trade_dates = df_SL4[symbol].nonzero()
    #print SL_trade_dates[0][0]
    if len(SL_trade_dates[0]):
        print "\nFirst trading date of Strategy Learner (impact=0.5): ", df_SL4.index.values[SL_trade_dates[0][0]]
        print "Trading times of Strategy Learner (impact=0.5): ", len(SL_trade_dates[0]), "\n"
    else:
        print "\nFirst trading date of Strategy Learner (impact=0.5): ", 0
        print "Trading times of Strategy Learner (impact=0.5): ", "No trading"

    # Benchmark

    df_benchmark = Benchmark(symbol=symbol, sd=start_date, ed=end_date, sv=100000)
    Benchmark_portval = compute_portvals(df_benchmark, start_val = 100000, commission=0.0, impact=0.0, symbol=symbol)
    Benchmark_portval_stats = compute_portvals_stats(Benchmark_portval)

    BM_trade_dates = df_benchmark[symbol].nonzero()
    #print df_benchmark
    print "\nFirst trading date of Benchmark: ", df_benchmark.index.values[BM_trade_dates[0][0]]
    print "Trading times of Benchmark: ", len(BM_trade_dates[0]), "\n"


    ############################
    #
    # Print Stats
    #
    ############################

                                                                                              
    print "Date Range: {} to {}".format(start_date, end_date)                                                                                             
    print                                                                                             
    print "Sharpe Ratio of SL1: {}".format(SL1_portval_stats[0])          
    print "Sharpe Ratio of SL2: {}".format(SL2_portval_stats[0])    
    print "Sharpe Ratio of SL3: {}".format(SL3_portval_stats[0])    
    print "Sharpe Ratio of SL4: {}".format(SL4_portval_stats[0])                                                                                  
    print "Sharpe Ratio of Benchmark: {}".format(Benchmark_portval_stats[0])                                                                                              
    print                                                                                             
    print "Cumulative Return of SL1: {}".format(SL1_portval_stats[1])          
    print "Cumulative Return of SL2: {}".format(SL2_portval_stats[1])    
    print "Cumulative Return of SL3: {}".format(SL3_portval_stats[1])    
    print "Cumulative Return of SL4: {}".format(SL4_portval_stats[1])                                                                                          
    print "Cumulative Return of Benchmark: {}".format(Benchmark_portval_stats[1])                                                                                             
    print
    print "Average Daily Return of SL1: {}".format(SL1_portval_stats[2])          
    print "Average Daily Return of SL2: {}".format(SL2_portval_stats[2])     
    print "Average Daily Return of SL3: {}".format(SL3_portval_stats[2])          
    print "Average Daily Return of SL4: {}".format(SL4_portval_stats[2])                                                                                   
    print "Average Daily Return of Benchmark: {}".format(Benchmark_portval_stats[2])                                                                                              
    print                                                                                                     
    print "Standard Deviation of SL1: {}".format(SL1_portval_stats[3]) 
    print "Standard Deviation of SL2: {}".format(SL2_portval_stats[3])   
    print "Standard Deviation of SL3: {}".format(SL3_portval_stats[3]) 
    print "Standard Deviation of SL4: {}".format(SL4_portval_stats[3])                                                                                            
    print "Standard Deviation of Benchmark: {}".format(Benchmark_portval_stats[3])                                                                                                
    print                                                                                                                                                                             
    print "Final Portfolio Value SL1: {}".format(SL1_portval[-1]) 
    print "Final Portfolio Value SL2: {}".format(SL2_portval[-1]) 
    print "Final Portfolio Value SL3: {}".format(SL3_portval[-1]) 
    print "Final Portfolio Value SL4: {}".format(SL4_portval[-1])
    print "Final Portfolio Value Benchmark: {}".format(Benchmark_portval[-1])   

    portfolio_df = pd.DataFrame(index=Benchmark_portval.index, columns=['Strategy Learner (impact=0.0)', \
                                                                     'Strategy Learner (impact=0.005)', \
                                                                     'Strategy Learner (impact=0.05)', \
                                                                     'Strategy Learner (impact=0.5)', 'Benchmark'])
    
    portfolio_df['Strategy Learner (impact=0.0)']   = SL1_portval / SL1_portval[0]
    portfolio_df['Strategy Learner (impact=0.005)'] = SL2_portval / SL2_portval[0]
    portfolio_df['Strategy Learner (impact=0.05)']  = SL3_portval / SL3_portval[0]
    portfolio_df['Strategy Learner (impact=0.5)']   = SL4_portval / SL4_portval[0]
    portfolio_df['Benchmark'] = Benchmark_portval / Benchmark_portval[0]

    #manual_buy = indicators_manual[indicators_manual['Final_Signal'] == 1]
    #print manual_buy.index
    #manual_sell = indicators_manual[indicators_manual['Final_Signal'] == -1]
    #print manual_sell.index

    ax = portfolio_df.plot(fontsize=16, color = ["red", "orange", "green", "navy", "black"])                                                                                                
    ax.set_xlabel("Dates", fontsize=16)                                                                                             
    ax.set_ylabel("Normalized Portfolio Values", fontsize=16)
    #ymin, ymax = ax.get_ylim()
    #plt.vlines(manual_buy.index,ymin,ymax,color='g')
    #plt.vlines(manual_sell.index,ymin,ymax,color='r')
    #filename = "Figure2.png"
    #plt.savefig(filename)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(9, 6)
    figure.suptitle("Strategy Learner with various impact factors Vs. Benchmark", fontsize=16)
    # when saving, specify the DPI
    figure.savefig("Figure3.png")

if __name__ == "__main__":

    #sd = [int(m) for m in sys.argv[1].split(",")]
    #ed = [int(n) for n in sys.argv[2].split(",")]

    #print "sd: ", sd
    #print "ed: ", ed

    main(symbol="JPM", start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31))
    alt(symbol="JPM", start_date=dt.datetime(2008,1,1), end_date=dt.datetime(2009,12,31))

