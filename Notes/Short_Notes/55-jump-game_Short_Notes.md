## LeetCode 55: Jump Game - Quick Revision Notes

---

### 1. Key Problem Characteristics & Constraints

*   **Goal:** Determine if it's possible to reach the **last index** starting from `index 0`.
*   **Jump Rule:** `nums[i]` is the *maximum* jump length from `index i`.
*   **Input:** `nums` (integer array).
*   **Constraints:**
    *   `1 <= nums.length <= 10^4`
    *   `0 <= nums[i] <= 10^5`

---

### 2. Core Algorithmic Approach (Greedy - Optimal)

*   **Idea:** Keep track of the `farthest_reach` possible from `index 0` up to the current position `i`.
*   **Logic:**
    1.  Initialize `farthest_reach = 0`.
    2.  Iterate `i` from `0` to `n-1` (array length `n`).
    3.  **Critical Check:** If `i > farthest_reach`, it means `i` is unreachable. IMPOSSIBLE to reach the end. Return `False`.
    4.  **Update `farthest_reach`:** `farthest_reach = max(farthest_reach, i + nums[i])`. This extends the maximum reachable boundary.
    5.  **Early Exit:** If `farthest_reach >= n - 1` (last index), we've reached or surpassed the end. Return `True`.
    6.  If the loop completes without returning `False` (meaning no unreachable gaps were encountered), it implies the last index was reachable. Return `True`.

---

### 3. Time/Space Complexity

*   **Greedy Approach:**
    *   **Time Complexity:** O(N) - Single pass through the array.
    *   **Space Complexity:** O(1) - Uses a few constant extra variables.
*   *For comparison:*
    *   DP (Top-Down/Bottom-Up): O(N^2) time, O(N) space.
    *   Brute Force (Recursion): O(2^N) time, O(N) space.

---

### 4. Critical Edge Cases

*   **`nums.length == 1` (e.g., `[0]`, `[5]`):** Returns `True`. (Handled by `farthest_reach >= n - 1` where `n-1` is `0`).
*   **Zero Jumps trapping:** `[3,2,1,0,4]` (stuck at index 3). Returns `False`. (Handled by `if i > farthest_reach: return False`).
*   **Reaching exactly the last index:** `[2,3,1,1,0]`. Returns `True`. (Handled by early exit `farthest_reach >= n - 1`).

---

### 5. Key Patterns & Techniques

*   **Greedy Algorithm:** Making the locally optimal choice (maximizing current reach) leads to a globally optimal solution.
*   **"Maximum Reach" / "Farthest Point" Tracking:** A common pattern for problems involving covering a range or reaching a target.
*   **Early Exit Conditions:** Crucial for efficiency; return `True` as soon as the goal is guaranteed, or `False` if failure is confirmed.