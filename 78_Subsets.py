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
		res_l = []
		# generate bitmask
		n = len(nums)
		max_bit = 1 << n

		for i in range(2**n):
			bit_mask = bin(i|max_bit)[3:]
			res_l.append([num for num, mask in zip(nums, bit_mask) if mask =='1'])


		return res_l

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3]
    print(so.subsets(nums))


