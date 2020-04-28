###### Python Imports ########

import numpy
import random


###### INITIALISATIONS #######

population = [[1,2],[-2,3],[4,-1],[5,2],[-3,3]]
#population.astype(int)
function = lambda x,y : (x)*2 + (y)*2


####### Fitness Function #########

def random_fitness(population):

    fitness_val_list = [function(i[0], i[1]) for i in population]
    return fitness_val_list

####### Parents Tournament Selection #########

def parents_tournament(population,fitness_scores_list):

        selected_parents = []
        population_size = len(fitness_scores_list)

    
        for i in range(0, population_size):

            # Take two parent 
            parent_1 = random.randint(0, len(fitness_scores_list) - 1)
            parent_2 = random.randint(0, len(fitness_scores_list) - 1)

            # Compare scores
            # The parent with the higher fitness wins
            if fitness_scores_list[parent_1] > fitness_scores_list[parent_2]:
                ch_winner = population[parent_1]
            else:
                ch_winner = population[parent_2]

            # Add to list
            selected_parents.append(ch_winner)

        return selected_parents




print(parents_tournament(population,random_fitness(population)))

