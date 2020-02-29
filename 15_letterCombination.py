"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/2/26.
"""


class Solution(object):
	def __init__(self):
		self.d2s = {"2":"abc",
		            "3": "def",
		            "4": "ghi",
		            "5": "jkl",
		            "6": "mno",
		            "7": "pqrs",
		            "8": "tuv",
		            "9": "wxyz"}

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		s = str(digits)
		result = []
		for i in s:
			m = self.d2s.get(i)
			if m:
				result = self.__grow(result, m)

		return result

	def __grow(self, l, d):
		res = []
		for i in d:
			if not l:
				res.append(i)
			else:
				for j in l:
					res.append(j+i)

		return res


if __name__ == '__main__':
	so = Solution()
	h = "234"
	print(so.letterCombinations(h))

