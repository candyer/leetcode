# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/

# Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
		res, stack = [], []
		if root:
			stack.append(root)
		while stack:
			res.append([node.val for node in stack])
			tmp = []
			for node in stack:
				if node.left:
					tmp.append(node.left)
				if node.right:
					tmp.append(node.right)
			stack = tmp
		return res[::-1]
