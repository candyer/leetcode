# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/


# Valid Parentheses


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

def isValid(s: str) -> bool:
    symbles = {"(": ")","{" :"}", "[":"]"}
    stack = []
    for c in s:
        if c in symbles:
            stack.append(c)
        else:
            if not stack or c != symbles[stack.pop()]:
                return False
    # return False if stack else True
    return not stack
        

assert(isValid("()") == True)
assert(isValid("()[]{}") == True)
assert(isValid("{[]}") == True)
assert(isValid("(]") == False)
assert(isValid("([)]") == False)
assert(isValid("{[])}(") == False)
assert(isValid('{') == False)





