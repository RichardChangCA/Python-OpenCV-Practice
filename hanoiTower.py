#实现递归函数解决hanoi塔问题
def my_hanoi(n, A, B, C): #n个盘子从A放到B借助C
    if (n == 1):
        print(A  + ' -> ' + B)
    else:
        my_hanoi(n-1, A, C, B)
        print(A + ' -> ' + B)
        my_hanoi(n-1, C, B, A)


my_hanoi(5, 'source', 'target', 'transfer')
