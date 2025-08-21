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
        # num_days = len(prices)
        # if num_days < 2:
        #     return 0
        # left_profits = [0] * num_days
        # min_price = prices[0]
        # for day in range(1, num_days):
        #     min_price = min(min_price, prices[day])
        #     left_profits[day] = max(left_profits[day - 1], prices[day] - min_price)
        # right_profits = [0] * num_days
        # max_price = prices[-1]
        # for day in range(num_days - 2, -1, -1):
        #     max_price = max(max_price, prices[day])
        #     right_profits[day] = max(right_profits[day + 1], max_price - prices[day])
        # total_max_profit = 0
        # for day in range(num_days):
        #     total_max_profit = max(total_max_profit, left_profits[day] + right_profits[day])
        # return total_max_profit

        # Approach 3
        # memo = {}
        # num_days = len(prices)
        # def find_max_profit(day, transactions_left, is_holding):
        #     if day == num_days or transactions_left == 0:
        #         return 0
        #     state = (day, transactions_left, is_holding)
        #     if state in memo:
        #         return memo[state]
        #     idle_profit = find_max_profit(day + 1, transactions_left, is_holding)
        #     if is_holding:
        #         action_profit = prices[day] + find_max_profit(day + 1, transactions_left - 1, False)
        #     else:
        #         action_profit = -prices[day] + find_max_profit(day + 1, transactions_left, True)
        #     result = max(idle_profit, action_profit)
        #     memo[state] = result
        #     return result
        # return find_max_profit(0, 2, False)

        # Approach 4
        num_days = len(prices)
        if num_days < 2:
            return 0
        num_transactions = 2
        profits_table = [[0] * num_days for _ in range(num_transactions + 1)]
        for k in range(1, num_transactions + 1):
            max_balance = -prices[0]
            for day in range(1, num_days):
                profits_table[k][day] = max(profits_table[k][day - 1], prices[day] + max_balance)
                max_balance = max(max_balance, profits_table[k - 1][day] - prices[day])
        return profits_table[num_transactions][-1]

        # Approach 5
        # if not prices:
        #     return 0
        # num_transactions = 2
        # buy_profits = [float('-inf')] * (num_transactions + 1)
        # sell_profits = [0] * (num_transactions + 1)
        # for price in prices:
        #     for k in range(1, num_transactions + 1):
        #         buy_profits[k] = max(buy_profits[k], sell_profits[k - 1] - price)
        #         sell_profits[k] = max(sell_profits[k], buy_profits[k] + price)
        # return sell_profits[num_transactions]

        # Approach 6

        # Approach 7