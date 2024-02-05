from genetic.pool import init_pool, transition
from common import GENERATION, POOL_SIZE
from calculate.calculator import calculate
import numpy as np
import random

def fitness_function(formulus_history):
    formulus_value = {}
    for formula, results in formulus_history.items():

        not_none = np.array([el != -1 for el in results.flatten()])
        valid_value = np.count_nonzero(not_none)
        #改良の余地ありそう(同じ要素が同じ位置にあったらそれでペナルティを課すとか)
        count_ones = sum(np.array_equal(results, other_results) for other_results in formulus_history.values())

        assert count_ones != 0
        value = valid_value / count_ones
        
        formulus_value[formula] = value
    return formulus_value


def main():
    formulus = init_pool()
    formulus_history = {formula: calculate(formula) for formula in formulus}

    formulus_value = fitness_function(formulus_history)

    for _ in range(GENERATION):

        # Transition to the next generation of formulas
        print(formulus)
        print("Maximum value is {}".format(max(formulus_value.values())))
        max_value_formula = [key for key, value in formulus_value.items() if value == max(formulus_value.values())]
        print("Term with maximum value is {}".format(max_value_formula))
        #max_value_formulaのformulus_historyでのvalueを全てprint
        print("Representation with maximum value is {}".format([formulus_history[formula] for formula in max_value_formula]))
        
        formulus = transition(formulus)
        # Update formulus_history(もしformulus_historyにformulaがなければ追加)
        for formula in formulus:
            if formula not in formulus_history:
                formulus_history[formula] = calculate(formula)

        #formulus_valueから上位POOL_SIZE個のformulaを選んでlistにする
        formulus = [x[0] for x in sorted(formulus_value.items(), key = lambda x : (x[1], random.random()), reverse=True)][:POOL_SIZE]

        formulus_value = fitness_function(formulus_history)
        
        #print(formulus_history)
if __name__ == "__main__":
    main()