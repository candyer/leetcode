# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435/

# Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree.

# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.



class Solution:
    def dfs(self, root: TreeNode, is_left: bool) -> int:
        if not root.left and not root.right: #It's a leaf
            return root.val if is_left else 0
        total = 0
        if root.left:
            total += self.dfs(root.left, True)
        if root.right:
            total += self.dfs(root.right, False)  
        return total

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, True)



