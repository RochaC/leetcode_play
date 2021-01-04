"""
" File Description:
" Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"
" Created by Rocha(chenzhihao) on 2021/1/4.
" Mail: chenzh@wifi.com
"""
import numpy as np


class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""

		self.word1 = word1
		self.word2 = word2

		i = len(word1)
		j = len(word2)

		# base case
		self.dp = np.full((i, j), -1)

		return self.help(i - 1, j - 1)

	def help(self, i, j):
		if i < 0:
			return j + 1
		if j < 0:
			return i + 1

		if self.dp[i][j] != -1:
			return self.dp[i][j]

		if self.word1[i] == self.word2[j]:
			self.dp[i][j] = self.help(i - 1, j - 1)
		else:
			self.dp[i][j] = min(
				self.help(i - 1, j) + 1,  # add
				self.help(i, j - 1) + 1,  # replace
				self.help(i - 1, j - 1) + 1  # delete
			)

		return self.dp[i][j]


if __name__ == '__main__':
	word1 = ""
	word2 = ""

	so = Solution()
	print(so.minDistance(word1, word2))
