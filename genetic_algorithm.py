###### Python Imports ########

import numpy
import random


###### INITIALISATIONS #######

population = [[1,2],[-2,3],[4,-1],[5,2],[-3,3]]
#population.astype(int)
function = lambda x,y : (x)*2 + (y)*2


####### Fitness Function #########

def fitness(chromosome):

    fitness_val = function(chromosome[0],chromosome[1])

    return fitness_val

####### Parents Tournament Selection #########

def binary_tournament(parent_a,parent_b):


    if(fitness(parent_a) > fitness(parent_b)):

        return parent_a
    else :

        return parent_b

######## Crossover #############
def crossover(parent_a,parent_b):

    offspring = [parent_a[0],parent_b[1]]

    return offspring
    

########## Mutation  ###############

def random_ind_gen(chromosome):

    return random.randint(0, len(chromosome) - 1), random.randint(0, len(chromosome) - 1)

def mutate_population(population):

    mutated_population = []

    for chromosome in population :

        if 0 <= random.uniform(0, 1) <= 0.5:

            mutated_chromosome = mutate_chromosome(chromosome)

            mutate_population.append(mutated_chromosome)

        else :

            mutated_population.append(chromosome)


def mutate_chromosome(chromosome,index):

    index_1, index_2 = index

    # Swap members at given indices
    chromosome[index_1], chromosome[index_2] = chromosome[index_2], chromosome[index_1]

    return chromosome





print(crossover(parents_tournament(population,random_fitness(population)),4))

