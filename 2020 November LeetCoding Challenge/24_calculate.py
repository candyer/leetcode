# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3542/

# Basic Calculator II


# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
# The integer division should truncate toward zero.


# Example 1:
# Input: "3+2*2"
# Output: 7

# Example 2:
# Input: " 3/2 "
# Output: 1

# Example 3:
# Input: " 3+5 / 2 "
# Output: 5

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


def calculate(s: str) -> int:
        stack, n, i = [], len(s), 0
        while i < n:
            if s[i] != ' ':
                if s[i].isdigit():
                    num = 0
                    while i < n and s[i].isdigit():
                        num *= 10
                        num += int(s[i])
                        i += 1
                    i -= 1
                    if stack and stack[-1] in '*/':
                        operator = stack.pop()
                        a = stack.pop()
                        if operator == '*':
                            stack.append(a * num)
                        else:
                            stack.append(a // num)
                    else:
                        stack.append(num) 
                else:
                    stack.append(s[i])
            i += 1

        i = 0
        while i < len(stack) - 1:
            a = stack[i]
            operator = stack[i + 1]
            b = stack[i + 2]
            i += 2
            if operator == '+':
                stack[i] = a + b
            else:
                stack[i] = a - b
        return stack[-1]


assert(calculate("9/40-323+5/20*311") == -323)
assert(calculate("9/40-323+100/20*311") == 1232)
assert(calculate("3+2*2") == 7)
assert(calculate(" 3/2 ") == 1)
assert(calculate(" 3+5 / 2 ") == 5)
assert(calculate(" 9 /4 -3+5 / 2 ") == 1)
assert(calculate(" 42315") == 42315)
assert(calculate("321+123*2") == 567)
assert(calculate(" 9 /40 -323+5 / 2 ") == -321)








