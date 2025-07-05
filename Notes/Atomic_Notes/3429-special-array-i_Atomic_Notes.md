Here is a set of atomic notes for LeetCode problem 3429-special-array-i, designed for spaced repetition learning:

-   **Concept**: Definition of a "Special Array"
    *   **Context**: Problem 3429-special-array-i. An array `nums` is "special" if every pair of its adjacent elements `(nums[i], nums[i+1])` consists of numbers with *different* parity.
    *   **Example**: `[2, 1, 4]` is special. `[4, 3, 1, 6]` is not special because `(3, 1)` have the same parity (both odd).

-   **Concept**: Parity of a Number
    *   **Context**: Fundamental concept used in LeetCode problem 3429 to determine if a number is even or odd.
    *   **Example**: 2 is even (parity 0), 3 is odd (parity 1).

-   **Concept**: How to Check Parity Programmatically
    *   **Context**: Determining if an integer `x` is even or odd in programming.
    *   **Example**: Use the modulo operator: `x % 2 == 0` for even; `x % 2 == 1` (or `x % 2 != 0`) for odd.

-   **Concept**: Core Algorithmic Approach - Iterative Check
    *   **Context**: The most straightforward and efficient strategy for "Special Array I".
    *   **Example**: Loop through adjacent elements and verify the parity condition directly.

-   **Concept**: Iteration Pattern for Adjacent Elements
    *   **Context**: When a problem requires checking pairs of `(current, previous)` elements in an array.
    *   **Example**: Iterate using `for i in range(1, len(nums)):` and compare `nums[i]` with `nums[i-1]`.

-   **Concept**: Condition for an Array to be *Not* Special
    *   **Context**: Identifying a violation of the "special array" rule.
    *   **Example**: If `nums[i] % 2 == nums[i-1] % 2` (i.e., both are even or both are odd) for any `i`, the array is not special.

-   **Concept**: Short-Circuiting Optimization
    *   **Context**: Improving efficiency in algorithms where a single failure condition invalidates the entire result.
    *   **Example**: As soon as an adjacent pair with the same parity is found, immediately return `false` without checking the rest of the array.

-   **Concept**: Python's `all()` Built-in Function
    *   **Context**: A concise and efficient way to check if all items in an iterable are true, useful for "all conditions must pass" scenarios.
    *   **Example**: `all(nums[i] % 2 != nums[i - 1] % 2 for i in range(1, len(nums)))` effectively checks all pairs and short-circuits.

-   **Concept**: Time Complexity of the Solution (O(N))
    *   **Context**: Measuring the performance of the iterative solution for "Special Array I".
    *   **Example**: It performs a single pass through `N` elements (at most `N-1` comparisons), making it `O(N)` time complexity.

-   **Concept**: Space Complexity of the Solution (O(1))
    *   **Context**: Measuring the memory usage of the iterative solution for "Special Array I".
    *   **Example**: It uses a constant amount of extra memory (e.g., loop index, parity variables) regardless of input size, resulting in `O(1)` space complexity.

-   **Concept**: Edge Case - Single Element Array
    *   **Context**: How to handle arrays with `nums.length == 1`.
    *   **Example**: `nums = [1]`. A single-element array has no adjacent pairs, so it inherently satisfies the "special" condition and should return `True`. Python's `all()` on an empty iterable correctly handles this.

-   **Concept**: Impact of Problem Constraints
    *   **Context**: How given constraints (`N` and `nums[i]` ranges) influence algorithm choice and performance expectations.
    *   **Example**: `1 <= nums.length <= 100` and `1 <= nums[i] <= 100`. Small array size confirms `O(N)` is very efficient. Small integer values ensure modulo operations are fast and no overflow issues.

-   **Concept**: Direct Problem Translation Pattern
    *   **Context**: A common strategy for solving "Easy" LeetCode problems.
    *   **Example**: Directly converting the problem's definition (e.g., "every pair must have different parity") into an iterative code check.