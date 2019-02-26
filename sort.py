#实现一个sort函数，通过参数指定比较函数用来实现按不同顺序进行排序，冒泡排序
from __future__ import print_function
def bubble_sort_low(lis):
    for n in range(len(lis)-1):
        for i in range(len(lis)-n-1):
            j=i+1
            if(lis[i] > lis[j]):
                x=lis[i]
                lis[i]=lis[j]
                lis[j]=x
    for i in lis:
            print(i, end='')


def bubble_sort_high(lis):
    for n in range(len(lis)-1):
        for i in range(len(lis)-n-1):
            j=i+1
            if(lis[i] < lis[j]):
                x=lis[i]
                lis[i]=lis[j]
                lis[j]=x
    for i in lis:
            print(i, end='')


def bubble_sort(lis, index):
    if(index == 1):
        bubble_sort_low(lis)
    else:
        bubble_sort_high(lis)


bubble_sort([2,4,5,6,1,3,9,8,7], 1)
print('\nLingfeng')
bubble_sort([2,4,5,6,1,3,9,8,7], 0)
