# 1. Reverse an Array
arr = [10, 20, 30, 40, 50]

reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)
