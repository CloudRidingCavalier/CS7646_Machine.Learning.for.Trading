"""Assess a betting strategy.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt

def author(): 
        return 'zfu66' # replace tb34 with your Georgia Tech username.

def gtid():
    return 903369876 # replace with your GT ID number

def get_spin_result(win_prob):
    result = False
    if np.random.random() <= win_prob:
        result = True
    return result

def test_code():
    
    win_prob = 18.0/38.0 # set appropriately to the probability of a win
    np.random.seed(gtid()) # do this only once
    print get_spin_result(win_prob) # test the roulette spin
    
    ############################
    #
    # Experiment 1, Figure 1
    #
    ############################
    
    result1 = np.full((10, 301), 80.0)
    result1[:,0] = np.zeros(10)
    
    for episode in range(10):
        episode_winnings = 0.0
        spin_counter = 0
        while episode_winnings < 80.0:
            won = False
            bet_amount = 1
            continue_to_next_episode = False
            while not won:
                won = get_spin_result(win_prob)
                spin_counter += 1
                if won:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                if spin_counter <= 300:
                    result1[episode, spin_counter] = episode_winnings
                else:
                    continue_to_next_episode = True
                    break
            if continue_to_next_episode:
                break
    
    # plot figure 1
    
    plt.rcParams.update({'font.size': 20})
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(20,10))
    palette = plt.get_cmap('Set1')
    color_num = 0
    for episode in range(10):
        color_num += 1
        line_label = "Episode" + str(episode+1)
        plt.plot(range(301), result1[episode,:], marker='', linewidth=1, alpha=0.9, label=line_label)
    plt.legend(loc=4, ncol=2)
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.yticks(np.arange(-256, 100, step=16))
    plt.xticks(np.arange(0, 301, step=20))
    plt.title("Figure1: running simple simulator 10 times", loc='left', fontsize=24, fontweight=0, color='orange')
    plt.ylabel("Winnings")
    plt.xlabel("Spins")
    plt.savefig("Figure1.png")
    
    ############################
    #
    # Experiment 1, Figure 2
    #
    ############################
    
    result2 = np.full((1000, 301), 80.0)
    result2[:,0] = np.zeros(1000)
    
    for episode in range(1000):
        episode_winnings = 0.0
        spin_counter = 0
        while episode_winnings < 80.0:
            won = False
            bet_amount = 1
            continue_to_next_episode = False
            while not won:
                won = get_spin_result(win_prob)
                spin_counter += 1
                if won:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                if spin_counter <= 300:
                    result2[episode, spin_counter] = episode_winnings
                else:
                    continue_to_next_episode = True
                    break
            if continue_to_next_episode:
                break
    
    # plot figure 2
    result2_mean = np.mean(result2, axis=0)
    result2_std  = np.std(result2, axis=0)
    
    plt.rcParams.update({'font.size': 20})
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(20,10))
    palette = plt.get_cmap('Set1')
    plt.errorbar(range(301), result2_mean, result2_std, fmt='-o')
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.yticks(np.arange(-256, 100, step=16))
    plt.xticks(np.arange(0, 301, step=20))
    plt.title("Figure2: running simple simulator 1000 times, mean of winnings with standard deviation", loc='left', fontsize=24, fontweight=0, color='orange')
    plt.ylabel("Winnings")
    plt.xlabel("Spins")
    plt.savefig("Figure2.png")
    
    ############################
    #
    # Experiment 1, Figure 3
    #
    ############################
    
    # plot figure 3
    result2_median = np.median(result2, axis=0)
    result2_std  = np.std(result2, axis=0)
    
    plt.rcParams.update({'font.size': 20})
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(20,10))
    palette = plt.get_cmap('Set1')
    plt.errorbar(range(301), result2_median, result2_std, fmt='-o')
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.yticks(np.arange(-256, 100, step=16))
    plt.xticks(np.arange(0, 301, step=20))
    plt.title("Figure3: running simple simulator 1000 times, median of winnings with standard deviation", loc='left', fontsize=24, fontweight=0, color='orange')
    plt.ylabel("Winnings")
    plt.xlabel("Spins")
    plt.savefig("Figure3.png")
    
    ############################
    #
    # Experiment 2, Figure 4
    #
    ############################
    
    result3 = np.full((1000, 301), -256.0)
    result3[:,0] = np.zeros(1000)
    
    for episode in range(1000):
        episode_winnings = 0.0
        spin_counter = 0
        initial_bank_roll = 256
        current_bank_roll = initial_bank_roll
        while episode_winnings < 80.0:
            won = False
            bet_amount = 1
            continue_to_next_episode = False
            if current_bank_roll < 1:
                break
            if episode_winnings <= -256:
                break
            while not won:
                won = get_spin_result(win_prob)
                spin_counter += 1
                if won:
                    episode_winnings = episode_winnings + bet_amount
                    current_bank_roll = initial_bank_roll + episode_winnings
                else:
                    episode_winnings = episode_winnings - bet_amount
                    if episode_winnings <= -256:
                        result3[episode, spin_counter] = -256
                        continue_to_next_episode = True
                        break
                    current_bank_roll = initial_bank_roll + episode_winnings
                    if current_bank_roll < bet_amount * 2:
                        bet_amount = current_bank_roll
                    else:
                        bet_amount = bet_amount * 2
                if spin_counter <= 300:
                    result3[episode, spin_counter] = episode_winnings
                else:
                    continue_to_next_episode = True
                    break
            if continue_to_next_episode:
                break
    
    # plot figure 4
    result3_mean = np.mean(result3, axis=0)
    result3_std  = np.std(result3, axis=0)
    
    plt.rcParams.update({'font.size': 20})
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(20,10))
    palette = plt.get_cmap('Set1')
    plt.errorbar(range(301), result3_mean, result3_std, fmt='-o')
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.yticks(np.arange(-256, 100, step=16))
    plt.xticks(np.arange(0, 301, step=20))
    plt.title("Figure4: running realistic simulator 1000 times, mean of winnings with standard deviation", loc='left', fontsize=24, fontweight=0, color='orange')
    plt.ylabel("Winnings")
    plt.xlabel("Spins")
    plt.savefig("Figure4.png")
    
    ############################
    #
    # Experiment 2, Figure 5
    #
    ############################
    
    # plot figure 5
    result3_median = np.median(result3, axis=0)
    result3_std  = np.std(result3, axis=0)
    
    plt.rcParams.update({'font.size': 20})
    plt.style.use('seaborn-darkgrid')
    plt.figure(figsize=(20,10))
    palette = plt.get_cmap('Set1')
    plt.errorbar(range(301), result3_median, result3_std, fmt='-o')
    plt.xlim([0, 300])
    plt.ylim([-256,100])
    plt.yticks(np.arange(-256, 100, step=16))
    plt.xticks(np.arange(0, 301, step=20))
    plt.title("Figure5: running realistic simulator 1000 times, median of winnings with standard deviation", loc='left', fontsize=24, fontweight=0, color='orange')
    plt.ylabel("Winnings")
    plt.xlabel("Spins")
    plt.savefig("Figure5.png")  
 		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
