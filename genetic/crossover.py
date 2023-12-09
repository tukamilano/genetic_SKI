import random
from calculate.detect import detect_clause
from calculate.reduction import repeat_reduce

def crossover(crossover_list):
    new_crossover_list = []
    for crossover_pair in crossover_list:
        crossover_pos_0 = random.randint(0, len(crossover_pair[0]) - 1)
        crossover_pos_1 = random.randint(0, len(crossover_pair[1]) - 1)
        crossover_range_0, crossover_range_len_0 = detect_clause(crossover_pair[0], crossover_pos_0)
        crossover_range_1, crossover_range_len_1 = detect_clause(crossover_pair[1], crossover_pos_1)

        new_crossover_0 = crossover_pair[0][:crossover_pos_0] + crossover_range_1 + crossover_pair[0][crossover_pos_0 + crossover_range_len_0:]
        new_crossover_0 = repeat_reduce(new_crossover_0)
        if new_crossover_0 != None:
            new_crossover_list.append(new_crossover_0)

        new_crossover_1 = crossover_pair[1][:crossover_pos_1] + crossover_range_0 + crossover_pair[1][crossover_pos_1 + crossover_range_len_1:]
        new_crossover_1 = repeat_reduce(new_crossover_1)

        if new_crossover_1 != None:
            new_crossover_list.append(new_crossover_1)

    return new_crossover_list