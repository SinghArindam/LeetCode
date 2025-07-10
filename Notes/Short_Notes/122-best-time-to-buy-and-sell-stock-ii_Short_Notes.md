Here are concise short notes for LeetCode Problem 122: "Best Time to Buy and Sell Stock II", suitable for quick revision:

---

### LeetCode 122: Best Time to Buy and Sell Stock II - Quick Revision Notes

**1. Problem Characteristics & Constraints:**
*   **Goal:** Maximize total profit from stock transactions.
*   **Key Rule:** Multiple (unlimited) transactions allowed.
*   **Holdings:** Can hold at most one share at any time (must sell before buying again).
*   **Flexibility:** Can buy and immediately sell on the same day.
*   **No Fees/Cooldowns:** No transaction costs or forced waiting periods.
*   **Input:** `prices` array (`1 <= N <= 3*10^4`, `0 <= prices[i] <= 10^4`).

**2. Core Algorithmic Approach (Optimal Solution): Greedy**
*   **Concept:** Since unlimited transactions are allowed (and no fees/cooldowns), simply capture *every single positive price increase*.
*   **Logic:** Iterate through the `prices` array from day 1 (`i`) to `N-1`. If `prices[i] > prices[i-1]`, add the difference (`prices[i] - prices[i-1]`) to a running `total_profit`.
*   **Why it works:** Any multi-day profit (e.g., buy at `P_low`, sell at `P_high`) can be equivalently decomposed into a sum of consecutive daily profits (e.g., `(P_day2 - P_day1) + (P_day3 - P_day2) + ...`). Summing all positive daily differences correctly captures the maximum total profit.

**3. Complexity:**
*   **Time Complexity:** **O(N)** - Single pass through the `prices` array.
*   **Space Complexity:** **O(1)** - Uses a few constant variables.

**4. Critical Edge Cases:**
*   **Empty/Single-Element Array:** Handled; loop won't run, `total_profit` remains 0. Correct (no possible profit).
*   **Strictly Increasing Prices (`[1,2,3,4,5]`):** Correctly sums `(2-1)+(3-2)+(4-3)+(5-4) = 4`.
*   **Strictly Decreasing/Flat Prices (`[7,6,4,3,1]`, `[5,5,5]`):** `prices[i] > prices[i-1]` condition is never met; `total_profit` remains 0. Correct (no opportunities for positive profit).
*   The greedy approach inherently handles these by only adding positive differences.

**5. Key Patterns / Techniques:**
*   **Greedy Strategy for Unlimited Transactions:** This is the most crucial takeaway. When you can transact as much as you want without penalties, taking every small profit is optimal.
*   **Profit Decomposition:** The total profit `(P_sell - P_buy)` can be seen as `sum(max(0, P_i - P_{i-1}))` for all `i` between `buy_day` and `sell_day`.
*   **Contrast with Stock Problem Variants:**
    *   **I (One Transaction):** Requires tracking `min_price_so_far`. Greedy *sum* doesn't work.
    *   **III/IV (K Transactions):** Requires DP with transaction count as a state.
    *   **Cooldown/Fees:** Requires DP modifications to account for additional constraints.
*   **Linear Scan (O(N)):** Always consider if a single pass can solve array problems by making local optimal choices.