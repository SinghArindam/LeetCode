Here are concise short notes for quick revision of LeetCode problem 135 - Candy:

---

### LeetCode 135: Candy (Hard) - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Distribute minimum total candies to `n` children in a line.
*   **Rules:**
    1.  Each child gets **at least 1 candy**.
    2.  Children with **higher rating** must get **more candies** than their immediate neighbors.
*   **Input:** `ratings` array (integer values).
*   **Constraints:** `1 <= n <= 2 * 10^4`, `0 <= ratings[i] <= 2 * 10^4`.
    *   `n` can be large.
    *   Ratings are non-negative.

**2. Core Algorithmic Approach (Two-Pass Iterative Dynamic Programming):**
This is the most common and robust optimal approach.
*   **Logic:** Conditions depend on both left and right neighbors. Solve by propagating requirements in two directions, then combine.
*   **Steps:**
    1.  **Initialization:** Create `candies` array of size `n`, initialize all elements to `1`. (Satisfies "at least 1 candy").
    2.  **First Pass (Left-to-Right):**
        *   Iterate `i` from `1` to `n-1`.
        *   If `ratings[i] > ratings[i-1]`: `candies[i] = candies[i-1] + 1`. (Ensures current child gets more than left neighbor).
        *   (If `ratings[i] <= ratings[i-1]`, no change from this pass is needed for `candies[i]`, as `candies[i]` starts at 1 and `candies[i-1]` is set appropriately).
    3.  **Second Pass (Right-to-Left):**
        *   Iterate `i` from `n-2` down to `0`.
        *   If `ratings[i] > ratings[i+1]`: `candies[i] = max(candies[i], candies[i+1] + 1)`. (Ensures current child gets more than right neighbor, `max` accounts for any prior increases from L-R pass).
    4.  **Final Sum:** Sum all values in the `candies` array.

*   **Alternative:** Recursive DP with Memoization works similarly, calculating requirements from left and right directions, then taking `max`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** O(N)
    *   Each of the two passes iterates through `N` elements once.
*   **Space Complexity:** O(N)
    *   For the `candies` array.
*   *Note:* An advanced O(1) space solution exists (slope tracking), but it's significantly more complex to implement correctly.

**4. Critical Edge Cases to Remember:**
*   **`n = 1`:** The single child gets 1 candy. (Correctly handled by initialization).
*   **All ratings are the same (e.g., `[2,2,2]`):** Each child gets 1 candy. (Conditions for `>` neighbors are never met, so all `candies[i]` remain 1).
*   **Strictly increasing ratings (e.g., `[1,2,3]`):** Candies `[1,2,3]`. (L-R pass sets it; R-L pass finds no `>` condition).
*   **Strictly decreasing ratings (e.g., `[3,2,1]`):** Candies `[3,2,1]`. (L-R pass keeps `[1,1,1]`; R-L pass propagates increments from right).
*   **V-shape (`[3,2,1,2,3]`):** Candies `[3,2,1,2,3]`. (Valley gets 1, then values increase outwards).
*   **A-shape (`[1,2,3,2,1]`):** Candies `[1,2,3,2,1]`. (Peak correctly receives `max` candies from both sides).

**5. Key Patterns or Techniques Used:**
*   **Dynamic Programming (DP):** The problem has optimal substructure and overlapping subproblems. Local choices (`+1` candy) combine to a global minimum.
*   **Two-Pass Iteration:** A common strategy for problems with dependencies in both directions (left & right).
*   **Greedy Approach:** Incrementing candies by 1 based on a higher rating is a greedy local decision that, when combined with the two-pass `max()` strategy, leads to the global minimum.
*   **Minimization via `max()`:** When an element needs to satisfy multiple "at least X" conditions (e.g., from left and from right), the required minimum is `max(all_conditions)`.
*   **Memoization:** (If using recursive DP) Optimizes recursive calls by storing results of subproblems.