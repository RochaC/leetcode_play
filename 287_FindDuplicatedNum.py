"""
" File Description:
" floyd's torise
"
" Created by Rocha(chenzhihao) on 2020/3/8.
"""


class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		hare = nums[0]
		tortoise = nums[0]

		while True:
			hare = nums[nums[hare]]     # 2x speed
			tortoise = nums[tortoise]
			print("Hare is %s, tortoise is %s" %(hare,tortoise))
			if hare == tortoise:
				break

		hare = nums[0]
		while True:
			if hare == tortoise:
				break
			hare = nums[hare]
			tortoise = nums[tortoise]
			print("Same speed. Hare is %s, tortoise is %s" % (hare, tortoise))

		return tortoise

if __name__ == '__main__':
    so = Solution()
    nums = [3,1,3,4,2]
    print(so.findDuplicate(nums))