class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit_today = price - min_price
            if profit_today > max_profit:
                max_profit = profit_today
        return max_profit