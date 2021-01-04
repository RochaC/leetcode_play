"""
" File Description:
" Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
"
" Created by Rocha(chenzhihao) on 2020/12/17.
" Mail: chenzh@wifi.com
"""


class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		i=0
		length = len(nums)

		if length == 0:
			return 1
		# print("input is :%s" %nums)


		# swap every num to pos num[i] - 1,
		# then find the first number not line with the pos
		while i < length:
			if nums[i] == (i + 1) or nums[i] <= 0 or nums[i] > length :
				i += 1
				continue
			else:
				to = nums[i] - 1
				if nums[to] == nums[i]:
					i += 1
					continue
				# print("change %s to %s" %(nums[i], to))

				nums[i], nums[to] = nums[to], nums[i]

				if i > to:
					i = to


			# print(nums)

		res = 0
		for (i,v) in enumerate(nums):
			if i+1 != v:
				res = i+1
				break

		# bad case
		if res == 0:
			res = length + 1

		return  res



if __name__ == '__main__':
	nums = [3,4,-1,1]
	so = Solution()
	print(so.firstMissingPositive(nums))


