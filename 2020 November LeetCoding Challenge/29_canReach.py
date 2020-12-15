# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/568/week-5-november-29th-november-30th/3548/

# Jump Game III

# Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.



# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3

# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
 

# Constraints:
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length

############################################################################### BFS
from typing import List
def canReach(arr: List[int], start: int) -> bool:
    n = len(arr)
    visit = {start}
    stack = [start]
    while stack:
        cur_pos = stack.pop()
        for next_pos in [cur_pos + arr[cur_pos], cur_pos - arr[cur_pos]]:
            if 0 <= next_pos < n:
                if arr[next_pos] == 0:
                    return True
                if next_pos not in visit:
                    stack.append(next_pos)
                    visit.add(next_pos)
    return False




############################################################################### DFS
from typing import List
def canReach(arr: List[int], start: int) -> bool:
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        arr[start] = -arr[start] # mark as visited
        return canReach(arr, start + arr[start]) or canReach(arr, start - arr[start])
    return False


print(canReach([4,2,3,0,3,1,2], 5) == True)
print(canReach([4,2,3,0,3,1,2], 0) == True)
print(canReach([3,0,2,1,2], 2) == False)
print(canReach([3,8,2,1,2], 2) == False)





