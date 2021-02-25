# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/


# Score of Parentheses

# Given a balanced parentheses string S, compute the score of the string based on the following rule:
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 
# Example 1:
# Input: "()"
# Output: 1

# Example 2:
# Input: "(())"
# Output: 2

# Example 3:
# Input: "()()"
# Output: 2

# Example 4:
# Input: "(()(()))"
# Output: 6
 
# Note:
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50


def scoreOfParentheses(S: str) -> int:
    stack = [0]
    for c in S:
        if c == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    return stack.pop()

                 
assert(scoreOfParentheses("()") == 1)
assert(scoreOfParentheses("(())") == 2)
assert(scoreOfParentheses("()()") == 2)
assert(scoreOfParentheses("(()(()))") == 6)
















