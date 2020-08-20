# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/

# Reorder List

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

	def get_mid(self, head: ListNode) -> ListNode:
		fast = head
		slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		return slow

	def reverse_linked_list(self, head: ListNode) -> ListNode:
		new_head = None
		while head:
			nexts = head.next
			head.next = new_head
			new_head = head
			head = nexts
		return new_head

	def reorderList(self, head: ListNode) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head:
			return
		mid = self.get_mid(head)
		right_head = mid.next
		mid.next = None
		left_head = head
		right_head = self.reverse_linked_list(right_head)
		while left_head and right_head:
			nexts = left_head.next
			left_head.next = right_head
			right_head = right_head.next
			left_head.next.next = nexts
			left_head = nexts





