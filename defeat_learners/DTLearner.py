"""
	A simple wrapper for Decision Tree Regression
	Student Name: ZHENG FU
	GT User ID: zfu66
	GT ID: 903369876
"""

import numpy as np
import pandas as pd

class DTLearner(object):

    def __init__(self, leaf_size=1, verbose=False):

        self.leaf_size = leaf_size
        self.tree = None
        self.verbose = verbose
        if self.verbose:
            self.debug()

    def author(self):
        return 'zfu66' # replace tb34 with your Georgia Tech username

    def debug(self):
    	print "This is on debug mode."

    def addEvidence(self, dataX, dataY):
		"""
		@summary: Add training data to learner
		@param dataX: X values of data to add
		@param dataY: the Y training values
		"""
		self.tree = self.build_tree(dataX, dataY)

    def query(self, points):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Estimate a set of test points given the model we built.  		   	  			    		  		  		    	 		 		   		 		  
        @param points: should be a numpy array with each row corresponding to a specific query.  		   	  			    		  		  		    	 		 		   		 		  
        @returns the estimated values according to the saved model.  		   	  			    		  		  		    	 		 		   		 		  
        """  	

        preds = []
        
        for point in range(points.shape[0]):
            
            current_observation = points[point,:]
            row = 0

            # Not leaf
            while(self.tree[row,0] != 'leaf'):
            	feature = int(float(self.tree[row,0]))
            	split_value = float(self.tree[row,1])

            	if float(current_observation[feature]) <= split_value:
            		row=row + int(float(self.tree[row,2]))	#Left_Tree
            	else:
            		row=row + int(float(self.tree[row,3]))	#Right_Tree

            preds.append(float(self.tree[row,1]))

        return np.asarray(preds)

    def identify_best_feature(self, dataX, dataY):

    	best_feature = 0
    	PCC_list = []

    	for feature in range(0, dataX.shape[1]):
            correlation = np.corrcoef(dataX[:,feature], dataY)
            correlation = abs(correlation[0,1])
            PCC_list.append(correlation)

        max_value = max(PCC_list)
        best_feature = PCC_list.index(max_value)

        return int(best_feature)

    def build_tree(self, dataX, dataY):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: build a decision tree learner  		   	  			    		  		  		    	 		 		   		 		  
        @param dataX: X values of data to add  		   	  			    		  		  		    	 		 		   		 		  
        @param dataY: the Y training values  		   	  			    		  		  		    	 		 		   		 		  
        """  		

        if dataX.shape[0] <= self.leaf_size:
        	return np.array([["leaf",np.mean(dataY),-1,-1]])

        if np.all(dataY[0] == dataY, axis=0):	
        	return np.array([["leaf",dataY[0],-1,-1]])
        else:
        	feature = self.identify_best_feature(dataX, dataY)
        	split_value  = np.median(dataX[:,feature])	
        	max_value    = np.max(dataX[:,feature])

        	if split_value == max_value: # No right tree
        		return np.array([["leaf",np.mean(dataY),-1,-1]])	#empty right sub-tree. Only left sub-tree formed

        	Left_Tree  = self.build_tree(dataX[dataX[:,feature] <= split_value], dataY[dataX[:,feature] <= split_value])
        	Right_Tree = self.build_tree(dataX[dataX[:,feature] >  split_value], dataY[dataX[:,feature] > split_value])

        	root = np.array([[feature, split_value, 1, Left_Tree.shape[0]+1]])
        	root_left = np.append(root, Left_Tree, axis=0)
        	whole_tree = np.append(root_left, Right_Tree, axis=0)
        	return whole_tree

if __name__=="__main__":  		

    print ("This is a Decision Tree Learner\n")

    

















