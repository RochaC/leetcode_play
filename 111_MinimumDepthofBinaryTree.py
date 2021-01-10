"""
" File Description:
" Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"
" Created by Rocha(chenzhihao) on 2021/1/6.
" Mail: chenzh@wifi.com
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0

		q = []
		q.append(root)
		level = 1

		while q:
			size = len(q)

			for i in range(size):
				node = q.pop(0)
				if not node.left and not node.right:
					return level

				# add adj
				if node.left :
					q.append(node.left)

				if node.right :
					q.append(node.right)

			level += 1

		return level