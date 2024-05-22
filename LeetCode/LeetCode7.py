from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)-1):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit


prices = [7, 1, 4, 5, 3, 6, 9]
sol = Solution()
print(sol.maxProfit(prices))
