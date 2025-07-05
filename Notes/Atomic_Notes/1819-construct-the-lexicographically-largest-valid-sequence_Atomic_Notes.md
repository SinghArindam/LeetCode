Here is a set of atomic notes for LeetCode problem 1819, formatted for spaced repetition learning:

---

-   **Concept**: Problem Goal - Sequence Construction
    -   **Context**: LeetCode 1819 asks to build a sequence of integers of a specific length, `2*n - 1`.
    -   **Example**: For `n=3`, the sequence length is `2*3-1 = 5`.

-   **Concept**: Rule for Number 1 Occurrence
    -   **Context**: The integer `1` must appear exactly once in the constructed sequence.
    -   **Example**: In the valid sequence `[3,1,2,3,2]` for `n=3`, `1` appears at index 1.

-   **Concept**: Rule for Numbers 2 to `n` Occurrences
    -   **Context**: Each integer `i` from `2` to `n` must appear exactly twice in the constructed sequence.
    -   **Example**: For `n=3`, numbers `2` and `3` each appear twice in `[3,1,2,3,2]`.

-   **Concept**: Rule for Distance between Paired Occurrences
    -   **Context**: For every integer `i` between `2` and `n`, the absolute difference between the indices of its two occurrences (its "distance") must be exactly `i`.
    -   **Example**: In `[3,1,2,3,2]`, `3` is at index 0 and 3 (distance `|3-0|=3`). `2` is at index 2 and 4 (distance `|4-2|=2`).

-   **Concept**: Output Requirement - Lexicographically Largest
    -   **Context**: The problem requires returning the valid sequence that is lexicographically largest. This means trying larger numbers at earlier positions.
    -   **Example**: `[3,1,2,3,2]` is lexicographically larger than `[2,3,1,2,3]` because `3 > 2` at the first differing position (index 0).

-   **Concept**: Constraints on `n`
    -   **Context**: The input integer `n` is constrained to `1 <= n <= 20`. This range often suggests that an exponential time complexity solution with significant pruning might be acceptable.

-   **Concept**: Solution Existence Guarantee
    -   **Context**: The problem statement guarantees that a valid solution always exists under the given constraints. This simplifies the backtracking logic as we don't need to handle "no solution" cases.

-   **Concept**: Core Algorithmic Approach - Backtracking
    -   **Context**: A recursive backtracking (Depth-First Search) algorithm is the optimal approach to construct the sequence by filling positions one by one.
    -   **Example**: The `backtrack(index, n)` function attempts to fill `res[index]`.

-   **Concept**: Greedy Choice for Lexicographical Order
    -   **Context**: To ensure the first valid solution found is lexicographically largest, at each empty position (`index`), the algorithm attempts to place numbers `i` from `n` **down to `1`** (largest first).

-   **Concept**: Backtracking State - `res` Vector
    -   **Context**: A `std::vector<int>` (e.g., `res`) is used to store the sequence being built. It's initialized with a placeholder (e.g., `0`) for empty slots.
    -   **Example**: `res.assign(size, 0);` to create a vector of `size` zeros.

-   **Concept**: Backtracking State - `used` Vector
    -   **Context**: A `std::vector<bool>` (e.g., `used`) tracks which numbers `i` (from `1` to `n`) have already been fully placed in the sequence (either `1` once, or both occurrences of `i > 1`).
    -   **Example**: `used[i] = true;` after `i` is placed.

-   **Concept**: Backtracking Base Case (Success Condition)
    -   **Context**: The recursive backtracking function returns `true` when the `index` has reached the end of the sequence, indicating all positions are successfully filled and a valid sequence has been found.
    -   **Example**: `if (index == res.size()) { return true; }`

-   **Concept**: Optimization - Skipping Already Filled Positions
    -   **Context**: If the current position `res[index]` is already non-zero (meaning it was filled as the second occurrence of a number placed earlier), the algorithm skips choice exploration for this position and moves directly to the next.
    -   **Example**: `if (res[index] != 0) { return backtrack(index + 1, n); }`

