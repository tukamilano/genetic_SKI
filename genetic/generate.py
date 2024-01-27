import random
from common import GENERATE_MAX_DEPTH

def generate(depth=0, max_depth=GENERATE_MAX_DEPTH):
    s = random.randint(0,1)
    depth += 1
    if s == 0 or depth == max_depth:
        t = random.randint(0,2)
        if t == 0:
            x = 'S'
        elif t == 1:
            x = 'K' 
        elif t == 2:
            x = 'I'
    else:
        x = 'A' + generate(depth) + generate(depth)
    return x 