"""
" File Description:
" A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.
"
" Created by Rocha(chenzhihao) on 2020/12/22.
" Mail: chenzh@wifi.com
"""


class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		l = len(s)
		f = [0] * (l + 1)
		f[0] = 1

		for i in range(1, l+1):
			# if decode itself is 0, then nothing
			if s[i-1] == '0':
				f[i] = 0
			else:
				f[i] += f[i-1]

			if (s[i-2] == '1' or s[i-2] == '2') and s[i-1] <= '6':
				f[i] += f[i-2]


		return f[-1]


if __name__ == '__main__':
	s = "2611055971756562"
	so = Solution()
	print(so.numDecodings(s))





