# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

# Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each person is described 
# by a pair of integers (h, k), where h is the height of the person and k is the number 
# of people in front of this person who have a height greater than or equal to h. Write 
# an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]



############ solution 1 ###########
from typing import List
def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
	n = len(people)
	people.sort()
	res = [[-1, -1]] * n
	for h, k in people:
		count = 0
		i = 0
		while count < k:
			height = res[i][0]
			if height == -1 or height >= h:
				count += 1
			i += 1
		while res[i] != [-1, -1]:
			i += 1
		res[i] = [h, k]
	return res


############ solution 2 ###########
def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
	res = []
	for h, k in sorted(people, key = lambda x:(-x[0], x[1])):
		res.insert(k, [h, k])
	return res


assert(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])
assert(reconstructQueue([[1,3],[2,3],[3,0],[9,0],[7,0],[5,1]]) == [[3,0],[7,0],[5,1],[1,3],[2,3],[9,0]])

