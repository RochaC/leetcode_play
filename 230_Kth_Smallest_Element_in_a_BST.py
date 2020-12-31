"""
" File Description:
" Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"
" Created by Rocha(chenzhihao) on 2020/12/30.
" Mail: chenzh@wifi.com
"""


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		st = []
		cur = root

		while st or cur:
			if cur:
				st.append(cur)
				cur = cur.left
			else:
				cur = st.pop()
				k -= 1

				if k == 0:
					return cur.val

				cur = cur.right








