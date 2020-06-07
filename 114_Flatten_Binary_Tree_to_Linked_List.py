"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/6/7.
"""

import copy


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if(root):
			if (root.right and root.left):
				self.flatten(root.left)
				self.flatten(root.right)
				cur = root.left
				while (cur.right):
					cur = cur.right
				cur.right = root.right
				root.right = root.left
				root.left = None
			elif (root.left and not root.right):
				self.flatten(root.left)
				root.right = root.left
				root.left = None
			elif (not root.left and root.right):
				self.flatten(root.right)
			else:
				return
