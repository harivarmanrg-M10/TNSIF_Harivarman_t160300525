# 6. Rotate an Array
arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n

rotated = []

for i in range(n - k, n):
    rotated.append(arr[i])

for i in range(0, n - k):
    rotated.append(arr[i])

print(rotated)
