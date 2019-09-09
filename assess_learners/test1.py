"""                                                                                               
Test a learner.  (c) 2015 Tucker Balch                                                                                                
                                                                                                                                
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
"""                                                                                               
                                                                                                                                
import numpy as np                                                                                                
import math                                                                                               
import LinRegLearner as lrl                                                                                               
import sys 

import DTLearner as dtl
import RTLearner as rtl
import BagLearner as bl
import matplotlib.pyplot as plt

def author(self):
    return 'zfu66' # replace tb34 with your Georgia Tech username

def computing_RMSE_CORR_BagLearner(trainX, trainY, testX, testY, primary_learner, max_leaf_size=None, max_bag_size=None, iterations=1):

    import DTLearner as dtl
    import RTLearner as rtl
    import BagLearner as bl
    
    no_results = np.zeros((1, 1))
    if max_leaf_size is None and max_bag_size is None:
        return no_results, no_results, no_results, no_results

    max_dim = max_bag_size or max_leaf_size
    
    #empty_set = np.zeros((max_dim, iterations))
    RMSE_IN  = np.zeros((max_dim, iterations))
    RMSE_OUT = np.zeros((max_dim, iterations))
    CORR_IN  = np.zeros((max_dim, iterations))
    CORR_OUT = np.zeros((max_dim, iterations))


    for i in range(1, max_dim):
        for j in range(iterations):
           
            if max_leaf_size is not None:
                learner = primary_learner(learner=dtl.DTLearner, kwargs={"leaf_size":i}, bags=10)
            elif max_bag_size is not None:
                learner = primary_learner(learner=dtl.DTLearner, kwargs={"leaf_size":20}, bags=i)
            else:
                pass

            learner.addEvidence(trainX, trainY)

            predY = learner.query(trainX)
            rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
            RMSE_IN[i, j] = rmse
            corr = np.corrcoef(predY, y=trainY)
            CORR_IN[i, j] = corr[0, 1]

            # Evaluate out-of-sample
            predY = learner.query(testX)
            rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
            RMSE_OUT[i, j] = rmse
            corr = np.corrcoef(predY, y=testY)
            CORR_OUT[i, j] = corr[0, 1]
    
    RMSE_in_mean = np.mean(RMSE_IN, axis=1)
    RMSE_out_mean = np.mean(RMSE_OUT, axis=1)
    CORR_in_mean = np.mean(CORR_IN, axis=1)
    CORR_out_mean = np.mean(CORR_OUT, axis=1)

    return RMSE_in_mean, RMSE_out_mean, CORR_in_mean, CORR_out_mean


def computing_RMSE_CORR_TreeLearner(trainX, trainY, testX, testY, primary_learner, max_leaf_size=None, iterations=10):

    import DTLearner as dtl
    import RTLearner as rtl
    import BagLearner as bl
    
    no_results = np.zeros((1, 1))
    if max_leaf_size is None:
        return no_results, no_results, no_results, no_results

    max_dim = max_leaf_size
    
    #empty_set = np.zeros((max_dim, iterations))
    RMSE_IN  = np.zeros((max_dim, iterations))
    RMSE_OUT = np.zeros((max_dim, iterations))
    CORR_IN  = np.zeros((max_dim, iterations))
    CORR_OUT = np.zeros((max_dim, iterations))


    for i in range(1, max_dim):
        for j in range(iterations):
           
            if max_leaf_size is not None:
                learner = primary_learner(leaf_size=i)
            else:
                pass

            learner.addEvidence(trainX, trainY)

            predY = learner.query(trainX)
            rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
            RMSE_IN[i, j] = rmse
            corr = np.corrcoef(predY, y=trainY)
            CORR_IN[i, j] = corr[0, 1]

            # Evaluate out-of-sample
            predY = learner.query(testX)
            rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
            RMSE_OUT[i, j] = rmse
            corr = np.corrcoef(predY, y=testY)
            CORR_OUT[i, j] = corr[0, 1]
    
    RMSE_in_mean = np.mean(RMSE_IN, axis=1)
    RMSE_out_mean = np.mean(RMSE_OUT, axis=1)
    CORR_in_mean = np.mean(CORR_IN, axis=1)
    CORR_out_mean = np.mean(CORR_OUT, axis=1)

    return RMSE_in_mean, RMSE_out_mean, CORR_in_mean, CORR_out_mean

def generate_plot(in_sample, out_of_sample, title, png_file, xlabel, ylabel, legend_loc="lower right", xaxis_length=1):

    x = np.arange(1, xaxis_length + 1)
    plt.figure(figsize=(12,8))
    plt.plot(x, in_sample, label="in-sample", linewidth=2.5)
    plt.plot(x, out_of_sample, label="out-of-sample", linewidth=2.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc=legend_loc)
    plt.title(title)
    plt.savefig(png_file, format='png')

if __name__=="__main__":

    #############################
    ##
    ## Read Data
    ##
    #############################
    
    if len(sys.argv) != 2:
        print "Usage: python testlearner.py <filename>"
        sys.exit(1)                                                                                               

    data = np.genfromtxt(sys.argv[1], delimiter=",")

    if np.isnan(data[0]).all():
        data = data[1:]
    if np.isnan(data[:, 0]).all():
        data = data[:, 1:]  

    #############################
    ##
    ## Q2: change leaf size
    ##
    #############################

    np.random.seed(2019)
    np.random.shuffle(data)
    max_leaf_size = 200
    max_bag_size  = 100

    # compute how much of the data is training and testing
    train_rows = int(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data[:train_rows,0:-1]
    trainY = data[:train_rows,-1]
    testX = data[train_rows:,0:-1]
    testY = data[train_rows:,-1]

    # Leaf size
  
    RMSE_in_mean, RMSE_out_mean, CORR_in_mean, CORR_out_mean = computing_RMSE_CORR_BagLearner(trainX, trainY, testX, testY, primary_learner=bl.BagLearner, max_leaf_size=max_leaf_size)
    in_sample = RMSE_in_mean
    out_of_sample = RMSE_out_mean
    title = "Figure2. RMSEs of training and testing BagLearner + DTLearner by different leaf size"
    png_file = "Figure21.png"
    xlabel = "Leaf Size"
    ylabel = "RMSE"

    generate_plot(in_sample, out_of_sample, title, png_file, xlabel, ylabel, legend_loc="lower right", xaxis_length=max_leaf_size)

    RMSE_diff = np.subtract(RMSE_in_mean, RMSE_out_mean)
    RMSE_diff_max = np.argmax(RMSE_diff > 0)

    print RMSE_diff_max




