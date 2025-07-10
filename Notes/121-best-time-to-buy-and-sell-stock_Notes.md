Here are comprehensive notes for the LeetCode problem "121. Best Time to Buy and Sell Stock".

---

## 1. Problem Summary

The problem asks us to find the maximum profit that can be achieved by performing at most one transaction (buying one stock and selling it later). We are given an array `prices`, where `prices[i]` represents the price of a stock on day `i`.

The rules are:
*   We must choose a **single day** to buy and a **different day in the future** to sell. This implies the selling day's index must be greater than the buying day's index.
*   If no profit can be achieved (e.g., prices are always decreasing), we should return `0`.

**Constraints:**
*   `1 <= prices.length <= 10^5` (The array will not be empty)
*   `0 <= prices[i] <= 10^4` (Prices are non-negative)

---

## 2. Explanation of All Possible Approaches

### Approach 1: Brute Force

**Logic:**
The most straightforward way to solve this problem is to consider every possible pair of buy and sell days. We iterate through each day `i` as a potential buy day, and then iterate through each subsequent day `j` (where `j > i`) as a potential sell day. For each pair `(i, j)`, we calculate the profit `prices[j] - prices[i]` and keep track of the maximum profit found so far.

**Algorithm:**
1.  Initialize `max_profit = 0`.
2.  Iterate `buy_day` from `0` to `prices.length - 2` (inclusive, as we need at least one day after for selling).
    *   Iterate `sell_day` from `buy_day + 1` to `prices.length - 1` (inclusive).
        *   Calculate `current_profit = prices[sell_day] - prices[buy_day]`.
        *   If `current_profit > max_profit`, update `max_profit = current_profit`.
3.  Return `max_profit`.

**Example Walkthrough (`prices = [7,1,5,3,6,4]`):**

| `buy_day` (i) | `prices[i]` | `sell_day` (j) | `prices[j]` | `current_profit` | `max_profit` |
| :------------ | :---------- | :------------- | :---------- | :--------------- | :----------- |
| 0 (Day 1)     | 7           | 1 (Day 2)      | 1           | 1 - 7 = -6       | 0            |
|               |             | 2 (Day 3)      | 5           | 5 - 7 = -2       | 0            |
|               |             | 3 (Day 4)      | 3           | 3 - 7 = -4       | 0            |
|               |             | 4 (Day 5)      | 6           | 6 - 7 = -1       | 0            |
|               |             | 5 (Day 6)      | 4           | 4 - 7 = -3       | 0            |
| 1 (Day 2)     | 1           | 2 (Day 3)      | 5           | 5 - 1 = 4        | 4            |
|               |             | 3 (Day 4)      | 3           | 3 - 1 = 2        | 4            |
|               |             | 4 (Day 5)      | 6           | 6 - 1 = 5        | 5            |
|               |             | 5 (Day 6)      | 4           | 4 - 1 = 3        | 5            |
| 2 (Day 3)     | 5           | 3 (Day 4)      | 3           | 3 - 5 = -2       | 5            |
|               |             | 4 (Day 5)      | 6           | 6 - 5 = 1        | 5            |
|               |             | 5 (Day 6)      | 4           | 4 - 5 = -1       | 5            |
| ...           |             | ...            | ...         | ...              | 5            |

**Complexity Analysis:**
*   **Time Complexity:** O(N^2)
    *   The outer loop runs N-1 times.
    *   The inner loop runs up to N-1 times (decreasing with `i`).
    *   In the worst case, it's roughly (N-1) * (N/2) operations, which simplifies to O(N^2).
*   **Space Complexity:** O(1)
    *   We only use a few variables to store `max_profit`, `buy_day`, `sell_day`, and `current_profit`.

### Approach 2: One-Pass (Optimized / Greedy)

