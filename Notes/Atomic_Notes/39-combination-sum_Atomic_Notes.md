Here is a set of atomic notes for LeetCode problem 39-combination-sum, based on the provided comprehensive and short notes:

---

-   **Concept**: Problem Goal
    *   **Context**: Given an array of **distinct** integers `candidates` and a `target` integer. Find all **unique combinations** of `candidates` where the chosen numbers sum up to `target`.
    *   **Example**: `candidates = [2,3,6,7], target = 7` -> `Output: [[2,2,3],[7]]`

-   **Concept**: Unlimited Item Usage
    *   **Context**: A key characteristic of "Combination Sum" (LeetCode 39) is that numbers from `candidates` can be chosen an **unlimited number of times**.
    *   **Example**: To sum to 7, `2` can be used multiple times (`[2,2,3]`).

-   **Concept**: Combination Uniqueness (Order Irrelevant)
    *   **Context**: Combinations are considered unique if the frequency of at least one number is different. The order of numbers within a combination does not matter for uniqueness.
    *   **Example**: `[2,3,2]` is considered the same as `[2,2,3]`.

-   **Concept**: Backtracking Algorithm Core
    *   **Context**: Backtracking is a recursive algorithmic technique used for solving combinatorial search problems. It builds solutions incrementally, and "backtracks" (undoes choices) when a partial solution cannot lead to a valid final solution.
    *   **Example**: Typically involves maintaining a `current_combination` list, adding/removing elements (`append`/`pop`), and making recursive calls.

-   **Concept**: Backtracking `start_index` for Uniqueness
    *   **Context**: To prevent duplicate combinations (permutations, e.g., `[2,3]` and `[3,2]`), a `start_index` parameter is passed to the recursive backtracking calls. This ensures numbers are picked in a non-decreasing order of their original indices.
    *   **Example**: The `for` loop for choices starts from `start_index`, and `i` (the current loop index) is passed to the next recursive call (`backtrack(i, ...)`).

-   **Concept**: Backtracking for Unlimited Item Usage
    *   **Context**: To allow a candidate number `candidates[i]` to be reused multiple times in a combination, the recursive call passes the *current index* (`i`) as the `start_index` for the next recursion level.
    *   **Example**: `backtrack(i, current_combination + [num], current_sum + num)`.

-   **Concept**: Backtracking Pruning via Sorting
    *   **Context**: Sorting the `candidates` array in ascending order is a crucial optimization for backtracking. It enables efficient early pruning of invalid paths.
    *   **Example**: If `candidates = [2,3,6,7]`, and `current_sum + 6` already exceeds `target`, then `current_sum + 7` will also exceed `target`.

-   **Concept**: Backtracking Early Pruning Condition
    *   **Context**: After sorting `candidates`, use `if current_sum + candidates[i] > target: break` inside the `for` loop that iterates through choices.
    *   **Example**: This `break` statement efficiently prunes the current path and all subsequent options at the same recursion level, as they would also exceed the target.

-   **Concept**: Backtracking Base Case (Success)
    *   **Context**: If the `current_sum` exactly equals the `target`, a valid combination has been found.
    *   **Example**: Append a *copy* of `current_combination` (`list(current_combination)`) to the `result` list and `return` to terminate this specific recursive path.

-   **Concept**: Backtracking Step (Undo Choice)
    *   **Context**: After a recursive call returns (meaning all possibilities from that choice have been explored), `current_combination.pop()` is used to remove the last added number.
    *   **Example**: This "undoes" the choice, allowing the algorithm to explore other candidate numbers at the current recursion level's loop.

-   **Concept**: Dynamic Programming Core Idea
    *   **Context**: A bottom-up approach that builds solutions for larger sums by leveraging already computed solutions for smaller sums. It stores intermediate results to avoid redundant calculations.
    *   **Example**: `dp[i]` stores all combinations that sum to `i`.

-   **Concept**: DP Table Initialization
    *   **Context**: A `dp` array is created where `dp[i]` will store lists of unique combinations that sum up to `i`. The base case `dp[0]` is initialized as `[[]]` (one way to make sum 0 is with an empty combination).
    *   **Example**: `dp = [[] for _ in range(target + 1)]; dp[0] = [[]]`.

-   **Concept**: DP Loop Order for Uniqueness & Unlimited Use
    *   **Context**: The specific order of loops in DP is crucial for correct unique combinations with unlimited item usage: outer loop iterates through `candidates` (`for num in candidates`), and the inner loop iterates through sums from `num` up to `target` (`for i in range(num, target + 1)`).
    *   **Example**: This order ensures combinations are built in a canonical way (e.g., `[2,3]` is formed, but `[3,2]` is not) and allows `num` to be added multiple times.

-   **Concept**: DP Combination Building
    *   **Context**: For each `num` and sum `i`, new combinations for `dp[i]` are formed by taking existing `combo`s from `dp[i - num]` and appending the current `num`.
    *   **Example**: `for combo in dp[i - num]: dp[i].append(combo + [num])`.

-   **Concept**: Backtracking Time Complexity
    *   **Context**: The theoretical worst-case time complexity is exponential (roughly `O(N^(target / min_candidate))`), but due to effective pruning (sorting + `break`), it is highly efficient and practical for the given constraints.
    *   **Example**: For `candidates=[1], target=40`, the depth is 40.

-   **Concept**: Backtracking Space Complexity
    *   **Context**: The space complexity is `O(M + K * M)`, where `M` is the maximum length of a combination (representing recursion stack depth), and `K` is the total number of valid combinations stored in the result list.
    *   **Example**: `M` can be up to `target / min(candidates)`.

-   **Concept**: Dynamic Programming Time Complexity
    *   **Context**: The time complexity is `O(N * T * K_max_intermediate * M)`, where `N` is `len(candidates)`, `T` is `target`, `K_max_intermediate` is the maximum number of combinations for any intermediate sum `i <= target`, and `M` is the maximum combination length.
    *   **Example**: Generally polynomial, but can be slower than highly optimized backtracking for small output sizes due to constant factors.

-   **Concept**: Dynamic Programming Space Complexity
    *   **Context**: The space complexity is `O(T * K_max_intermediate * M)`, as the `dp` table stores lists of combinations for all sums from `0` up to `target`.
    *   **Example**: The `dp` array holds many intermediate combination lists.

-   **Concept**: Edge Case: `target < min(candidates)`
    *   **Context**: This occurs when the target sum is smaller than the smallest number available in `candidates`.
    *   **Example**: `candidates = [5,6], target = 3`. Both Backtracking and Dynamic Programming approaches correctly result in an empty list `[]` as no combination can be formed.

-   **Concept**: General Pattern: Pruning Search Space
    *   **Context**: A critical optimization technique for exponential search algorithms like backtracking, involving cutting off invalid or redundant branches early to improve efficiency.
    *   **Example**: `if current_sum > target: return` (general check) or `if current_sum + num > target: break` (with sorting).