#!/usr/bin/env python
# -*- coding: utf-8 -*-
#prueba e.e

import random

linux_flag = 1
board_size = 8
population_size = 100
mutation_percent = 0.02
limit_gens = 500
eliticism = 0
population = []
offsprings = []
fitness = []
fitness_new = []
cant_selected = int(population_size * 0.1)

#colors of the board (only in linux)
class bcolors:
	RED	   =	'\033[91m'
	GREEN  =	'\033[92m'
	BLACK  =	'\033[30m'
	WHITE  =	'\033[0m'


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
        for j in range(board_size):
            #adding the genes
            individual.append(random.randint(0,board_size-1))
        #add to the population or group 
        #adds the fitness to the fitness array that corresponds to population too. 
        add_individual(individual, 0)
        

#Function that returns the total of collisions of an individual
def check(individual):
    collisions = 0
    #Check collisions in row
    for i in range(board_size):
        if i not in individual:
            collisions += 1

    #Check collisions in diagonals
    for i in range(0,board_size-1):
    
        #Check right upper
        for j, k in zip(range(individual[i]-1,-1,-1), range(i+1,board_size)):
            if individual[k] == j:
                collisions += 1
                break
                
        #Check right lower
        for j, k in zip(range(individual[i]+1,board_size), range(i+1,board_size)):
            if individual[k] == j:
                collisions += 1
                break
                
    return collisions


#Function that mutate child 
def mutate_after_creation(child): 
    for i in range(len(child)): 
        random_mutate = random.randint(0,100) / 100
        if (random_mutate < mutation_percent): 
            child[random.randint(0,board_size-1)] = random.randint(0,board_size-1) #change a random gen 
    add_individual(child, 1)

#Function that represents the process of selection, which 
def tournament_selection():
    
    random_selection = random.sample(list(enumerate(fitness)),cant_selected)
    #print(random_selection)
    best_fitness = min(random_selection, key = lambda t: t[1]) #minimun fitness on the sample, tuple = (index, fitness)
    #print(best_fitness)
    best_individual = population[best_fitness[0]]
    return best_individual


def elitism():
    list_index_fitness = list(enumerate(fitness))
    best = sorted(list_index_fitness, key = lambda t: t[1])
    best = best[:cant_selected]
    for i in best:
        add_individual(population[i[0]],1)
    
    
    

#Function that combines the father and the mother, returns two childs 
def crossover(father, mother):
    pos = random.randint(1,6)
    child_one = father[:pos]+mother[pos:]
    child_two = mother[:pos]+father[pos:]
    #return (child_one, child_two)
    mutate_after_creation(child_one)
    mutate_after_creation(child_two)

def create_new_population(): 
    global population
    global offsprings
    global fitness
    global fitness_new
    if (eliticism == 1): 
        for i in range(int((population_size - cant_selected)/2)):
            best_1 = tournament_selection()
            best_2 = tournament_selection()
            crossover(best_1,best_2)
        elitism()
    else: 
        for i in range(int(population_size/2)):
            best_1 = tournament_selection()
            best_2 = tournament_selection()
            crossover(best_1,best_2)
    population = offsprings
    fitness = fitness_new
    offsprings = [] 
    fitness_new = [] 
    
    
   
def get_matrix_solution(solution): 
    matrix = []
    len_sol = len(solution)
    for i in range(len_sol): 
        row = []
        for j in range(len_sol): #row
            if (i != solution[j]):
                row.append(0)
            else: 
                row.append(1)
        matrix.append(row)
    return matrix
    
def print_solution(solution):
    matrix_solution = get_matrix_solution(solution)
    matrix_cont = 0 
    
    #Condition if program running in Windows OS
    if not linux_flag:
    	bcolors.RED = ""
    	bcolors.WHITE = ""
    	bcolors.GREEN = ""
    	bcolors.BLACK = ""
    	
    for i in range(board_size*2+1): #para futuro deberia ser solution * 2 - 1
        if (i == 0):
            print(bcolors.RED + "  " + " - ".join("+" for i in range(board_size+1)) + bcolors.WHITE)
        elif (i%2 != 0):
            answer = " " + bcolors.RED + " |" + bcolors.WHITE 
            row = matrix_solution[matrix_cont]
            for j in range(len(solution)):
                answer += " "
                if(row[j] == 0 and (matrix_cont+j) %2 == 1): answer += bcolors.BLACK
                if(row[j] == 1):answer += bcolors.GREEN
                answer += str(row[j]) + bcolors.RED + " |" + bcolors.WHITE
            answer += "  " + str(matrix_cont)
            matrix_cont += 1 
            print(answer)
        elif (i%2 == 0):
            print(bcolors.RED + "  " + " - ".join("+" for i in range(board_size+1)) + bcolors.WHITE)
             
