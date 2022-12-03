def print_result(f):
    def wrapper(a):
        print(f.__name__)
        res = f(a)
        if type(res) == list:
            for i in res:
                print(i)
        elif type(res) == dict:
            for k,v in res.items():
                print(k, '=', v)
        elif type(res) == int or type(res) == str:
            print(res)
        elif type(res) == zip:
            for name, number in res:
                print(name, number)
        else:
            print("nothing to show")
        return res
    return wrapper

def print_result1(f):
    print(f.__name__)
    res = f()
    if type(res) == list:
        for i in res:
            print(i)
    elif type(res) == dict:
        for k,v in res.items():
            print(k, '=', v)
    elif type(res) == int or type(res) == str:
        print(res)
    else:
        print("nothing to show")
    return res


@print_result1
def test_1():
    return 1


@print_result1
def test_2():
    return 'iu5'


@print_result1
def test_3():
    return {'a': 1, 'b': 2}


@print_result1
def test_4():
    return [1, 2]




