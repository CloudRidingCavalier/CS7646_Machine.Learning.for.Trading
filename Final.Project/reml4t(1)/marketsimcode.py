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
import os  		   	  			    		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def compute_portvals(orders_df, start_val = 1000000, commission=9.95, impact=0.005, symbol="JPM"):  		   	  			    		  		  		    	 		 		   		 		  
    
    # this is the function the autograder will call to test your code  		   	  			    		  		  		    	 		 		   		 		  
    # NOTE: orders_file may be a string, or it may be a file object. Your  		   	  			    		  		  		    	 		 		   		 		  
    # code should work correctly with either input  		   	  			    		  		  		    	 		 		   		 		  
    # TODO: Your code here  		   	  			    		

    #####################
    ##
    ##  Loading orders as dataframe and sorting by date
    ##
    #####################

    #orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    #orders_df = orders_df.sort_index()
    #orders_df.index = pd.to_datetime(orders_df.index)

    #####################
    ##
    ##  Generate Price dataframe
    ##
    #####################

    start_date = orders_df.index.values[0]
    end_date = orders_df.index.values[-1]
    dates = pd.date_range(start_date, end_date)
    prices_df = get_data([symbol], dates, True)
    prices_df = prices_df.drop(['SPY'], axis=1)
    prices_df['Cash'] = np.ones(prices_df.shape[0])

    #print "This is prices df."
    #print prices_df.head(5)

    #####################
    ##
    ##  Generate Trades dataframe
    ##
    #####################

    trades_df = prices_df * 0.0

    for row_index, row in orders_df.iterrows():
        share_name  = symbol
        share_price = prices_df.loc[row_index, share_name]
        share_units = row[share_name]

        cash_flow = 0

        if share_units > 0:
          cash_flow = -1
        elif share_units < 0:
          cash_flow = 1
        else:
          cash_flow = 0

        trades_df.loc[row_index, share_name] += np.absolute(share_units) * cash_flow * -1
        trades_df.loc[row_index, "Cash"]     += np.absolute(share_units) * share_price * (cash_flow - impact) - commission

    #print "This is trades df."
    #print trades_df.head(5)

    #####################
    ##
    ##  Generate Holding dataframe
    ##
    #####################

    holding_df = trades_df
    holding_df.loc[start_date, 'Cash'] = start_val + trades_df.loc[start_date, 'Cash']

    for i in range(1, holding_df.shape[0]):
        for j in range (0, holding_df.shape[1]):
            new_val = holding_df.iloc[i,j] + holding_df.iloc[i-1,j]
            holding_df.iloc[i,j] = new_val

    #print "This is holding df."
    #print holding_df.head(5)

    #####################
    ##
    ##  Generate portifolio value dataframe
    ##
    #####################

    port_vals = prices_df * holding_df
    port_vals["port_val"] = port_vals.sum(axis=1)
    portvals = port_vals.loc[:,"port_val"]

    #print "This is port_vals"
    #print port_vals.head(5)

    return portvals  		

def author():                                                               
    return 'zfu66' #Change this to your user ID        	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def compute_portvals_stats(portvals):  		   	  			    		  		  		    	 		 		   		 		  
     		  
    # Process orders  		   	  			    		  		  		    	 		 		   		 		  	   	  			    		  		  		    	 		 		   		 		  
    if isinstance(portvals, pd.DataFrame):  		   	  			    		  		  		    	 		 		   		 		  
        portvals = portvals[portvals.columns[0]] # just get the first column  		   	  			    		  		  		    	 		 		   		 		  
    else:  		   	  			    		  		  		    	 		 		   		 		  
        "warning, code did not return a DataFrame"  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Get portfolio stats  		   	  			    		  		  		    	 		 		   		 		   		   	  			    		  		  		    	 		 		   		 		  
    rfr = 0
    sf  = 252
    cum_ret = ( portvals[-1] / portvals[0] ) - 1
    dr = ( portvals / portvals.shift(1)) - 1
    avg_daily_ret = dr.mean()
    std_daily_ret = dr.std()
    a = np.sqrt(sf)
    sharpe_ratio = a*((dr.subtract(rfr)).mean())/std_daily_ret 		   	  			    		  		  		    	 		 		   		 		  
    
    return [sharpe_ratio, cum_ret, avg_daily_ret, std_daily_ret] 		   	  			    		  		  		    	 		 		   		 		  

if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "This is a package to calculate portfolio values"  		   	  			    		  		  		    	 		 		   		 		  
