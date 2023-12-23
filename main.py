from genetic.pool import init_pool, transition
from calculate.calculator import fitness_function
from common import TEST_TIMES, GENERATION, TERM

def function1(length=TEST_TIMES):
    return [i+1 for i in range(length)]

def function2(length=TEST_TIMES):
    return [i+2 for i in range(length)]

def function3(length=TEST_TIMES):
    return [i+3 for i in range(length)]

def function4(length=TEST_TIMES):
    return [2*i for i in range(length)]

def function5(length=TEST_TIMES):
    return [i+4 for i in range(length)]

function_list = [function1(), function2(), function3(), function4(), function5()]

def main():
    formulus = init_pool()
    for _ in range(GENERATION):
        fitness = fitness_function(formulus, function_list, TERM)
        # Display the maximum and average value of fitness
        print("Maximum value is {}".format(max(fitness.values())))
        print("Average value is {}".format(sum(fitness.values())/len(fitness)))
        # Check if the maximum value of fitness equals 2 times TEST_TIMES
        if max(fitness.values()) == 2 * TEST_TIMES:
            print("Solution found")
            # Display the formula(s) that have the maximum fitness value
            print("Solution is {}".format([x for x in fitness.keys() if fitness[x] == max(fitness.values())]))                
            break
        # Transition to the next generation of formulas
        formulus = transition(fitness)

if __name__ == "__main__":
    main()