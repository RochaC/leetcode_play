"""
" File Description:
" Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		return self.build(0, len(nums) - 1, nums)

	def build(self, start, end, nums):
		if start == end:
			return TreeNode(nums[start])
		if start > end: return None

		mid = start + (end-start) // 2

		root = TreeNode(nums[mid])
		root.left = self.build(start, mid - 1, nums)
		root.right = self.build(mid + 1, end, nums)

		return root


if __name__ == '__main__':
	nums = [-10, -3, 0, 5, 9]
	so = Solution()
	so.sortedArrayToBST(nums)
