from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        # compare max profit
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit


# prices = [7,1,5,3,6,4] # 5
prices = [7,6,4,3,1] # 0
solution = Solution()
print(solution.max_profit(prices))