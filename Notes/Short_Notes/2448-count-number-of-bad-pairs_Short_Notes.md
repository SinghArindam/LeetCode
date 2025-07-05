Here's a concise summary for quick revision of LeetCode Problem 2448: Count Number of Bad Pairs.

---

### LeetCode 2448: Count Number of Bad Pairs - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Definition of a Bad Pair (i, j):**
    *   `i < j` (strict order of indices)
    *   `j - i != nums[j] - nums[i]` (index difference is NOT equal to value difference)
*   **Goal:** Return the total count of such bad pairs.
*   **Constraints:**
    *   `nums.length (N)`: `1` to `10^5` (implies O(N) or O(N log N) solution needed, O(N^2) is too slow).
    *   `nums[i]`: `1` to `10^9` (values can be large).

**2. Core Algorithmic Approach (Optimized):**
*   **Key Insight / Transformation:**
    *   It's often easier to count "good pairs" and subtract from total, OR directly count "bad pairs" by understanding the good pair condition.
    *   A pair `(i, j)` is a **good pair** if `i < j` AND `j - i == nums[j] - nums[i]`.
    *   Rearrange the good pair condition: `j - nums[j] == i - nums[i]`.
    *   This means `f(i) == f(j)` where `f(x) = x - nums[x]`.
*   **Strategy (Direct Bad Pair Counting):**
    1.  Initialize `bad_pairs_count = 0`.
    2.  Use a **hash map** (e.g., Python `dict`) `diff_counts` to store frequencies of the calculated `(index - value)` values (`f(x)`).
    3.  Iterate through `nums` with index `i` and value `num`:
        *   Calculate `current_diff = i - num`.
        *   For the current `i`, there are `i` previous indices (`0` to `i-1`). These are the total potential partners for `i` that satisfy `p < i`.
        *   Out of these `i` previous indices, `diff_counts.get(current_diff, 0)` of them form **good pairs** with `i` (because their `p - nums[p]` equals `current_diff`).
        *   The rest `(i - diff_counts.get(current_diff, 0))` form **bad pairs** with `i`. Add this amount to `bad_pairs_count`.
        *   Increment the count for `current_diff` in `diff_counts` (to include the current `i` for future `j > i` calculations).
    4.  Return `bad_pairs_count`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity: O(N)**
    *   Single pass through the array.
    *   Hash map operations (lookup, insert) are O(1) on average.
*   **Space Complexity: O(N)**
    *   In the worst case, all `N` values of `(i - nums[i])` could be unique, requiring the hash map to store up to `N` distinct keys.

**4. Critical Edge Cases:**
*   **`N = 1`:** No `(i, j)` pairs with `i < j` are possible. The algorithm correctly returns `0` as the loop for `i=0` adds `0-0=0` bad pairs.
*   **All Good Pairs:** (e.g., `[1,2,3,4,5]`) where `i - nums[i]` is constant. The `diff_counts.get(current_diff, 0)` will always equal `i`, resulting in `i - i = 0` bad pairs added at each step. Correctly returns `0`.
*   **Large `nums[i]` Values:** `i - nums[i]` can be negative and large (e.g., `0 - 10^9`). Python's integers handle this automatically, and hash maps accommodate these values as keys.

**5. Key Patterns / Techniques Used:**
*   **Condition Reformulation:** Transform complex conditions (`j - i != nums[j] - nums[i]`) into simpler forms (`f(i) == f(j)`). This is crucial for optimizing pair-counting problems.
*   **Hash Map for Frequency/Pair Counting:** The go-to data structure for efficiently tracking occurrences of calculated values (`f(x)`) to find pairs (`f(i) == f(j)`), typically resulting in O(N) solutions.
*   **"Total - Good/Bad" Complement Strategy:** Though the primary solution directly counts bad pairs, the underlying logic uses the concept of subtracting good pairs from a total (total previous elements `i` minus good pairs `diff_counts.get(key,0)`). This is a common pattern for many counting problems.