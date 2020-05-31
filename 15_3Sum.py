"""
" File Description:
" Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:

The solution set must not contain duplicate triplets.
"
" Created by Rocha(chenzhihao) on 2020/2/26.
"""


class Solution(object):
	def __init__(self):
		self.solution = []

	def findDiff(self, nums, p, next_p):
		again = True
		while (again and (p <= next_p - 1)):
			again = False
			if (nums[p] == nums[p + 1]):
				p += 1
				again = True

	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		sorted_nums = sorted(nums)
		nums_len = len(nums)
		p1 = 0
		p2 = p1 + 1
		p3 = nums_len - 1

		if (nums_len < 3 ):
			return []

		while ( p1 < p3 ):
			n1 = sorted_nums[p1]
			n2 = sorted_nums[p2]
			n3 = sorted_nums[p3]
			s = n1 + n2 + n3

			if (s < 0):
				while(p2<p3):
					if(sorted_nums[p2] != sorted_nums[p2+1]):
						p2 += 1
						break
					p2 += 1
			elif (s == 0):
				print("append [%s %s %s]" % (n1, n2, n3))
				self.solution.append([n1, n2, n3])
				while(p2<p3):
					if(sorted_nums[p2] != sorted_nums[p2+1]):
						p2 += 1
						break
					p2 += 1
			else:
				while(p3>p2):
					if(sorted_nums[p3] != sorted_nums[p3-1]):
						p3 -= 1
						break
					p3 -= 1

			# reset
			if (p2 >= p3):
				while(p1<p3):
					if(sorted_nums[p1] != sorted_nums[p1+1]):
						p1 += 1
						break
					p1 += 1
				p2 = p1 + 1
				p3 = nums_len - 1
				if(p2 >= p3):
					break


		return self.solution


if __name__ == '__main__':
	so = Solution()
	S = [0,0,0,0]

	so.threeSum(S)
