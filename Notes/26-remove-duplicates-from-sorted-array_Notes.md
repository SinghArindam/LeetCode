## LeetCode Problem 26: Remove Duplicates from Sorted Array - Comprehensive Notes

---

### 1. Problem Summary

The problem asks us to modify an integer array `nums` **in-place** such that all duplicate elements are removed, and each unique element appears only once. The array `nums` is guaranteed to be sorted in **non-decreasing order**. Crucially, the **relative order** of the unique elements must be preserved. After modification, the function should return `k`, which is the total count of unique elements. The first `k` elements of the `nums` array should contain these unique elements in their original relative order. The contents beyond the `k`-th element do not matter.

**Key Constraints & Requirements:**
*   **Input Array:** `nums` is sorted in non-decreasing order.
*   **In-place Modification:** The array must be modified without using extra space proportional to the input size (ideally O(1) extra space).
*   **Relative Order Preservation:** The order of the unique elements must remain the same as in the original array.
*   **Output:** Return `k` (the number of unique elements). The modified array `nums` should have its first `k` elements as the unique elements.
*   **Constraints on `nums.length`:** `1 <= nums.length <= 3 * 10^4`. This means the array will never be empty.

---

### 2. Explanation of All Possible Approaches

Given the "in-place" constraint, the options are somewhat limited, especially for true O(1) auxiliary space.

#### 2.1. Naive Approach (Not truly in-place / O(N) Space)

*   **Concept:** Iterate through the array, add unique elements to a *new* list. After iterating, copy the elements from the new list back to the original `nums` array.
*   **Steps:**
    1.  Initialize an empty list `unique_elements`.
    2.  Iterate through `nums`. For each element, check if it's already the last element added to `unique_elements` (this works because the array is sorted, so duplicates are adjacent). If it's different or `unique_elements` is empty, add it.
    3.  Once the iteration is complete, copy `unique_elements` back into `nums` using slice assignment (`nums[:] = unique_elements`).
    4.  Return `len(unique_elements)`.
*   **Suitability:** This approach achieves the correct result and preserves relative order. However, it uses O(N) auxiliary space for `unique_elements`, violating the strict "in-place" (O(1) space) requirement often implied by such problems.

#### 2.2. Two-Pointer Approach (Optimal - O(1) Space)

*   **Concept:** This is the standard and most efficient approach for in-place modifications on sorted arrays. It uses two pointers:
    *   A "slow" pointer (`i`) that tracks the position where the next unique element should be placed.
    *   A "fast" pointer (`j`) that iterates through the array to find new unique elements.
*   **Logic:** Since the array is sorted, all duplicate elements will be adjacent. We only need to keep the first occurrence of each number.
    *   The element at `nums[0]` is always unique in the context of the output. So, `i` can start at 0.
    *   The `j` pointer iterates from the second element (`nums[1]`) to the end.
    *   If `nums[j]` is *different* from `nums[i]`, it means we've found a new unique element. We then increment `i` (to move to the next slot for a unique element) and copy `nums[j]` to `nums[i]`.
    *   If `nums[j]` is *the same* as `nums[i]`, it's a duplicate. We simply ignore it and increment `j`, letting the fast pointer skip over all duplicates.
*   **Suitability:** This approach is truly in-place, modifying the array directly with only two integer pointers, resulting in O(1) auxiliary space.

#### 2.3. Pythonic Slice Assignment (Provided Solution - O(N) Space, but concise)

*   **Concept:** This leverages Python's list comprehension and slice assignment feature to achieve the desired result in a single line. While syntactically compact and elegant, it conceptually operates similarly to the "Naive Approach" in terms of memory.
*   **Logic:**
    *   It constructs a *new* list using a list comprehension: `[nums[i] for i in range(len(nums)) if (i==0 or nums[i]!=nums[i-1])]`.
    *   The condition `(i==0 or nums[i]!=nums[i-1])` checks if the current element `nums[i]` is the first element of the array, or if it's different from the *immediately preceding* element. Because the array is sorted, this effectively selects only the first occurrence of each number.
    *   The `nums[:] = ...` syntax then replaces the entire content of the original `nums` list with the elements from this newly generated list. This is what makes it "in-place" *from the caller's perspective*, as the `nums` object itself is mutated, not replaced.
    *   Finally, `return len(nums)` returns the length of the new `nums` list, which is `k`.
*   **Suitability:** This is highly Pythonic and concise. It's often acceptable in coding challenges due to Python's memory management, but it's important to understand that a temporary O(N) list is created behind the scenes before being assigned back.

---

### 3. Detailed Explanation of Logic

