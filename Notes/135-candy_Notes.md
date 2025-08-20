The problem asks us to distribute candies to `n` children standing in a line, each with a given `rating`. The distribution must adhere to two rules:
1.  Each child must receive at least one candy.
2.  Children with a higher rating must receive more candies than their immediate neighbors.

We need to find the minimum total number of candies required to satisfy these conditions.

**Constraints:**
*   `n` (number of children) is `ratings.length`.
*   `1 <= n <= 2 * 10^4`
*   `0 <= ratings[i] <= 2 * 10^4`

---

## 1. Problem Summary

We are given an array `ratings` representing the rating of `n` children. Our goal is to assign a minimum number of candies to each child such that:
*   Every child gets at least 1 candy.
*   If a child has a higher rating than an adjacent child, they must receive strictly more candies than that neighbor.

We need to return the total sum of candies distributed. This is a classic dynamic programming problem where the decision for one child's candy count depends on its neighbors, and we seek a global minimum.

---

## 2. Explanation of All Possible Approaches

This problem can be approached in several ways, ranging from intuitive greedy passes to more complex DP or graph-based solutions.

### Naive Approach (Conceptual)

A truly "naive" approach would involve trying all possible candy distributions and checking if they satisfy the conditions, then picking the minimum sum. This would be computationally infeasible due to the exponential search space. For example, if each child can get `1` to `N` candies, the combinations are vast.

Instead, when discussing "approaches," we typically refer to algorithmic strategies that attempt to solve the problem efficiently, often starting from simpler valid solutions to more optimized ones.

### Approach 1: Two-Pass Iterative Dynamic Programming (One Array)

This is a very common and efficient solution. It leverages the fact that a child's candy count depends on both left and right neighbors.

**Logic:**
1.  **Initialization:** Create a `candies` array of size `n`, and initialize all elements to `1`. This satisfies the first condition (at least one candy) for all children.
2.  **First Pass (Left to Right):** Iterate from the second child (`i = 1`) to the last child.
    *   If `ratings[i] > ratings[i-1]`, it means the current child has a higher rating than its left neighbor. To satisfy the condition, `candies[i]` *must* be `candies[i-1] + 1`. We update `candies[i]` accordingly.
    *   If `ratings[i] <= ratings[i-1]`, we don't do anything in this pass. The current child already has 1 candy, and potentially more (if its right neighbor has a higher rating, which we'll handle in the next pass). The crucial part is that `candies[i-1]` already satisfies its left condition, and `candies[i]` is currently `1` or higher. We are only concerned with the *increasing* relationship from left to right.
    *   After this pass, `candies[i]` will correctly reflect the minimum candies needed to satisfy the `ratings[i] > ratings[i-1]` condition (if applicable) and `candies[i] >= 1`.
3.  **Second Pass (Right to Left):** Iterate from the second-to-last child (`i = n-2`) down to the first child (`i = 0`).
    *   If `ratings[i] > ratings[i+1]`, it means the current child has a higher rating than its right neighbor. To satisfy this condition, `candies[i]` *must* be at least `candies[i+1] + 1`.
    *   However, `candies[i]` might already have been increased in the first pass (e.g., if `ratings[i]` was greater than `ratings[i-1]`). We need to take the *maximum* of its current value and `candies[i+1] + 1` to ensure both left and right neighbor conditions are met. `candies[i] = max(candies[i], candies[i+1] + 1)`.
    *   If `ratings[i] <= ratings[i+1]`, we don't update `candies[i]` in this pass, as the condition from the right is already satisfied or doesn't apply for increasing from the right perspective.
4.  **Final Sum:** Sum up all the values in the `candies` array.

**Example Trace:** `ratings = [1,0,2]`
*   `n = 3`, `candies = [1, 1, 1]`
*   **L->R Pass:**
    *   `i = 1` (`ratings[1]=0`, `ratings[0]=1`): `0 <= 1`, no change. `candies = [1, 1, 1]`
    *   `i = 2` (`ratings[2]=2`, `ratings[1]=0`): `2 > 0`, `candies[2] = candies[1] + 1 = 1 + 1 = 2`. `candies = [1, 1, 2]`
*   **R->L Pass:**
    *   `i = 1` (`ratings[1]=0`, `ratings[2]=2`): `0 <= 2`, no change. `candies = [1, 1, 2]`
    *   `i = 0` (`ratings[0]=1`, `ratings[1]=0`): `1 > 0`, `candies[0] = max(candies[0], candies[1] + 1) = max(1, 1 + 1) = max(1, 2) = 2`. `candies = [2, 1, 2]`
*   **Total Sum:** `2 + 1 + 2 = 5`. Correct.

**Time Complexity:** O(N)
*   O(N) for initialization.
*   O(N) for the first pass.
*   O(N) for the second pass.
*   O(N) for the final sum.
*   Total: O(N)

**Space Complexity:** O(N)
*   O(N) for the `candies` array.

### Approach 2: Two-Pass Iterative Dynamic Programming (Two Arrays)

