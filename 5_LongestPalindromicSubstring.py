"""
" File Description:
" Given a string s, find the longest palindromic substring in s.
  You may assume that the maximum length of s is 1000.

	Example 1:

	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.
	Example 2:

	Input: "cbbd"
	Output: "bb"
"
" Created by Rocha(chenzhihao) on 2020/2/24.
"""


class Solution(object):
	def __init__(self):
		self.longest_str = ""

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		longest_length = 0
		length = len(s)

		if not s:
			return self.longest_str

		window = 0
		start = 0
		end = 0

		while start < length or end+window < length:
			window1 = self.__comparePalindrome(s, start-window, end+window)
			window2 = self.__comparePalindrome(s, start-window, end+window+1)
			longest_length = max(window1, window2)

			start += 1
			end += 1


		return self.longest_str


	def __comparePalindrome(self, s, i, j):
		length = len(s)
		tmp_longest_str = ""
		window_size = -1

		while i >= 0 and j < length:
			if s[i] == s[j]:
				tmp_longest_str = s[i:j + 1]
				i -= 1
				j += 1
				window_size += 1
			else:
				break

		if len(tmp_longest_str) > len(self.longest_str):
			self.longest_str = tmp_longest_str

		return window_size


if __name__ == '__main__':
	so = Solution()
	s = "abcbadabcb"
	print(so.longestPalindrome(s))




