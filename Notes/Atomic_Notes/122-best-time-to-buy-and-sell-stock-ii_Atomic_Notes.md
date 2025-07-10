Here is a set of atomic notes for LeetCode Problem 122: "Best Time to Buy and Sell Stock II", formatted for spaced repetition learning:

---

-   **Concept**: Maximize Total Profit from Stock Transactions
    -   **Context**: The primary goal of LeetCode Problem 122, given a list of daily stock prices.
    -   **Example**: For `prices = [7,1,5,3,6,4]`, the goal is to find the maximum sum of profits from multiple buy/sell operations (e.g., buy at 1, sell at 5; buy at 3, sell at 6 for total profit 7).

-   **Constraint: Multiple/Unlimited Transactions**
    -   **Concept**: You can buy and sell the stock as many times as you want.
    -   **Context**: This is the most crucial rule in LeetCode 122 that enables the simple greedy strategy, differentiating it from other stock problems.
    -   **Example**: If `prices = [1,2,3]`, you can buy at 1, sell at 2 (+1 profit), then buy at 2, sell at 3 (+1 profit), totaling 2.

-   **Constraint: One Share at a Time**
    -   **Concept**: You can only hold at most one share of the stock at any given time.
    -   **Context**: Implies you must sell your current stock before buying another one.
    -   **Example**: You cannot buy on Day 0 and then buy again on Day 1 without selling the Day 0 stock first.

-   **Constraint: No Transaction Fees or Cooldowns**
    -   **Concept**: There are no additional costs associated with transactions, nor any forced waiting periods between selling and buying.
    -   **Context**: The absence of these constraints further simplifies the optimal strategy in LeetCode 122, allowing for a pure greedy approach.
    -   **Example**: After selling on Day `i`, you can buy again immediately on Day `i` (if profitable) or Day `i+1`.

-   **Constraint: Same Day Buy/Sell Interpretation**
    -   **Concept**: While you can buy and sell on the "same day" conceptually, it practically means you can buy on day `i` and sell on day `i+1` immediately if `prices[i+1] > prices[i]`.
    -   **Context**: This reinforces the idea of immediate re-entry and profit-taking on consecutive upward price movements.
    -   **Example**: If `prices = [1, 5]`, you buy at 1 (Day 0) and sell at 5 (Day 1) for a profit of 4.

-   **Inefficient Approach: Brute Force (Recursive/Backtracking)**
    -   **Concept**: Explores every possible combination of buying, selling, or doing nothing on each day.
    -   **Context**: A conceptually straightforward but computationally infeasible approach for LeetCode 122 without memoization.
    -   **Example**: Leads to O(2^N) time complexity due to an exponential search space.

-   **General Approach: Dynamic Programming (DP)**
    -   **Concept**: Defines DP states (e.g., `dp[i][0]` for max profit without stock on day `i`, `dp[i][1]` for max profit with stock on day `i`) to solve overlapping subproblems.
    -   **Context**: A common pattern for many stock problems, but for LeetCode 122, the greedy solution is simpler and more optimal due to unlimited transactions.
    -   **Example**: Transition `dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])`.

-   **Optimal Approach: Greedy Strategy**
    -   **Concept**: Since unlimited transactions are allowed, capture every single positive price increase.
    -   **Context**: The most efficient and intuitive solution for LeetCode 122.
    -   **Example**: For `prices = [1, 5, 3, 6]`, profit is `(5-1)` + `(6-3) = 4 + 3 = 7`.

-   **Principle: Profit Decomposition**
    -   **Concept**: A large profit from buying at `P_buy` and selling at `P_sell` (where `P_sell > P_buy`) can be equivalently achieved by summing all positive daily differences (`max(0, prices[k] - prices[k-1])`) between `buy_day` and `sell_day`.
    -   **Context**: This mathematical property justifies why the greedy approach works for LeetCode 122.
    -   **Example**: For `prices = [1, 2, 3, 4, 5]`, `(5-1) = 4` is equivalent to `(2-1)+(3-2)+(4-3)+(5-4) = 4`.

