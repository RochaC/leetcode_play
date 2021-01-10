"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/3/1.
"""


class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		track = []
		self.backtrack(res, 0, nums, track)

		return res

	def backtrack(self, res, start, nums, track):
		res.append(track.copy())
		size = len(nums)
		for i in range(start, size):
			track.append(nums[i])
			self.backtrack(res, i + 1, nums, track)
			track.pop()

		return


if __name__ == '__main__':
	so = Solution()
	nums = [1, 2, 3]
	print(so.subsets(nums))

	# for i in range(2,2):
	# 	print(i)