This approach is very similar to Approach 1, but uses two separate arrays to store the results of the left-to-right and right-to-left passes, and then combines them.

**Logic:**
1.  **Initialization:**
    *   Create `left_to_right` array of size `n`, initialized to `1`.
    *   Create `right_to_left` array of size `n`, initialized to `1`.
2.  **First Pass (Left to Right):** Populate `left_to_right`.
    *   Iterate from `i = 1` to `n-1`.
    *   If `ratings[i] > ratings[i-1]`, then `left_to_right[i] = left_to_right[i-1] + 1`.
    *   Otherwise, `left_to_right[i]` remains `1`.
    *   This array ensures `candies[i] > candies[i-1]` if `ratings[i] > ratings[i-1]`.
3.  **Second Pass (Right to Left):** Populate `right_to_left`.
    *   Iterate from `i = n-2` down to `0`.
    *   If `ratings[i] > ratings[i+1]`, then `right_to_left[i] = right_to_left[i+1] + 1`.
    *   Otherwise, `right_to_left[i]` remains `1`.
    *   This array ensures `candies[i] > candies[i+1]` if `ratings[i] > ratings[i+1]`.
4.  **Final Sum:** Iterate from `i = 0` to `n-1`. For each child, the minimum candies needed is the maximum of the candies required by its left neighbor relation and its right neighbor relation.
    *   `total_candies += max(left_to_right[i], right_to_left[i])`.

**Example Trace:** `ratings = [1,0,2]`
*   `n = 3`
*   `left_to_right = [1, 1, 1]`
*   `right_to_left = [1, 1, 1]`
*   **L->R Pass (for `left_to_right`):**
    *   `i = 1`: `ratings[1]=0 <= ratings[0]=1`. `left_to_right[1]` remains `1`. `[1,1,1]`
    *   `i = 2`: `ratings[2]=2 > ratings[1]=0`. `left_to_right[2] = left_to_right[1] + 1 = 1 + 1 = 2`. `[1,1,2]`
*   **R->L Pass (for `right_to_left`):**
    *   `i = 1`: `ratings[1]=0 <= ratings[2]=2`. `right_to_left[1]` remains `1`. `[1,1,1]`
    *   `i = 0`: `ratings[0]=1 > ratings[1]=0`. `right_to_left[0] = right_to_left[1] + 1 = 1 + 1 = 2`. `[2,1,1]`
*   **Combine and Sum:**
    *   `i = 0`: `max(left_to_right[0], right_to_left[0]) = max(1, 2) = 2`
    *   `i = 1`: `max(left_to_right[1], right_to_left[1]) = max(1, 1) = 1`
    *   `i = 2`: `max(left_to_right[2], right_to_left[2]) = max(2, 1) = 2`
*   **Total Sum:** `2 + 1 + 2 = 5`. Correct.

**Time Complexity:** O(N)
*   O(N) for initialization (two arrays).
*   O(N) for the first pass.
*   O(N) for the second pass.
*   O(N) for the final sum.
*   Total: O(N)

**Space Complexity:** O(N)
*   O(N) for `left_to_right` array.
*   O(N) for `right_to_left` array.
*   Total: O(N)

**Comparison of Approach 1 vs. 2:** Approach 1 is slightly more space-efficient by merging the two-pass logic into a single `candies` array. Both are O(N) time and O(N) space and are generally considered optimal iterative DP solutions.

### Approach 3: Single-Pass Iterative Dynamic Programming (Slope Tracking)

This approach aims for O(1) extra space by tracking the lengths of increasing and decreasing slopes. It's more complex to reason about correctly.

**Logic:**
The idea is to iterate through the ratings and identify slopes (increasing, decreasing, or flat).
*   Initialize `total_candies = 1` (for the first child).
*   `up_slope_len`: length of current increasing sequence.
*   `down_slope_len`: length of current decreasing sequence.
*   `peak_len`: length of the most recent increasing sequence *before* a potential decreasing sequence started. This helps adjust candies for the peak of an A-shape (e.g., `[1,2,3,2,1]`) or when a down slope becomes longer than the preceding up slope (e.g., `[3,2,1,2]` or `[4,3,2,1]`).

The rules for updating `total_candies` and slope lengths:
1.  **`ratings[i] > ratings[i-1]` (Increasing Slope):**
    *   `up_slope_len` increments.
    *   `down_slope_len` resets to 0 (new increasing slope starts).
    *   `peak_len` becomes the current `up_slope_len` (this is the peak length if a decreasing slope were to follow).
    *   `total_candies += 1 + up_slope_len`. (e.g., if up_slope_len=0, add 1 for current child; if up_slope_len=1, add 2 for current child, meaning it gets 1 more than its left neighbor, which got 1 more than its left, etc.)
2.  **`ratings[i] == ratings[i-1]` (Flat):**
    *   All slope lengths (`up_slope_len`, `down_slope_len`, `peak_len`) reset to 0. This is because a flat segment acts as a reset point; children with equal ratings only need 1 candy, and it breaks any 'greater than' chain.
    *   `total_candies += 1`.
