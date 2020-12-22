"""
" File Description:
" 
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
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		dummy_node = ListNode(0)
		dummy_node.next = head

		fast = dummy_node
		slow = dummy_node


		for i in range(n):
			fast = fast.next

		while fast.next:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next

		return dummy_node.next

