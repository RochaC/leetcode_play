"""
" File Description:
" Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"
" Created by Rocha(chenzhihao) on 2020/12/17.
" Mail: chenzh@wifi.com
"""


class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices) == 0:
			return 0

		min_price = prices[0]
		max_profit = 0
		start = True

		for price in prices:
			min_price = min(min_price, price)
			if start:
				start = False
				continue

			profit = price - min_price
			max_profit = max(max_profit, profit)

		return max_profit


if __name__ == '__main__':
	prices = [7, 1, 5, 3, 6, 4]
	so = Solution()
	print(so.maxProfit(prices))
