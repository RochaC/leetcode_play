"""
" File Description:
" 
"
" Created by Rocha(chenzhihao) on 2020/6/26.
"""


class Solution(object):
	def __getDp(self, candidates, sum):
		if not self.dp[sum]:
			self.dp[sum] = []
			for i in candidates:
				left = sum - i
				if (left == 0):
					self.dp[sum].append([i])
					return self.dp[sum]

				elif (left > 0):
					ok = False
					if not self.dp[left]:
						self.__getDp(candidates, left)
					if self.dp[left]:
						ok = True

					if(ok):
						for comb in self.dp[left]:
							tmp = comb.copy()
							tmp.append(i)
							tmp = sorted(tmp)
							if tmp not in self.dp[sum]:
								self.dp[sum].append(tmp)
				else:
					return None
		else:
			return self.dp[sum]


	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		self.dp = [None] * (target+1)
		candidates = sorted(candidates)

		self.__getDp(candidates, target)

		return self.dp[target]

if __name__ == '__main__':
	candidates = [2, 3, 5]
	target = 8
	so = Solution()
	print(so.combinationSum(candidates, target))