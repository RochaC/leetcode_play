"""
" File Description:
" Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.
"
" Created by Rocha(chenzhihao) on 2020/3/5.
"""


class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		self.backtrack(res, [], nums)
		return res

	def backtrack(self, res, track, nums):
		size = len(nums)
		if len(track) == size:
			res.append(track.copy())
			return

		for i in range(size):
			if nums[i] in track:
				continue

			track.append(nums[i])
			self.backtrack(res, track, nums)
			track.pop()

if __name__ == '__main__':
	so = Solution()
	print(so.permute([1,2,3]))
