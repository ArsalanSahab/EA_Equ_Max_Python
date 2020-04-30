####### IMPORTS ########

import random
import genetic_algorithm as ga



'''
Problem : Maxmise Output of given equation

Given Equation : x^2 + y^2

Techniques : Evolutionary Algortihm > Genetic Algorithm
Sub-Techniques Required : 

    1. Parent Selection > Binary Tournament
    2. Crossover 
    3. Mutation
    4. Survivor Selection > Truncation

Extra Info : 

    1. Produce 4 Off Springs
    2. CrossOver = x(Parent 1), y(Parent 2)
    3. Mutation Rate = 50%
    4. 20 Generations


Initial Generation :

Chromosome 1 = {1,2}
Chromosome 2 = {-2,3}
Chromosome 3 = {4,-1}
Chromosome 4 = {5,2}
Chromosome 5 = {-3,3}



'''




def function_init(chromosome):

    return ((chromosome[0]*chromosome[0]) + (chromosome[1]*chromosome[1]))



def ga_driver(population):


    new_generation = []

    for i in range(20):

        for j in range(3):

            # Get 4 Random numbers

            index_1 = random.randint(0,3)
            index_2 = random.randint(0,3)
            index_3 = random.randint(0,3)
            index_4 = random.randint(0,3)

            
            #print("Index 1 = " + str(index_1))
           


            # Perform Binary Tournament

            parent_1 = ga.binary_tournament(population[index_1],population[index_3])
            parent_2 = ga.binary_tournament(population[index_4],population[index_2])


            # Generate OffSprings 

            offspring_1 = ga.crossover(parent_1,parent_2)
            offspring_2 = ga.crossover(parent_2,parent_1)


            new_generation.append(offspring_1)
            new_generation.append(offspring_2)

        population = new_generation
        
        ga.truncate(population)

        print("Current Generation Statistics : " )
        print("Generation = " + str((i+1)))
        print("Elements : " ,population)
        print("Highest Fitness Value = " + str(ga.fitness(ga.function,population[0])))







def main():


    ###### INITIALISATIONS #######

    population = [[1,2],[-2,3],[4,-1],[5,2],[-3,3]]
   
    #function = lambda x,y : (x)**2 + (y)**2

    population.sort(key=function_init,reverse=True)

    print("Current Generation Statistics : " )
    print("Generation = 0")
    print("Elements : " ,population)
    print("Highest Fitness Value = " + str(ga.fitness(ga.function,population[0])))


    ga_driver(population)








if __name__ == "__main__":

    main()
