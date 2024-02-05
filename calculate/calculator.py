from common import TEST_TIMES, LIMIT_NUM, ONE_TERM, ZERO_TERM, TERM
from calculate.reduction import repeat_reduce
import numpy as np

def encoding(num):
    if num == 0:
        return ZERO_TERM
    else:
        return ('A' + TERM) * (num - 1) + ONE_TERM

def decoding(expression):
    for num in range(LIMIT_NUM):
        if expression == ZERO_TERM:
            return 0
        if expression == ('A'+ TERM) * num + ONE_TERM:
            return num + 1
    return None

def calculate(formula):
    results = np.zeros((TEST_TIMES, TEST_TIMES), dtype=int)
    for num_0 in range(TEST_TIMES):
        for num_1 in range(TEST_TIMES):
            result = repeat_reduce('AA' + formula + encoding(num_0) + encoding(num_1))
            if result == None or decoding(result) == None:
                results[num_0][num_1] = -1
            else:
                results[num_0][num_1] = decoding(result)
    
    return results