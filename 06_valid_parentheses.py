# 6. Valid Parentheses - Stack

s = "({[]})"

stack = []
pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

valid = True

for char in s:
    if char in "({[":
        stack.append(char)
    else:
        if not stack or stack[-1] != pairs[char]:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

print(valid)
