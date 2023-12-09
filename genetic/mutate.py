import random
from calculate.detect import detect_clause
from calculate.reduction import repeat_reduce
from genetic.generate import generate

def mutate(mutate_list):
    new_mutate_list = []
    for mutate in mutate_list:
        mutate_pos = random.randint(0, len(mutate) - 1)
        _, mutate_range_len = detect_clause(mutate, mutate_pos)
        new_mutate = mutate[:mutate_pos] + generate() + mutate[mutate_pos + mutate_range_len:]
        new_mutate = repeat_reduce(new_mutate)

        if new_mutate != None:

            new_mutate_list.append(new_mutate)

    return new_mutate_list