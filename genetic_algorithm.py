###### Python Imports ########

#import numpy
import random


###### INITIAL POPULATION #######

population = [[1,2],[-2,3],[4,-1],[5,2],[-3,3]]


####### Fitness Function #########

def random_fitness(population):

    return random.sample(population,4)


