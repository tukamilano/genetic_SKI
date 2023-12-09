import random
from genetic.generate import generate
from genetic.mutate import mutate
from genetic.crossover import crossover
from calculate.reduction import repeat_reduce
from common import POOL_SIZE


def init_pool(size=POOL_SIZE):
    formulus = []

    while True:
        formula = repeat_reduce(generate())
        if formula != None:
            if formula not in formulus:
                formulus.append(formula)
            if len(formulus) == size:
                return formulus

def transition(formulus_results, elite_rate=0.2, crossover_rate=0.2, mutate_rate=0.3):

    #formulus_resultsを昇順に揃える
    formulus = [x[0] for x in sorted(formulus_results.items(), key = lambda x : x[1], reverse=True)]

    #crossoverする個体をピックアップ(formulus_resultsからランダムで２つ組を選ぶのをlen(formulus_results)*crossover_rate回繰り返す)
    crossover_list = []
    for _ in range(int(len(formulus)*crossover_rate)):
        crossover_list.append(random.choice(formulus))
    new_crossover_list = crossover(crossover_list)
    #formulus_resultsと重なっているnew_crossover_listの要素をmutated_listから削除
    for x in formulus:
        if x in new_crossover_list:
            new_crossover_list.remove(x)
    
    #mutateする個体をピックアップ(formulus_resultsからランダムで一つを選ぶのをlen(formulus_results)*mutate_rate回繰り返す)
    mutate_list = []
    for _ in range(int(len(formulus)*mutate_rate)):
        mutate_list.append(random.choice(formulus))
    new_mutated_list = mutate(mutate_list)
    #formulus_resultsとmutated_listのどちらかと重なっているmutated_listの要素をmutated_listから削除
    for x in formulus:
        if x in new_mutated_list:
            new_mutated_list.remove(x)
    for x in new_crossover_list:
        if x in new_mutated_list:
            new_mutated_list.remove(x)

    new_formulus = formulus[:int(len(formulus)*elite_rate)] + new_crossover_list + new_mutated_list
    #len(formulus)にnew_formulusの要素数が足りない場合はelite以外からランダムに重複がないように選ぶ
    while len(new_formulus) < len(formulus):
        x = random.choice(formulus)
        if x not in new_formulus:
            new_formulus.append(x)

    return new_formulus