import random
from genetic.generate import generate
from genetic.mutate import mutate
from genetic.crossover import crossover
from calculate.reduction import repeat_reduce
from common import POOL_SIZE, ELITE_RATE, CROSSOVER_RATE, MUTATE_RATE

def init_pool(size=POOL_SIZE):
    formulus = []

    while True:
        formula = repeat_reduce(generate())
        if formula != None:
            if formula not in formulus:
                formulus.append(formula)
            if len(formulus) == size:
                return formulus

def transition(formulus, elite_rate=ELITE_RATE, crossover_rate=CROSSOVER_RATE, mutate_rate=MUTATE_RATE):
    #formulus = [x[0] for x in sorted(formulus_results.items(), key = lambda x : (x[1], random.random()), reverse=True)]
    #crossoverする個体をピックアップ(formulus_resultsからランダムで２つ組を選ぶのをlen(formulus_results)*crossover_rate回繰り返す)
    crossover_pair_list = []
    for _ in range(int(len(formulus)*crossover_rate)):
        crossover_pair_list.append(random.sample(formulus, 2))
        #crossover_pair_list.append(random.sample(formulus[:int(len(formulus)*elite_rate)], 2))
    new_crossover_pair_list = crossover(crossover_pair_list)
    #リストをflattenにして重複を削除
    new_crossover_list = []
    for x in new_crossover_pair_list:
        new_crossover_list.append(x)
    
    #mutateする個体をピックアップ(formulus_resultsからランダムで一つを選ぶのをlen(formulus_results)*mutate_rate回繰り返す)
    mutate_list = []
    for _ in range(int(len(formulus)*mutate_rate)):
        mutate_list.append(random.choice(formulus))
        #mutate_list.append(random.choice(formulus[:int(len(formulus)*elite_rate)]))
    new_mutated_list = mutate(mutate_list)

    new_formulus = list(set(formulus[:int(len(formulus)*elite_rate)] + new_crossover_list + new_mutated_list))
    """
    #new_formulusの要素数がlen(formulus)より多い場合はlen(new_formulus) == len(formulus)になるまでランダムで削除
    if POOL_SIZE < len(new_formulus):
        for _ in range(len(new_formulus) - POOL_SIZE):
            new_formulus.remove(random.choice(new_formulus))
    """
    #len(formulus)にnew_formulusの要素数が足りない場合はelite以外からランダムに重複がないように選ぶ
    while len(new_formulus) < POOL_SIZE:
        x = random.choice(formulus)
        if x not in new_formulus:
            new_formulus.append(x)

    return new_formulus