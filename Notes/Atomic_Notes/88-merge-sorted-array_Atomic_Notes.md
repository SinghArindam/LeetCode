Here is a set of atomic notes for LeetCode problem 88-merge-sorted-array, formatted for spaced repetition learning:

---

**Problem Number: 88-merge-sorted-array**

- - -

**Concept**: Problem Objective
**Context**: Merge two already sorted integer arrays, `nums1` (containing `m` valid elements) and `nums2` (containing `n` elements), into a single sorted array.
**Example**: Merge `[1,2,3]` (from `nums1`) and `[2,5,6]` (from `nums2`).

- - -

**Concept**: In-Place Modification Requirement
**Context**: The merged result must be stored directly within `nums1`. The function should modify `nums1` and not return anything.
**Example**: `nums1[:] = ...` or direct index assignment `nums1[k] = value` is used.

- - -

**Concept**: `nums1` Pre-allocated Capacity
**Context**: `nums1` has a total length of `m + n`. The first `m` elements are valid sorted numbers, and the last `n` elements are placeholders (usually zeros) providing sufficient space for `nums2`.
**Example**: If `m=3, n=3`, `nums1` might be `[1,2,3,0,0,0]`. The `0`s are where `nums2` elements will go.

- - -

**Concept**: Optimal Approach - Merge from the End
**Context**: To avoid overwriting valid elements in `nums1` during an in-place merge, the most efficient strategy is to start filling `nums1` from its *end* (largest index) backwards.
**Example**: Placing the largest element into `nums1[m+n-1]`, then the next largest into `nums1[m+n-2]`, etc.

- - -

**Concept**: Pointer `p1` Initialization (Last Valid `nums1`)
**Context**: Pointer `p1` should initially point to the last valid element in `nums1`.
**Example**: `p1 = m - 1`. If `m=3`, `p1` starts at index 2.

- - -

**Concept**: Pointer `p2` Initialization (Last `nums2` Element)
**Context**: Pointer `p2` should initially point to the last element in `nums2`.
**Example**: `p2 = n - 1`. If `n=3`, `p2` starts at index 2.

- - -

**Concept**: Pointer `p` Initialization (Target Write Position)
**Context**: Pointer `p` should initially point to the last available position in `nums1` where a merged element will be placed.
**Example**: `p = m + n - 1`. If `m=3, n=3`, `p` starts at index 5.

- - -

**Concept**: Main Merge Loop Condition
**Context**: The primary merge loop continues as long as there are elements left to compare in *both* `nums1`'s valid section and `nums2`.
**Example**: `while p1 >= 0 and p2 >= 0:`

- - -

**Concept**: Main Merge Loop Logic (Comparison & Placement)
**Context**: Inside the main loop, compare `nums1[p1]` and `nums2[p2]`. The larger of the two is placed at `nums1[p]`. Both the source pointer (`p1` or `p2`) and the target pointer (`p`) are then decremented.
**Example**: `if nums1[p1] > nums2[p2]: nums1[p] = nums1[p1]; p1 -= 1; else: nums1[p] = nums2[p2]; p2 -= 1; p -= 1;`

- - -

**Concept**: Handling Remaining `nums2` Elements
**Context**: After the main loop, if `p2` is still non-negative, it means `nums2` still has elements. These remaining `nums2` elements are guaranteed to be smaller than any remaining `nums1` elements (which would have already been placed), so they are copied directly into the beginning of `nums1`.
**Example**: `while p2 >= 0: nums1[p] = nums2[p2]; p2 -= 1; p -= 1;`

- - -

**Concept**: Handling Remaining `nums1` Elements
**Context**: After the main loop, if `p1` is still non-negative, it means `nums1` still has elements. No action is needed for these elements; they are already in their correct sorted positions within the lower indices of `nums1`.
**Example**: If `nums1 = [1,2,3,0,0,0], m=3, nums2=[4,5,6], n=3`, after merging the larger elements, `nums1[0..2]` might still hold `[1,2,3]`, which is correct.

- - -

**Concept**: Optimal Time Complexity
**Context**: The two-pointer from the end approach processes each element from `nums1` (valid part) and `nums2` at most once.
**Example**: `O(m + n)` time complexity.

- - -

**Concept**: Optimal Space Complexity
**Context**: All operations are performed directly within the `nums1` array, and only a constant number of pointers are used.
**Example**: `O(1)` space complexity.

- - -

**Concept**: Edge Case: `m = 0`
**Context**: If `nums1` initially has no valid elements (`m=0`), `p1` starts at `-1`. The main merge loop is skipped, and only the loop for copying remaining `nums2` elements executes, correctly populating `nums1` entirely from `nums2`.
**Example**: `nums1 = [0,0,0], m = 0, nums2 = [1,2,3], n = 3` results in `nums1 = [1,2,3]`.

- - -

**Concept**: Edge Case: `n = 0`
**Context**: If `nums2` is empty (`n=0`), `p2` starts at `-1`. Both the main merge loop and the `nums2` remaining elements loop are skipped. `nums1` remains unchanged, which is correct as it's already sorted.
**Example**: `nums1 = [1,2,3], m = 3, nums2 = [], n = 0` results in `nums1 = [1,2,3]`.

- - -

**Concept**: Algorithmic Pattern: Two-Pointer Technique
**Context**: This problem is a classic application of the two-pointer technique, using multiple pointers (`p1`, `p2`, `p`) to efficiently traverse and process elements from different arrays or sections simultaneously.
**Example**: Used in problems like finding pairs with a specific sum, or merging sorted lists/arrays.

- - -

**Concept**: Algorithmic Pattern: Merge Sort's Merge Step
**Context**: The core logic of the optimal solution directly applies the "merge" step found in the Merge Sort algorithm, adapted for in-place modification with pre-allocated space.
**Example**: Understanding this connection helps recognize similar merging patterns in other sorting or array problems.

- - -

**Concept**: Naive Approach: Copy and Sort
**Context**: A simpler (but less optimal) approach involves copying `nums2` elements into `nums1`'s placeholder zeros, then sorting the entire `nums1` array.
**Example**: In Python: `nums1[m:] = nums2; nums1.sort()`. Or `nums1[:] = nums1[:m] + nums2; nums1.sort()`.

- - -

**Concept**: Complexity of Naive Copy and Sort
**Context**: This approach typically has higher time and space complexity due to the sorting step and potential temporary list creation.
**Example**: `O((m + n) log (m + n))` time complexity and `O(m + n)` space complexity (e.g., due to Timsort's auxiliary space or list concatenation).

---