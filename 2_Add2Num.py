"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/2/23.
"""


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		i = 0
		s = 0

		cur1 = l1
		cur2 = l2
		while (cur1 or cur2):
			n1 = 0
			n2 = 0

			if cur1:
				n1 = cur1.val * 10 ** i
				cur1 = cur1.next
			if cur2:
				n2 = cur2.val * 10 ** i
				cur2 = cur2.next

			print("n1:%s"%n1)
			print("n2:%s"%n2)
			s += n1 + n2
			i += 1

			print("s: %s" %s)

		head = ListNode(None)
		cur = head
		s = list(str(s))
		s.reverse()
		for ss in s:
			cur.next = ListNode(int(ss))
			cur = cur.next

		return head.next


if __name__ == '__main__':
	h1 = ListNode(None)
	h1.next = ListNode(0)
	# h1.next.next = ListNode(3)

	h2 = ListNode(None)
	h2.next = ListNode(1)
	# h2.next.next = ListNode(3)

	so = Solution()
	r = so.addTwoNumbers(h1.next, h2.next)

	cur = r
	while cur:
		print("cur:%s" %cur.val)
		cur = cur.next