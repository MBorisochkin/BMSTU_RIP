import json
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

path = '../data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(list(field(arg, 'job-name')), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda value: value.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda value: value + " с опытом Python", arg))


@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    return list(map(lambda value: value[0] + ', зарплата: ' + str(value[1]) + ' руб', list(zip(arg, salary))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
