Here's a concise summary of LeetCode Problem 39 (Combination Sum) suitable for quick revision:

---

### LeetCode 39: Combination Sum - Quick Revision Notes

#### 1. Key Problem Characteristics & Constraints:
*   **Goal:** Find all **unique combinations** of `candidates` that sum to `target`.
*   **Key Feature:** Numbers from `candidates` can be chosen an **unlimited number of times**.
*   **Uniqueness:** Combinations are unique based on frequencies (e.g., `[2,2,3]` is the same as `[2,3,2]`). Order *within* a combination does not matter.
*   **Candidates:** Array of **distinct** integers.
*   **Constraints:** `1 <= N <= 30`, `2 <= candidates[i] <= 40`, `1 <= target <= 40`.
*   **Output Size:** Total unique combinations for `target` < 150.

#### 2. Core Algorithmic Approaches:

**A. Backtracking (Recommended Optimal)**
*   **Concept:** Recursive search that builds combinations incrementally.
*   **State:** `(start_index, current_combination, current_sum)`.
*   **Recursive Step:** Iterate `for i in range(start_index, len(candidates))`.
    *   **Unlimited Use:** Pass `i` (current index) to the next recursive call (`backtrack(i, ...)`) to allow reusing `candidates[i]`.
    *   **Uniqueness:** `start_index` ensures numbers are picked in non-decreasing order (e.g., `[2,3]` but not `[3,2]`).
    *   **Pruning:**
        *   `if current_sum == target:` Add `list(current_combination)` to result and `return`.
        *   **Crucial Optimization:** Sort `candidates` array initially. Then, `if current_sum + candidates[i] > target: break` (prunes current branch and all subsequent larger numbers at this level).
    *   **Backtrack:** `current_combination.pop()` after recursive call to explore other paths.

**B. Dynamic Programming (Alternative Optimal)**
*   **Concept:** Builds solutions bottom-up using a DP table.
*   **`dp` Array:** `dp[i]` stores a list of all unique combinations that sum to `i`.
*   **Base Case:** `dp[0] = [[]]` (empty combination for sum 0).
*   **Iteration:**
    1.  Outer loop: `for num in candidates:` (Iterate through each available number).
    2.  Inner loop: `for i in range(num, target + 1):` (Iterate through sums from `num` up to `target`).
    3.  Innermost: `for combo in dp[i - num]: dp[i].append(combo + [num])`.
*   **Uniqueness:** The order of loops (`num` first, then `i`) implicitly handles uniqueness by ensuring numbers are added in a specific (non-decreasing) order.

#### 3. Time & Space Complexity Facts:
*   Let `N = len(candidates)`, `T = target`, `M = T / min(candidates)` (max combo length), `K = total unique combinations (final output)`.
*   **Backtracking (Optimized):**
    *   **Time:** Exponential (related to `N^M`), but highly optimized by sorting and pruning. Efficient in practice for given constraints.
    *   **Space:** `O(M)` for recursion stack depth + `O(K * M)` for storing the result list.
*   **Dynamic Programming:**
    *   **Time:** `O(N * T * K_max_at_intermediate_sum * M)`. `K_max_at_intermediate_sum` refers to the max number of combinations for any sum `i <= target`.
    *   **Space:** `O(T * K_max_at_intermediate_sum * M)` for the `dp` table.

#### 4. Critical Edge Cases to Remember:
*   **`target < min(candidates)` (e.g., `candidates = [5,6], target = 3`):** Both Backtracking and DP approaches correctly return `[]` (empty list), as no combination can be formed.
*   **`candidates` contains only one number:** (e.g., `candidates = [2], target = 7`). Both approaches correctly handle this, returning `[]` if no exact sum, or the valid combination (`[[2,2,2]]` for `target=6`).
*   *(Note: Constraints (`target >= 1`, `candidates.length >= 1`) rule out `target=0` and empty `candidates` list for this specific problem.)*

#### 5. Key Patterns & Techniques Used:
*   **Backtracking Paradigm:** Recursive exploration with "choices" and "undoing choices".
*   **`start_index` Parameter:** Standard technique in backtracking for unique combinations (avoiding permutations).
*   **Sorting Input:** Essential for early pruning optimization (`break` condition) in backtracking and often helpful for uniqueness logic.
*   **Unlimited Item Usage:**
    *   Backtracking: Passing the *current* index (`i`) to the next recursive call.
    *   DP: Outer loop over `candidates`, inner loop over `target` sums starting from `num`.
*   **Pruning:** Critical for efficiency, cutting off invalid branches early.
*   **Dynamic Programming Table Design:** `dp[sum]` stores results for intermediate sums.