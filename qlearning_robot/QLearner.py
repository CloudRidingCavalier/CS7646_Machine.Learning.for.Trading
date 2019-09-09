"""                                                                                               
Template for implementing QLearner  (c) 2015 Tucker Balch                                                                                             
                                                                                              
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
import random as rand                                                                                             
                                                                                              
class QLearner(object):                                                                                               
                                                                                              
    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):                                                                                             
                                                                                              
        self.verbose = verbose                                                                                                
        self.num_actions = num_actions
        self.num_states = num_states                                                                                                
        self.s = 0                                                                                                
        self.a = 0

        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna

        self.QTable = np.zeros((num_states, num_actions))
        self.Reward = np.zeros((num_states, num_actions))

        self.Transition = np.zeros((num_states, num_actions, num_states))
        self.Tc = np.zeros((num_states, num_actions, num_states))

    def author(self):
        return 'zfu66'                                                                                        
                                                                                              
    def querysetstate(self, s):                                                                                               
        """                                                                                               
        @summary: Update the state without updating the Q-table                                                                                               
        @param s: The new state                                                                                               
        @returns: The selected action                                                                                             
        """   

        if np.random.uniform() < self.rar:
            action = rand.randint(0, self.num_actions-1)
        else:
            action = self.QTable[s,:].argmax()

        self.s = s
        self.a = action
                                                                                                                                                                                          
        if self.verbose: print "s =", s,"a =",action                                                                                              
        return action                                                                                             
                                                                                              
    def query(self,s_prime,r):                                                                                                
        """                                                                                               
        @summary: Update the Q table and return an action                                                                                             
        @param s_prime: The new state                                                                                             
        @param r: The ne state                                                                                                
        @returns: The selected action                                                                                             
        """  

        if np.random.uniform() < self.rar:
            action = rand.randint(0, self.num_actions-1)
        else:
            action = self.QTable[s_prime,:].argmax()

        previous_Q_value = (1 - self.alpha) * self.QTable[self.s, self.a]
        updated_Q_value  = previous_Q_value + self.alpha * (r + (self.gamma * self.QTable[s_prime, self.QTable[s_prime,:].argmax()]))

        self.QTable[self.s, self.a] = updated_Q_value
        self.rar = self.rar * self.radr

        ############################
        #
        # Dyna algorithm
        #
        ############################

        if(self.dyna > 0):
            self.updateModel(self.s, self.a, s_prime, r)
            self.hallucinate()

        ############################
        #
        # Return action
        #
        ############################

        self.s = s_prime
        self.a = action  

        if self.verbose: print "s =", s_prime,"a =",action,"r =",r                                                                                                
        return action     

    def updateModel(self, s, a, s_prime, r):
        """                                                                                               
        @summary: Update both reward and model according to the Dyna lecture materials                                                                                
        @param s_prime: The new state                                                                                             
        @param r: The reward                                                                                   
        @param s: The current state
        @param a: The current action                                                                                        
        """  

        self.Tc[s, a, s_prime] = self.Tc[s, a, s_prime] + 1
        self.Transition = self.Tc / self.Tc.sum(axis=2, keepdims=True)
        self.Reward[s, a] = ((1 - self.alpha) * self.Reward[s, a]) + (self.alpha * r)   

    def hallucinate(self):
        """                                                                                               
        @summary: Performing Hallucinate, genearate random s and a                                                                               
                                                                                   
        """  

        for iteration in range(self.dyna):

            s_rand = rand.randint(0, self.num_states - 1)
            a_rand = rand.randint(0, self.num_actions - 1)
            
            transition = self.Transition[s_rand, a_rand, :]
            s_prime    = np.random.multinomial(self.num_states, transition).argmax()
            reward     = self.Reward[s_rand, a_rand]

            previous_Q_value = (1 - self.alpha) * self.QTable[s_rand, a_rand]
            updated_Q_value  = previous_Q_value + self.alpha * (reward + (self.gamma * self.QTable[s_prime, self.QTable[s_prime,:].argmax()]))

            self.QTable[s_rand, a_rand] = updated_Q_value                                                                                      
                                                                                              
if __name__=="__main__":                                                                                              
    print "Remember Q from Star Trek? Well, this isn't him"                                                                                               
