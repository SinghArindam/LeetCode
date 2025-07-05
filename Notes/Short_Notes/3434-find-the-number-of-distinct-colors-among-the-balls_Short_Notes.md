Here are concise short notes for quick revision of LeetCode problem 3434:

---

### LeetCode 3434: Find Distinct Colors Among Balls (Quick Revision)

#### 1.  Key Problem Characteristics & Constraints:
*   **Goal:** Track number of *distinct* colors among balls *after each query*.
*   **Balls:** Labeled `0` to `limit`. Initially uncolored. Uncolored balls don't count.
*   **Queries `[x, y]`:** Ball `x` gets color `y`. Balls can be recolored.
*   **`limit` is HUGE (up to `10^9`)**: Implies *cannot* use an array indexed by ball ID.
*   **`n` (queries) is MODERATE (up to `10^5`)**: Requires an `O(N)` or `O(N log N)` solution.
*   Colors `y` are positive integers (up to `10^9`).

#### 2.  Core Algorithmic Approach: Incremental Tracking with Hash Maps
*   **Data Structures:**
    1.  `ball_to_color` (Hash Map): `ball_id -> current_color`. Stores color of *only colored balls*.
    2.  `color_freq` (Hash Map): `color_id -> count_of_balls_with_this_color`. Tracks frequency of each *active* color.
*   **Distinct Colors Count:** `len(color_freq)` (because `color_freq` only stores colors with count > 0).
*   **Process per query `[ball, new_color]`:**
    1.  **Check `ball`'s `prev_color`:**
        *   If `ball` was colored (in `ball_to_color`):
            *   Get `prev_color`.
            *   **Optimization:** If `prev_color == new_color`, no change; append `len(color_freq)` and skip.
            *   Decrement `color_freq[prev_color]`.
            *   **CRITICAL:** If `color_freq[prev_color]` becomes 0, `del color_freq[prev_color]` (no longer distinct).
    2.  **Update `ball_to_color[ball] = new_color`**.
    3.  **Increment `color_freq[new_color]`**: Use `color_freq.get(new_color, 0) + 1` for new or existing colors.
    4.  **Append `len(color_freq)` to result list**.

#### 3.  Important Time/Space Complexity:
*   **Time Complexity:** `O(N)` average. Each query involves a few hash map operations, which are `O(1)` on average.
*   **Space Complexity:** `O(N)` average. `ball_to_color` stores up to `N` unique balls. `color_freq` stores up to `N` unique colors.

#### 4.  Critical Edge Cases:
*   **Ball colored for the first time:** `ball_to_color` won't have it; `color_freq.get(new_color, 0)` correctly initializes.
*   **Ball changes color:** Both old and new color frequencies are correctly adjusted.
*   **Ball re-colored with *same* color:** Handled by explicit `prev_color == new_color` check, prevents redundant operations.
*   **Color frequency drops to zero:** `del color_freq[prev_color]` is vital to ensure `len(color_freq)` remains accurate.
*   **Large `limit`:** Hash maps are sparse, only storing data for queried ball IDs, efficiently handling the large range.
*   Ball label 0: Handled like any other integer key in a hash map.

#### 5.  Key Patterns or Techniques Used:
*   **Hash Maps for Sparse Data / Large Ranges:** Efficiently map arbitrary, large-range IDs to values.
*   **Frequency Tracking:** Using a map to count occurrences to derive distinct counts.
*   **Incremental Updates (Delta Calculation):** Modifying state based on the *change* from the current operation, rather than rebuilding from scratch. This yields `O(1)` updates per operation.
*   **Handling Removal from Distinct Set:** Explicitly removing items from frequency map when their count drops to zero is crucial for accurate `len()` results.