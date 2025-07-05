Here are concise short notes for LeetCode problem 88: Merge Sorted Array, suitable for quick revision:

---

### LeetCode 88: Merge Sorted Array - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Merge two *sorted* arrays (`nums1` (m elements) & `nums2` (n elements)) into `nums1`.
*   **In-Place:** Modification must happen directly within `nums1`.
*   **Capacity:** `nums1` has `m+n` length, with `n` trailing zeros as placeholders for `nums2` elements.
*   **Input:** `nums1` (first `m` elements valid, rest `0`s), `m`, `nums2` (all `n` elements valid), `n`.
*   **Constraints:** `0 <= m, n <= 200`, `1 <= m + n <= 200`.

**2. Core Algorithmic Approach (Optimal): Two Pointers from the End**
*   **Insight:** To merge in-place without overwriting `nums1`'s valid elements, fill `nums1` from its *end* (`m+n-1`) backwards.
*   **Pointers:**
    *   `p1 = m - 1`: Points to the last valid element in `nums1`.
    *   `p2 = n - 1`: Points to the last element in `nums2`.
    *   `p = m + n - 1`: Points to the current position in `nums1` to place a merged element.
*   **Main Loop (`while p1 >= 0 and p2 >= 0`):**
    *   Compare `nums1[p1]` and `nums2[p2]`.
    *   Place the *larger* element at `nums1[p]`.
    *   Decrement the pointer of the array from which the element was taken (`p1` or `p2`).
    *   Decrement `p`.
*   **Handle Remaining Elements (`while p2 >= 0`):**
    *   After the main loop, if `nums2` still has elements (`p2 >= 0`), copy them to the remaining available slots at the beginning of `nums1` (from `p` downwards).
    *   If `nums1` has remaining elements (`p1 >= 0`), *no action needed*. They are already in their correct sorted positions relative to each other within the initial part of `nums1`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(m + n)`
    *   Each element is compared and placed exactly once.
*   **Space Complexity:** `O(1)`
    *   All operations are in-place; only a few constant-space pointers are used.

**4. Critical Edge Cases to Remember:**
*   **`m = 0` (empty `nums1` initial part):** `p1` starts at `-1`. The main loop is skipped. Only the `nums2` remaining elements loop runs, correctly copying all of `nums2` into `nums1`.
*   **`n = 0` (empty `nums2`):** `p2` starts at `-1`. Both loops are skipped. `nums1` remains unchanged, which is correct as it's already sorted.
*   **One array runs out significantly earlier:** The remaining elements logic correctly handles scenarios where all `nums1` elements are smaller/larger than all `nums2` elements, or vice-versa.

**5. Key Patterns or Techniques Used:**
*   **Two-Pointer Technique:** Essential for efficient processing of sorted arrays.
*   **Merge from the End:** A powerful pattern for in-place array modifications when destination array has sufficient trailing space. Prevents data overwrites.
*   **Merge Sort's Merge Step:** This problem directly applies the core logic of merging two sorted subarrays, adapted for in-place constraints.