-   **Greedy Algorithm Steps**
    -   **Concept**: Initialize `total_profit = 0`. Iterate `i` from 1 to `n-1`. If `prices[i] > prices[i-1]`, add `prices[i] - prices[i-1]` to `total_profit`.
    -   **Context**: The straightforward implementation of the greedy strategy for LeetCode 122.
    -   **Example**: `prices = [1, 5, 2, 6]`: `total_profit += (5-1)=4`; `total_profit` remains 4 for `2-5`; `total_profit += (6-2)=4`. Final `total_profit = 8`.

-   **Time Complexity of Greedy Solution**
    -   **Concept**: O(N).
    -   **Context**: The greedy algorithm for LeetCode 122 involves a single pass through the `prices` array.
    -   **Example**: For an input array of `N` elements, the algorithm performs approximately `N` constant-time operations.

-   **Space Complexity of Greedy Solution**
    -   **Concept**: O(1).
    -   **Context**: The greedy algorithm for LeetCode 122 uses a fixed, small number of variables regardless of input size.
    -   **Example**: Only `n` (length), `total_profit`, and the loop index `i` are stored.

-   **Edge Case Handling: Empty/Single-Element Array**
    -   **Concept**: Returns 0 profit.
    -   **Context**: The greedy loop (`range(1, n)`) naturally handles these cases by not executing, leaving `total_profit` at its initial 0.
    -   **Example**: `maxProfit([])` returns `0`. `maxProfit([100])` returns `0`.

-   **Edge Case Handling: Strictly Increasing Prices**
    -   **Concept**: Correctly sums all positive daily differences, resulting in `(max_price - min_price)`.
    -   **Context**: The greedy approach efficiently accumulates profit across continuous upward trends.
    -   **Example**: `maxProfit([1,2,3,4,5])` yields `(2-1)+(3-2)+(4-3)+(5-4) = 4`.

-   **Edge Case Handling: Strictly Decreasing/Flat Prices**
    -   **Concept**: Returns 0 profit.
    -   **Context**: The condition `prices[i] > prices[i-1]` is never met, so no profit is added.
    -   **Example**: `maxProfit([7,6,5,4])` yields `0`. `maxProfit([5,5,5])` yields `0`.

-   **General Pattern: Greedy for Unlimited Actions**
    -   **Concept**: When a problem allows unlimited operations (like transactions) without penalizing sequential choices (e.g., no fees, cooldowns), a greedy strategy is often optimal.
    -   **Context**: A core insight derived from LeetCode 122 applicable to various algorithm problems.
    -   **Example**: If you can always take a local gain without hindering future gains, do so.

-   **Contrast with Stock Problem Variant I (At most One Transaction)**
    -   **Concept**: Requires finding the *single largest* price difference, typically by tracking `min_price_so_far`, not summing all positive daily differences.
    -   **Context**: Highlights why the greedy "sum daily differences" approach is specific to LeetCode 122's unlimited transaction rule.
    -   **Example**: For `[7,1,5,3,6,4]`, Stock I profit is `6-1=5`. Stock II profit is `(5-1)+(6-3)=7`.

-   **Contrast with Stock Problem Variants III/IV (Limited Transactions)**
    -   **Concept**: Problems with a fixed limit (K) on transactions typically necessitate Dynamic Programming, often incorporating the transaction count into the DP state.
    -   **Context**: LeetCode 122's simplicity stems from the *absence* of such limits.
    -   **Example**: `dp[k][i][hold_status]` state is common for these problems.

-   **Contrast with Stock Problem Variants with Cooldown/Fees**
    -   **Concept**: Additional constraints like a cooldown period after selling or a fixed transaction fee require more complex DP states or modified greedy conditions.
    -   **Context**: The straightforward greedy solution for LeetCode 122 works because these complicating factors are absent.
    -   **Example**: With fees, you'd only add `prices[i] - prices[i-1]` if it's greater than the fee.