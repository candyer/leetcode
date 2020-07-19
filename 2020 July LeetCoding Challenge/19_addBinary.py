# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3395/

# Add Binary

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.


# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.


def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]



def addBinary(a: str, b: str) -> str:
    i, j, res, carry = len(a) - 1, len(b) - 1, [], 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            d1 = int(a[i])
        else:
            d1 = 0
        if j >= 0:
            d2 = int(b[j])
        else:
            d2 = 0
        digit = d1 + d2 + carry
        res.append(str(digit % 2))
        carry = digit // 2
        i -= 1
        j -= 1
    return ''.join(res[::-1])

        
assert(addBinary("11", "1") == '100')
assert(addBinary("1010", "1011") == '10101')

