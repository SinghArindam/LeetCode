class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        first_buy_profit = float('-inf')
        first_sell_profit = 0
        second_buy_profit = float('-inf')
        second_sell_profit = 0
        for current_price in prices:
            first_buy_profit = max(first_buy_profit, -current_price)
            first_sell_profit = max(first_sell_profit, first_buy_profit + current_price)
            second_buy_profit = max(second_buy_profit, first_sell_profit - current_price)
            second_sell_profit = max(second_sell_profit, second_buy_profit + current_price)
        return second_sell_profit