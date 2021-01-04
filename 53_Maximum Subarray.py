"""
" File Description:
" Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"
" Created by Rocha(chenzhihao) on 2020/12/23.
" Mail: chenzh@wifi.com
"""


class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		l = len(nums)
		dp = [None] * len(nums)
		if l < 1:
			return 0

		dp[0] = nums[0]

		for i in range(1, l):
			dp[i] = max(nums[i] + dp[i - 1], nums[i])

		return max(dp)


if __name__ == '__main__':
	nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	so = Solution()
	print(so.maxSubArray(nums))
