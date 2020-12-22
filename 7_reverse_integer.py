"""
" File Description:
" Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"
" Created by Rocha(chenzhihao) on 2020/12/15.
" Mail: chenzh@wifi.com
"""

import sys

class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		res = 0
		neg = False
		maxint = 2**31 -1
		minint = - 2**31

		if x < 0:
			neg = True
			x = abs(x)

		while x != 0:
			res = (x % 10 + res * 10)
			x //= 10

			if not neg and res > maxint:
				return 0
			elif neg and res > abs(maxint):
				return 0

		if neg:
			res = -res
		return res

if __name__ == '__main__':
    so = Solution()
    print(so.reverse(1534236469))