"""
" File Description:
" Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"
" Created by Rocha(chenzhihao) on 2020/2/26.
"""


class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# catalan tree
		d = []

		for i in range(n + 1):
			d.append(0)
			if i in (0, 1):
				d[i] = 1
				continue
			for k in range(i):
				d[i] += d[k] * d[i - k - 1]

		return d[n]


if __name__ == '__main__':
	so = Solution()
	print(so.numTrees(5))
