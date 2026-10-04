# 7. Find the Most Frequent Element
arr = [2, 5, 2, 8, 5, 2, 3, 5, 2]

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

most_frequent = arr[0]

for num in frequency:
    if frequency[num] > frequency[most_frequent]:
        most_frequent = num

print("Most Frequent Element:", most_frequent)
print("Frequency:", frequency[most_frequent])
