# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/

# Letter Case Permutation


# Given a string S, we can transform every letter individually to be lowercase or uppercase 
# to create another string.
# Return a list of all possible strings we could create. You can return the output in any order.

# Example 1:
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: S = "3z4"
# Output: ["3z4","3Z4"]

# Example 3:
# Input: S = "12345"
# Output: ["12345"]

# Example 4:
# Input: S = "0"
# Output: ["0"]
 

# Constraints:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.


from typing import List
from itertools import product
def letterCasePermutation(S: str) -> List[str]:
    tmp = []
    for c in S:
        if c.isalpha():
            tmp.append([c.lower(), c.upper()])
        else:
            tmp.append(c)
    return [''.join(i) for i in product(*tmp)]



assert(letterCasePermutation("abc") == ['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC'])
assert(letterCasePermutation("a1b2") == ['a1b2', 'a1B2', 'A1b2', 'A1B2'])
assert(letterCasePermutation("3z4") == ['3z4', '3Z4'])
assert(letterCasePermutation("12345") == ['12345'])
assert(letterCasePermutation("0") == ['0'])
