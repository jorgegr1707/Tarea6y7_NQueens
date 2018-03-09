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
