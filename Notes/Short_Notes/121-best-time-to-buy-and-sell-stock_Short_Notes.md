Here are concise short notes for LeetCode problem 121:

---

## LeetCode 121: Best Time to Buy and Sell Stock (Quick Revision Notes)

### 1. Key Problem Characteristics & Constraints
*   **Goal:** Maximize profit from a **single transaction** (buy then sell).
*   **Rule:** Must buy on one day and sell on a **different day in the future**.
*   **Output:** Return max profit; `0` if no profit possible.
*   **Constraints:**
    *   `1 <= prices.length <= 10^5` (array never empty)
    *   `0 <= prices[i] <= 10^4` (prices non-negative)

### 2. Core Algorithmic Approach (One-Pass / Greedy)
*   **Logic:** Iterate through the prices, keeping track of the lowest price seen so far (`min_price`). For each current price (potential sell day), calculate the potential profit by subtracting `min_price`. Update the overall maximum profit found.
*   **Algorithm:**
    1.  Initialize `min_price = prices[0]` (or `infinity`).
    2.  Initialize `max_profit = 0`.
    3.  For each `current_price` in `prices`:
        *   If `current_price < min_price`: Update `min_price = current_price` (found a better buy point).
        *   Else (`current_price >= min_price`): Calculate `current_profit = current_price - min_price`. Update `max_profit = max(max_profit, current_profit)`.
    4.  Return `max_profit`.

### 3. Important Time/Space Complexity Facts
*   **Time Complexity:** O(N)
    *   A single pass through the `prices` array.
*   **Space Complexity:** O(1)
    *   Uses only a few constant variables (`min_price`, `max_profit`).

### 4. Critical Edge Cases
*   **Array with one element:** Correctly returns `0` (no future day to sell).
*   **Strictly decreasing prices:** Correctly returns `0` (no profit possible, `min_price` always updates, `max_profit` stays `0`).
*   **Strictly increasing prices:** Correctly finds max profit (buys at first min, sells at last max).
*   **Profit initialization:** `max_profit = 0` correctly handles cases where no profit can be made.

### 5. Key Patterns or Techniques Used
*   **Greedy Approach:** Makes locally optimal choices (update `min_price` or `max_profit`) which lead to a globally optimal solution.
*   **Tracking Minimum/Maximum So Far:** Common pattern where a running min/max value is maintained to optimize calculations for subsequent elements.
*   **Single-Pass Optimization:** Transforms a naive O(N^2) brute-force solution into an efficient O(N) solution by carrying forward necessary state.
*   **"Buy Before Sell" Constraint:** Naturally handled by processing the array in forward order and always using the `min_price` *encountered up to the current day*.