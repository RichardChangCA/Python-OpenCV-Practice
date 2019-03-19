def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    half = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    for i in arr:
        if i < half:
            left.append(i)
        elif i > half:
            right.append(i)
        else:
            middle.append(i)
    # print("left", left)
    # print("middle", middle)
    # print("right", right)
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([4,5,6,3,6,7,42,1,4,6,2,44,776]))