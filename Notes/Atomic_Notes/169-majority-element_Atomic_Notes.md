Here is a set of atomic notes for LeetCode problem 169 - Majority Element, generated from the provided comprehensive and short notes:

---

-   **Concept**: LeetCode 169 Problem Goal
    **Context**: Find the "majority element" in a given integer array `nums`.
    **Example**: The element must appear *more than* `⌊n / 2⌋` times, where `n` is the array size.

-   **Concept**: Majority Element Existence Guarantee
    **Context**: For LeetCode 169, the problem guarantees that the majority element *always exists* in the input array.
    **Example**: This simplifies solutions by removing the need to handle cases where no majority element is found.

-   **Concept**: LeetCode 169 Problem Constraints
    **Context**: Defines the allowed size of the input array `n` and the range of values for elements `nums[i]`.
    **Example**: `1 <= n <= 5 * 10^4`, `-10^9 <= nums[i] <= 10^9`.

-   **Concept**: Follow-up Challenge for Majority Element
    **Context**: The problem poses an additional challenge to solve it with optimal time and space complexity.
    **Example**: Achieve O(N) time complexity and O(1) space complexity.

-   **Concept**: Brute-Force Counting Approach for Majority Element
    **Context**: For each unique element, count its occurrences by iterating through the entire array.
    **Example**: Nested loops, where the outer loop picks an element and the inner loop counts its frequency.

-   **Concept**: Brute-Force Majority Element Complexity
    **Context**: Analysis of the brute-force counting approach's performance.
    **Example**: Time: O(N^2) (due to nested iteration or repeated `nums.count()`). Space: O(1).

-   **Concept**: Sorting Approach for Majority Element
    **Context**: If the array `nums` is sorted, the majority element (appearing `> n/2` times) will necessarily be located at the middle index.
    **Example**: For `nums = [2,2,1,1,1,2,2]`, sorted becomes `[1,1,1,2,2,2,2]`. The element at index `len(nums)//2` (which is 3) is `2`.

-   **Concept**: Sorting Approach Complexity for Majority Element
    **Context**: Analysis of the sorting approach's performance.
    **Example**: Time: O(N log N) (for typical comparison sorts like Timsort). Space: O(N) (for auxiliary space, or O(1) if truly in-place).

-   **Concept**: Efficient Hash Map Approach for Majority Element
    **Context**: Use a hash map (dictionary) to store and increment counts for each element while iterating through the array only once.
    **Example**: `counts[num] = counts.get(num, 0) + 1` for each `num` in `nums`.

-   **Concept**: Efficient Hash Map Complexity for Majority Element
    **Context**: Analysis of the efficient hash map approach's performance.
    **Example**: Time: O(N) (single pass to build counts). Space: O(N) (worst case, if all elements are unique, to store counts).

-   **Concept**: Inefficient Hash Map Implementation Pitfall
    **Context**: A common mistake is to repeatedly call `list.count(element)` inside a loop to populate a frequency map.
    **Example**: `for num in nums: if num not in d: d[num] = nums.count(num)`. This leads to O(N^2) time complexity.

-   **Concept**: Boyer-Moore Voting Algorithm Principle
    **Context**: Finds the majority element by "cancelling" out occurrences of the current candidate with occurrences of different elements.
    **Example**: Each time a non-candidate element is encountered, it's considered to "outvote" or cancel one instance of the current candidate. The majority element will always have a positive net count.

-   **Concept**: Boyer-Moore Voting Algorithm Steps
    **Context**: The specific procedural logic of the Boyer-Moore Voting Algorithm.
    **Example**:
    1. Initialize `candidate = None`, `count = 0`.
    2. For each `num` in `nums`:
        - If `count == 0`, set `candidate = num` and `count = 1`.
        - Else if `num == candidate`, `count += 1`.
        - Else (`num != candidate`), `count -= 1`.
    3. Return `candidate`.

-   **Concept**: Boyer-Moore Voting Algorithm Optimal Complexity
    **Context**: Analysis of the performance of the Boyer-Moore Voting Algorithm.
    **Example**: Time: O(N) (achieved with a single pass through the array). Space: O(1) (uses only a few constant extra variables).

-   **Concept**: Impact of Guarantee on Boyer-Moore Algorithm
    **Context**: Because the majority element is guaranteed to exist in LeetCode 169, a second pass to verify the `candidate` found by Boyer-Moore is not necessary.
    **Example**: The `candidate` returned after the first pass is definitively the majority element without further checks.

-   **Concept**: Handling `n=1` Edge Case
    **Context**: All discussed algorithms (Brute-Force, Sorting, Hash Map, Boyer-Moore) correctly identify the majority element for an array with a single element.
    **Example**: For `nums = [7]`, all methods correctly return `7`.

-   **Concept**: Handling All Elements Same Edge Case
    **Context**: All discussed algorithms correctly identify the majority element even when all elements in the array are identical.
    **Example**: For `nums = [3, 3, 3, 3]`, all methods correctly return `3`.

-   **Concept**: Frequency Counting General Technique
    **Context**: Hash maps (dictionaries) are a fundamental and efficient data structure for counting occurrences of elements in a collection.
    **Example**: Storing `element: count` pairs in a dictionary.

-   **Concept**: Leveraging Sorting for Positional Properties
    **Context**: Sorting an array can reveal inherent properties related to element positions, which can be useful for certain problems.
    **Example**: Finding the median, k-th smallest element, or the majority element (as seen in this problem).

-   **Concept**: Algorithm Complexity Trade-offs
    **Context**: When choosing an algorithm, it's crucial to evaluate and balance its time complexity against its space complexity requirements.
    **Example**: An O(N) time, O(N) space hash map solution might be preferred over O(N log N) sorting if constant space isn't a strict requirement.