#### 3.1. Logic Behind the Provided Solution (Pythonic Slice Assignment)

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Create a new list containing only unique elements.
        # The condition `i==0 or nums[i]!=nums[i-1]` ensures:
        # 1. The first element (at index 0) is always included.
        # 2. For subsequent elements, it's included only if it's different
        #    from its immediate predecessor. Since the array is sorted,
        #    this effectively picks the first occurrence of each unique number.
        unique_list = [nums[i] for i in range(len(nums)) if (i==0 or nums[i]!=nums[i-1])]
        
        # Replace the contents of the original 'nums' list with the 'unique_list'.
        # The `nums[:] = ...` syntax performs an in-place modification of the list's
        # contents, rather than re-assigning the 'nums' variable to a new list object.
        nums[:] = unique_list
        
        # The length of the modified 'nums' list is the number of unique elements (k).
        return len(nums)
```

**Step-by-step Breakdown:**

1.  **`unique_list = [nums[i] for i in range(len(nums)) if (i==0 or nums[i]!=nums[i-1])]`**:
    *   This is a list comprehension. It iterates through the indices `i` from `0` to `len(nums) - 1`.
    *   For each `i`, it checks the condition `(i==0 or nums[i]!=nums[i-1])`.
        *   `i==0`: This ensures that the very first element of the array `nums[0]` is *always* included in `unique_list`. This is crucial because `nums[0]` is always a unique element in the context of the modified array.
        *   `nums[i]!=nums[i-1]`: For any subsequent element (`i > 0`), this condition checks if the current element `nums[i]` is different from the element immediately preceding it (`nums[i-1]`). Since the input array `nums` is sorted, if `nums[i]` is different from `nums[i-1]`, it means we've encountered a new unique value (the first occurrence of this value). If `nums[i]` were equal to `nums[i-1]`, it would be a duplicate, and it would be skipped by the `if` condition.
    *   The result of this line is a new Python list (`unique_list`) containing only the unique elements from `nums`, in their original relative order.

2.  **`nums[:] = unique_list`**:
    *   This is a slice assignment. In Python, `nums[:]` refers to the *entire content* of the list `nums`.
    *   Assigning another list (`unique_list`) to `nums[:]` means that the elements of `unique_list` are copied into `nums`, effectively replacing `nums`'s original contents. This modifies the list object that `nums` refers to *in-place*. The `nums` variable itself still points to the same list object in memory, but that object's internal array of elements has been updated. This is why it satisfies the "in-place" requirement from a functional perspective for the LeetCode judge.

3.  **`return len(nums)`**:
    *   After the slice assignment, the `nums` list now contains only the unique elements. Its length is exactly `k`, the number of unique elements. This value is returned.

#### 3.2. Logic Behind Optimal Alternative (Two-Pointer Approach)

This approach is more aligned with the strict O(1) space interpretation of "in-place" and is commonly preferred in languages like C++ or Java where list re-allocation is less transparent or more costly.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Although constraints say 1 <= nums.length, good practice
            return 0

        # 'i' (slow pointer) tracks the position for the next unique element.
        # It also implicitly represents the count of unique elements found so far (k).
        i = 0 

        # 'j' (fast pointer) iterates through the array to find new unique elements.
        for j in range(1, len(nums)):
            # If the element at 'j' is different from the element at 'i',
            # it means we've found a new unique element.
            if nums[j] != nums[i]:
                # Increment 'i' to move to the next slot for a unique element.
                i += 1
                # Place the new unique element at the 'i' position.
                # This effectively moves unique elements to the beginning of the array.
                nums[i] = nums[j]
        
        # 'i + 1' gives the total number of unique elements.
        # 'i' is 0-indexed, so if i is 0, it means 1 unique element (nums[0]).
        # If i is 4, it means 5 unique elements (nums[0] through nums[4]).
        return i + 1
```

**Step-by-step Breakdown:**

1.  **Edge Case `if not nums:`**: Although the problem constraints (`1 <= nums.length`) mean `nums` will never be empty, it's good defensive programming to handle an empty array. An empty array has 0 unique elements.

