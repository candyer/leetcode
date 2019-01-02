# https://leetcode.com/problems/univalued-binary-tree/description/


# 965. Univalued Binary Tree


# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true

# Example 2:
# Input: [2,2,2,5,2]
# Output: false
 
# Note:
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].

Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def dfs(self, node, value):
		if node:
			value.add(node.val)
			self.dfs(node.left, value)
			self.dfs(node.right, value)
		
		
	def isUnivalTree(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		value = set()
		self.dfs(root, value)
		if len(value) == 1:
			return True
		return False