**Logic:**
The key insight here is that to maximize profit for a given sell day, we need to have bought the stock at the lowest possible price *before or on that sell day*. We can maintain a variable `min_price` that tracks the minimum price encountered so far as we iterate through the `prices` array. For each new `price` (potential sell day), we calculate the potential profit by subtracting `min_price` from the `current_price`. We then update our `max_profit` if this new potential profit is greater. We also continuously update `min_price` if we find an even lower price.

**Algorithm:**
1.  Initialize `min_price` to a very large number (or the first price in the array, `prices[0]`, since the array is guaranteed to have at least one element).
2.  Initialize `max_profit = 0`.
3.  Iterate through each `price` in the `prices` array:
    *   If `current_price < min_price`:
        *   Update `min_price = current_price`. (We found a new potential best day to buy).
    *   Else (if `current_price >= min_price`):
        *   Calculate `current_profit = current_price - min_price`.
        *   Update `max_profit = max(max_profit, current_profit)`. (We try to sell on this day, using the lowest `min_price` found so far).
4.  Return `max_profit`.

**Example Walkthrough (`prices = [7,1,5,3,6,4]`):**

Initial: `min_price = 7`, `max_profit = 0`

| `price` (current day) | `min_price > price`? | Action                                   | `min_price` | `current_profit` | `max_profit` |
| :-------------------- | :------------------- | :--------------------------------------- | :---------- | :--------------- | :----------- |
| 7 (Day 1)             | False (7 > 7 is false) | `current_profit = 7 - 7 = 0`             | 7           | 0                | 0            |
| 1 (Day 2)             | True (7 > 1)         | `min_price = 1`                          | 1           | -                | 0            |
| 5 (Day 3)             | False (1 > 5 is false) | `current_profit = 5 - 1 = 4`             | 1           | 4                | 4            |
| 3 (Day 4)             | False (1 > 3 is false) | `current_profit = 3 - 1 = 2`             | 1           | 2                | 4            |
| 6 (Day 5)             | False (1 > 6 is false) | `current_profit = 6 - 1 = 5`             | 1           | 5                | 5            |
| 4 (Day 6)             | False (1 > 4 is false) | `current_profit = 4 - 1 = 3`             | 1           | 3                | 5            |

Result: `max_profit = 5`

**Complexity Analysis:**
*   **Time Complexity:** O(N)
    *   We iterate through the `prices` array exactly once. Each operation inside the loop is constant time.
*   **Space Complexity:** O(1)
    *   We only use a few variables (`min_price`, `max_profit`, `current_profit`).

---

## 3. Detailed Explanation of the Logic

### Logic behind Brute Force:
The brute force approach directly translates the problem statement into code: "choose a single day to buy... and choosing a different day in the future to sell". By using nested loops, `i` represents the buy day and `j` represents the sell day, with the condition `j > i` explicitly enforced by the inner loop's starting point (`buy_day + 1`). This ensures we always buy before we sell. We exhaust all possible valid buy-sell pairs and simply pick the one that yields the highest profit. While correct, its quadratic time complexity makes it inefficient for large inputs (N up to 10^5).

### Logic behind the Provided Optimal Solution (One-Pass / Greedy):
The optimal solution is a greedy approach. At any point in time, as we iterate through the `prices` array, we want to maximize the potential profit if we were to sell on the *current day*. To do this, we must have bought the stock at the lowest possible price *up to and including the current day*.

The `min_price` variable serves this purpose. It keeps track of the absolute minimum price encountered from the beginning of the array up to the current day being processed.

When we are at `prices[i]`:
1.  **If `prices[i]` is less than `min_price`**: This means we've found a new lowest price point so far. This `prices[i]` becomes our new `min_price`. We don't calculate profit here because we just found a *new* potential buy day, and we still need a *future* day to sell to make a profit.
2.  **If `prices[i]` is greater than or equal to `min_price`**: This means `prices[i]` could be a profitable selling day if we bought at `min_price`. We calculate the `current_profit = prices[i] - min_price`. Since `min_price` always holds the lowest price encountered *before or at* `prices[i]`, this `current_profit` represents the maximum profit we could achieve if `prices[i]` were the *selling* day. We then compare this `current_profit` with our `max_profit` found so far and update `max_profit` accordingly.

