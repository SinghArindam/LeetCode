Here are concise short notes for quick revision of LeetCode Problem 3429: "Special Array I".

---

### LeetCode 3429: Special Array I - Quick Revision Notes

**1. Problem Characteristics & Constraints:**
*   **Definition:** An array `nums` is "special" if *every* adjacent pair `(nums[i], nums[i+1])` has different parity (one even, one odd).
*   **Input:** `nums` (array of integers).
*   **Output:** `true` if special, `false` otherwise.
*   **Constraints:**
    *   `1 <= nums.length <= 100` (Small array size)
    *   `1 <= nums[i] <= 100` (Small integer values)

**2. Core Algorithmic Approach:**
*   **Strategy:** Direct iteration and check.
*   **Steps:**
    1.  Iterate through the array starting from the second element (index 1).
    2.  For each element `nums[i]`, compare its parity with `nums[i-1]`.
    3.  **Parity Check:** Use modulo `2` (`x % 2`). Different parities mean `nums[i] % 2 != nums[i-1] % 2`.
    4.  If parities are *the same* for any adjacent pair, immediately return `false` (array is not special).
    5.  If the loop completes without finding any such pair, return `true`.

**3. Time/Space Complexity:**
*   **Time Complexity:** `O(N)`
    *   Single pass through the array (at most N-1 comparisons).
    *   Each comparison is constant time.
*   **Space Complexity:** `O(1)`
    *   Uses a constant amount of extra memory (variables for loop index, parities).

**4. Critical Edge Cases:**
*   **`nums.length == 1`:** An array with one element has no adjacent pairs, so it *always* satisfies the condition. Should return `true`.
    *   (Python's `all()` on an empty iterable correctly returns `True`).
*   **`nums.length == 2`:** Checks just one pair `(nums[0], nums[1])`.
*   **First pair violates:** If `nums[0]` and `nums[1]` have the same parity, the function should immediately return `false` (short-circuit).

**5. Key Patterns / Techniques Used:**
*   **Iterating Adjacent Elements:** Common pattern `for i in range(1, len(arr)): compare arr[i] with arr[i-1]`.
*   **Parity Check:** Standard use of modulo operator `x % 2`.
*   **Short-circuiting Logic:** Returning `false` immediately upon violation is crucial for efficiency and correctness.
    *   Pythonic way: `all(condition for item in iterable)` - this short-circuits on the first `False`.
    *   Traditional way: `for ... if condition: return False; return True` after loop.
*   **Direct Problem Translation:** Simple problems often map directly to iterative checks of conditions.