"""
" File Description:
" Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"
" Created by Rocha(chenzhihao) on 2020/2/26.
"""


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.checked = False


class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		que = []
		que.append(root)
		res = []

		while que:
			node = que[-1]

			if node.left and not node.left.checked:
				que.append(node.left)
				continue

			res.append(node.val)
			node.checked = True
			que.pop()

			if node.right and not node.right.checked:
				que.append(node.right)
				continue

		return res


if __name__ == '__main__':
	t = TreeNode(1)
	t.right = TreeNode(2)
	t.right.left = TreeNode(3)

	so = Solution()
	print(so.inorderTraversal(t))
