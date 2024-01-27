from calculate.reduction import repeat_reduce
from common import TEST_TIMES, ONE_TERM, ZERO_TERM, TERM

def encoding(num):
    if num == 0:
        return ZERO_TERM
    else:
        return ('A' + TERM) * (num - 1) + ONE_TERM

def decoding(expression):
    for num in range(TEST_TIMES):
        if expression == ZERO_TERM:
            return 0
        if expression == ('A'+ TERM) * num + ONE_TERM:
            return num + 1
    return None
    
def calculate(formula):
    results = []
    for num in range(TEST_TIMES):
        # Apply repeat_reduce function to 'A' + formula + encoded number
        result = repeat_reduce('A' + formula + encoding(num))

        if result == None or decoding(result) == None:
            results.append("undefined")
        else:
            results.append(decoding(result))       
    
    return results

def fitness_function(formulus, values_list):
    fitness = {}
    for formula in formulus:
        # Calculate results for each formula
        results = calculate(formula)

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