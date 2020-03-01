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


class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		l = []
		l.append(root)
		res = []

		while l:
			cur = l.pop()
			if isinstance(cur, TreeNode):
				if cur.right:
					l.append(cur.right)
				l.append(cur.val)
				if cur.left:
					l.append(cur.left)
			else:
				res.append(cur)

		return res


if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    so = Solution()
    print(so.inorderTraversal(t))
