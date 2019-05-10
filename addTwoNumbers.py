# https://leetcode.com/problems/add-two-numbers/description/

# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order 
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        count1 = 0
        while l1:
            num1 += l1.val * pow(10, count1)
            count1 += 1
            l1 = l1.next
        count2 = 0
        while l2:
            num2 += l2.val * pow(10, count2)
            count2 += 1 
            l2 = l2.next

        num = map(int, list(str(num1 + num2)))
        l = ListNode(num[0])
        for n in num[1:]:
            tmp = ListNode(n)
            tmp.next = l
            l = tmp
        return l