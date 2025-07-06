Here are concise short notes for quick revision of LeetCode problem 26: "Remove Duplicates from Sorted Array":

---

### LeetCode 26: Remove Duplicates from Sorted Array - Quick Notes

**1. Key Problem Characteristics & Constraints:**
*   **Input:** `nums` is an integer array, **sorted in non-decreasing order**.
*   **Goal:** Remove duplicates `in-place` (O(1) auxiliary space preferred).
*   **Output:** Return `k`, the number of unique elements. The first `k` elements of `nums` must contain the unique elements in their `original relative order`. Remaining elements don't matter.
*   **Constraints:** `1 <= nums.length <= 3 * 10^4` (array is never empty).

**2. Core Algorithmic Approach (Optimal):**
*   **Two-Pointer Technique:**
    *   **`slow_pointer (i)`:** (Write pointer) Tracks the position for the next unique element to be placed. Starts at `0`.
    *   **`fast_pointer (j)`:** (Read pointer) Iterates through the array to find new unique elements. Starts at `1`.
    *   **Logic:**
        1.  If `nums[fast_pointer]` is **different** from `nums[slow_pointer]`:
            *   Increment `slow_pointer`.
            *   Copy `nums[fast_pointer]` to `nums[slow_pointer]` (found new unique, shift it left).
        2.  If `nums[fast_pointer]` is **same** as `nums[slow_pointer]`:
            *   Do nothing (it's a duplicate), just let `fast_pointer` continue.
    *   **Return:** `slow_pointer + 1` (since `slow_pointer` is 0-indexed index of last unique element).
*   *(Note: Python's `nums[:] = list_comp` is concise but typically uses O(N) temp space, while the two-pointer is truly O(1) space.)*

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(N)` (Single pass with fast pointer).
*   **Space Complexity:** `O(1)` (for the Two-Pointer approach, only a few variables).

**4. Critical Edge Cases:**
*   **Array with one element (`[X]`):** `slow_pointer` remains `0`, `fast_pointer` loop doesn't run. Correctly returns `1`.
*   **Array with all unique elements (`[1,2,3,4,5]`):** `slow_pointer` increments and copies on every iteration. `nums` becomes `[1,2,3,4,5]`. Correctly returns `N`.
*   **Array with all duplicate elements (`[7,7,7,7]`):** `slow_pointer` remains `0`. `fast_pointer` skips all duplicates. Correctly returns `1`.

**5. Key Patterns or Techniques Used:**
*   **Two-Pointer Technique:** Classic and highly efficient for in-place modifications on sorted arrays (filtering, compacting, merging).
*   **Leveraging Sorted Property:** Crucial for adjacent duplicate checks; simplifies logic significantly.
*   **In-place Modification:** Understanding the difference between O(1) auxiliary space (strict "in-place") and re-assigning/slicing in languages like Python (which might use temporary O(N) space).
*   **Filtering/Compacting Arrays:** A common interview problem type.