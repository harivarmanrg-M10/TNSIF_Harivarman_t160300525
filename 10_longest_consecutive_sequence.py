# 10. Longest Consecutive Sequence - Hashing
# O(n) average time

arr = [100, 4, 200, 1, 3, 2]

numbers = set(arr)
longest = 0

for num in numbers:
    # Start counting only if num is the beginning of a sequence
    if num - 1 not in numbers:
        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
