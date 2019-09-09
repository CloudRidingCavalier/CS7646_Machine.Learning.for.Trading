"""  		   	  			    		  		  		    	 		 		   		 		  
template for generating data to fool learners (c) 2016 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import math  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
# this function should return a dataset (X and Y) that will work  		   	  			    		  		  		    	 		 		   		 		  
# better for linear regression than decision trees  		   	  			    		  		  		    	 		 		   		 		  
def best4LinReg(seed=1489683273):  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		   	  			    		  		  		    	 		 		   		 		  
    X = np.zeros((100,2))  		   	  			    		  		  		    	 		 		   		 		  
    Y = np.random.random(size = (100,))*200-100  		   	  			    		  		  		    	 		 		   		 		  
    # Here's is an example of creating a Y from randomly generated  		   	  			    		  		  		    	 		 		   		 		  
    # X with multiple columns  		   	  			    		  		  		    	 		 		   		 		  
    # Y = X[:,0] + np.sin(X[:,1]) + X[:,2]**2 + X[:,3]**3 
    data1 = np.random.random(size = (100,))*200-100
    data2 = 10 * data1
    #print data1
    #print data2
    X[:,0] = data1
    X[:,1] = data2
    #print X
    Y = X[:,0] + X[:,1]
    #print Y
    return X, Y  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def best4DT(seed=1489683273):  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		 
    X = np.zeros((100,10))  		  
    data1 = np.random.random(size = (100,))*200-100  	
    Y = np.sort(data1)

    filtered = [m for m in list(Y) if m <= 0.0]
    all_one = np.repeat([1], len(filtered))
    all_zero = np.repeat([0], 100-len(filtered))
    data2 = np.concatenate((all_one, all_zero))
    #print data2

    for i in range(10):
      X[:,i] = data2

    #print X

    return X, Y  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
    return 'zfu66' #Change this to your user ID  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "Freedom!"  		   
    X1, Y1 = best4DT(seed=1489683273)			  
    #X1, Y1 = best4LinReg(seed=1489683273)   		  		  		    	 		 		   		 		  
