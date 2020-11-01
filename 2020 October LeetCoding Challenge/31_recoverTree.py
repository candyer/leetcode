# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3514/

# Recover Binary Search Tree

# You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. 
# Recover the tree without changing its structure.

# Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


# Example 1:
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

# Example 2:
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

# Constraints:
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        Morris traversal
        """
        first, second, is_first_time, pre = None, None, True, TreeNode(float('-inf'))
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = root
                    root = root.left
                else:
                    tmp.right = None
                    if pre.val > root.val and is_first_time:
                        first = pre
                        is_first_time = False
                    if pre.val > root.val and not is_first_time:
                        second = root
                    pre = root
                    root = root.right
            else:
                if pre.val > root.val and is_first_time:
                    first = pre
                    is_first_time = False
                if pre.val > root.val and not is_first_time:
                    second = root
                pre = root
                root = root.right

        if first and second:
            first.val, second.val = second.val, first.val










