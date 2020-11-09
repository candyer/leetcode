# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3525/


# Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B 
# where V = |A.val - B.val| and A is an ancestor of B.

# A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.


# Example 1:
#         8
#       /   \
#      3     10
#     / \     \
#    1   6     14
#       / \    /
#      4   7  13   
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

# Example 2:
# 1
#  \
#   2
#    \
#     0
#    /
#   3
# Input: root = [1,null,2,null,0,3]
# Output: 3

# Constraints:
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 10^5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root, maxi, mini):
            maxi, mini = max(maxi, root.val), min(mini, root.val)
            self.res = max(self.res, maxi - mini)
            if root.left:
                dfs(root.left, maxi, mini)
            if root.right:            
                dfs(root.right, maxi, mini)
        self.res = 0
        dfs(root,  root.val,  root.val)
        return self.res









