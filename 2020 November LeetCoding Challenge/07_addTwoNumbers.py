# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/


# Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists 
# is not allowed.

# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def push_stack(self, l, stack):
        while l:
            stack.append(l.val)
            l = l.next
        return stack        

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = self.push_stack(l1, []), self.push_stack(l2, [])
        carry = 0
        res = ListNode(0)
        while s1 or s2:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            res.val = carry % 10
            head = ListNode(carry // 10)
            head.next = res
            res = head
            carry //= 10
        if res.val:
            return res.next
        return res






