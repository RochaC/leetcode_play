"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/3/8.
"""


class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		self.res = []
		self.max = n
		self.backTrack("", 0, 0)

		return self.res

	def backTrack(self, s, open, close):
		if (len(s) == 2*self.max):
			self.res.append(s)
			return

		if open < self.max:
			self.backTrack(s+"(", open+1, close)
		if close < open:
			self.backTrack(s+")", open, close+1)

		return

if __name__ == '__main__':
	so = Solution()
	print(so.generateParenthesis(3))

