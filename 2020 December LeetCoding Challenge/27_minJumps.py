# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3582/

# Jump Game IV


# Given an array of integers arr, you are initially positioned at the first index of the array.
# In one step you can jump from index i to index:
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.

# Example 3:
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

# Example 4:
# Input: arr = [6,1,9]
# Output: 2

# Example 5:
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
 

# Constraints:
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8


from typing import List
from collections import defaultdict
def minJumps(arr: List[int]) -> int:
    n = len(arr)
    if n <= 1: return 0
    graph = defaultdict(list)
    for i in range(n):
        graph[arr[i]].append(i)
    
    cur, visited, steps = [0], {0}, 0
    while cur:
        nxt = []
        for node in cur:
            if node == n - 1:
                return steps
            
            #check the same value
            for child in graph[arr[node]]:
                if child not in visited:
                    visited.add(child)
                    nxt.append(child)
            graph.pop(arr[node])
            
            #check the neighbours
            for child in [node - 1, node + 1]:
                if 0 <= child < n and child not in visited:
                    visited.add(child)
                    nxt.append(child)
        steps += 1
        cur = nxt
    return -1     


assert(minJumps([100,-23,-23,404,100,23,23,23,3,404]) == 3)
assert(minJumps([7]) == 0)
assert(minJumps([7,6,9,6,9,6,9,7]) == 1)
assert(minJumps([6,1,9]) == 2)
assert(minJumps([11,22,7,7,7,7,7,7,7,22,13]) == 3)








