# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/


# Binary Tree Level Order Traversal

# Given the root of a binary tree, 
# return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

 
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, stack = [[root.val]], [root]
        while stack:
            nodes, level_vals = [], []
            for node in stack:
                if node.left:
                    nodes.append(node.left)
                    level_vals.append(node.left.val)
                if node.right:
                    nodes.append(node.right)
                    level_vals.append(node.right.val)
            stack = nodes
            if level_vals:
                res.append(level_vals)
        return res

#DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, level):
            if not node:
                return 
            if len(res) < level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        res = []
        dfs(root, 0)
        return res



