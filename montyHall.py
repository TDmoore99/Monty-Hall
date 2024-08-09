import numpy as np
import random
from random import randrange, randint

# Seed the random generator to be able to repeat results accuratley
random.seed(42) 

# Function that simulates monty hall opening a door
# remember he knows whats behind each one so wont open the winner
def reveal_unopened_door(winning_door,picked_door,opened_doors):
    # Remember Monty knows
    if 0 != winning_door and 0 != picked_door and not opened_doors[0]:           
        opened_door=0
    if 1 != winning_door and 1 != picked_door and not opened_doors[1]:
        opened_door=1
    if 2 != winning_door and 2 != picked_door and not opened_doors[2]:
        opened_door=2
            
    return opened_door 

# Function to get an unopened door
def get_unopened_door(picked_door,revealed_doors):
    #get the first free door that is not revealed
    for index, value in enumerate(revealed_doors):
        if not (value) and picked_door!=index:            
            return index

# Function to play the game
def execute_round(switch_door):
    #Set the variables
    opened_doors=[False,False,False]
    winning_door = randrange(3) # it can be 0, 1, or 2! We don't know the truth yet.
    picked_door = randrange(3) # it can be 0, 1, or 2! 

    #Monty Hall opens a door
    open_door = reveal_unopened_door(winning_door,picked_door,opened_doors)
    opened_doors[open_door] = True

    # Change your door choice or not
    if (switch_door):
        picked_door = get_unopened_door(picked_door,opened_doors)

    # Did you win
    if (picked_door == winning_door):
        return True
    else:
        return False

# Lets play the game several times switching the door
simulations = 1000000 #number of times to simulate
results = np.zeros(simulations) #a lot of zeros
for i in range(simulations):
    winner = execute_round(True)
    results[i] = int(winner==True)# Convert the bollean output to and int

probability = np.sum(results)/simulations
print ("The probablity of winning when switching doors is",probability,"based on",simulations,"simulations.")
changing_ratios = np.cumsum(results) / (np.arange(1,simulations+ 1))

# Lets play the game several times NOT switching the door
results = np.zeros(simulations) #a lot of zeros
for i in range(simulations):
    winner = execute_round(False)
    results[i] = int(winner==True)# Convert the bollean output to and int

probability = np.sum(results)/simulations
print ("The probablity of winning when not switching doors is",probability,"based on",simulations,"simulations.")
not_changing_ratios = np.cumsum(results) / (np.arange(1,simulations+ 1))

  
