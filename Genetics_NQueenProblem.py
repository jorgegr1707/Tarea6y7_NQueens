import random

population_size = 100
mutation_percent = 0.02 
limit_gens = 50
population = []
offsprings = []
fitness = []
fitness_new = []

#Function that adds the individual to a generatio and calculates fitness
def add_individual(child, new_or_old): 
    #new is 1, old is 0 
    if (new_or_old==0): 
        population.append(child)
        fitness.append(check(child))
        
    else: 
        offsprings.append(child)
        fitness_new.append(check(child))
        

#Function that generate the population, also evaluates it 
def generate_population(): 
    for i in range(population_size):
        #generates only one
        individual = []
        for j in range(8):
            #adding the genes
            individual.append(random.randint(0,7))
        #add to the population or group 
        #adds the fitness to the fitness array that corresponds to population too. 
        add_individual(individual, 0)
        

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
    #print(collisions)
    return collisions

#Function that does the mutation in a % of the population 
def mutate():
    mutation = 0.02
    for i in range (int(population_size * mutation)):
        individual = population[random.randint(0, population_size)]  #choose a random individual
        individual[random.randint(0,7)] = random.randint(0,7) #change a random gen

#Other approach to mutate 
def mutate_after_creation(child): 
    for i in range(len(child)): 
        random_mutate = random.randint(0,100) / 100
        if (random_mutate < mutation_percent): 
            child[random.randint(0,7)] = random.randint(0,7) #change a random gen 
    add_individual(child, 1)

#Function that represents the process of selection, which 
def tournament_selection():
    cant_selection = 15  #number of individuals to selectionate
    random_selection = random.sample(list(enumerate(fitness)),cant_selection)
    #print(random_selection)
    best_fitness = min(random_selection, key = lambda t: t[1]) #minimun fitness on the sample, tuple = (index, fitness)
    #print(best_fitness)
    best_individual = population[best_fitness[0]]
    return best_individual
    

#Function that combines the father and the mother, returns two childs 
def crossover(father, mother):
    pos = random.randint(1,7)
    child_one = father[:pos]+mother[pos:]
    child_two = mother[:pos]+father[pos:]
    #return (child_one, child_two)
    mutate_after_creation(child_one)
    mutate_after_creation(child_two)

def create_new_population(): 
    for i in range(population_size):
        best_1 = tournament_selection()
        best_2 = tournament_selection()
        crossover(best_1,best_2)
    global population
    global offsprings
    global fitness
    global fitness_new
    #print(population)
    #print(offsprings)
    print(sum(fitness))
    print(sum(fitness_new))
    print("quak")
    population = offsprings
    fitness = fitness_new
    offsprings = [] 
    fitness_new = [] 
    
    
    
def main():
    generate_population()
    for i in range(limit_gens): 
        create_new_population()
    solution = [6, 4, 2, 0, 5, 7, 1, 3] 
    print(check(solution))
    

if __name__ == "__main__":
    main()
