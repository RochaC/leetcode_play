"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/3/5.
"""



class Solution(object):
	def __init__(self):
		self.res = []

	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self._permute([], nums)

		return self.res

	def _permute(self, stack, nums):
		if len(stack) == len(nums):
			self.res.append(stack[:])
		else:
			for i in nums:
				if i not in stack:
					stack.append(i)
					self._permute(stack, nums)
					stack.pop()
				else:
					continue

		return


if __name__ == '__main__':
	so = Solution()
	so.permute([1,2,3])
	print(so.res)