def is_int(number):
    try:
        int(number)
        return True
    
    except ValueError:
        return False

def choose_option():
    option = input("Choose option: ")
    if is_int(option):
        option = int(option)
        if 0 < option < 3:
            return option
            
    input("Incorrect value, press ENTER to go back")
    option = choose_option()
    return option


def modify_board_size():
    global board_size
    b_size = input("Enter board size (minimum 4): ")
    if is_int(b_size):
        b_size = int(b_size)
        if b_size >= 4:
            board_size = b_size
        else:
            input("Board should be bigger, press ENTER to go back")
            modify_board_size()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_board_size()


def modify_population_size():
    global population_size
    global cant_selected #int(population_size * 0.1)
    
    p_size = input("Enter population size (minimum 50): ")
    if is_int(p_size):
        p_size = int(p_size)
        if p_size >= 50:
            population_size = p_size
            cant_selected = int(population_size * 0.1)
        else:
            input("Population should be bigger, press ENTER to go back")
            modify_population_size()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_population_size()
            

def modify_mutation_percent():
    global mutation_percent    
    m_size = input("Enter mutation percent (1-5): ")
    if is_int(m_size):
        m_size = int(m_size)
        if 1 <= m_size <= 5:
            mutation_percent = m_size/100
        else:
            input("Outside the range of allowed values, press ENTER to go back")
            modify_mutation_percent()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_mutation_percent()


def modify_limit_gens():
    global limit_gens
    g_size = input("Enter generations limit (minimum 50): ")
    if is_int(g_size):
        g_size = int(g_size)
        if g_size >= 50:
            limit_gens = g_size
        else:
            input("Outside the range of allowed values, press ENTER to go back")
            modify_limit_gens()
    else:
        input("Incorrect value, press ENTER to go back")
        modify_limit_gens()


def modify_elitism():
    global eliticism
    e_value = input("Elitism? (yes:1 no:0): ")
    if is_int(e_value):
        e_value = int(e_value)
        if e_value == 0 or e_value == 1:
            eliticism = e_value
    else:
        input("Incorrect value, press ENTER to go back")
        modify_elitism()


def choose_step_print():
    option = input("Want to print step by step? (yes:1 no:0): ")
    if is_int(option):
        option = int(option)
        if 0 <= option < 2:
            return option
            
    input("Incorrect value, press ENTER to go back")
    option = choose_option()
    return option

            
def main():
    solution = 0
    print("\nN-Queen Problem Solution using genetics\n")
    print("To start the program choose the types of values to use\n")
    print("\n 1.Default values(*)\n 2.Custom values")
    print("\n(*)Default values: \n\t-Board size: 8 \n\t-Population: 100 individuals\n\t-Generations: 500",
    	"\n\t-Percent mutation: 2% \n\t-Elitism:No apply\n")
    option = choose_option()
    
    if option == 2:
        modify_board_size()
        modify_population_size()
        modify_limit_gens()
        modify_mutation_percent()
        modify_elitism()
    
    steps_flag = choose_step_print()
    generate_population()
    for i in range(limit_gens): 
        create_new_population()
        if steps_flag:
            best_fitness = min(fitness)
            index = fitness.index(best_fitness)
            best_gen = population[index] 
            print("\nGeneration: "+ str(i))
            print("  Best gen: " + str(population[index]) + ", fitness: " + str(best_fitness))
        if 0 in fitness:
            print("\nThere IS a solution in the population. \nStats:")
            #print("Number of individuals: " + str(population_size))
            print("Number of generations executed: " + str(i) + " of " + str(limit_gens))
            #print("Mutation percent: " + str(mutation_percent))
            index = fitness.index(0)
            print("Short answer: " + str(population[index]))
            print("\nLong answer: \n1: queens\n0: blank space")
            print_solution(population[index])
            solution = 1
            break
    if(solution == 0): 
        print("There was no solution in the final population.")
        #print("Number of individuals: " + str(population_size))
        #print("Number of generations executed: " + str(limit_gens))
        #print("Mutation percent: " + str(mutation_percent))


if __name__ == "__main__":
    main()
    
