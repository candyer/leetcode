# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/


# Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together 
# the nodes of the first two lists.


# Example 1:
# 1 -> 2 -> 4
# 1 -> 3 -> 4
# ------------------------
# 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]
 

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


