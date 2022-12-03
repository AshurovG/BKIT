import json
from unique import Unique
from field import field
from operator import concat
from gen_random import gen_random
from print_result import print_result
from cm_timer import cm_timer_1


@print_result
def f1(a):
    return Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True)


@print_result
def f2(a):
    return filter(lambda a: a.startswith('программист'), a)


@print_result
def f3(a):
    return list(map(lambda x: concat(x, ' c опытом Python'), a))


@print_result
def f4(a):
    c = zip(a, gen_random(len(a), 100000, 200000))
    return c


with open('data_light.json', "r", encoding="utf-8") as f:
    data = json.loads(f.read())
    with cm_timer_1():
        (f4(f3(f2(f1(data)))))