This works because we are essentially asking: "For every possible sell day, what's the best buy day *before it* (or on it)?" By keeping `min_price` updated, we always have the best possible buy day readily available for any given sell day. Since we iterate through all days, we guarantee that we will eventually find the global maximum profit.

---

## 4. Time and Space Complexity Analysis

### Brute Force:
*   **Time Complexity:** O(N^2) - Due to nested loops iterating through all possible buy and sell day pairs.
*   **Space Complexity:** O(1) - Only a few variables are used, irrespective of input size.

### Optimal Solution (Provided Code):
*   **Time Complexity:** O(N)
    *   The algorithm iterates through the `prices` array exactly once (a single `for` loop).
    *   Inside the loop, operations (comparisons, subtractions, `max` function) are all constant time, O(1).
    *   Therefore, the total time complexity is proportional to the number of elements in the `prices` array, N.
*   **Space Complexity:** O(1)
    *   Only two variables (`min_price` and `max_profit`) are used, plus `current_profit` temporarily. The memory usage does not grow with the input size N.

---

## 5. Edge Cases and How They Are Handled

1.  **Empty `prices` array**:
    *   **Constraint Handling**: The problem constraint `1 <= prices.length` states that the array will not be empty. So, this specific edge case doesn't need explicit handling in the code.
2.  **`prices` array with only one element**: (e.g., `prices = [7]`)
    *   **Logic**: According to the problem, you must buy on one day and sell on a *different day in the future*. With only one day, no transaction is possible.
    *   **Code Handling**:
        *   `min_price` is initialized to `prices[0]`.
        *   `max_profit` is initialized to `0`.
        *   The loop runs once for `price = prices[0]`.
        *   `if min_price > price` (i.e., `prices[0] > prices[0]`) is `False`.
        *   The `else` block executes: `current_profit = prices[0] - min_price` (which is `prices[0] - prices[0] = 0`).
        *   `max_profit = max(0, 0) = 0`.
        *   The loop finishes, and `0` is returned, which is correct.
3.  **Prices are in strictly decreasing order**: (e.g., `prices = [7,6,4,3,1]`)
    *   **Logic**: No profit can be made as prices only go down. The maximum profit should be `0`.
    *   **Code Handling**:
        *   `min_price` starts at `7`.
        *   When `price = 6`, `min_price` becomes `6`. `max_profit` remains `0`.
        *   When `price = 4`, `min_price` becomes `4`. `max_profit` remains `0`.
        *   ...and so on. `min_price` keeps getting updated to the current `price` because `min_price` will always be greater than the new, smaller `price`. The `else` block (where profit is calculated) is never entered.
        *   `max_profit` remains `0` throughout and is correctly returned.
4.  **Prices are in strictly increasing order**: (e.g., `prices = [1,2,3,4,5]`)
    *   **Logic**: The best strategy is to buy on the first day (`1`) and sell on the last day (`5`) for a profit of `5-1=4`.
    *   **Code Handling**:
        *   `min_price` starts at `1`.
        *   When `price = 2`: `min_price` (1) is not greater than `2`. `current_profit = 2 - 1 = 1`. `max_profit = max(0, 1) = 1`.
        *   When `price = 3`: `min_price` (1) is not greater than `3`. `current_profit = 3 - 1 = 2`. `max_profit = max(1, 2) = 2`.
        *   ...and so on. `min_price` stays `1`. `max_profit` correctly updates to `1, 2, 3, 4`.
        *   Returns `4`, which is correct.
