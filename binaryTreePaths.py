# https://leetcode.com/problems/binary-tree-paths/description/

# 257. Binary Tree Paths

# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, paths, path, node):
        if not node.left and not node.right:
            paths.append(path)
            return
        if node.left:
            self.dfs(paths, path+[str(node.left.val)], node.left)
        if node.right:
            self.dfs(paths, path+[str(node.right.val)], node.right)
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []
        self.dfs(paths, [str(root.val)], root)
        return ['->'.join(path) for path in paths]