import DTLearner as dt
import numpy as np

learner = dt.DTLearner(leaf_size = 1, verbose = False) # constructor
# Some data to test the DTLearner
x0 = np.array([0.885, 0.725, 0.560, 0.735, 0.610, 0.260, 0.500, 0.320])
x1 = np.array([0.330, 0.390, 0.500, 0.570, 0.630, 0.630, 0.680, 0.780])
x2 = np.array([9.100, 10.900, 9.400, 9.800, 8.400, 11.800, 10.500, 10.000])
x = np.array([x0, x1, x2]).T
y = np.array([4.000, 5.000, 6.000, 5.000, 3.000, 8.000, 7.000, 6.000])


learner.addEvidence(x, y) # training step
Y = learner.query(x) # query

print Y