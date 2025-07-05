Here are concise short notes for quick revision of LeetCode problem 27 "Remove Element":

---

### **LeetCode 27: Remove Element - Quick Revision Notes**

#### 1. Key Problem Characteristics & Constraints

*   **Goal:** Remove all occurrences of `val` from `nums` **in-place**.
*   **Output:** Return `k`, the count of elements in `nums` **not** equal to `val`.
*   **Array State:**
    *   The first `k` elements of `nums` must contain the elements not equal to `val`.
    *   The **order** of these `k` elements **can be changed**.
    *   Elements beyond the first `k` positions **do not matter**.
*   **Constraints:**
    *   `0 <= nums.length <= 100` (Small array size, but logic applies to larger).
    *   `0 <= nums[i], val <= 100`.

#### 2. Core Algorithmic Approach

*   **Two-Pointer (Read/Write) Method (Optimal & Recommended):**
    *   **Pointers:**
        *   `k` (or `write_idx`, `slow_runner`): Points to the next position where a non-`val` element should be placed. Also counts valid elements. Starts at `0`.
        *   `j` (or `read_idx`, `fast_runner`): Iterates through *all* elements of the array. Starts at `0`.
    *   **Steps:**
        1.  Initialize `k = 0`.
        2.  Iterate `j` from `0` to `len(nums) - 1`.
        3.  **Inside Loop:**
            *   **If `nums[j] != val`:** (Found a valid element)
                *   `nums[k] = nums[j]` (Move valid element to the front).
                *   `k += 1` (Advance write pointer, increment count).
            *   **If `nums[j] == val`:** (Found an element to "remove")
                *   Do nothing. `k` does not advance, effectively skipping this element.
        4.  Return `k`.

*   *(Alternative: Two Pointers - Swap/Shrinking Window)*: Also optimal in complexity, but Read/Write is often simpler and involves fewer writes.

#### 3. Important Time/Space Complexity Facts

*   **Time Complexity: O(N)**
    *   Single pass: The `j` pointer visits each element exactly once.
*   **Space Complexity: O(1)**
    *   In-place modification: Only a few constant variables (`k`, `j`) are used. No auxiliary data structures.

#### 4. Critical Edge Cases to Remember

*   **Empty Array:** `nums = []`, `val = X`. (Returns `0`. Correctly handled as `k` remains `0` and loop doesn't run).
*   **Array with all `val` elements:** `nums = [2,2,2], val = 2`. (Returns `0`. `k` never increments).
*   **Array with no `val` elements:** `nums = [1,2,3], val = 4`. (Returns `len(nums)`. `k` increments every time).
*   **Single Element Array:** `nums = [5], val = 5` (returns 0) or `nums = [5], val = 3` (returns 1). (Handled).
*   **`val` at beginning, middle, or end:** The two-pointer logic inherently handles these positions correctly.

#### 5. Key Patterns or Techniques Used

*   **Two-Pointer Technique (specifically Read/Write or Slow/Fast):**
    *   Fundamental for in-place array manipulation, filtering, and compression.
    *   One pointer (`j`) reads all elements, while the other (`k`) writes only desired elements.
*   **In-Place Modification:** Crucial constraint, dictating that no significant auxiliary space can be used. Solved by overwriting elements within the original array.
*   **Leveraging Problem Statement:** The allowances for order change and "don't care" about elements beyond `k` simplify the solution greatly, avoiding complex shifts or actual deletions.
*   **Similar Problems:** This pattern is highly reusable for problems like:
    *   **Remove Duplicates from Sorted Array (LC 26)**
    *   **Move Zeroes (LC 283)**
    *   Various array partitioning problems.