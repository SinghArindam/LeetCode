Here is a set of atomic notes for LeetCode problem 121-best-time-to-buy-and-sell-stock, designed for spaced repetition learning:

- **Concept**: Problem Goal - Maximize single transaction profit.
    - **Context**: Find the maximum profit achievable by buying a stock on one day and selling it on a *different, future* day.
    - **Example**: Given `prices = [7,1,5,3,6,4]`, the goal is to find the maximum profit (which is 5, by buying at 1 and selling at 6).

- **Concept**: "Buy Before Sell" Rule.
    - **Context**: A stock must be bought on a day (`i`) *before* or *on* the day it is sold (`j`), meaning `i <= j`. (In practice, typically `i < j` for profit).
    - **Example**: Cannot buy on Day 5 and sell on Day 2.

- **Concept**: Zero Profit Default.
    - **Context**: If it's impossible to make any profit (e.g., prices continuously decrease), the maximum profit is considered to be `0`.
    - **Example**: For `prices = [7,6,4,3,1]`, the returned profit should be `0`.

- **Concept**: Brute Force Approach Logic.
    - **Context**: Checks every possible pair of buy and sell days (`buy_day < sell_day`) to calculate profit and find the maximum.
    - **Example**: Uses nested loops: outer loop for `buy_day`, inner loop for `sell_day` starting from `buy_day + 1`.

- **Concept**: Brute Force Time Complexity.
    - **Context**: Calculated by iterating through all possible buy-sell pairs.
    - **Example**: O(N^2), where N is the number of days/prices.

- **Concept**: Brute Force Space Complexity.
    - **Context**: Only a few fixed variables are used regardless of input size.
    - **Example**: O(1).

- **Concept**: Optimal One-Pass Approach Logic (Greedy).
    - **Context**: To maximize profit for a potential sell day, you must have bought the stock at the lowest possible price *encountered so far* (on or before that sell day).
    - **Example**: Iterates once through prices, maintaining a `min_price` and `max_profit`.

- **Concept**: `min_price` Variable Role.
    - **Context**: Stores the lowest stock price encountered from the beginning of the array up to the *current day* being processed. It represents the best potential buy point.
    - **Example**: For `prices = [7,1,5]`, `min_price` starts at 7, then becomes 1. When at 5, `min_price` is still 1.

- **Concept**: Calculating `current_profit` in Optimal Approach.
    - **Context**: If the `current_price` is greater than or equal to `min_price`, a potential profit `(current_price - min_price)` is calculated. This is the max profit if selling on the current day.
    - **Example**: If `min_price = 1` and `current_price = 5`, `current_profit = 5 - 1 = 4`.

- **Concept**: Updating `max_profit` in Optimal Approach.
    - **Context**: The `max_profit` variable is updated to be the maximum of its current value and the `current_profit` calculated.
    - **Example**: `max_profit = max(max_profit, current_profit)`.

- **Concept**: Optimal Solution Time Complexity.
    - **Context**: Achieved by processing each price exactly once in a single loop.
    - **Example**: O(N), where N is the number of days/prices.

- **Concept**: Optimal Solution Space Complexity.
    - **Context**: Only a constant number of variables (`min_price`, `max_profit`) are used.
    - **Example**: O(1).

- **Concept**: Handling Single-Element Price Array.
    - **Context**: Problem constraints guarantee `prices.length >= 1`. If `prices.length == 1`, no future day exists to sell, so the algorithm correctly returns `0` (initial `max_profit`).
    - **Example**: `prices = [10]` results in `max_profit = 0`.

- **Concept**: Handling Strictly Decreasing Prices.
    - **Context**: The `min_price` will continuously update to the current lower price. The condition for profit calculation (`current_price >= min_price`) will either not be met or yield non-positive profit, keeping `max_profit` at `0`.
    - **Example**: For `prices = [7,6,4,3,1]`, `max_profit` remains `0`.

- **Concept**: Handling Strictly Increasing Prices.
    - **Context**: The `min_price` will quickly settle on the first (lowest) price, and `max_profit` will continuously increase as the `current_price` rises.
    - **Example**: For `prices = [1,2,3,4,5]`, `min_price` becomes `1`, and `max_profit` correctly updates to `4`.

- **Concept**: `max_profit` Initialization.
    - **Context**: Initializing `max_profit` to `0` is crucial because it correctly represents the case where no profitable transaction is possible.
    - **Example**: If all potential profits are negative, `max_profit` will stay `0`.

- **Concept**: Greedy Algorithm Pattern Application.
    - **Context**: The optimal solution makes locally optimal choices at each step (either finding a new lower buy price or maximizing profit with the current lowest buy price), leading to a globally optimal solution.
    - **Example**: At each day, we either update our best buy price or try to sell at the current price using our best buy price found so far.

- **Concept**: Tracking Minimum/Maximum So Far Pattern.
    - **Context**: A common optimization technique where a running minimum or maximum value is maintained to efficiently perform calculations or identify "best" points in a sequence.
    - **Example**: The `min_price` variable exemplifies this pattern, summarizing the lowest price history.

- **Concept**: Single-Pass Optimization Technique.
    - **Context**: Transforming an O(N^2) brute-force solution into an O(N) solution by identifying and carrying forward all necessary information (e.g., `min_price`) in a single pass, avoiding redundant calculations.
    - **Example**: This problem is a prime example of optimizing nested loops into a single loop.

- **Concept**: Implicit "Buy Before Sell" Constraint Handling in Optimal.
    - **Context**: The forward iteration ensures that any `min_price` considered for a profit calculation always refers to a day that has already occurred (on or before the `current_price` day), thus satisfying the buy-before-sell rule.
    - **Example**: If `current_price` is at index `j`, `min_price` is the minimum of `prices[0...j]`, guaranteeing its index `i <= j`.