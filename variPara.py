#自己实现一个函数支持可变参数
from __future__ import print_function
def info_input(identity, name, sex, addr, *more_detail):
    print(identity, end = ' ')
    print(name, end = ' ')
    print(sex, end = '')
    print(addr, end = ' ')
    print(more_detail)

info_input(2649, 'Richard', 'male', 'Tianjin', 'sports', 'movie')

def info_input_2(identity, name, sex, addr, *tup, **dic):
    print(identity, end = ' ')
    print(name, end = ' ')
    print(sex, end = '')
    print(addr, end = ' ')
    print(tup)
    print(dic)

info_input_2(2649, 'Lingfeng', 'male', 'Tianjin', 'sports', 'movie', **{'math':99 , 'PE':98})
info_input_2(2649, 'Lingfeng', 'male', 'Tianjin', 'sports', 'movie', {'math':99 , 'PE':98})
info_input_2(2649, 'Lingfeng', 'male', 'Tianjin', *('sports', 'movie'), **{'math':99 , 'PE':98})
