#ʵ�ֵݹ麯�����hanoi������
def my_hanoi(n, A, B, C): #n�����Ӵ�A�ŵ�B����C
    if (n == 1):
        print(A  + ' -> ' + B)
    else:
        my_hanoi(n-1, A, C, B)
        print(A + ' -> ' + B)
        my_hanoi(n-1, C, B, A)


my_hanoi(5, 'source', 'target', 'transfer')