-   **Concept**: Pruning - Checking if Number is Already Used
    -   **Context**: Before attempting to place a number `i` at `index`, the algorithm checks if `i` has already been fully placed (`used[i]`). If so, it skips this choice, reducing redundant exploration.
    -   **Example**: `if (used[i]) { continue; }`

-   **Concept**: Placement Logic for Number 1
    -   **Context**: If the number being considered is `1`, it only occupies the current `res[index]` position and does not require a second paired spot.
    -   **Example**: `res[index] = 1;`

-   **Concept**: Placement Logic for Numbers `i > 1`
    -   **Context**: If the number being considered is `i > 1`, it must occupy two positions: the current `res[index]` and `res[index + i]` (the second occurrence at distance `i`).
    -   **Example**: `res[index] = i; res[index + i] = i;`

-   **Concept**: Pruning - Bounds Check for Second Occurrence
    -   **Context**: When placing a number `i > 1`, the algorithm verifies that the required second position `index + i` is within the sequence bounds (`res.size()`). Invalid placements are skipped.
    -   **Example**: `index + i < res.size()` is a necessary condition.

-   **Concept**: Pruning - Availability Check for Second Occurrence
    -   **Context**: When placing a number `i > 1`, the algorithm verifies that the required second position `res[index + i]` is currently empty (contains `0`). Invalid placements are skipped.
    -   **Example**: `res[index + i] == 0` is a necessary condition.

-   **Concept**: Backtracking (Undoing Choices)
    -   **Context**: If a recursive call from a particular choice `i` does not lead to a valid solution, the algorithm "undoes" that choice by resetting the occupied positions in `res` to `0` and marking `i` as unused, allowing other choices to be explored.
    -   **Example**: `res[index] = 0; if (i != 1) res[index + i] = 0; used[i] = false;`

-   **Concept**: Time Complexity of Backtracking Solution
    -   **Context**: The time complexity is exponential with `N`, but highly optimized by pruning techniques. It is efficient enough for `N=20`.
    -   **Example**: It's much faster than `O((2N-1)!)` or `O(N^(2N-1))`.

-   **Concept**: Space Complexity of Backtracking Solution
    -   **Context**: The space complexity is `O(N)` for storing the `res` vector, the `used` vector, and the recursion stack depth.
    -   **Example**: `res` is `O(2N-1)`, `used` is `O(N+1)`, recursion stack is `O(2N-1)`.

-   **Concept**: Handling `n = 1` Edge Case
    -   **Context**: For `n=1`, the sequence length is `1`, and the only number to place is `1`. The algorithm correctly handles this by placing `1` at `res[0]`, resulting in `[1]`.

-   **Concept**: General Pattern - Backtracking for Generation Problems
    -   **Context**: Backtracking is a standard and powerful technique for problems involving the generation of sequences, permutations, or combinations that must satisfy specific constraints.
    -   **Example**: Useful for Sudoku solvers, N-Queens problem, solving mazes.

-   **Concept**: General Pattern - Optimizing for Lexicographical Order
    -   **Context**: To find the lexicographically largest (or smallest) sequence, always prioritize choices in a specific order (e.g., largest values first for largest sequence, smallest values first for smallest sequence) at each step of the backtracking.

-   **Concept**: General Pattern - Importance of Effective Pruning
    -   **Context**: For exponential algorithms like backtracking, implementing rigorous validity checks (bounds, availability, `used` flags) *before* making a choice and recursing is critical for performance by significantly reducing the search space.

-   **Concept**: General Pattern - Problems with Paired Placements & Distance Constraints
    -   **Context**: This problem's requirement for numbers `i > 1` to occupy two specific positions (`k` and `k+i`) is a common pattern. It necessitates careful multi-position checks and synchronized state updates during backtracking.

-   **Concept**: General Pattern - `N` Constraint as a Hint
    -   **Context**: In competitive programming, a relatively small `N` (e.g., `N <= 20` or `N <= 15`) often suggests that an exponential time complexity solution (like backtracking or state-space DP) with effective pruning will pass within time limits.