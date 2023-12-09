from calculate.reduction import repeat_reduce
from common import TEST_TIMES

# It might be worth trying to encode with 4 variations by swapping 'S' and 'K'
def encoding(num):
    return 'A' * num + 'K' * (num + 1)

def decoding(term):
    # Find the number of 'A's and 'K's in the term
    num_A = term.count('A')
    num_K = term.count('K')

    # Check if the pattern matches 'A' * num + 'K' * (num + 1)
    if term == 'A' * num_A + 'K' * num_K and num_K - num_A == 1:
        return num_A
    else:
        return None

def squared(length=TEST_TIMES):
    # Generate a list of pairs (i, i^2) for i in range of length
    return [(i, i**2) for i in range(length)]

def calculate(formula):
    results = []
    for num in squared():
        # Apply repeat_reduce function to 'A' + formula + encoded number
        result = repeat_reduce('A' + formula + encoding(num[0]))
        if result == None or decoding(result) != None:
            results.append("undefined")
        elif num[1] != decoding(result):
            results.append("wrong")
        else:
            results.append("correct")          
    
    return results

def fitness_function(formulus):
    fitness = {}
    for formula in formulus:
        # Calculate results for each formula
        results = calculate(formula)
        # Compute the value as 2 times the count of "correct" plus the count of "wrong"
        value = (2 * results.count("correct") + results.count("wrong"))
        # Create a dictionary with formula as key and value as value
        fitness[formula] = value
    return fitness
