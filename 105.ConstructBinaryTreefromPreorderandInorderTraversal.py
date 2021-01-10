"""
" File Description:
"
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
"
" Created by Rocha(chenzhihao) on 2021/1/5.
" Mail: chenzh@wifi.com
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def buildTree(self, preorder, inorder):
		return self.build(preorder, 0, len(preorder) -1 , inorder, 0, len(inorder) - 1)

	def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
		if pre_start > pre_end:
			return

		in_root_idx = inorder.index(preorder[pre_start])
		left_size = in_root_idx - in_start

		root = TreeNode(preorder[pre_start])
		root.left = self.build(preorder, pre_start+1, pre_start+left_size, inorder, in_start, in_root_idx-1)
		root.right = self.build(preorder, pre_start+left_size+1, pre_end, inorder, in_root_idx+1, in_end)

		return root
