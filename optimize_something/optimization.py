"""MC1-P2: Optimize a portfolio.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: ZHENG FU (replace with your name)                                                               
GT User ID: zfu66 (replace with your User ID)                                                               
GT ID: 903369876 (replace with your GT ID)       		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		   			    		  		  		    	 		 		   		 		  
import pandas as pd  		   	  			    		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import datetime as dt  		   	  			    		  		  		    	 		 		   		 		  
from util import get_data, plot_data 
import scipy.optimize as spo

# Function for computing Sharpe Ratio

def sharpe_ratio(allocs, normed, sv, rfr, td):
  alloced  = normed * allocs
  pos_vals = alloced * sv
  port_val = pos_vals.sum(axis=1) 
  daily_returns = ( port_val / port_val.shift(1) ) - 1
  stdev_daily_returns = daily_returns.std()

  sr = ( ((daily_returns.subtract(rfr)).mean()) / stdev_daily_returns ) * np.sqrt(td)
  negative_sr = -1 * sr
  return negative_sr # Maximizing sr = Minimizing -sr
   		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		   	  			    		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		   	  			    		  		  		    	 		 		   		 		  
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):  	

    #####################################
    ##
    ## Prepare input data for optimizations
    ##
    #####################################	   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		   	  			    		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		   	  			    		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		 

    # Fill in possible np.nan values:
    prices_all.fillna(method="ffill",inplace=True)
    prices_all.fillna(method="bfill",inplace=True)  	 

    # Loading symbols and SPY prices
    prices = prices_all[syms]  # only portfolio symbols  		   	  			    		  		  		    	 		 		   		 		  
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later

    # Normalizing prices
    normed = prices / prices.values[0]    		 

    # Setup parameters
    start_value      = 1000000 # start value
    risk_free_return = 0.0     # risk free return
    trading_days     = 252.0   # trading days in a year	  

    ########################################
    ##
    ## Optimizaion of Portifolio Allocation by Maximizing Sharp Ratio
    ##
    ########################################

    # find the allocations for the optimal portfolio  		   	  			    		  		  		    	 		 		   		 		  
    # note that the values here ARE NOT meant to be correct for a test case  		   	  			    		  		  		    	 		 		   		 		  
    allocs = np.asarray([0.2, 0.2, 0.3, 0.3]) # add code here to find the allocations 

    # Use a uniform allocation of 1/n to each of the n assets as your initial guess.
    initial_guess_allocs = [ (1.0 / len(syms) ) ] * len(syms)

    # For bounds, you simply need to pass in a sequence of 2-tuples (<low>, <high>). 
    # Just remember that you need to supply as many tuples as the number of stocks in your portfolio.
    assignment_bounds = ( (0.0, 1.0), ) * len(syms)

    # For constraints, it's a little tricky. 
    # You need to pass in a sequence of dicts (dictionaries), one dictionary per constraint. 
    # Each dictionary must specify the type of constraint ('eq' for equality, or 'ineq' for inequality), 
    # and a function that returns 0 only when the input satisfies the constraint 
    # (this is the same input that is supplied to your evaluation function). 
    # E.g. to constrain the sum of all values in the input array to be less than 50, 
    # you could pass in the following (lambdas are just anonymous functions defined on-the-spot):
    assignment_constraints = ({ 'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs) })

    # Performing optimizaion via scipy.optimize
    results = spo.minimize(sharpe_ratio, initial_guess_allocs, \
                           args = (normed, start_value, risk_free_return, trading_days, ), \
                           method = 'SLSQP', options = {'disp':True}, \
                           bounds = assignment_bounds, \
                           constraints = assignment_constraints )
    allocs = results.x

    ########################################
    ##
    ## Computing Daily Portfolio Values
    ##
    ########################################
    		  		  		    	 		 		   		 		  
    # Get daily portfolio value  		   	  			    		  		  		    	 		 		   		 		  
    port_val = prices_SPY # add code here to compute daily portfolio values
    alloced  = normed * allocs
    pos_vals = alloced * start_value
    port_val = pos_vals.sum(axis=1) 

    ########################################
    ##
    ## Computing Statistics
    ##
    ########################################

    cr, adr, sddr, sr = [0.25, 0.001, 0.0005, 2.1] # add code here to compute stats  			

    daily_return = ( port_val / port_val.shift(1) ) - 1
    cr           = ( port_val[-1] / port_val[0] ) - 1
    adr          = daily_return.mean()
    sddr         = daily_return.std()
    sr           = ( ((daily_return.subtract(risk_free_return)).mean()) / sddr ) * np.sqrt(trading_days)   		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		   	  			    		  		  		    	 		 		   		 		  
    if gen_plot:  		   	  			    		  		  		    	 		 		   		 		  
        # add code to plot here  	
        prices_port = port_val / port_val[0]
        prices_SPY  = prices_SPY / prices_SPY[0]	   	  			    		  		  		    	 		 		   		 		  
        df_temp = pd.concat([prices_port, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)  
        plot_data(df_temp, title="Daily Portfolio Value and SPY")	   	  			    		  		  		    	 		 		   		 		  
        pass  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    # This function WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			    		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			    		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			    		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008,6,1)
    end_date = dt.datetime(2009,6,1)
    symbols = ['IBM', 'X', 'GLD', 'JPM']  		
      		   	  			    		  		  		    	 		 		   		 		  
    # Assess the portfolio  		   	  			    		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = True)  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Print statistics  		   	  			    		  		  		    	 		 		   		 		  
    print "Start Date:", start_date  		   	  			    		  		  		    	 		 		   		 		  
    print "End Date:", end_date  		   	  			    		  		  		    	 		 		   		 		  
    print "Symbols:", symbols  		   	  			    		  		  		    	 		 		   		 		  
    print "Allocations:", allocations  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio:", sr  		   	  			    		  		  		    	 		 		   		 		  
    print "Volatility (stdev of daily returns):", sddr  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return:", adr  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return:", cr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
