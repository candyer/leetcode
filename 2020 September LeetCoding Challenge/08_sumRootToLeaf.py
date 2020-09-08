# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/


# Sum of Root To Leaf Binary Numbers
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number 
# starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, 
# then this could represent 01101 in binary, which is 13.

# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.

 
# Example 1:
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 
# Note:
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

########################################## BFS
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int: 
        stack, res = [], 0
        stack.append((root, 0))
        while stack:
            node, path = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += path * 2 + node.val
                path = path * 2 + node.val
                stack.append((node.left, path))
                stack.append((node.right, path))
        return res 


########################################## DFS
class Solution:
    def dfs(self, root, res):
        if not root:
            return 0
        res = res * 2 + root.val
        if not root.left and not root.right:
            return res
        return self.dfs(root.left, res) + self.dfs(root.right, res)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    
