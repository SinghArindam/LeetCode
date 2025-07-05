This document provides a comprehensive analysis of LeetCode problem 3434, "Find the Number of Distinct Colors Among the Balls".

---

### 1. Problem Summary

The problem asks us to track the number of distinct colors applied to a set of balls after a series of queries. We are given:
*   `limit`: An integer representing the maximum label for balls. Balls are labeled from `0` to `limit`. Initially, all `limit + 1` balls are uncolored.
*   `queries`: A 2D array, where each `query[i] = [x, y]` means ball `x` is marked with color `y`.
    *   A ball can be recolored multiple times.
    *   Colors are positive integers. Uncolored balls do not count towards distinct colors.

After each query, we need to determine the total number of distinct colors present among all currently colored balls. The final output should be an array `result` where `result[i]` is the number of distinct colors after the `i`-th query.

**Constraints Highlight:**
*   `limit` can be very large (`10^9`), implying that we cannot use an array to store colors for all balls directly indexed by ball label.
*   `n` (number of queries) is up to `10^5`, suggesting that an `O(N)` or `O(N log N)` solution is required, not `O(N * limit)` or `O(N * M)` where M is the number of colored balls (which could be up to `min(N, limit+1)`).

---

### 2. Explanation of All Possible Approaches

#### A. Naive Approach: Re-calculate Distinct Colors After Each Query

**Idea:**
Maintain a data structure that stores the current color of each ball. After each query, iterate through all currently colored balls, collect their colors into a temporary set, and then take the size of the set.

**Data Structures:**
Since `limit` is very large, an array of size `limit+1` to store ball colors is not feasible due to memory constraints. We must use a hash map (dictionary in Python) to store only the balls that have been colored.
*   `ball_to_color_map`: A hash map where `key = ball_id` and `value = current_color`.

**Steps for each query `[x, y]`:**
1.  Update `ball_to_color_map[x] = y`.
2.  Create a new `set` of colors.
3.  Iterate through all `values` (colors) in `ball_to_color_map` and add them to the set.
4.  The number of distinct colors is `len(set)`. Add this to the `result` array.

#### B. Optimized Approach (The Provided Solution): Incremental Tracking with Frequency Maps

**Idea:**
To avoid re-iterating and rebuilding a set of colors after every query, we can maintain two pieces of information that allow us to update the count of distinct colors efficiently:
1.  The current color of each ball.
2.  The frequency of each color (how many balls currently have that specific color).

When a ball's color changes:
*   Its previous color might lose one ball. If that color's frequency drops to zero, it means that color is no longer present among *any* balls, and thus is no longer "distinct".
*   Its new color gains one ball. If this new color was previously not present (frequency 0), it now becomes a distinct color.

By managing these frequency counts, the number of distinct colors is simply the number of colors with a frequency greater than zero. This can be directly observed by the number of entries in the frequency map.

**Data Structures:**
*   `ball_to_color`: A hash map (`dict` in Python) where `key = ball_id` and `value = current_color`. This stores the current color of any ball that has been colored at least once.
*   `color_freq`: A hash map (`dict` in Python) where `key = color_id` and `value = count_of_balls_with_this_color`. This tracks the frequency of each color currently applied to *at least one* ball.

**Steps for each query `[ball, color]`:**
1.  **Check if the `ball` was previously colored:**
    *   If `ball` is in `ball_to_color`:
        *   Get `prev_color = ball_to_color[ball]`.
        *   **Optimization:** If `prev_color == color` (the ball is being colored with its existing color), no change to distinct colors occurs. Append the current distinct count (`len(color_freq)`) to `result` and continue to the next query.
        *   Decrement `color_freq[prev_color]` by 1.
        *   If `color_freq[prev_color]` becomes 0, it means `prev_color` is no longer used by any ball. Remove `prev_color` from `color_freq` (or `del color_freq[prev_color]`) to signify it's no longer a distinct color.
