'''
Problem : Maxmise Output of given equation

Given Equation : 2x + 2y

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

print("this shit is workin bro")

 '''
    parents = numpy.empty((num_parents, population.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness_val == numpy.max(fitness_val))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = population[max_fitness_idx, :]
        fitness_val[max_fitness_idx] = -99999999999

    return parents '''