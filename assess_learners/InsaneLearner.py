import numpy as np
import BagLearner as bg
import LinRegLearner as lrl
class InsaneLearner(object):
    def __init__(self, verbose = False):
        self.learners = []
        if verbose:
            print "Debugging InsaneLearner"
        for i in range(0,20):
            self.learners.append(bg.BagLearner(lrl.LinRegLearner,kwargs={},bags=20))
    def author(self):
        return 'zfu66' # replace tb34 with your Georgia Tech username
    def addEvidence(self, dataX, dataY):
        for learner in self.learners:
            learner.addEvidence(dataX, dataY)
    def query(self, points):  		   	  			    		  		  		    	 		 		   		 		  
        results = np.array([learner.query(points) for learner in self.learners])
        return np.mean(results, axis=0)
if __name__=="__main__":
    print ("This is a Insane Learner\n")

    













