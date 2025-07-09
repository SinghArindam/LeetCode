Here is a set of atomic notes for LeetCode problem 189-rotate-array, formatted for spaced repetition learning:

---

-   **Concept**: Problem Goal - Rotate Array
    -   **Context**: Given an integer array `nums` and a non-negative integer `k`.
    -   **Example**: Rotate `nums` to the right by `k` steps.

-   **Concept**: In-place Modification Requirement
    -   **Context**: The problem explicitly requires modifying the input array `nums` directly.
    -   **Example**: Do not return a new array; `nums` should be changed.

-   **Concept**: Optimal Space Complexity Goal
    -   **Context**: A follow-up question specifically asks for an `O(1)` extra space solution.
    -   **Example**: Achieved by the Three-Reversal Trick or Cyclic Replacements, unlike Python slicing which uses `O(N)`.

-   **Concept**: Brute-Force Approach (Repeated Single Rotation)
    -   **Context**: Simulates rotation `k` times, each time moving the last element to the front and shifting others right.
    -   **Example**: `nums = [1,2,3], k=1`. `temp=3`. Shift `[1,2]` to `[_,1,2]`. Place `temp`: `[3,1,2]`. Repeat for `k` steps.

-   **Concept**: Brute-Force Time Complexity
    -   **Context**: For the repeated single rotation approach.
    -   **Example**: `O(N * k)`. If `k` is close to `N`, this becomes `O(N^2)`, which is inefficient.

-   **Concept**: Brute-Force Space Complexity
    -   **Context**: For the repeated single rotation approach.
    -   **Example**: `O(1)` because only a single temporary variable is used per step.

-   **Concept**: Extra Array Approach
    -   **Context**: Create a new auxiliary array to place elements at their correct rotated positions, then copy back.
    -   **Example**: For `nums[i]`, its new position is `(i + k) % n`. Copy `nums[i]` to `rotated_nums[(i+k)%n]`.

-   **Concept**: Extra Array Time Complexity
    -   **Context**: For the approach using an auxiliary array.
    -   **Example**: `O(N)` (one pass to fill, one pass to copy back).

-   **Concept**: Extra Array Space Complexity
    -   **Context**: For the approach using an auxiliary array.
    -   **Example**: `O(N)` because an auxiliary array of the same size `N` is created.

-   **Concept**: Python Slicing Approach
    -   **Context**: Leverages Python's concise list slicing and concatenation to perform rotation.
    -   **Example**: `nums[:] = nums[-k:] + nums[:-k]`.

-   **Concept**: Python Slicing Time Complexity
    -   **Context**: For the Python slicing approach.
    -   **Example**: `O(N)` (slicing and concatenation operations are proportional to list length).

-   **Concept**: Python Slicing Space Complexity
    -   **Context**: For the Python slicing approach.
    -   **Example**: `O(N)` because slicing creates new temporary lists, and concatenation creates another new list of size `N`. Not truly `O(1)` space.

-   **Concept**: Modulo Arithmetic for `k`
    -   **Context**: Always apply `k = k % n` at the beginning of rotation problems.
    -   **Example**: If `nums.length = 7` and `k = 10`, `k` becomes `10 % 7 = 3`. If `k=7`, `k` becomes `7 % 7 = 0`. Handles `k > n` and `k` being a multiple of `n`.

-   **Concept**: In-place Reversal (Three-Reversal Trick)
    -   **Context**: The most common and elegant `O(1)` space approach for array rotation.
    -   **Example**: 1. Reverse entire array. 2. Reverse first `k` elements. 3. Reverse remaining `n-k` elements.

-   **Concept**: Three-Reversal Trick Step 1: Reverse Entire Array
    -   **Context**: The first step in the optimal in-place reversal algorithm.
    -   **Example**: `[1,2,3,4,5,6,7]` becomes `[7,6,5,4,3,2,1]`. This places elements destined for the beginning (e.g., `5,6,7`) at the beginning (but reversed), and vice-versa.

-   **Concept**: Three-Reversal Trick Step 2: Reverse First `k` Elements
    -   **Context**: The second step in the optimal in-place reversal algorithm, applied to the initial `k` elements after the full array reversal.
    -   **Example**: Given `[7,6,5,4,3,2,1]` and `k=3`, reverse `[7,6,5]` to `[5,6,7]`. Array becomes `[5,6,7,4,3,2,1]`. This correctly orders the first part of the rotated array.

-   **Concept**: Three-Reversal Trick Step 3: Reverse Remaining `n-k` Elements
    -   **Context**: The third step in the optimal in-place reversal algorithm, applied to the elements from index `k` to `n-1` after the previous reversals.
    -   **Example**: Given `[5,6,7,4,3,2,1]` and `n-k=4`, reverse `[4,3,2,1]` to `[1,2,3,4]`. Array becomes `[5,6,7,1,2,3,4]`. This correctly orders the second part.

-   **Concept**: In-place Reversal Time Complexity
    -   **Context**: For the three-reversal trick.
    -   **Example**: `O(N)` because each element is swapped a constant number of times across the three reversals.

-   **Concept**: In-place Reversal Space Complexity
    -   **Context**: For the three-reversal trick.
    -   **Example**: `O(1)` because only a few pointers and temporary variables are used for swapping, no auxiliary data structure scaled with `N`.

-   **Concept**: Cyclic Replacements Approach
    -   **Context**: An alternative `O(1)` space approach that directly places elements into their final positions by following cycles.
    -   **Example**: Start a cycle at index `start`. Move `nums[start]` to `(start+k)%n`, then the value at `(start+k)%n` to `((start+k)%n + k)%n`, and so on, until the cycle returns to `start`. Repeat for `gcd(n, k)` cycles.

-   **Concept**: Cyclic Replacements Time Complexity
    -   **Context**: For the cyclic replacements approach.
    -   **Example**: `O(N)` because each element is visited and moved exactly once.

-   **Concept**: Cyclic Replacements Space Complexity
    -   **Context**: For the cyclic replacements approach.
    -   **Example**: `O(1)` because only a few temporary variables are used.

-   **Concept**: In-place Swapping Pattern
    -   **Context**: Fundamental operation for `O(1)` space array modifications like reversal.
    -   **Example**: `arr[start], arr[end] = arr[end], arr[start]`.

-   **Concept**: Python `nums[:] = new_list` vs. `nums = new_list`
    -   **Context**: Understanding how to modify a list's content in-place in Python.
    -   **Example**: `nums[:] = new_list` replaces the *contents* of the original `nums` list. `nums = new_list` would rebind the `nums` variable to a *new list object*, not modifying the original object.

-   **Concept**: Edge Case: `k = 0` or `k` is a multiple of `n`
    -   **Context**: These scenarios mean no effective rotation is needed.
    -   **Example**: Handled correctly by `k = k % n`, which results in `k = 0`. Solutions often have an early exit if `k` is 0 after modulo.

-   **Concept**: Edge Case: `nums.length = 1`
    -   **Context**: A single-element array.
    -   **Example**: `k = k % 1` will always result in `k = 0`, meaning no rotation, which is correct. Most solutions handle this implicitly or with an early exit if `n <= 1`.

-   **Concept**: Constraint on `nums.length`
    -   **Context**: The problem states `1 <= nums.length`.
    -   **Example**: An empty array (`nums.length = 0`) is not a valid input, so explicit checks for `n=0` are not strictly necessary per constraints.

-   **Concept**: Problem Decomposition as a Strategy
    -   **Context**: Breaking down a complex array manipulation (like rotation) into a series of simpler, well-understood operations (like reversal).
    -   **Example**: The three-reversal trick is a prime example of this strategy.