5.  **Prices with ups and downs**: (e.g., `prices = [7,1,5,3,6,4]`)
    *   **Logic**: This is the general case that the algorithm is designed for, finding the optimal buy point *before* a higher sell point, even if prices dip again later.
    *   **Code Handling**: As shown in the walkthrough example in section 2, the algorithm correctly identifies the `min_price` of `1` (on day 2) and the later `price` of `6` (on day 5) to yield the `max_profit` of `5`. The intermediate dip to `3` and `4` does not affect the optimal choice because `min_price` remains `1`.

---

## 6. Clean, Well-Commented Version of the Optimal Solution

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit achievable from a single buy and sell transaction.

        Args:
            prices: A list of integers where prices[i] is the price of a given
                    stock on the i-th day.

        Returns:
            The maximum profit that can be achieved. If no profit can be achieved,
            returns 0.
        """
        # Initialize min_price to the first day's price.
        # This variable will keep track of the lowest price encountered so far.
        # It's our potential "buy" price.
        # Constraints guarantee prices list has at least one element.
        min_price = prices[0]
        
        # Initialize max_profit to 0.
        # This variable will store the maximum profit found across all possible transactions.
        # If no profit is possible (e.g., prices always decrease), 0 is the correct default.
        max_profit = 0
        
        # Iterate through each price in the prices array.
        # Each 'price' in this loop represents a potential selling day's price.
        for price in prices:
            # Case 1: Current price is lower than the minimum price found so far.
            # This means we found a new, better day to potentially buy the stock.
            # We update min_price to this new low, as buying here would give us a
            # better base for future potential profits.
            if min_price > price:
                min_price = price
            # Case 2: Current price is higher than or equal to the minimum price found so far.
            # This means we can potentially make a profit by selling on this day.
            # We calculate the profit if we bought at 'min_price' and sold at 'price'.
            else:
                current_profit = price - min_price
                
                # Update max_profit if the current transaction yields a higher profit.
                # We always want to store the largest profit found so far.
                max_profit = max(max_profit, current_profit)
                
        # After iterating through all prices, max_profit will hold the highest
        # profit achievable from a single transaction.
        return max_profit
```

---

## 7. Key Insights and Patterns

1.  **Greedy Approach**: The optimal solution employs a greedy strategy. At each step, it makes the locally optimal decision (either updating the `min_price` or updating the `max_profit` based on the current `min_price`). This local optimality leads to a globally optimal solution because the choice made at each step doesn't preclude a better future choice; it merely updates the best possible "buy" point or "sell" outcome so far.

2.  **Tracking Minimum/Maximum So Far**: This is a very common pattern in array processing problems. When you need to find the "best" value (minimum, maximum, or a derived value like profit) that depends on prior elements in a sequence, maintaining a running minimum or maximum (or other relevant aggregated value) is highly effective. Examples include:
    *   Finding the maximum element in an array.
    *   Finding the minimum element in an array.
    *   Kadane's Algorithm for Maximum Subarray Sum (where you track the maximum sum ending at the current position, and the overall maximum sum). Our problem is a specific application of this idea where we want `max(price[j] - price[i])` for `j > i`. This is equivalent to `max(price[j] - min_price_up_to_j)`.

3.  **Single Pass Optimization**: Many problems that initially seem to require nested loops (O(N^2) complexity) can often be optimized to a single pass (O(N) complexity) by realizing that all the necessary information from previous iterations can be summarized and carried forward in a few variables. Here, `min_price` summarizes all the relevant information from `prices[0]` to `prices[i-1]` for calculating the profit at `prices[i]`.

4.  **Buy Before Sell Constraint**: The condition "buy before you sell" (`buy_day < sell_day`) is naturally handled by iterating and always considering the `min_price` *up to the current day* as the potential buy point for a sale on the current day. This ensures that any `min_price` used for a profit calculation always occurred on or before the `current_price` (potential sell day).

This problem is a foundational "greedy algorithm" problem and a great introduction to the pattern of optimizing an N^2 brute force solution to N by maintaining relevant state.