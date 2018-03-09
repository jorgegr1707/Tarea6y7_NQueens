from random import randint

population_size = 100
population = []
fitness = []

#Function that returns the total of collisions of an individual
def check(individual):

    collisions = 0

    #Check collisions in row
    for i in range(1,9):
        if i not in individual:
            collisions += 1

    #Check collisions in diagonals
    for i in range(0,7):

        #Check right upper
        for j, k in zip(range(individual[i]-1,-1,-1), range(i+1,8)):
            if individual[k] == j:
                collisions += 1

        #Check right lower
        for j, k in zip(range(individual[i]+1,8), range(i+1,8)):
            if individual[k] == j:
                collisions += 1
            
    print(collisions)
    return collisions


def mutate():

    mutation = 0.02
    for i in range (int(population_size * mutation)):
        individual = population[randint(0, population_size)]  #choose a random individual
        individual[randint(0,7)] = randint(0,7) #change a random gen


def tournament_selection():

    cant_selection = 15  #number of individuals to selectionate
    random_selection = random.sample(list(enumerate(fitness)),cant_selection)
    best_fitness = min(random_selection, key = lambda t: t[1]) #minimun fitness on the sample, tuple = (index, fitness)
    best_individual = population[best_fitness[0]]
    return best_individual


def crossover(father, mother):

    pos = randint(1,7)
    child_one = father[:pos]+mother[pos:]
    child_two = mother[:pos]+father[pos:]
    return (child_one, child_two)


def main():

    
    #Generate population
    #TODO: Maybe we could use a function that generate the population instead
    #      of the main
    for i in range(population_size):
        individual = []
        for j in range(8):
            individual.append(randint(0,7))
        population.append(individual)
        fitness.append(check(population[i]))

if __name__ == "__main__":
    main()
