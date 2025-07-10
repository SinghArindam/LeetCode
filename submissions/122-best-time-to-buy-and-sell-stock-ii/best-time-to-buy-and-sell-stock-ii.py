class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        total_profit = 0
        for i in range(1,n):
            if prices[i-1]<prices[i]:
                print(prices[i-1], prices[i])
                total_profit += prices[i]-prices[i-1]
        return total_profit

        