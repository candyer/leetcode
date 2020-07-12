# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3385/

# Maximum Width of Binary Tree

# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. 
# The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes 
# (the leftmost and right most non-null nodes in the level, where the null nodes 
# between the end-nodes are also counted into the length calculation.

# Example 1:
# Input: 
# 		   1
# 		 /   \
# 		3     2
# 	   / \     \  
# 	  5   3     9 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

# Example 2:
# Input: 
# 		  1
# 		 /  
# 		3    
# 	   / \       
# 	  5   3     
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).

# Example 3:
# Input: 
# 		  1
# 		 / \
# 		3   2 
# 	   /        
# 	  5      
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).

# Example 4:
# Input: 
# 		  1
# 		 / \
# 		3   2
# 	   /     \  
# 	  5       9 
# 	 /         \
# 	6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

# Note: Answer will in the range of 32-bit signed integer.


from collections import deque
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		queue = deque()
		queue.append([root, 1])
		res = 0
		while queue:
			width = queue[-1][1] - queue[0][1] + 1
			res = max(res, width)
			for i in range(len(queue)):
				node, count = queue.popleft()
				if node.left: queue.append([node.left, count * 2])
				if node.right: queue.append([node.right, count * 2 + 1])
		return res













