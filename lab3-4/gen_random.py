from random import randint


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)


d = gen_random(2, 100, 500)
for i in d:
    print(i)
