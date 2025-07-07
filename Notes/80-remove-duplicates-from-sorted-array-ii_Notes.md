## LeetCode Problem 80: Remove Duplicates from Sorted Array II

### 1. Problem Summary

The problem asks us to modify a given integer array `nums`, which is sorted in **non-decreasing order**, such that each unique element appears **at most twice**. The modification must be done **in-place**, meaning we must use O(1) extra memory. The relative order of the elements must be preserved. We need to return `k`, the new length of the modified array, with the first `k` elements of `nums` containing the final result. Elements beyond the first `k` positions do not matter.

**Constraints:**
*   `1 <= nums.length <= 3 * 10^4`
*   `-10^4 <= nums[i] <= 10^4`
*   `nums` is sorted in non-decreasing order.

### 2. Explanation of Possible Approaches

#### A. Naive Approach (Conceptual, Violates Space Constraint)

*   **Idea:** The most straightforward way to conceptualize duplicate removal might involve using auxiliary data structures.
*   **Steps:**
    1.  Create a new empty list, say `temp_list`.
    2.  Iterate through the `nums` array. For each element, maintain a count of its occurrences.
    3.  If the current element has appeared less than twice (or its count is less than 2), append it to `temp_list`.
    4.  After iterating through all elements, copy the elements from `temp_list` back into `nums`.
*   **Limitations:** This approach fundamentally violates the O(1) extra space constraint because `temp_list` can grow up to the size of the original array (N elements). It is generally not accepted for "in-place" problems with strict space requirements.

#### B. Optimal Approach: Two Pointers (In-place Modification)

*   **Idea:** This is the standard and most efficient way to solve in-place array modification problems, especially with sorted arrays. We use two pointers: a "read" pointer and a "write" pointer. The "read" pointer iterates through the original array, while the "write" pointer determines where the next valid element should be placed in the modified array.
*   **General Strategy for "at most K duplicates":**
    1.  **Initialize Write Pointer:** A pointer, let's call it `slow` (or `write_idx`), is initialized to `K`. This is because the first `K` elements of a sorted array are always considered valid (they can be distinct or `K` duplicates of the first element).
    2.  **Initialize Read Pointer:** Another pointer, `fast` (or `read_idx`), is also initialized to `K`. It will iterate through the array to read elements.
    3.  **Iterate and Conditionally Copy:**
        *   Iterate `fast` from `K` up to `len(nums) - 1`.
        *   At each step, check if the element `nums[fast]` is *different* from the element `K` positions behind the `slow` pointer in the already processed part of the array (i.e., `nums[slow - K]`).
        *   If `nums[fast] != nums[slow - K]` (meaning `nums[fast]` is not the `(K+1)`th consecutive duplicate of `nums[slow-K]`):
            *   Copy `nums[fast]` to `nums[slow]`.
            *   Increment `slow` by 1.
        *   Always increment `fast` by 1 to move to the next element.
    4.  **Return Length:** The final value of `slow` will be the new length `k` of the modified array.

*   **Adaptation for "at most 2 duplicates" (K=2):**
    *   The `slow` pointer starts at `2`.
    *   The `fast` pointer starts at `2`.
    *   The condition to keep `nums[fast]` becomes `if nums[fast] != nums[slow - 2]:`. This check ensures that `nums[fast]` is not the third (or more) occurrence of the same number that `nums[slow - 2]` represents.

### 3. Detailed Explanation of Logic

