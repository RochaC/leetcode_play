"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/12/29.
" Mail: chenzh@wifi.com
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution1(object):
	def reverseList(self, head):
		"""
		Iterative
		:type head: ListNode
		:rtype: ListNode
		"""
		prev = None

		while head:
			head_next = head.next
			head.next = prev

			# move cur
			prev = head
			head = head_next

		return prev

class Solution2(object):
	def reverseList(self, head):
		"""
		Recursive
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head

		prev = self.reverseList(head.next)
		head.next.next = head
		head.next = None

		return prev

if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	head = ListNode()
	cur = head

	for i in nums:
		node = ListNode(i)
		cur.next = node
		cur = cur.next

	so = Solution2()
	res_head = so.reverseList(head)

	while res_head:
		print(res_head.val)
		res_head = res_head.next
