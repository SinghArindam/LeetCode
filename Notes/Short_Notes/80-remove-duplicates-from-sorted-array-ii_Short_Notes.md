Here are concise short notes for quick revision of LeetCode Problem 80: "Remove Duplicates from Sorted Array II".

---

### **LeetCode 80: Remove Duplicates from Sorted Array II - Quick Revision Notes**

**1. Key Problem Characteristics & Constraints:**
*   **Input:** `nums` - sorted (non-decreasing) integer array.
*   **Goal:** Modify `nums` **in-place** (O(1) extra space) to keep each unique element **at most twice**.
*   **Output:** Return `k` (new length). First `k` elements of `nums` contain the result. Relative order must be preserved.
*   **Constraints:** `1 <= nums.length`, so no empty array.

**2. Core Algorithmic Approach (Two Pointers - Optimal):**
*   **Concept:** Use two pointers, a `slow` (write) pointer and a `fast` (read) pointer.
*   **Initialization:**
    *   Handle base case: If `len(nums) <= 2`, return `len(nums)`.
    *   `slow = 2`: First two elements are always valid, this is where the next *new* valid element will be written.
    *   `fast = 2`: Starts iterating from the third element.
*   **Iteration:**
    *   Loop `while fast < len(nums)`:
        *   **Decision Logic:** `if nums[fast] != nums[slow - 2]:`
            *   This checks if `nums[fast]` is different from the element that is two positions behind the `slow` pointer in the "result" segment.
            *   If true, `nums[fast]` is NOT the third (or more) occurrence of that number; it's a valid element to keep.
            *   If false, `nums[fast]` IS the third (or more) occurrence, so it should be skipped.
        *   **Action (if valid):** `nums[slow] = nums[fast]` then `slow += 1`.
        *   **Advance:** Always `fast += 1`.
*   **Return:** `slow` (which is `k`).

**3. Time/Space Complexity Facts:**
*   **Optimal Two-Pointer:**
    *   **Time:** O(N) - Single pass through the array.
    *   **Space:** O(1) - Constant extra variables (`slow`, `fast`). Strictly in-place.
*   **Python List Comprehension (Alternative - Not strictly O(1) space):**
    *   `nums[:] = [nums[i] for i in range(len(nums)) if (i<2) or (nums[i]!=nums[i-2])]`
    *   **Time:** O(N).
    *   **Space:** O(N) - Creates a temporary new list, then assigns back. *Important distinction for "in-place".*

**4. Critical Edge Cases to Remember:**
*   **Array length 1 or 2:** `[1]`, `[1,1]`, `[1,2]` - All are valid and returned as is (`k=length`). (Handled by base case).
*   **All same elements:** `[1,1,1,1,1]` -> `[1,1]`, `k=2`.
*   **No duplicates:** `[1,2,3,4,5]` -> `[1,2,3,4,5]`, `k=5`.
*   **Every element appears twice:** `[1,1,2,2,3,3]` -> `[1,1,2,2,3,3]`, `k=6`.

**5. Key Patterns / Techniques Used:**
*   **Two-Pointer Technique (Read/Write):** Fundamental for in-place array modifications.
*   **Generalization for "at most K duplicates":** The core condition `if nums[fast] != nums[slow - K]` is a powerful pattern. For this problem, `K=2`.
*   **Leveraging Sorted Input:** Enables efficient comparisons of adjacent/nearby elements to identify duplicates.