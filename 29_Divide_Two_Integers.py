"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/6/7.
"""


class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[List[int]]
		:rtype: List[List[int]]
		"""
		intervals.sort(key=lambda x: x[0])
		p = 0

		while(p < len(intervals)-1):
			if(intervals[p][0]<=intervals[p+1][0]):
				if(intervals[p][1] >= intervals[p+1][0] and intervals[p][1] <= intervals[p+1][1]):
					intervals[p][1] = intervals[p+1][1]
					intervals.pop(p+1)
				elif(intervals[p][1] > intervals[p+1][1]):
					intervals.pop(p + 1)
				else:
					p += 1
			else:
				p += 1

		return intervals


if __name__ == '__main__':
	so = Solution()
	l = [[1,4],[2,3]]
	print(so.merge(l))
