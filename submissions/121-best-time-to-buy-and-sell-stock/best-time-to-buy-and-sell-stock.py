class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if min_price > price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
        return max_profit      

        