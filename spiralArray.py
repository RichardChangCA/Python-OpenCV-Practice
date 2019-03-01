"""
螺旋矩阵：给定一个m*n要素的矩阵，按照螺旋顺序，返回该矩阵的所有要素
[[1,2,3],
 [4,5,6],
 [7,8,9]]
应该返回[1,2,3,6,9,8,7,4,5]
m 行 n列
"""
m = 5
n = 4
arr = [x for x in range(1,m*n + 1)]
arr_new = []
for i in range(n):
    start = i * m
    arr_new.append(arr[start:start + m])
print(arr_new)

arr_output = []
for i in range(n):
    if(i % 2 == 0):
        for j in range(m):
            arr_output.append(arr_new[i][j])
    else:
        for j in range(m):
            arr_output.append(arr_new[i][m-j-1])

print(arr_output)
