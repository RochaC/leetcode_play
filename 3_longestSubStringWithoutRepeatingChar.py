"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/2/23.
"""


class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		max_length = 0
		length = len(s)

		for p in range(length):
			pe = p + max_length + 1         # short cut
			while pe < length + 1:
				if len(set(s[p:pe])) == len(s[p:pe]):
					max_length = max(len(s[p:pe]), max_length)
					pe += 1
				else:
					break


		return max_length


if __name__ == '__main__':
	so = Solution()
	s = "abcabc"
	length = so.lengthOfLongestSubstring(s)
	print("max length is %s" % length)
