###### Python Imports ########

import numpy
import random
import eq_max

####### Fitness Function #########

function = lambda x,y : (x)**2 + (y)**2

def fitness(function,chromosome):

    fitness_val = function(chromosome[0],chromosome[1])

    return fitness_val

####### Parents Tournament Selection #########

def binary_tournament(parent_a,parent_b):


    if(fitness(function,parent_a) > fitness(function,parent_b)):

        return parent_a
    else :

        return parent_b

    return None

######## Crossover #############
def crossover(parent_a,parent_b):

    offspring = [parent_a[0],parent_b[1]]

    mutate_chromosome(offspring)

    return offspring
    

########## Mutation  ###############


def mutate_chromosome(chromosome):


    # If random umber is between 0 and mutation percentage than mutate
    if 0 <= random.uniform(0, 1) <= 0.5:
        # Swap members at given indices
        chromosome[0], chromosome[1] = chromosome[1], chromosome[0]

         return chromosome
    else :

         return chromosome

   


##### Truncation ########

def truncate(population):

    population.sort(key=eq_max.function_init,reverse=True)
    del population[5:]

    return population










