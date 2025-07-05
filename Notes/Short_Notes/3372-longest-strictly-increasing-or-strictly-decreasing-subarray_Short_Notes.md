Here's a concise summary for quick revision of LeetCode 3372: "Longest Strictly Increasing or Strictly Decreasing Subarray".

---

**LeetCode 3372: Longest Strictly Increasing or Strictly Decreasing Subarray**

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Find length of the longest *contiguous* subarray that is **either** strictly increasing (`a < b < c`) **or** strictly decreasing (`a > b > c`).
*   **"Strictly" means no equality.** `[3,3]` is neither.
*   **Base Case:** A single-element subarray `[x]` has length 1 and is considered both.
*   **Constraints:** `1 <= nums.length <= 50`, `1 <= nums[i] <= 50`. (Small N suggests even O(N^3) might pass, but O(N) is optimal).

**2. Core Algorithmic Approach (Optimal Single Pass):**
*   **Strategy:** Iterate through the array once, maintaining two independent counters for the lengths of the current strictly increasing and strictly decreasing subarrays ending at the current element.
*   **Initialization:** `max_len = 1`, `current_inc_len = 1`, `current_dec_len = 1`. (Because any single element forms a valid subarray of length 1).
*   **Iteration (from `i=1` to `n-1`):**
    *   **For Increasing:** If `nums[i] > nums[i-1]`, increment `current_inc_len`. Else, reset `current_inc_len = 1`.
    *   **For Decreasing:** If `nums[i] < nums[i-1]`, increment `current_dec_len`. Else, reset `current_dec_len = 1`.
    *   **Update Max:** `max_len = max(max_len, current_inc_len, current_dec_len)`.

**3. Time/Space Complexity:**
*   **Time:** `O(N)` - Single pass through the array.
*   **Space:** `O(1)` - Uses a fixed number of variables.

**4. Critical Edge Cases:**
*   **Single Element Array:** `[5]` -> Output: 1. (Handled by initialization and loop skipping).
*   **All Identical Elements:** `[3,3,3,3]` -> Output: 1. (Crucially, `nums[i] == nums[i-1]` causes *both* `current_inc_len` and `current_dec_len` to reset to 1).
*   **Fully Monotonic Arrays:** `[1,2,3]` (increasing) or `[3,2,1]` (decreasing) -> Correctly returns N.
*   **Mixed Monotonicity:** `[1,4,3,3,2]` -> Output: 2. (`[1,4]`, `[4,3]`, `[3,2]` are longest segments).

**5. Key Patterns/Techniques:**
*   **Sliding Window (Implicit):** The `current_len` variables effectively define dynamic windows.
*   **Kadane's Algorithm Adaptation:** Similar to finding max subarray sum, but instead of sum, it tracks lengths of monotonic sequences.
*   **Independent State Tracking:** Maintaining separate counters for distinct properties (increasing/decreasing) in a single pass.
*   **Resetting Counters:** Common strategy for "longest run/streak" problems when the property breaks. Reset value is typically 1 (new element starts a run).