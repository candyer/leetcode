# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/


# Average of Levels in Binary Tree


# Given a non-empty binary tree,
# return the average value of the nodes on each level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. 
# Hence return [3, 14.5, 11].

# Note:
# The range of node's value is in the range of 32-bit signed integer.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [root]
        res = []
        level_sum = root.val
        while stack:
            res.append(level_sum / len(stack))
            tmp = []
            level_sum = 0
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    tmp.append(node.right)
                    level_sum += node.right.val
            stack = tmp
        return res











