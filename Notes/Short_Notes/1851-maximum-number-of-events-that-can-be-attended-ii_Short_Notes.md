Here are concise notes for quick revision of LeetCode 1851: Maximum Number of Events That Can Be Attended II.

---

### LeetCode 1851: Maximum Number of Events That Can Be Attended II

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Maximize total `value` by attending at most `k` events.
*   **Events:** `[startDay, endDay, value]`.
*   **Rule:** Non-overlapping. If event A ends on `E_A`, event B must start on `S_B` where `S_B >= E_A + 1` (i.e., `S_B > E_A`).
*   **Constraints:**
    *   `1 <= k <= events.length`
    *   `1 <= k * events.length <= 10^6` (Crucial hint for complexity - suggests `N*K` or `N*K*logN`).
    *   `startDay/endDay` up to `10^9` (relative ordering matters, not absolute values).

**2. Core Algorithmic Approach:**
*   **Dynamic Programming (DP) with Memoization (Top-Down).**
*   **Pre-processing:** Sort `events` array by `startDay`.
*   **DP State:** `dp(i, count)` represents the maximum value achievable by considering events from index `i` onwards, with `count` events remaining to be attended.
*   **Recursive Choices for `dp(i, count)`:**
    1.  **Skip `events[i]`:** Call `dp(i + 1, count)`.
    2.  **Attend `events[i]`:** Add `events[i][2]` (its value), then find the *next non-overlapping event* and call `dp(next_idx, count - 1)`.
*   **Next Non-Overlapping Event (`next_idx`)**: Found efficiently using `bisect_right` on the sorted `events` array. Search for the first event whose `startDay` is strictly greater than `events[i][1]` (current event's `endDay`).

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(N log N + N * K * log N)`
    *   `O(N log N)` for initial sorting.
    *   `O(N * K)` states for DP (`N` event indices, `K` counts).
    *   `O(log N)` per state for `bisect_right` call.
    *   Dominant term: `O(N * K * log N)`. This fits within `10^6 * log(N_{max}) ~ 10^7` operations.
*   **Space Complexity:** `O(N * K)` for the memoization cache (DP table).
    *   Feasible due to `N * K <= 10^6` constraint.

**4. Critical Edge Cases:**
*   **`k = 0`:** Handled by `count == 0` base case in DP (returns 0).
*   **Empty `events` list / `i == n`:** Handled by `i == n` base case in DP (returns 0).
*   **All events overlap:** The `bisect_right` will often return `n` (no future non-overlapping event), effectively allowing only one event to be chosen (the max valued one).
*   **`startDay`/`endDay` are large (`10^9`):** Handled correctly as only relative order matters. `float('inf')` used with `bisect_right` for comparison.

**5. Key Patterns & Techniques Used:**
*   **Dynamic Programming (DP):** Classic "Choose or Not Choose" problem structure, exhibiting optimal substructure and overlapping subproblems.
*   **Sorting:** Essential for processing events chronologically and enabling efficient lookups.
*   **Binary Search (`bisect_right`):** Optimizes finding the next valid item from `O(N)` to `O(log N)`, critical for performance.
*   **Memoization (`functools.lru_cache`):** Simplifies DP implementation by automatically caching results, preventing redundant computations.
*   **Tuple Comparison with `bisect_right`:** Using `[target_val, float('inf'), float('inf')]` as the search key to ensure `bisect_right` correctly finds the first tuple whose first element (e.g., `startDay`) is strictly greater than `target_val`.