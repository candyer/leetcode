# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/


# Pseudo-Palindromic Paths in a Binary Tree

# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be 
# pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# Example 1:
#     2
#    / \
#   3   1
#  / \   \
# 3   1   1
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are three paths going from 
# the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. 
# Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] 
# can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

# Example 2:
#     2
#    / \
#   1   1
#  / \   
# 1   3   
#      \
#       1
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are three paths going from 
# the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. 
# Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] 
# (palindrome).

# Example 3:
# Input: root = [9]
# Output: 1
 
# Constraints:
# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(root):
            arr[root.val - 1] = not arr[root.val - 1]
            if not(root.left or root.right):
                if arr.count(False) <= 1:
                    self.res += 1
                    arr[root.val - 1] = not arr[root.val - 1]
                    return
                
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            arr[root.val - 1] = not arr[root.val - 1]
        
        self.res = 0
        arr = [True] * 9
        dfs(root)
        return self.res




