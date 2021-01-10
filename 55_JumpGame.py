"""
" File Description:
" Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"
" Created by Rocha(chenzhihao) on 2020/5/31.
"""


class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		sz = len(nums)
		fartherst = 0
		for i in range(sz-1):
			fartherst = max(fartherst, i+nums[i])
			if fartherst <= i: return False       # cannot jump

		return fartherst>=sz-1


if __name__ == '__main__':
	n = [0]
	so = Solution()
	print(so.canJump(n))