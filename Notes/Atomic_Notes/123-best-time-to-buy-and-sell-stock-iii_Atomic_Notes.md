Here is a set of atomic notes for LeetCode problem 123, "Best Time to Buy and Sell Stock III", suitable for spaced repetition:

-   **Concept**: Problem Goal - Maximize Profit
    -   **Context**: Find the maximum profit from buying and selling a stock based on an array of daily prices.
    -   **Example**: `prices = [3,3,5,0,0,3,1,4]`, max profit is `6`.

-   **Concept**: Constraint - At Most Two Transactions
    -   **Context**: The problem explicitly limits the total number of buy-sell pairs to a maximum of two.
    -   **Example**: N/A

-   **Concept**: Constraint - No Simultaneous Transactions
    -   **Context**: You must sell any currently held stock before you can buy another one. A new transaction can only begin after the previous one is fully completed.
    -   **Example**: N/A

-   **Concept**: Input Size Implication
    -   **Context**: `prices.length` up to 10^5 implies that solutions with O(N) or O(N log N) time complexity are required; O(N^2) or higher would be too slow.
    -   **Example**: N/A

-   **Concept**: Optimal Approach Name
    -   **Context**: The most efficient solution for this problem is a Space-Optimized Dynamic Programming (often called a State Machine DP).
    -   **Example**: N/A

-   **Concept**: `buy_profits[k]` State Definition
    -   **Context**: In the State Machine DP, `buy_profits[k]` stores the maximum profit (or minimum cost/net value) after completing `k-1` full transactions and *then* buying the `k`-th stock.
    -   **Example**: `buy_profits[1]` represents the net value after buying the 1st stock (since `k-1=0` transactions completed).

-   **Concept**: `sell_profits[k]` State Definition
    -   **Context**: In the State Machine DP, `sell_profits[k]` stores the maximum total profit after completing `k` full transactions (i.e., after selling the `k`-th stock).
    -   **Example**: `sell_profits[2]` represents the total maximum profit after completing two transactions.

-   **Concept**: `buy_profits[k]` Update Rule
    -   **Context**: The recurrence for `buy_profits[k]` considers either keeping its previous best value or buying the `k`-th stock today using the best profit from `k-1` completed transactions (`sell_profits[k-1]`).
    -   **Example**: `buy_profits[k] = max(buy_profits[k], sell_profits[k - 1] - price)`

-   **Concept**: `sell_profits[k]` Update Rule
    -   **Context**: The recurrence for `sell_profits[k]` considers either keeping its previous best value or selling the `k`-th stock today, adding the current `price` to the profit/cost of having bought the `k`-th stock (`buy_profits[k]`).
    -   **Example**: `sell_profits[k] = max(sell_profits[k], buy_profits[k] + price)`

-   **Concept**: Initialization of `buy_profits` Array
    -   **Context**: `buy_profits` elements are initialized to `float('-inf')` to ensure any actual purchase (which costs money, thus making the net profit negative or less positive) will correctly update these values.
    -   **Example**: `buy_profits = [float('-inf')] * (num_transactions + 1)`

-   **Concept**: Initialization of `sell_profits` Array
    -   **Context**: `sell_profits` elements are initialized to `0`. `sell_profits[0]` acts as a base case (zero profit for zero transactions), crucial for calculating `buy_profits[1]`.
    -   **Example**: `sell_profits = [0] * (num_transactions + 1)`

-   **Concept**: Final Result Retrieval
    -   **Context**: After iterating through all prices, the maximum profit for the allowed number of transactions (`num_transactions`, which is 2) is found in `sell_profits[num_transactions]`.
    -   **Example**: For K=2, the solution returns `sell_profits[2]`.

-   **Concept**: Time Complexity of Optimal Solution
    -   **Context**: The optimal solution involves one loop over prices (N iterations) and an inner loop for K transactions (2 iterations).
    -   **Example**: O(N * K), which simplifies to O(N) since K=2 is a constant.

-   **Concept**: Space Complexity of Optimal Solution
    -   **Context**: The optimal solution uses two arrays (`buy_profits`, `sell_profits`) whose size depends only on the number of allowed transactions, K.
    -   **Example**: O(K), which simplifies to O(1) since K=2 is a constant.

-   **Concept**: Edge Case - Empty Prices Array
    -   **Context**: If the input `prices` list is empty, no transactions can be made.
    -   **Example**: The code explicitly returns `0` for `prices = []`.

-   **Concept**: Edge Case - Prices Length Less Than Two
    -   **Context**: If `prices.length` is less than 2 (e.g., `[7]`), a buy-sell transaction cannot be completed.
    -   **Example**: The algorithm correctly returns `0` as no profit can be generated.

-   **Concept**: Edge Case - Strictly Decreasing Prices
    -   **Context**: If all prices are decreasing (`[7,6,4,3,1]`), no profitable transaction is possible.
    -   **Example**: The `sell_profits` array will correctly remain `0` throughout the execution, indicating no profit.

-   **Concept**: DP Pattern - Fixed Number of Transactions
    -   **Context**: The State Machine DP pattern (`buy_k`, `sell_k` variables) is a general and efficient approach for stock problems with a fixed, maximum number of allowed transactions (K).
    -   **Example**: Applicable to LeetCode 188 (Best Time to Buy and Sell Stock IV) for general K.

-   **Concept**: DP Pattern - Transaction Dependency
    -   **Context**: The updates for `buy_profits[k]` and `sell_profits[k]` ensure correct transaction ordering: `buy_profits[k]` depends on `sell_profits[k-1]` (previous transaction completed), and `sell_profits[k]` depends on `buy_profits[k]` (current transaction bought).
    -   **Example**: This prevents simultaneous transactions and ensures a buy precedes a sell.

-   **Concept**: Alternative - Two-Pass Dynamic Programming
    -   **Context**: For K=2 specifically, the problem can be solved by breaking it into finding the best single transaction up to day `i` and the best single transaction from day `i` onwards, then summing for all `i`.
    -   **Example**: Calculating `left_profits[i]` and `right_profits[i]` arrays and finding `max(left_profits[i] + right_profits[i])`.