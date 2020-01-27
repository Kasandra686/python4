from functools import reduce


def reducer_func(el_prev, el):
    return el_prev + el


list = {el for el in range(100, 1001) if el % 2 == 0}
print(reduce(reducer_func, list))