3.  **`ratings[i] < ratings[i-1]` (Decreasing Slope):**
    *   `up_slope_len` resets to 0 (new decreasing slope starts).
    *   `down_slope_len` increments.
    *   `total_candies += down_slope_len`. This adds candies `1, 2, 3...` for the decreasing sequence.
    *   **Crucial Adjustment for Peaks:** If `peak_len < down_slope_len`, it means the current decreasing slope is "deeper" (longer) than the preceding increasing slope. In such a scenario, the child at the peak of the preceding increasing slope might not have received enough candies to satisfy the condition from *its* right side (which is the beginning of the current decreasing slope). We need to increment `total_candies` by 1 to effectively give one extra candy to the peak child to satisfy the deeper right slope.

This approach is notoriously tricky to implement correctly and prove its correctness. While it achieves O(1) extra space, the logic is less intuitive than the two-pass DP.

**Time Complexity:** O(N)
*   One pass through the `ratings` array.

**Space Complexity:** O(1)
*   A few constant variables to track slope lengths.

### Approach 4: BFS (Breadth-First Search) / Queue based (Starting from Local Minima)

This approach views the problem as a graph traversal where candies are propagated from "valleys" (local minima) outwards.

**Logic:**
1.  **Initialization:** Create a `candies` array of size `n`, initialized to `0`. (Could be 1, then update to 0 if needed. 0 helps track unassigned).
2.  **Identify Local Minima:** Iterate through all children. A child `i` is a local minimum if its rating is less than or equal to both its left and right neighbors (or if it's an end child, less than or equal to its single neighbor).
    *   If `i` is a local minimum, set `candies[i] = 1` and add `i` to a queue.
3.  **BFS Traversal:** While the queue is not empty:
    *   Dequeue a `kid_index`.
    *   **Check Left Neighbor:** If `kid_index > 0` (has a left neighbor):
        *   `neighbor_index = kid_index - 1`.
        *   If `ratings[neighbor_index] > ratings[kid_index]` (neighbor has higher rating) AND `candies[neighbor_index] < candies[kid_index] + 1` (neighbor currently has fewer candies than required by `kid_index`):
            *   Update `candies[neighbor_index] = candies[kid_index] + 1`.
            *   Enqueue `neighbor_index`.
    *   **Check Right Neighbor:** If `kid_index < n - 1` (has a right neighbor):
        *   `neighbor_index = kid_index + 1`.
        *   If `ratings[neighbor_index] > ratings[kid_index]` (neighbor has higher rating) AND `candies[neighbor_index] < candies[kid_index] + 1`:
            *   Update `candies[neighbor_index] = candies[kid_index] + 1`.
            *   Enqueue `neighbor_index`.
4.  **Final Sum:** Sum up all values in the `candies` array.

**Time Complexity:** O(N)
*   O(N) to identify local minima and populate the initial queue.
*   In the BFS, each child's candy count is updated and added to the queue at most once. Each check is O(1).
*   Total: O(N)

**Space Complexity:** O(N)
*   O(N) for `candies` array.
*   O(N) for the queue in the worst case (e.g., all children are local minima initially, or a long sequence of increasing ratings).

### Approach 5: Sorting by Rating

This approach processes children in increasing order of their ratings. This ensures that when we consider a child, any neighbor with a *lower* rating has already been processed and its candy count finalized (or at least set to its minimum).

**Logic:**
1.  **Initialization:** Create a `candies` array of size `n`, initialized to `1`.
2.  **Sort Children:** Create a list of tuples `(rating, index)` for all children and sort this list by `rating` in ascending order.
3.  **Iterate through Sorted Children:** For each `(rating, index)` pair from the sorted list:
    *   Let `i` be the `index`.
    *   **Check Left Neighbor:** If `i > 0` and `ratings[i] > ratings[i-1]`:
        *   `candies[i] = max(candies[i], candies[i-1] + 1)`. The `max` is crucial because a higher-rated neighbor might have already caused `candies[i]` to increase.
    *   **Check Right Neighbor:** If `i < n - 1` and `ratings[i] > ratings[i+1]`:
        *   `candies[i] = max(candies[i], candies[i+1] + 1)`.
    *   The property of sorting ensures that when `ratings[i] > ratings[i-1]`, `ratings[i-1]` must be less than or equal to `ratings[i]`. If `ratings[i-1]` is strictly less, it was processed *before or at the same time* as `ratings[i]`, so `candies[i-1]` already reflects its minimum requirement from its left side. When `ratings[i]` is greater, `candies[i]` is updated to ensure `candies[i] > candies[i-1]`. A similar logic applies for the right neighbor.
4.  **Final Sum:** Sum up all values in the `candies` array.

**Time Complexity:** O(N log N)
*   O(N) for initialization.
*   O(N log N) for sorting the children.
*   O(N) for iterating through sorted children and updating.
*   O(N) for final sum.
*   Total: O(N log N)

**Space Complexity:** O(N)
*   O(N) for `candies` array.
*   O(N) for the sorted list of `(rating, index)` pairs.

### Approach 6: Recursive Dynamic Programming with Memoization

This is the approach provided as the active solution in the code. It explicitly defines two recursive functions, one for satisfying the left condition and one for the right, and then combines their results.

**Logic:**
1.  **Memoization Dictionaries:** `memo_left = {}` and `memo_right = {}` to store computed results for `get_left_candies` and `get_right_candies` respectively.
2.  **`get_left_candies(i)` function:**
    *   Base Case: If `i` is 0 (first child) or `ratings[i] <= ratings[i-1]` (current child's rating is not greater than its left neighbor), it only needs 1 candy from its left perspective.
    *   Recursive Case: If `ratings[i] > ratings[i-1]`, it needs `1 + get_left_candies(i-1)`.
    *   Memoize and return the result.
3.  **`get_right_candies(i)` function:**
    *   Base Case: If `i` is `n-1` (last child) or `ratings[i] <= ratings[i+1]` (current child's rating is not greater than its right neighbor), it only needs 1 candy from its right perspective.
    *   Recursive Case: If `ratings[i] > ratings[i+1]`, it needs `1 + get_right_candies(i+1)`.
    *   Memoize and return the result.
4.  **Calculate Total Candies:** Iterate from `i = 0` to `n-1`. For each child `i`, its required candies are `max(get_left_candies(i), get_right_candies(i))`. Sum these maximums.

**Python Specifics:**
*   `sys.setrecursionlimit` is necessary for large `N` (up to 2 * 10^4) to prevent Python's default recursion limit from being exceeded, as a strictly increasing/decreasing sequence would lead to a deep recursion stack.

**Example Trace:** `ratings = [1,0,2]`
*   `num_kids = 3`
*   `total_candies = 0`
*   **For i = 0 (rating 1):**
    *   `get_left_candies(0)`: `i=0`, returns 1.
    *   `get_right_candies(0)`: `ratings[0]=1 > ratings[1]=0`. Calls `1 + get_right_candies(1)`.
        *   `get_right_candies(1)`: `ratings[1]=0 <= ratings[2]=2`. Returns 1.
        *   So, `get_right_candies(0)` returns `1 + 1 = 2`.
    *   `total_candies += max(1, 2) = 2`. `total_candies = 2`.
*   **For i = 1 (rating 0):**
    *   `get_left_candies(1)`: `ratings[1]=0 <= ratings[0]=1`. Returns 1.
    *   `get_right_candies(1)`: `ratings[1]=0 <= ratings[2]=2`. Returns 1.
    *   `total_candies += max(1, 1) = 1`. `total_candies = 2 + 1 = 3`.
*   **For i = 2 (rating 2):**
    *   `get_left_candies(2)`: `ratings[2]=2 > ratings[1]=0`. Calls `1 + get_left_candies(1)`.
        *   `get_left_candies(1)`: `ratings[1]=0 <= ratings[0]=1`. Returns 1.
        *   So, `get_left_candies(2)` returns `1 + 1 = 2`.
    *   `get_right_candies(2)`: `i=2 == num_kids-1`. Returns 1.
    *   `total_candies += max(2, 1) = 2`. `total_candies = 3 + 2 = 5`.
*   **Return 5**. Correct.

**Time Complexity:** O(N)
*   Each `get_left_candies(i)` and `get_right_candies(i)` is computed at most once due to memoization.
*   There are `N` states for `get_left_candies` and `N` states for `get_right_candies`.
*   Each computation (after memoization lookup) is O(1).
*   The final loop iterates N times.
*   Total: O(N)

**Space Complexity:** O(N)
*   O(N) for `memo_left` dictionary.
*   O(N) for `memo_right` dictionary.
*   O(N) for recursion stack depth in the worst case (e.g., strictly increasing/decreasing ratings).
*   Total: O(N)

---

## 3. Detailed Explanation of Logic and Alternative Approaches

The provided solution code includes multiple approaches, each with its own advantages and disadvantages.

**Logic behind the provided active solution (Approach 6 - Recursive DP with Memoization):**

The core idea is that a child's candy count `C_i` must satisfy:
*   `C_i >= 1`
*   If `R_i > R_{i-1}`, then `C_i > C_{i-1}` (equivalently, `C_i >= C_{i-1} + 1`)
*   If `R_i > R_{i+1}`, then `C_i > C_{i+1}` (equivalently, `C_i >= C_{i+1} + 1`)

To find the minimum `C_i`, it must be `max(required_from_left, required_from_right, 1)`. Since `required_from_left` and `required_from_right` already account for the `+1` increment from their respective sides and the base of 1, simply taking the `max` between `get_left_candies(i)` and `get_right_candies(i)` gives the minimum total needed for child `i`.

*   `get_left_candies(i)` computes the minimum candies `child i` needs *if we only consider its left neighbor*. If `ratings[i]` is greater than `ratings[i-1]`, then `child i` must have at least `get_left_candies(i-1) + 1` candies. Otherwise (if `ratings[i] <= ratings[i-1]` or it's the first child), it only needs `1` from the left perspective.
*   `get_right_candies(i)` computes the minimum candies `child i` needs *if we only consider its right neighbor*. If `ratings[i]` is greater than `ratings[i+1]`, then `child i` must have at least `get_right_candies(i+1) + 1` candies. Otherwise (if `ratings[i] <= ratings[i+1]` or it's the last child), it only needs `1` from the right perspective.

By taking `max(get_left_candies(i), get_right_candies(i))`, we ensure that `child i` satisfies *both* its left and right neighbor conditions simultaneously with the minimum possible candies. For example, if `ratings = [1, 2, 1]`:
*   Child 0 (rating 1): `get_left_candies(0)=1`, `get_right_candies(0)` considers `ratings[0] > ratings[1]` (false, `1 <= 2`). So `get_right_candies(0)=1`. Max is 1.
*   Child 1 (rating 2): `get_left_candies(1)` considers `ratings[1] > ratings[0]` (`2 > 1`). So `1 + get_left_candies(0) = 1 + 1 = 2`. `get_right_candies(1)` considers `ratings[1] > ratings[2]` (`2 > 1`). So `1 + get_right_candies(2) = 1 + 1 = 2`. Max is 2.
*   Child 2 (rating 1): `get_left_candies(2)` considers `ratings[2] > ratings[1]` (false, `1 <= 2`). So `get_left_candies(2)=1`. `get_right_candies(2)=1`. Max is 1.
Total: `1 + 2 + 1 = 4`. This is correct for `[1,2,2] -> [1,2,1]` from example, which is essentially `[1,2,1]` in terms of logic.

**Alternative Approaches (from the provided code):**

*   **Approach 1 & 2 (Two-Pass Iterative DP):** These are the most commonly cited and often preferred solutions for their simplicity and iterative nature. They achieve the same optimal time and space complexity as the recursive DP (O(N) time, O(N) space) but without the overhead of recursion stack or the need to adjust recursion limits. Approach 1 is slightly more space-efficient (one array vs. two). For competitive programming, these are often easier to implement quickly and debug.
*   **Approach 3 (Single-Pass Slope Tracking):** This approach aims for O(1) space, which is a significant optimization if memory is extremely tight and `N` is very large. However, its logic is quite intricate and harder to get right, making it less favorable for general use unless O(N) space is strictly prohibited.
*   **Approach 4 (BFS from Local Minima):** This is a valid and intuitive approach for problems that can be modeled as propagation from a source. It has the same complexity as the two-pass DP (O(N) time, O(N) space). It's a good alternative perspective, especially if you're comfortable with graph algorithms.
*   **Approach 5 (Sorting by Rating):** This is a correct approach, but its time complexity is O(N log N) due to the sorting step, making it less optimal than the O(N) DP solutions for large `N`. It might be simpler to reason about for some, as it processes independent children first.

**Why one might choose one over another:**

*   **Approach 1/2 (Two-Pass Iterative DP):** Generally the **recommended optimal iterative solution**. Simple, easy to understand, efficient (O(N) time, O(N) space).
*   **Approach 6 (Recursive DP with Memoization):** Conceptually elegant, directly maps to the recursive definition of the problem. Also O(N) time and O(N) space. Might have slightly higher constant factors due to function call overhead and dictionary lookups, and requires `sys.setrecursionlimit` for large inputs.
*   **Approach 3 (Single-Pass O(1) space):** Optimal space complexity. Choose if `N` is extremely large and memory is a critical constraint. Sacrifice readability and simplicity.
*   **Approach 4 (BFS):** Good alternative perspective, same complexity as two-pass DP. Choose if BFS naturally comes to mind.
*   **Approach 5 (Sorting):** Simpler for some to reason about, but not time-optimal due to sorting. Only choose if `N` is small enough that O(N log N) is acceptable or if the sorting insight makes the logic much clearer for you.

---

## 4. Time and Space Complexity Analysis

Let `N` be the number of children (`ratings.length`).

*   **Approach 1: Two-Pass Iterative DP (One Array)**
    *   **Time Complexity:** O(N)
        *   Initialization: O(N) to create and fill `candies` array.
        *   First pass (L->R): O(N) loop.
        *   Second pass (R->L): O(N) loop.
        *   Summation: O(N) loop.
        *   Total: O(N)
    *   **Space Complexity:** O(N)
        *   `candies` array: O(N).

*   **Approach 2: Two-Pass Iterative DP (Two Arrays)**
    *   **Time Complexity:** O(N)
        *   Initialization: O(N) to create and fill two arrays.
        *   First pass (L->R): O(N) loop.
        *   Second pass (R->L): O(N) loop.
        *   Summation: O(N) loop.
        *   Total: O(N)
    *   **Space Complexity:** O(N)
        *   `left_to_right` array: O(N).
        *   `right_to_left` array: O(N).
        *   Total: O(N)

*   **Approach 3: Single-Pass Iterative DP (Slope Tracking)**
    *   **Time Complexity:** O(N)
        *   Single pass loop: O(N).
    *   **Space Complexity:** O(1)
        *   A few constant variables for tracking slopes.

*   **Approach 4: BFS / Queue-based**
    *   **Time Complexity:** O(N)
        *   Initialization and initial queue population: O(N).
        *   BFS traversal: Each child is added to the queue and processed at most once. Each processing step (checking neighbors, updating candy, enqueuing) takes constant time. Total for BFS part is O(N).
        *   Summation: O(N).
        *   Total: O(N)
    *   **Space Complexity:** O(N)
        *   `candies` array: O(N).
        *   Queue: In the worst case (e.g., `[1,2,3,4,5]` or `[5,4,3,2,1]`), the queue can hold up to O(N) elements.

*   **Approach 5: Sorting by Rating**
    *   **Time Complexity:** O(N log N)
        *   Initialization: O(N).
        *   Sorting: O(N log N) (e.g., Python's `sorted` uses Timsort).
        *   Iteration through sorted children: O(N).
        *   Summation: O(N).
        *   Total: O(N log N)
    *   **Space Complexity:** O(N)
        *   `candies` array: O(N).
        *   Storing sorted `(rating, index)` pairs: O(N).

*   **Approach 6: Recursive DP with Memoization (Active Solution)**
    *   **Time Complexity:** O(N)
        *   Each of the `2N` states (`get_left_candies(i)` and `get_right_candies(i)`) is computed exactly once due to memoization. Each computation takes O(1) (after the first call, subsequent calls hit the memo).
        *   Final loop for summation: O(N).
        *   Total: O(N).
    *   **Space Complexity:** O(N)
        *   `memo_left` dictionary: O(N) to store `N` results.
        *   `memo_right` dictionary: O(N) to store `N` results.
        *   Recursion stack: In the worst case (e.g., strictly increasing/decreasing ratings), the recursion depth can be O(N).
        *   Total: O(N).

**Summary of Optimal Approaches:**
All approaches except Sorting by Rating (Approach 5) achieve O(N) time complexity. Approach 3 is optimal in space (O(1)), while others are O(N) space. The two-pass iterative DP solutions (Approach 1 & 2) and the recursive DP with memoization (Approach 6) are generally considered the main optimal solutions for their balance of efficiency and clarity.

---

## 5. Edge Cases and How They Are Handled

Let's examine how the optimal O(N) time solutions (specifically Approach 1 and Approach 6) handle various edge cases.

1.  **`n = 1` (Single Child):**
    *   **Problem Requirement:** Each child must have at least one candy.
    *   **Approach 1:** `candies = [1]`. First pass loop (`range(1, 1)`) does not run. Second pass loop (`range(-1, -1, -1)`) does not run. `sum(candies)` returns 1. **Correct.**
    *   **Approach 6:** `num_kids = 1`.
        *   `get_left_candies(0)`: `i=0`, returns 1.
        *   `get_right_candies(0)`: `i=0 == num_kids-1`, returns 1.
        *   `total_candies += max(1, 1) = 1`. **Correct.**

2.  **All Children have the Same Rating (e.g., `ratings = [2,2,2]`):**
    *   **Problem Requirement:** Each child gets 1. Total = `N`. (Condition 2: "higher rating gets more candies" is not applicable as no one has higher rating than neighbor).
    *   **Approach 1:** `candies = [1,1,1]`.
        *   L->R pass: `ratings[i] > ratings[i-1]` is never true. `candies` remains `[1,1,1]`.
        *   R->L pass: `ratings[i] > ratings[i+1]` is never true. `candies` remains `[1,1,1]`.
        *   Sum: 3. **Correct.**
    *   **Approach 6:**
        *   `get_left_candies(i)`: `ratings[i] <= ratings[i-1]` is always true (for `i>0`). Returns 1 for all `i`.
        *   `get_right_candies(i)`: `ratings[i] <= ratings[i+1]` is always true (for `i<num_kids-1`). Returns 1 for all `i`.
        *   `max(1, 1)` for each child, sum is `N`. **Correct.**

3.  **Strictly Increasing Ratings (e.g., `ratings = [1,2,3,4,5]`):**
    *   **Expected Candies:** `[1,2,3,4,5]`. Total = 15.
    *   **Approach 1:** `candies = [1,1,1,1,1]`.
        *   L->R pass: `candies` becomes `[1,2,3,4,5]` (e.g., `candies[1]=candies[0]+1=2`, `candies[2]=candies[1]+1=3`, etc.).
        *   R->L pass: `ratings[i] > ratings[i+1]` is never true. `candies` remains `[1,2,3,4,5]`.
        *   Sum: 15. **Correct.**
    *   **Approach 6:**
        *   `get_left_candies(i)` will compute `i+1` for all `i`. (e.g., `get_left_candies(4)` = `1 + get_left_candies(3)` = ... = `1+1+1+1+get_left_candies(0)` = `1+1+1+1+1 = 5`).
        *   `get_right_candies(i)` will always return 1, as `ratings[i]` is never greater than `ratings[i+1]`.
        *   `max(i+1, 1)` for each child will be `i+1`. Sum is `1+2+3+4+5 = 15`. **Correct.**

4.  **Strictly Decreasing Ratings (e.g., `ratings = [5,4,3,2,1]`):**
    *   **Expected Candies:** `[5,4,3,2,1]`. Total = 15.
    *   **Approach 1:** `candies = [1,1,1,1,1]`.
        *   L->R pass: `ratings[i] > ratings[i-1]` is never true. `candies` remains `[1,1,1,1,1]`.
        *   R->L pass:
            *   `i=3`: `ratings[3]=2 > ratings[4]=1`. `candies[3]=max(1, candies[4]+1) = max(1,1+1)=2`. `candies=[1,1,1,2,1]`
            *   `i=2`: `ratings[2]=3 > ratings[3]=2`. `candies[2]=max(1, candies[3]+1) = max(1,2+1)=3`. `candies=[1,1,3,2,1]`
            *   ...and so on. `candies` becomes `[5,4,3,2,1]`.
        *   Sum: 15. **Correct.**
    *   **Approach 6:**
        *   `get_left_candies(i)` will always return 1, as `ratings[i]` is never greater than `ratings[i-1]`.
        *   `get_right_candies(i)` will compute `num_kids - i` for each `i`. (e.g., `get_right_candies(0)` = `1 + get_right_candies(1)` = ... = `1+1+1+1+get_right_candies(4)` = `1+1+1+1+1 = 5`).
        *   `max(1, num_kids - i)` for each child will be `num_kids - i`. Sum is `5+4+3+2+1 = 15`. **Correct.**

5.  **V-shape (e.g., `ratings = [3,2,1,2,3]`):**
    *   **Expected Candies:** `[3,2,1,2,3]`. Total = 11. (Minimum 1 at `1`, then increases on both sides).
    *   Both Approach 1 and Approach 6 handle this correctly by ensuring the `max` operation accounts for both sides of the "V" and the increasing/decreasing slopes are propagated. The "valley" (rating 1) will get 1, and values will increase outwards.

6.  **A-shape (e.g., `ratings = [1,2,3,2,1]`):**
    *   **Expected Candies:** `[1,2,3,2,1]`. Total = 9. (Peak rating 3 gets 3, then decreases outwards).
    *   Both Approach 1 and Approach 6 handle this correctly as well. The peak will receive the max of candies from its left (3) and its right (3), thus 3. Children on slopes propagate correctly.

All the O(N) time complexity solutions (excluding the O(1) space one, which is tricky) handle these cases robustly because they ensure that both local conditions (`> left neighbor` and `> right neighbor`) are eventually satisfied by taking the maximum of the requirements from both sides.

---

## 6. Clean, Well-Commented Version of the Optimal Solution

The provided active solution is Approach 6 (Recursive DP with Memoization). I will comment that specific version.
For completeness and practical purposes, I'll also provide a well-commented version of Approach 1 (Two-Pass Iterative DP with One Array), which is often considered the most common and robust iterative optimal solution due to its balance of clarity, time, and space efficiency.

### Optimal Solution (Provided Active - Approach 6: Recursive DP with Memoization)

```python
import sys

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Increase the recursion limit for deep recursion, as required by this approach
        # For N up to 2 * 10^4, the recursion depth can be N. Default is usually 1000.
        sys.setrecursionlimit(2 * 10**4 + 5)
        
        num_kids = len(ratings)
        
        # Memoization dictionaries to store results of recursive calls
        # memo_left[i] will store the minimum candies for child i considering only its left neighbor
        memo_left = {}
        # memo_right[i] will store the minimum candies for child i considering only its right neighbor
        memo_right = {}
        
        # Helper function to calculate candies for child 'i' based on its left neighbor
        def get_left_candies(i):
            # If the result for this child is already memoized, return it directly
            if i in memo_left:
                return memo_left[i]
            
            # Base case: If it's the first child (i=0) or its rating is not greater than its left neighbor,
            # it only needs 1 candy from the left perspective.
            if i > 0 and ratings[i] > ratings[i - 1]:
                # Recursive step: If current child's rating is higher than left neighbor,
                # it needs 1 more candy than its left neighbor.
                res = 1 + get_left_candies(i - 1)
            else:
                # Otherwise, it satisfies the left condition with just 1 candy.
                res = 1
            
            # Memoize the result before returning
            memo_left[i] = res
            return res
        
        # Helper function to calculate candies for child 'i' based on its right neighbor
        def get_right_candies(i):
            # If the result for this child is already memoized, return it directly
            if i in memo_right:
                return memo_right[i]
            
            # Base case: If it's the last child (i=num_kids-1) or its rating is not greater than its right neighbor,
            # it only needs 1 candy from the right perspective.
            if i < num_kids - 1 and ratings[i] > ratings[i + 1]:
                # Recursive step: If current child's rating is higher than right neighbor,
                # it needs 1 more candy than its right neighbor.
                res = 1 + get_right_candies(i + 1)
            else:
                # Otherwise, it satisfies the right condition with just 1 candy.
                res = 1
            
            # Memoize the result before returning
            memo_right[i] = res
            return res
        
        total_candies = 0
        # Iterate through all children to calculate their final candy count
        for i in range(num_kids):
            # For each child, the minimum candies required is the maximum of the candies
            # needed to satisfy its left neighbor condition and its right neighbor condition.
            # This ensures both requirements are met.
            total_candies += max(get_left_candies(i), get_right_candies(i))
            
        return total_candies

```

### Alternative Optimal Solution (Approach 1: Two-Pass Iterative DP - One Array)

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_kids = len(ratings)
        
        # If there are no kids, no candies needed.
        if num_kids == 0:
            return 0
        
        # Initialize candies for all children to 1. This satisfies the first condition:
        # "Each child must have at least one candy."
        candies = [1] * num_kids
        
        # First pass: Iterate from left to right.
        # This pass ensures that children with a higher rating than their LEFT neighbor
        # get more candies than that neighbor.
        # Example: [1, 2, 0] -> candies becomes [1, 2, 1] after this pass
        # (child with rating 2 gets 2 candies because 2 > 1)
        for i in range(1, num_kids):
            if ratings[i] > ratings[i - 1]:
                # If current child's rating is higher, give it one more candy than its left neighbor.
                candies[i] = candies[i - 1] + 1
        
        # Second pass: Iterate from right to left.
        # This pass ensures that children with a higher rating than their RIGHT neighbor
        # get more candies than that neighbor.
        # Crucially, we take `max` to ensure the child satisfies *both* left and right conditions.
        # Example: [1, 0, 2] ->
        # After first pass: candies = [1, 1, 2]
        # In this pass, for child 0 (rating 1): ratings[0] > ratings[1] (1 > 0)
        # candies[0] must be > candies[1]. candies[0] = max(candies[0], candies[1] + 1)
        # = max(1, 1 + 1) = 2.
        # Final candies = [2, 1, 2]
        for i in range(num_kids - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # If current child's rating is higher than right neighbor,
                # it needs at least one more candy than its right neighbor.
                # We take the maximum of its current candy count (from L-R pass)
                # and the requirement from the right. This resolves conflicts and
                # ensures the minimum count satisfying both conditions.
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        # The total minimum candies required is the sum of candies in the array.
        return sum(candies)

```

---

## 7. Key Insights and Patterns

1.  **Dependency on Neighbors (Dynamic Programming):** The candy count for a child depends on its immediate neighbors. This local dependency often points towards Dynamic Programming. We can build up solutions for subproblems (individual children) and combine them.
2.  **Two-Pass Approach for Bidirectional Dependencies:** When a problem involves conditions dependent on both "left" and "right" (or "past" and "future" elements in a linear array), a two-pass approach is very common and effective.
    *   One pass propagates information/requirements in one direction (e.g., left-to-right).
    *   The second pass propagates information/requirements in the opposite direction (e.g., right-to-left).
    *   The final result for each element is often the maximum (or minimum, depending on the problem) of the values derived from these two passes, ensuring all conditions are met. This pattern is applicable to many array/list problems where elements have interactions with both previous and subsequent elements.
3.  **Greedy Decisions with Local Optimality Leading to Global Optimality:** In this problem, incrementing candies by 1 based on a higher rating is a greedy local decision. When combined with the two-pass or max-combination strategy, these local greedy decisions accumulate to the global minimum.
4.  **Minimization via `max()`:** When a requirement is "at least X" from one side and "at least Y" from another side, the actual minimum required is `max(X, Y)`. This is a common pattern in DP problems aiming for minimum values subject to multiple constraints.
5.  **Handling Equal Elements:** When `ratings[i] == ratings[i-1]`, it breaks the "greater than neighbor" chain. In such cases, the default `1` candy is usually sufficient, as no `> neighbor` condition applies from that specific side.
6.  **Recursion with Memoization as Iterative DP Equivalent:** Recursive solutions with memoization are often direct translations of iterative DP. They have the same asymptotic time and space complexity but might differ in constant factors and practical considerations (like recursion depth limits). Understanding both iterative and recursive forms provides flexibility.
7.  **Optimizing Space (O(1)):** While typically harder to implement correctly, achieving O(1) space complexity for array problems often involves careful tracking of "slopes" or "states" using a few variables, avoiding the need for auxiliary arrays. This is an advanced optimization.
8.  **BFS for Propagation:** For problems involving satisfying conditions by propagating values from source points (like local minima in this case), BFS can be a suitable approach.

This problem is an excellent example demonstrating different DP paradigms and their trade-offs, particularly the common two-pass iterative DP and its recursive memoized counterpart.