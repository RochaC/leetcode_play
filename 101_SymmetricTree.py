"""
" File Description:
" Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
	For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"
" Created by Rocha(chenzhihao) on 2021/1/4.
" Mail: chenzh@wifi.com
"""


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True

		return self.isMirror(root.left, root.right)

	def isMirror(self, left: TreeNode, right: TreeNode):
		if not left and not right:  # both is leaf
			return True
		if not left or not right:  # one is leaf
			return False

		return (left.val == right.val) and self.isMirror(left.right, right.left) \
		       and self.isMirror(left.left, right.right)
