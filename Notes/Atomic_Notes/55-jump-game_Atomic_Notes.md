Here's a set of atomic notes for LeetCode problem 55-jump-game, suitable for spaced repetition:

-   **Concept**: LeetCode 55: Jump Game Goal
    -   **Context**: Determine if it's possible to reach the **last index** of an array `nums`.
    -   **Example**: Start at `index 0`, `nums[i]` is your maximum jump length from `i`.

-   **Concept**: Jump Game: `nums[i]` meaning
    -   **Context**: Each element `nums[i]` represents the *maximum* jump length possible from `index i`.
    -   **Example**: If `nums[i] = 3`, you can jump 1, 2, or 3 steps forward from `i`.

-   **Concept**: Brute Force (Recursion) for Jump Game
    -   **Context**: Recursively try all possible jump lengths from the current position until the end is reached or all paths exhausted.
    -   **Example**: From `index i`, recursively call for `i+1`, `i+2`, ..., `i+nums[i]`.

-   **Concept**: Base Case: Reaching Last Index (Recursive Jump Game)
    -   **Context**: In a recursive solution, if the `current_index` is the last index (`n-1`), return `True`.

-   **Concept**: Base Case: Invalid Jump (Recursive Jump Game)
    -   **Context**: In a recursive solution, if the `current_index` goes beyond the array's bounds (`n-1`), return `False`.

-   **Concept**: Dynamic Programming (Top-Down with Memoization) for Jump Game
    -   **Context**: Improve brute-force recursion by storing results of subproblems (`memo[i]`) to avoid redundant calculations.
    -   **Example**: `memo[i]` stores `True/False` if the last index is reachable from `i`.

-   **Concept**: Dynamic Programming (Bottom-Up) for Jump Game
    -   **Context**: Iterate backwards from the last index, marking indices as "good" (can reach end) or "bad" (cannot).
    -   **Example**: `dp[n-1] = True`; for `i` from `n-2` down to `0`, `dp[i]` is `True` if any `dp[j]` (where `j` is reachable from `i`) is `True`.

-   **Concept**: Bottom-Up DP Initialization (Jump Game)
    -   **Context**: Initialize `dp[n-1] = True` as the last index is always reachable from itself.

-   **Concept**: Optimal Approach: Greedy Strategy (Jump Game)
    -   **Context**: The most efficient solution involves tracking `farthest_reach`, the maximum index reachable from `index 0` so far.
    -   **Example**: Continuously update `farthest_reach = max(farthest_reach, i + nums[i])`.

-   **Concept**: Greedy: Unreachable Current Index Check
    -   **Context**: If the current index `i` becomes greater than `farthest_reach`, it means `i` cannot be reached from previous positions, so the last index is unreachable.
    -   **Example**: `if i > farthest_reach: return False`.

-   **Concept**: Greedy: Updating `farthest_reach`
    -   **Context**: At each position `i`, calculate the furthest possible jump (`i + nums[i]`) and update `farthest_reach` to the maximum of its current value and this new potential reach.
    -   **Example**: `farthest_reach = max(farthest_reach, i + nums[i])`.

-   **Concept**: Greedy: Early Exit on Success
    -   **Context**: If `farthest_reach` reaches or surpasses the last index (`n - 1`), it signifies that the end is reachable, allowing an immediate `True` return.
    -   **Example**: `if farthest_reach >= n - 1: return True`.

-   **Concept**: Greedy: Loop Completion Implies Success
    -   **Context**: If the greedy algorithm iterates through the entire array without `i` exceeding `farthest_reach` and without an early `True` return, it implies the last index was reachable.
    -   **Example**: Covers cases like `nums = [0]` (n=1) or if `farthest_reach` precisely hits `n-1` at the very end.

-   **Concept**: Brute Force Jump Game Time Complexity
    -   **Context**: O(2^N) in the worst case due to exponential branching of recursive calls.

-   **Concept**: Brute Force Jump Game Space Complexity
    -   **Context**: O(N) due to the depth of the recursion call stack.

-   **Concept**: DP (Top-Down/Bottom-Up) Jump Game Time Complexity
    -   **Context**: O(N * MaxJumpLength), which can be O(N^2) in the worst case where `MaxJumpLength` is proportional to `N`.

-   **Concept**: DP (Top-Down/Bottom-Up) Jump Game Space Complexity
    -   **Context**: O(N) for the memoization table or DP array.

-   **Concept**: Greedy Approach Jump Game Time Complexity
    -   **Context**: O(N) because it involves a single pass through the array, performing constant time operations per element.

-   **Concept**: Greedy Approach Jump Game Space Complexity
    -   **Context**: O(1) as it uses only a few constant extra variables.

-   **Concept**: Edge Case: Array Length 1 (`nums.length == 1`)
    -   **Context**: Handled by greedy approach: `n-1` is `0`, and `farthest_reach` (initialized to `0`) immediately satisfies `0 >= 0`.
    -   **Example**: `nums = [0]` or `nums = [5]` correctly returns `True`.

-   **Concept**: Edge Case: Zero Jumps Trapping
    -   **Context**: Handled by `if i > farthest_reach: return False`. If `nums[i]=0` creates an impassable gap, `i` will eventually exceed `farthest_reach`.
    -   **Example**: `nums = [3,2,1,0,4]` correctly returns `False`.

-   **Concept**: Greedy Algorithm for Reachability
    -   **Context**: Jump Game is a classic example where making locally optimal choices (maximizing current reach) leads to a globally optimal solution for range coverage or target reachability problems.

-   **Concept**: "Maximum Reach" Thinking Pattern
    -   **Context**: A common algorithmic pattern used to solve problems involving covering a range or reaching a target by continually extending the furthest boundary reachable.

-   **Concept**: Early Exit Conditions in Greedy Algorithms
    -   **Context**: Crucial for efficiency; returning `True` as soon as the goal is guaranteed or `False` if failure is confirmed avoids unnecessary computations.