2.  **Update the `ball`'s color:**
    *   Set `ball_to_color[ball] = color`.
3.  **Update the frequency for the `new color`:**
    *   Increment `color_freq[color]` by 1. (Use `color_freq.get(color, 0) + 1` to handle cases where `color` is new).
4.  **Record the distinct count:**
    *   The number of distinct colors is `len(color_freq)`. Append this value to the `result` list.

---

### 3. Detailed Explanation of Logic

#### Naive Approach Logic:

The core idea is brute-force recalculation.
1.  **Initialization**: `ball_to_color_map = {}`, `results = []`.
2.  **Loop through queries**: For each `(ball, new_color)` in `queries`:
    a.  `ball_to_color_map[ball] = new_color` (Update the ball's color. If the ball was uncolored, it's added. If it was colored, its color is overwritten).
    b.  `distinct_colors_set = set()` (Create a fresh set).
    c.  `for color_val in ball_to_color_map.values():`
        `distinct_colors_set.add(color_val)` (Populate the set with all colors currently assigned to balls).
    d.  `results.append(len(distinct_colors_set))` (Store the count of distinct colors).
This approach is simple to understand but inefficient because step `c` involves iterating through potentially many colored balls in each query.

#### Optimized Approach Logic (Provided Solution):

This approach leverages hash maps for `O(1)` average time complexity for updates and lookups, allowing for incremental tracking.

1.  **Initialization**:
    *   `ball_to_color = {}`: Stores the current color of each ball. Keys are ball IDs (integers), values are colors (integers).
    *   `color_freq = {}`: Stores the count of how many balls currently have a particular color. Keys are colors (integers), values are counts (integers).
    *   `result = []`: Stores the distinct color count after each query.

