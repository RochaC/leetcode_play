"""
" File Description:
" Given n non-negative integers a1, a2, ..., an ,
 where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 Find two lines, which together with x-axis forms a container,
 such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"
" Created by Rocha(chenzhihao) on 2020/2/24.
"""


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		i = 0
		j = len(height)-1

		max_s = self.cal_s(height, i, j)

		while i <= j:
			if height[i] >= height[j]:
				j -= 1
			else:
				i += 1
			new_s = self.cal_s(height, i,j)
			max_s = max(max_s, new_s)

		return max_s

	def cal_s(self, height, i,j):
		h = min(height[i], height[j])
		w = j - i

		return  h * w


if __name__ == '__main__':
	so = Solution()
	h = [1,8,6,2,5,4,8,3,7]
	print(so.maxArea(h))