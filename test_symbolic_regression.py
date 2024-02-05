from genetic.pool import init_pool, transition
from common import TEST_TIMES, GENERATION
from calculate.reduction import repeat_reduce
from calculate.calculator import encoding, decoding

def function1(length=TEST_TIMES):
    return [i+1 for i in range(length)]

def function2(length=TEST_TIMES):
    return [2*i for i in range(length)]

def function3(length=TEST_TIMES):
    return [i*i for i in range(length)]

def function4(length=TEST_TIMES):
    return [i-1 if i != 0 else 0 for i in range(length)]

function_list = [function1(), function2(), function3(), function4()]

def calculate_symbolic(formula):
    results = []
    for num in range(TEST_TIMES):
        # Apply repeat_reduce function to 'A' + formula + encoded number
        result = repeat_reduce('A' + formula + encoding(num))

        if result == None or decoding(result) == None:
            results.append("undefined")
        else:
            results.append(decoding(result))       
    
    return results

def fitness_function_symbolic(formulus, values_list):
    fitness = {}
    for formula in formulus:
        # Calculate results for each formula
        results = calculate_symbolic(formula)

        gain_list = []
        # Compare the results with the values in values_list
        for values in values_list:
            for i in range(len(values)):
                if results[i] == "undefined":
                    continue
                elif results[i] == values[i]:
                    results[i] = "correct"
                else:
                    results[i] = "wrong"
                # Compute the value as 2 times the count of "correct" plus the count of "wrong"
            gain_list.append(2 * results.count("correct") + results.count("wrong"))

        # Create a dictionary with formula as key and value as value
        fitness[formula] = max(gain_list)
    return fitness

def main():
    formulus = init_pool()
    for _ in range(GENERATION):
        fitness = fitness_function_symbolic(formulus, function_list)
        # Display the maximum and average value of fitness
        print("Maximum value is {}".format(max(fitness.values())))
        print("Term with maximum value is {}".format([key for key, value in fitness.items() if value == max(fitness.values())]))

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