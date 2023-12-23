from calculate.reduction import repeat_reduce
from common import TEST_TIMES

def encoding(num,term):
    return ('A'+ term) * num + term

def decoding(expression,term):
    for num in range(TEST_TIMES):
        if expression == ('A'+ term) * num + term:
            return num
    return None
    
def calculate(formula, term):
    results = []
    for num in range(TEST_TIMES):
        # Apply repeat_reduce function to 'A' + formula + encoded number
        result = repeat_reduce('A' + formula + encoding(num, term))

        if result == None or decoding(result,term) == None:
            results.append("undefined")
        else:
            results.append(decoding(result,term))       
    
    return results

def fitness_function(formulus, values_list, term):
    fitness = {}
    for formula in formulus:
        # Calculate results for each formula
        results = calculate(formula, term)

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