2.  **Iterate through `queries`**: For each `(ball, color)` pair:

    a.  **Handle existing ball color (if any)**:
        `if ball in ball_to_color:`
        *   This means the ball `ball` was previously colored.
        *   `prev_color = ball_to_color[ball]`: Retrieve its previous color.

        `if prev_color == color:`
        *   This is an important optimization. If the ball is being re-colored with the *same* color it already had, then no change occurs to the set of distinct colors.
        *   `result.append(len(color_freq))`: Append the current distinct count and move to the next query. This avoids unnecessary map operations.

        `color_freq[prev_color] -= 1`: Decrement the count for the `prev_color`. One less ball has this color.

        `if color_freq[prev_color] == 0:`
        *   If the count for `prev_color` drops to zero, it means no balls currently have `prev_color`. Therefore, `prev_color` is no longer a distinct color.
        *   `del color_freq[prev_color]`: Remove `prev_color` from the `color_freq` map. This is crucial for `len(color_freq)` to accurately reflect the distinct colors.

    b.  **Update ball's new color**:
        `ball_to_color[ball] = color`: Assign the new `color` to `ball`. This overwrites the old color if one existed or adds a new entry if the ball was previously uncolored.

    c.  **Update frequency for the new color**:
        `color_freq[color] = color_freq.get(color, 0) + 1`: Increment the count for the `new color`.
        *   `color_freq.get(color, 0)` safely retrieves the current count for `color` (defaulting to 0 if `color` is not yet in the map, i.e., it's a brand new distinct color).
        *   This ensures `color` is added to `color_freq` with a count of 1 if it wasn't there before, or its existing count is increased.

    d.  **Append current distinct count**:
        `result.append(len(color_freq))`: `len(color_freq)` directly gives the number of distinct colors because `color_freq` only contains keys for colors that are currently held by at least one ball (i.e., `color_freq[c] > 0`).

3.  **Return `result`**: After processing all queries.

---

### 4. Time and Space Complexity Analysis

#### A. Naive Approach

*   **Time Complexity**:
    *   For each query `[x, y]`:
        *   Updating `ball_to_color_map[x] = y`: `O(1)` on average.
        *   Iterating through `ball_to_color_map.values()` and adding to a set: If `M` is the number of balls colored so far (which can be up to `N` or `limit+1`), this takes `O(M)` time.
    *   Since this `O(M)` operation happens for `N` queries, the total time complexity is `O(N * M)`. In the worst case, `M` can grow up to `N` (if all queries color distinct balls), leading to `O(N^2)`. If `limit` was small and we could use an array, it'd be `O(N * limit)`. Given `N=10^5`, `O(N^2)` (`10^10`) is too slow.

*   **Space Complexity**:
    *   `ball_to_color_map`: Stores at most `min(N, limit + 1)` ball-color pairs. In the worst case (all queries refer to distinct balls), this is `O(N)`.
    *   `distinct_colors_set`: Temporarily stores at most `N` distinct colors. `O(N)`.
    *   `result` array: Stores `N` integers. `O(N)`.
    *   Overall: `O(N)`.

#### B. Optimized Approach (Provided Solution)

*   **Time Complexity**:
    *   For each query `[ball, color]`:
        *   `ball in ball_to_color`: `O(1)` on average.
        *   `ball_to_color[ball]`, `color_freq[prev_color] -= 1`, `del color_freq[prev_color]`: All are `O(1)` on average for hash map operations.
        *   `ball_to_color[ball] = color`, `color_freq.get(color, 0) + 1`: All are `O(1)` on average.
        *   `len(color_freq)`: `O(1)` for Python dictionaries.
    *   Since each operation within the loop is `O(1)` on average, and there are `N` queries, the total time complexity is `O(N)`. This is highly efficient and required given the constraints.

*   **Space Complexity**:
    *   `ball_to_color`: Stores at most `min(N, limit + 1)` ball-color mappings. Max size is `N` entries. `O(N)`.
    *   `color_freq`: Stores at most `N` distinct colors (if all queries introduce a new distinct color). Max size is `N` entries. `O(N)`.
    *   `result` array: Stores `N` integers. `O(N)`.
    *   Overall: `O(N)`.

---

### 5. Edge Cases and How They Are Handled

*   **Ball colored for the first time**:
    *   The `if ball in ball_to_color:` check will be false. The code directly proceeds to `ball_to_color[ball] = color` and `color_freq[color] = color_freq.get(color, 0) + 1`. `color_freq.get(color, 0)` will correctly return 0, so the `new color` will be added to `color_freq` with a count of 1. This correctly increases the distinct color count.
*   **Ball changes color**:
    *   `if ball in ball_to_color:` is true. `prev_color` is retrieved.
    *   `color_freq[prev_color]` is decremented. If it becomes 0, `prev_color` is removed from `color_freq`, effectively reducing the distinct count by one (if it was unique to this ball).
    *   `color_freq[new_color]` is incremented. If `new_color` was not previously in `color_freq`, it gets added with count 1, effectively increasing the distinct count by one.
    *   This two-step process correctly adjusts the distinct color count based on the net change.
*   **Ball is re-colored with the *same* color**:
    *   The explicit `if prev_color == color:` check handles this efficiently. It recognizes that no change to distinct colors or frequencies is needed and directly appends the current `len(color_freq)` to `result`, then skips to the next query. Without this optimization, the code would still work: `color_freq[prev_color]` would be decremented and then `color_freq[color]` (which is the same as `prev_color`) would be incremented, resulting in no net change to `color_freq[color]` and thus `len(color_freq)` remaining the same. However, the explicit check avoids redundant hash map operations.
*   **All balls end up with the same color**:
    *   `color_freq` will eventually contain only one entry for that common color, and `len(color_freq)` will correctly be `1`.
*   **All balls end up with distinct colors**:
    *   `color_freq` will contain an entry for each unique color, and `len(color_freq)` will reflect the total number of unique colors.
*   **`limit` is large (`10^9`)**:
    *   The use of hash maps (`ball_to_color`, `color_freq`) avoids the memory and performance issues of array-based solutions when `limit` is large and the actual number of colored balls (`N`) is much smaller.
*   **Ball label `0`**:
    *   `queries[i][0]` can be `0`. Hash maps handle any valid integer key correctly.

---

### 6. Clean, Well-Commented Version of the Optimal Solution

```python
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # ball_to_color: A hash map (dictionary) to store the current color of each ball.
        # Key: ball_id (integer), Value: color_id (integer).
        # This is essential because 'limit' can be very large (up to 10^9),
        # so we cannot use an array to track all possible balls.
        ball_to_color = {}
        
        # color_freq: A hash map (dictionary) to store the frequency of each color.
        # Key: color_id (integer), Value: count of balls currently having this color (integer).
        # The number of distinct colors at any point is simply len(color_freq).
        color_freq = {}
        
        # result: A list to store the number of distinct colors after each query.
        result = []
        
        # Iterate through each query in the 'queries' list.
        for ball, color in queries:
            # Step 1: Handle the ball's previous color, if any.
            # Check if the ball 'ball' has been colored before.
            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                
                # Optimization: If the ball is being colored with its current color,
                # no change in distinct colors or frequencies is needed.
                if prev_color == color:
                    result.append(len(color_freq))
                    continue # Move to the next query
                
                # If the color is changing, decrement the count for the previous color.
                color_freq[prev_color] -= 1
                
                # If the count of the previous color drops to 0, it means no balls
                # are currently colored with 'prev_color'. Thus, it's no longer a distinct color.
                # Remove it from color_freq to accurately reflect the distinct count.
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]
            
            # Step 2: Update the ball's current color to the new color.
            ball_to_color[ball] = color
            
            # Step 3: Increment the frequency for the new color.
            # .get(color, 0) handles cases where 'color' is new (not in color_freq yet),
            # treating its initial count as 0 before incrementing.
            color_freq[color] = color_freq.get(color, 0) + 1
            
            # Step 4: Record the number of distinct colors after this query.
            # The number of distinct colors is simply the number of unique keys in color_freq,
            # because only colors with a count > 0 are present as keys.
            result.append(len(color_freq))
        
        return result

```

---

### 7. Key Insights and Patterns

1.  **Hash Maps for Sparse Data / Large Ranges**: When dealing with entities (like `ball_id` in this problem) that have a very large possible range (`limit = 10^9`) but only a small subset of them are active or relevant (`N = 10^5` queries), hash maps (dictionaries in Python, `HashMap` in Java, `unordered_map` in C++) are the go-to data structure. They allow efficient `O(1)` average time access for arbitrary keys, avoiding the memory and performance overhead of large arrays.

2.  **Frequency Tracking for Distinct Counts**: When a problem asks for the "number of distinct items" that change over time, maintaining a frequency map (or count map) is a highly effective pattern.
    *   You map `item -> count`.
    *   `len(frequency_map)` directly gives the number of distinct items, provided you correctly handle items whose count drops to zero (by removing them from the map). This makes `len()` an `O(1)` operation in Python.

3.  **Incremental Updates (Delta Calculation)**: Instead of recalculating a value (like "distinct count") from scratch after each operation, it's often far more efficient to calculate the *change* (delta) caused by the current operation and apply it to the previous state.
    *   In this problem, instead of iterating through all colored balls to rebuild a set of colors, we observe that changing one ball's color at most affects two color frequencies (decrement for old, increment for new). This allows `O(1)` updates per query, leading to an overall `O(N)` solution.

4.  **Handling Removal from Distinct Set**: When an item's count drops to zero in a frequency map, it means that item is no longer "present" or "distinct". It's crucial to remove this item from the frequency map to ensure that `len(frequency_map)` accurately reflects only those items that are currently active/distinct. Failing to remove zero-frequency items would lead to incorrect `len()` results and potentially inflate memory usage.

These patterns are fundamental for solving many dynamic counting, tracking, and distinct element problems efficiently.