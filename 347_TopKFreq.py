"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/3/8.
"""
from collections import Counter
import heapq

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		c = Counter(nums)
		return heapq.nlargest(k, c.keys(), key=c.get)


if __name__ == '__main__':
    so = Solution()
    l = [1,2,3,4,5,6,6,6,5,4,4,3,2,2,2,1]
    print(so.topKFrequent(l,2))