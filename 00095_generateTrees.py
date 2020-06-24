# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

# 95. Unique Binary Search Trees II

# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
 

# Constraints:
# 0 <= n <= 8


from typing import List
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	
	def dfs(self, left: int, right: int) -> List[TreeNode]:
		if left > right:
			return [None]
		res = []
		for i in range(left, right + 1):
			left_nodes = self.dfs(left, i - 1)
			right_nodes = self.dfs(i + 1, right)
			for left_node in left_nodes:
				for right_node in right_nodes:
					root = TreeNode(i)
					root.left = left_node
					root.right = right_node
					res.append(root)
		return res
					
	def generateTrees(self, n: int) -> List[TreeNode]:
		if n == 0:
			return []
		return self.dfs(1, n)


s = Solution()
print(s.generateTrees(3)) 


