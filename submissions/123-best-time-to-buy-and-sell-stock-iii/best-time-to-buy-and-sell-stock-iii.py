class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Approach 1
        # first_buy_profit = float('-inf')
        # first_sell_profit = 0
        # second_buy_profit = float('-inf')
        # second_sell_profit = 0
        # for current_price in prices:
        #     first_buy_profit = max(first_buy_profit, -current_price)
        #     first_sell_profit = max(first_sell_profit, first_buy_profit + current_price)
        #     second_buy_profit = max(second_buy_profit, first_sell_profit - current_price)
        #     second_sell_profit = max(second_sell_profit, second_buy_profit + current_price)
        # return second_sell_profit

        # Approach 2
        num_days = len(prices)
        if num_days < 2:
            return 0
        left_profits = [0] * num_days
        min_price = prices[0]
        for day in range(1, num_days):
            min_price = min(min_price, prices[day])
            left_profits[day] = max(left_profits[day - 1], prices[day] - min_price)
        right_profits = [0] * num_days
        max_price = prices[-1]
        for day in range(num_days - 2, -1, -1):
            max_price = max(max_price, prices[day])
            right_profits[day] = max(right_profits[day + 1], max_price - prices[day])
        total_max_profit = 0
        for day in range(num_days):
            total_max_profit = max(total_max_profit, left_profits[day] + right_profits[day])
        return total_max_profit

        # Approach 3

        # Approach 4

        # Approach 5

        # Approach 6

        # Approach 7