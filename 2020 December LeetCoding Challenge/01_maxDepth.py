# https://leetcode.com/explore/featured/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/

# Maximum Depth of Binary Tree


# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:
#       3
#      / \
#     9   20 
#       / \
#        15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1
 

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100


###################################################################### DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1





###################################################################### BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
            res += 1
        return res








