# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3532/


# Range Sum of BST

# Given the root node of a binary search tree, 
# return the sum of values of all nodes with a value in the range [low, high].

# Example 1:
#      10
#     /  \
#    5   15
#   / \    \
#  3   7   18
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23

# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.


Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = 0
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.res += root.val
                if low < root.val:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)
        dfs(root)
        return self.res

#############################################################################
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            val = node.val
            if low <= val <= high:
                res += val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res

