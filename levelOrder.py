# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# 102. Binary Tree Level Order Traversal



# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict
class Solution(object):
    def helper(self, root, res):
        level =  max_level = 0
        stack = [(root, 0)]
        d = defaultdict(list)
        while stack:
            node, level = stack.pop()
            if node:
                d[level].append(node.val)
                max_level = max(max_level, level + 1)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        for i in range(max_level):
            res.append(d[i])
        return res
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, res)
        return res

###############################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        return res




