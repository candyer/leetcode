# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3704/

# Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
 
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 100


from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([root, 0])
        queue.append([root, 0])
        d = defaultdict(int)
        while queue:
            node, i = queue.pop()
            d[i] += node.val
            if node.left:
                queue.append((node.left, i + 1))
            if node.right:
                queue.append((node.right, i + 1))
        maxi = max(d)
        return d[maxi]



from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            res = 0
            tmp = []
            for node in queue:
                res += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res

        