2.  **`i = 0`**:
    *   The `i` pointer is initialized to 0. This pointer will point to the last position where a unique element was placed. Effectively, `nums[0...i]` will contain the unique elements found so far.
    *   `nums[0]` is inherently unique (as it's the first element), so `i` starts pointing to its position. `i+1` will eventually be `k`.

3.  **`for j in range(1, len(nums)):`**:
    *   The `j` pointer starts from index 1 and iterates through the rest of the array. It's the "fast" pointer that searches for unique elements.

4.  **`if nums[j] != nums[i]:`**:
    *   This is the core comparison. If the element `nums[j]` (the current element being examined by the fast pointer) is *different* from `nums[i]` (the last confirmed unique element), it means `nums[j]` is a new unique value that needs to be kept.
    *   Since the array is sorted, if `nums[j]` is different from `nums[i]`, it must be a *greater* value (as `nums` is non-decreasing).

5.  **`i += 1`**:
    *   If `nums[j]` is unique, we first increment `i`. This moves the slow pointer to the *next available slot* where the new unique element will be placed.

6.  **`nums[i] = nums[j]`**:
    *   Then, we copy the unique element `nums[j]` into `nums[i]`. This effectively shifts unique elements to the front of the array.

7.  **`return i + 1`**:
    *   After the loop finishes, `i` points to the index of the *last* unique element. Since `i` is 0-indexed, `i + 1` gives the total count of unique elements (`k`). For example, if `i` is 0, it means only `nums[0]` is unique, and `k=1`. If `i` is 4, `nums[0]` through `nums[4]` are unique, and `k=5`.

---

### 4. Time and Space Complexity Analysis

#### 4.1. Naive Approach (Conceptual: Building a new list and copying back)

*   **Time Complexity: O(N)**
    *   Iterating through `nums` to build `unique_elements`: O(N)
    *   Copying `unique_elements` back to `nums`: O(N)
    *   Total: O(N)
*   **Space Complexity: O(N)**
    *   For storing the `unique_elements` list in the worst case (all elements are unique), it will store N elements.

#### 4.2. Two-Pointer Approach (Optimal)

*   **Time Complexity: O(N)**
    *   The `j` pointer traverses the array from the second element to the end once. Each element is visited and compared at most once.
    *   The operations inside the loop (increment `i`, assignment) are O(1).
    *   Total: O(N), where N is the length of `nums`.
*   **Space Complexity: O(1)**
    *   Only a few constant extra variables (`i`, `j`) are used, regardless of the input array size. No auxiliary data structures are created.

#### 4.3. Pythonic Slice Assignment (Provided Solution)

*   **Time Complexity: O(N)**
    *   The list comprehension iterates through `nums` once: O(N).
    *   The slice assignment `nums[:] = ...` involves creating a new list and then copying its elements. Creating the new list takes O(N) time. Copying it back also takes O(N) time.
    *   Total: O(N).
*   **Space Complexity: O(N)**
    *   The list comprehension creates a *new* temporary list in memory to hold the unique elements. In the worst case (all elements unique), this new list will be of size N. Even though this temporary list is then assigned back and the old `nums` elements are garbage-collected, at some point, both the old `nums` data and the new `unique_list` data might temporarily coexist in memory before the old data is freed. Hence, it's considered O(N) auxiliary space.

---

### 5. Edge Cases and How They Are Handled

*   **Empty Array (`nums = []`):**
    *   **Constraint:** The problem states `1 <= nums.length <= 3 * 10^4`, so `nums` will never be empty.
    *   **Two-Pointer (if modified to handle):** A check `if not nums: return 0` would handle this correctly. Without it, `range(1, 0)` would be empty, loop wouldn't run, `i=0`, returns `0+1=1`, which is incorrect for an empty array.
    *   **Pythonic Slice Assignment:** `range(len(nums))` would be `range(0)`, resulting in an empty `unique_list`. `nums[:] = []` would make `nums` empty, `len(nums)` returns `0`. Handles correctly.

*   **Array with One Element (`nums = [X]`):**
    *   **Two-Pointer:** `i=0`. `j` loop `range(1, 1)` is empty. Returns `i+1 = 0+1 = 1`. Correct.
    *   **Pythonic Slice Assignment:** `i=0` is included. `range(len(nums))` is `range(1)`. Loop runs for `i=0`. Condition `(0==0 or ...)` is true. `[nums[0]]` is created. `nums[:] = [nums[0]]`. `len(nums)` returns `1`. Correct.

*   **Array with All Unique Elements (`nums = [1, 2, 3, 4, 5]`):**
    *   **Two-Pointer:** For every `j`, `nums[j]` will always be different from `nums[i]`. So, `i` will increment in every iteration, and `nums[j]` will be copied to `nums[i]`. The array will effectively be copied onto itself. `k` will be `len(nums)`. Correct.
    *   **Pythonic Slice Assignment:** For every `i > 0`, `nums[i]!=nums[i-1]` will always be true. The `unique_list` will be identical to the original `nums`. `nums[:]` will be assigned `nums` itself. `len(nums)` returns `len(original_nums)`. Correct.

*   **Array with All Duplicate Elements (`nums = [7, 7, 7, 7]`):**
    *   **Two-Pointer:** `i=0`. `nums[0]` is `7`.
        *   `j=1`: `nums[1]` (`7`) == `nums[0]` (`7`). Do nothing. `j` increments.
        *   `j=2`: `nums[2]` (`7`) == `nums[0]` (`7`). Do nothing. `j` increments.
        *   `j=3`: `nums[3]` (`7`) == `nums[0]` (`7`). Do nothing. `j` increments.
        *   Loop ends. `i` is still `0`. Returns `i+1 = 1`. `nums` will be `[7, 7, 7, 7]`, but only the first `k=1` element `nums[0]` is relevant. Correct.
    *   **Pythonic Slice Assignment:**
        *   `i=0`: `nums[0]` (`7`) is included. `unique_list = [7]`
        *   `i=1`: `nums[1]` (`7`) == `nums[0]` (`7`). Not included.
        *   `i=2`: `nums[2]` (`7`) == `nums[1]` (`7`). Not included.
        *   ...and so on.
        *   `unique_list` becomes `[7]`.
        *   `nums[:] = [7]`. `nums` becomes `[7]`.
        *   Returns `len(nums)` which is `1`. Correct.

---

### 6. Clean, Well-Commented Version of the Optimal Solution

As discussed, the Two-Pointer approach is considered "optimal" due to its strict O(1) auxiliary space complexity.

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each
        unique element appears only once. The relative order of the elements
        is preserved. Returns the number of unique elements.

        Args:
            nums: A list of integers sorted in non-decreasing order.

        Returns:
            The number of unique elements (k). The first k elements of nums
            will contain the unique elements.
        """
        
        # According to constraints, nums.length is at least 1.
        # However, for robustness in general scenarios, one might add:
        # if not nums:
        #     return 0

        # 'slow_pointer' (i) tracks the position where the next unique element
        # should be placed. It also serves as a counter for unique elements.
        # Initially, the first element (at index 0) is considered unique.
        slow_pointer = 0 

        # 'fast_pointer' (j) iterates through the array from the second element
        # to find new unique elements.
        # We start from index 1 because nums[0] is already assumed to be unique
        # and correctly placed.
        for fast_pointer in range(1, len(nums)):
            # Compare the element at the fast_pointer with the element at the slow_pointer.
            # If they are different, it means we've found a new unique element.
            if nums[fast_pointer] != nums[slow_pointer]:
                # Increment the slow_pointer. This moves it to the next available slot
                # in the array where the new unique element will be placed.
                slow_pointer += 1
                
                # Copy the unique element found by the fast_pointer to the position
                # indicated by the slow_pointer. This effectively shifts unique
                # elements to the beginning of the array.
                nums[slow_pointer] = nums[fast_pointer]
        
        # The 'slow_pointer' now points to the index of the last unique element.
        # Since it's 0-indexed, the total count of unique elements (k) is
        # (slow_pointer + 1). For example, if slow_pointer is 0, it means
        # only nums[0] is unique, so k=1.
        return slow_pointer + 1

```

---

### 7. Key Insights and Patterns

1.  **Two-Pointer Technique for Sorted Arrays:** This problem is a classic example of the two-pointer technique applied to a sorted array for in-place modification. It's incredibly powerful for problems requiring filtering, merging, or modifying elements while maintaining order and minimizing space.
    *   **Mechanism:** One pointer (`slow_pointer` or `i`) typically marks the boundary of the processed/resultant part of the array, and the other (`fast_pointer` or `j`) explores the unprocessed part.
    *   **When to use:** When you need to modify an array in-place, especially if it's sorted, and the relative order of certain elements must be preserved. Common scenarios include removing duplicates, moving all zeros to the end, or merging two sorted arrays.

2.  **Leveraging Sorted Property:** The fact that the array is sorted in non-decreasing order is crucial. It simplifies the logic significantly because duplicates are guaranteed to be adjacent. If the array were unsorted, a hash set would be needed (O(N) space) or sorting would be required first (O(N log N) time).

3.  **In-place Modification Nuances:**
    *   **True O(1) Space:** For strict in-place modification, aim for solutions that only use a constant amount of auxiliary memory (e.g., a few integer variables for pointers). The two-pointer approach exemplifies this.
    *   **Python's `nums[:] = ...`:** While convenient and common in Python, it's important to understand that it often involves creating a temporary copy of the data, which leads to O(N) auxiliary space behind the scenes, even if the original list object is mutated. This is a trade-off for conciseness and expressiveness. Depending on the interview context or language, "in-place" might strictly imply O(1) auxiliary space.

4.  **Relative Order Preservation:** This constraint means you cannot simply use a `set` to get unique elements and then convert back to a list, as sets do not preserve order (or may not preserve the *original* relative order if multiple elements had the same value but were not adjacent in the input). The two-pointer approach naturally preserves relative order because elements are only moved forward from their original positions.

5.  **Return Value `k` vs. Array Length:** The problem asks to return `k` (the count of unique elements), and the array is modified such that the first `k` elements are the unique ones. The remaining elements don't matter. This is a common pattern for "in-place" problems where the original array size might be larger than the logical size of the result.

This problem is fundamental and serves as a great introduction to in-place algorithms and the two-pointer technique on sorted arrays.