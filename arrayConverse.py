"""����ת������������A�������B��ÿ��Ԫ��B[i][j]��ֵ����
A[0][0]��A[i][j]�Ӿ���Ԫ�صĺ�
"""

m = 5
n = 4
arr = [x for x in range(1,m*n + 1)]
A = []
for i in range(n):
    start = i * m
    A.append(arr[start:start + m])
#print(A)
for out_A in A:
    print(out_A)
B = [[0 for i in range(m)] for j in range(n)]

#print(B)
print("--------------")
def my_sum(i,j):
    return_value = 0
    for n2 in range(j + 1):
        for n1 in range(i + 1):
            return_value = return_value + A[n2][n1]
    return return_value

for j in range(n):
    for i in range(m):
        B[j][i] = my_sum(i,j)

#print(B)
for out_B in B:
    print(out_B)
