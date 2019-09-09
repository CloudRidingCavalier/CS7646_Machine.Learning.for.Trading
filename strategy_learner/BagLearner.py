"""
	A simple wrapper for Bag Learner
	Student Name: ZHENG FU
	GT User ID: zfu66
	GT ID: 903369876
"""

import numpy as np
import pandas as pd
#import LinRegLearner, DTLearner, RTLearner

class BagLearner(object):

    def __init__(self, learner, kwargs={"leaf_size":1}, bags=20, boost=False, verbose = False):

        self.bags = bags
        self.kwargs = kwargs
        self.boost = boost
        self.verbose = verbose
        if self.verbose:
            self.debug()

        learners = []
        for bag in range(bags):
            learners.append(learner(**kwargs))
        self.learners = learners

    def author(self):
        return 'zfu66' # replace tb34 with your Georgia Tech username

    def debug(self):
    	print "This is on debug mode."

    def addEvidence(self, dataX, dataY):
		
        for learner in self.learners:

            bag_index = np.random.choice(dataX.shape[0], dataX.shape[0])
            X = dataX[bag_index]
            Y = dataY[bag_index]
            learner.addEvidence(X, Y)

    def query(self, points):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Estimate a set of test points given the model we built.  		   	  			    		  		  		    	 		 		   		 		  
        @param points: should be a numpy array with each row corresponding to a specific query.  		   	  			    		  		  		    	 		 		   		 		  
        @returns the estimated values according to the saved model.  		   	  			    		  		  		    	 		 		   		 		  
        """  	

        results = np.array([learner.query(points) for learner in self.learners])
        return np.mean(results, axis=0)

if __name__=="__main__":  		

    print ("This is a Bag Learner\n")

    













