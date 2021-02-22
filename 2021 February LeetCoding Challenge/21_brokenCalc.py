# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3647/


# Broken Calculator

# On a broken calculator that has a number showing on its display, we can perform two operations:
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
# Return the minimum number of operations needed to display the number Y.

# Example 1:
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

# Example 2:
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.

# Example 3:
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

# Example 4:
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
 

# Note:
# 1 <= X <= 10^9
# 1 <= Y <= 10^9

def brokenCalc(X: int, Y: int) -> int:
    count = 0 
    while Y > X :
        count += 1 
        if Y % 2 == 0 :
            Y //= 2 
        else:
            Y += 1 
    return count + X - Y 


assert(brokenCalc(1, 10) == 6)
assert(brokenCalc(2, 3) == 2)
assert(brokenCalc(5, 8) == 2)
assert(brokenCalc(3, 10) == 3)
assert(brokenCalc(1024, 1) == 1023)
assert(brokenCalc(3, 8) == 3) # 3 -> 2 -> 4 ->8
assert(brokenCalc(6, 8) == 3) # 6 -> 5 -> 4 ->8