We will explain two specific implementations: the standard Two-Pointer approach (which strictly adheres to O(1) space) and the provided List Comprehension solution (which might not strictly be O(1) space in Python's underlying execution).

#### A. Optimal Two-Pointer Approach (Strict O(1) Space)

This approach is the most robust and strictly adheres to the space constraints.

*   **Initialization:**
    *   **Base Case:** If the array has `0`, `1`, or `2` elements, all of them are valid by definition (each appears at most twice). The problem constraints state `1 <= nums.length`, so an empty array is not a concern. Thus, if `len(nums) <= 2`, we simply return `len(nums)`.
    *   `slow = 2`: This pointer marks the position where the next *valid* element should be written. It starts at index 2 because the first two elements (`nums[0]` and `nums[1]`) are always part of the result.
    *   `fast = 2`: This pointer iterates through the original array from the third element onwards to read values.

*   **Iteration (using `while fast < len(nums)`):**
    *   **Condition Check (`if nums[fast] != nums[slow - 2]:`)**:
        *   `nums[slow - 2]` refers to an element already placed in the "result" section of the array. This element is two positions behind the current `slow` pointer.
        *   The condition `nums[fast] != nums[slow - 2]` effectively checks if `nums[fast]` is *not* the same as the element that appeared two positions before the current `slow` pointer's position.
        *   **If `nums[fast]` is different from `nums[slow - 2]`:** This means `nums[fast]` is either a brand new distinct number, or it is the second allowed occurrence of a number (where `nums[slow-1]` is the first occurrence). In either case, it's a valid element to keep.
            *   `nums[slow] = nums[fast]`: We copy the valid element from the `fast` pointer's position to the `slow` pointer's position.
            *   `slow += 1`: We increment `slow` to move the "write" pointer to the next available slot for writing.
        *   **If `nums[fast]` is equal to `nums[slow - 2]`:** This implies that `nums[slow - 2]`, `nums[slow - 1]`, and `nums[fast]` would all be the same value. Thus, `nums[fast]` is the third (or more) occurrence of that number, and it should be skipped. `slow` remains unchanged.
    *   **Advance `fast`:** In every iteration, regardless of whether `nums[fast]` was copied or skipped, `fast` is incremented to move to the next element in the original array.

*   **Return Value:** After the loop finishes, `slow` holds the final length `k` of the modified array.

**Example Trace (`nums = [0,0,1,1,1,1,2,3,3]`):**

| `slow` | `fast` | `nums[fast]` | `nums[slow-2]` | `nums[fast] != nums[slow-2]`? | Action                                   | `nums` (array state after action)               |
| :----- | :----- | :----------- | :------------- | :---------------------------- | :--------------------------------------- | :---------------------------------------------- |
| 2      | 2      | 1            | `nums[0]` (0)  | True (1 != 0)                 | `nums[2]=1`. `slow`=3. `fast`=3.         | `[0,0,1,1,1,1,2,3,3]`                           |
| 3      | 3      | 1            | `nums[1]` (0)  | True (1 != 0)                 | `nums[3]=1`. `slow`=4. `fast`=4.         | `[0,0,1,1,1,1,2,3,3]`                           |
| 4      | 4      | 1            | `nums[2]` (1)  | False (1 == 1)                | Skip. `fast`=5.                          | `[0,0,1,1,1,1,2,3,3]` (no change at `slow`)     |
| 4      | 5      | 1            | `nums[2]` (1)  | False (1 == 1)                | Skip. `fast`=6.                          | `[0,0,1,1,1,1,2,3,3]` (no change at `slow`)     |
| 4      | 6      | 2            | `nums[2]` (1)  | True (2 != 1)                 | `nums[4]=2`. `slow`=5. `fast`=7.         | `[0,0,1,1,2,1,2,3,3]`                           |
| 5      | 7      | 3            | `nums[3]` (1)  | True (3 != 1)                 | `nums[5]=3`. `slow`=6. `fast`=8.         | `[0,0,1,1,2,3,2,3,3]`                           |
| 6      | 8      | 3            | `nums[4]` (2)  | True (3 != 2)                 | `nums[6]=3`. `slow`=7. `fast`=9.         | `[0,0,1,1,2,3,3,3,3]`                           |
| 7      | 9      | -            | -              | -                             | Loop ends (`fast < len(nums)` is false)  | `[0,0,1,1,2,3,3,_,_]` (elements beyond k don't matter) |

Return `slow` (which is 7). The final array will have its first 7 elements as `[0,0,1,1,2,3,3]`. Correct.

#### B. Provided Solution Logic (List Comprehension)

The provided solution uses a Python list comprehension combined with slice assignment:
`nums[:] = [nums[i] for i in range(len(nums)) if (i<2) or (i>=2 and (nums[i]!=nums[i-1] or nums[i]!=nums[i-2]))]`

*   **Mechanism:**
    1.  A *new* list is constructed by iterating through the original `nums` array and applying the filtering condition.
    2.  After the new list is fully built, the slice assignment `nums[:] = new_list` effectively replaces the *contents* of the original `nums` list with the elements of the `new_list`. From an external perspective, this looks like an in-place modification, but internally, it involves creating a temporary list.
    3.  Finally, `len(nums)` (the length of the newly assigned list) is returned.

*   **Condition Breakdown `(i<2) or (i>=2 and (nums[i]!=nums[i-1] or nums[i]!=nums[i-2]))`:**
    *   `i < 2`: This part ensures that the first two elements (`nums[0]` and `nums[1]`) are *always* included in the new list. This correctly handles the initial allowed duplicates or single elements.
    *   `i >= 2`: This part applies to elements from the third one (`nums[2]`) onwards.
    *   `(nums[i]!=nums[i-1] or nums[i]!=nums[i-2])`: This is the core logic for filtering. It leverages De Morgan's laws: `(A or B)` is equivalent to `not (not A and not B)`.
        *   So, the condition is equivalent to `not (nums[i] == nums[i-1] and nums[i] == nums[i-2])`.
        *   This means: "Include `nums[i]` if it's **NOT** the case that `nums[i]` is identical to both the immediately preceding element (`nums[i-1]`) AND the element two positions before (`nums[i-2]`)".
        *   If `nums[i]`, `nums[i-1]`, and `nums[i-2]` are all the same, it implies `nums[i]` is the third (or more) occurrence of that number within the processed sequence. In this specific scenario, `(nums[i]==nums[i-1] and nums[i]==nums[i-2])` would be true, making the overall `not(...)` false, and thus `nums[i]` would *not* be included.
        *   In all other valid cases (e.g., `1,1,2` where `nums[i]=2`, `nums[i-1]=1`, `nums[i-2]=1`; or `1,2,2` where `nums[i]=2`, `nums[i-1]=2`, `nums[i-2]=1`), at least one of `nums[i]!=nums[i-1]` or `nums[i]!=nums[i-2]` would be true, and `nums[i]` would be included.

*   **Pros of this approach:** Very concise and idiomatic Python.
*   **Cons of this approach:**
    *   While `nums[:] = ...` modifies the list in-place, the *creation* of the list on the right-hand side using a list comprehension requires O(N) auxiliary space. This might violate the strict interpretation of "O(1) extra memory" in interview settings or for languages without similar slice assignment semantics. However, LeetCode's Python judge often accepts this due to the internal optimization or the spirit of "modifying `nums` directly."

### 4. Time and Space Complexity Analysis

#### A. Optimal Two-Pointer Approach (Strict O(1) Space)

*   **Time Complexity: O(N)**
    *   The `fast` pointer iterates through the array exactly once, visiting each element. The `slow` pointer also moves at most N times. Each operation (comparison, assignment, increment) takes constant time. Therefore, the total time taken is directly proportional to the number of elements in `nums`.
*   **Space Complexity: O(1)**
    *   Only a constant number of extra variables (`slow`, `fast`) are used, regardless of the input array size. No additional data structures are allocated that scale with the input size. This strictly adheres to the "O(1) extra memory" constraint.

#### B. Provided Solution (List Comprehension)

*   **Time Complexity: O(N)**
    *   The list comprehension iterates through the input array once (`range(len(nums))`) to construct the new list. Each element involves constant time operations (index lookup, comparisons).
*   **Space Complexity: O(N)**
    *   The list comprehension creates a *new list* (`[nums[i] for ... ]`) to store the filtered elements. In the worst case (e.g., `[1,1,2,2,3,3]`), this new list will have a size proportional to the original array (up to N elements). This newly created list is temporarily stored in memory before its contents are assigned back to `nums[:]`. Thus, it uses O(N) auxiliary space.

### 5. Edge Cases

1.  **Empty Array:** The problem constraints state `1 <= nums.length`, so an empty array is not a possible input.
2.  **Array with 1 or 2 elements:**
    *   `nums = [1]` or `nums = [1,1]` or `nums = [1,2]`.
    *   **Expected Output:** `k = 1` or `k = 2` respectively.
    *   **Two-Pointer Approach:** The initial `if len(nums) <= 2: return len(nums)` handles these cases correctly, returning the array's actual length.
    *   **Provided List Comprehension:** Correctly includes all elements as `i < 2` condition is true for all relevant indices, resulting in the original array being effectively returned.
3.  **Array with all same elements, more than two:**
    *   `nums = [1,1,1,1,1]`
    *   **Expected Output:** `k = 2`, `nums`'s first two elements become `[1,1]`.
    *   Both approaches correctly handle this, as their logic prevents more than two consecutive duplicates from being kept.
4.  **Array with no duplicates:**
    *   `nums = [1,2,3,4,5]`
    *   **Expected Output:** `k = 5`, `nums` remains `[1,2,3,4,5]`.
    *   Both approaches correctly preserve all elements as no element violates the "at most twice" rule.
5.  **Array where every element appears exactly twice:**
    *   `nums = [1,1,2,2,3,3]`
    *   **Expected Output:** `k = 6`, `nums` remains `[1,1,2,2,3,3]`.
    *   Both approaches correctly keep all elements.

### 6. Clean, Well-Commented Version of the Optimal Solution (Two-Pointer)

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array such that each unique element
        appears at most twice, modifying the array in-place.

        Args:
            nums: A list of integers sorted in non-decreasing order.

        Returns:
            The new length (k) of the array after removing duplicates.
        """

        # Handle edge cases: if the array has 0, 1, or 2 elements,
        # all of them are valid since each element can appear at most twice.
        # The problem constraints state 1 <= nums.length, so an empty array is not a concern.
        if len(nums) <= 2:
            return len(nums)

        # 'slow' pointer (also known as 'write_idx' or 'k'):
        # This pointer tracks the position where the next valid element
        # should be written in the modified portion of the array.
        # We initialize it to 2 because the first two elements (nums[0] and nums[1])
        # are always considered valid to be kept (e.g., [1,1] or [1,2]).
        slow = 2

        # 'fast' pointer (also known as 'read_idx' or 'i'):
        # This pointer iterates through the original array from the third element onwards.
        # It reads elements to decide if they should be kept.
        fast = 2

        # Iterate 'fast' pointer through the rest of the array.
        # The loop continues as long as 'fast' is within the array bounds.
        while fast < len(nums):
            # The core logic for deciding whether to keep nums[fast]:
            # We want to keep nums[fast] IF it is NOT the third (or more)
            # occurrence of the current number.
            # To check this, we compare nums[fast] with nums[slow - 2].
            # nums[slow - 2] represents an element that is already part of
            # our "result" section of the array, specifically the element
            # that is two positions behind the current 'slow' pointer.
            #
            # Example Scenario:
            # If nums = [1, 1, 1, 2, 2, 3]
            # When slow=2, fast=2: nums[fast]=1, nums[slow-2]=nums[0]=1. (1 == 1) -> Skip.
            #   (This correctly identifies the third '1' and skips it)
            #
            # When slow=2, fast=3: nums[fast]=2, nums[slow-2]=nums[0]=1. (2 != 1) -> Keep.
            #   (This correctly identifies a new number '2', or the second '1' if it were [1,1,2] here)
            #
            # If nums[fast] is different from nums[slow - 2]:
            # This means nums[fast] is either:
            # 1. A completely new distinct number (e.g., after [1,1], we see a '2').
            # 2. The second allowed occurrence of a number (e.g., after [1], we see a second '1').
            # In both valid cases, the element should be kept.
            if nums[fast] != nums[slow - 2]:
                # If valid, copy the element from the 'fast' pointer's position
                # to the 'slow' pointer's position in the array.
                nums[slow] = nums[fast]
                # Increment 'slow' to move to the next available slot for writing.
                slow += 1

            # Always increment 'fast' pointer to move to the next element
            # in the original array, regardless of whether the current element
            # was kept or skipped.
            fast += 1

        # The 'slow' pointer now holds the new length (k) of the array
        # with duplicates removed according to the problem's rules.
        # Elements beyond 'slow - 1' do not matter.
        return slow

```

### 7. Key Insights and Patterns

1.  **Two-Pointer Technique (Read/Write Pointers):** This problem is a fundamental application of the two-pointer pattern for in-place array modifications. One pointer (`fast` or `read_idx`) iterates through the entire array, while another (`slow` or `write_idx`) points to the next available position to write a valid element. This pattern is essential for O(1) space solutions on arrays.
2.  **Generalization for "at most K duplicates":** The core logic `if nums[fast] != nums[slow - K]:` is a highly reusable pattern for problems asking to keep an element at most `K` times in a sorted array.
    *   For "at most 1 duplicate" (LeetCode 26: Remove Duplicates from Sorted Array), `K=1`. The condition simplifies to `if nums[fast] != nums[slow - 1]:` (i.e., the current element is different from the last element added to the result).
    *   For "at most 2 duplicates" (this problem), `K=2`. The condition is `if nums[fast] != nums[slow - 2]:`. This ensures that `nums[fast]` is not the `(K+1)`th occurrence of the value `nums[slow-K]`.
    *   The `slow` pointer typically starts at `K`, and the `fast` pointer also starts at `K`.
3.  **In-place Modification Nuances in Python:** While Python's `nums[:] = new_list` syntax appears to modify the list "in-place," it actually involves creating a temporary `new_list` in memory on the right-hand side, which can consume O(N) auxiliary space. For strict O(1) space constraints (common in interviews for other languages like C++/Java), the explicit two-pointer assignment approach (like the `slow`/`fast` method provided) is preferred as it genuinely only uses a few constant-space variables. Always clarify the interpretation of "in-place" with the interviewer if unsure.
4.  **Leveraging Sorted Input:** The sorted nature of the input array is critical. It allows us to determine duplicate counts and values by simply looking at adjacent or nearby elements, avoiding the need for hash maps or other more complex data structures for counting.
5.  **Handling Initial Elements / Base Cases:** For problems where a fixed small number of initial elements are always valid (like the first `K` elements in "at most K duplicates"), it's often cleaner to handle these with a separate base case or by initializing the `write` pointer appropriately. This simplifies the main loop's logic and prevents potential "index out of bounds" errors (e.g., trying to access `nums[slow-K]` when `slow < K`).