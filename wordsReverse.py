# -*- coding: cp936 -*-
#�ַ��������ʷ�ת�����뱣�����пո�'I love China!'ת��Ϊ"China! love I"
from __future__ import print_function
str = 'I love China!'
str_1 = ''
tup = []
for i in str: 
    if i is ' ' :
        tup.append(str_1)
        str_1 = ''
    elif i is str[-1] :
        str_1 += i
        tup.append(str_1)
    else :
        str_1 += i
tup.reverse()
for i in tup :
    print(i, end = ' ') #����print������
