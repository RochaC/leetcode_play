"""
" File Description:
" Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"
" Created by Rocha(chenzhihao) on 2020/12/17.
" Mail: chenzh@wifi.com
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not l1: return l2
		if not l2: return l1

		if l1.val > l2.val:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2
		else:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
