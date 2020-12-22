"""
" File Description:
" Wrong version
"
" Created by Rocha(chenzhihao) on 2020/5/31.
"""

UNKOWN = 1
GOOD = 2
BAD = 3


class Solution(object):
	def canJumpFromN(self, pos, nums, mem):
		if (mem[pos] != UNKOWN):
			if (mem[pos] == GOOD):
				return True
			else:
				return False

		step = min(nums[pos], len(nums)-1)
		for i in range(1, step+1):
			if (self.canJumpFromN(pos + i, nums, mem)):
				mem[pos] = GOOD
				return True

		mem[pos] = BAD
		return False

	def canJump(self, nums):
		"""
		dp top-bottom version, would have stack problem
		:type nums: List[int]
		:rtype: bool
		"""
		max_l = len(nums)
		mem = [UNKOWN] * (max_l - 1)
		mem.append(GOOD)

		return self.canJumpFromN(0, nums, mem)


if __name__ == '__main__':
	so = Solution()
	nums = 0
	print(so.canJump(nums))
