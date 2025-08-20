Here is a set of atomic notes for LeetCode problem 135-candy, structured for spaced repetition:

---

**Problem: LeetCode 135 - Candy**

- **Concept**: Problem Goal
- **Context**: Distribute the minimum total candies to children in a line based on their ratings.
- **Example**: Find minimum total candies for `ratings = [1,0,2]`.

- **Concept**: Rule 1: Minimum Candies
- **Context**: Every child must receive at least one candy.
- **Example**: Initializing a `candies` array with `[1, 1, ..., 1]` satisfies this.

- **Concept**: Rule 2: Higher Rating, More Candies
- **Context**: A child with a higher rating must receive strictly more candies than their immediate neighbors (left and right).
- **Example**: If `ratings[i] > ratings[i-1]`, then `candies[i] > candies[i-1]`.

- **Concept**: Problem Constraints (N)
- **Context**: The number of children `n` can be up to `2 * 10^4`. This implies O(N) or O(N log N) solutions are preferred.
- **Example**: For `n = 20000`, an O(N^2) solution would be too slow.

- **Concept**: Problem Constraints (Ratings)
- **Context**: Ratings are non-negative, ranging from `0` to `2 * 10^4`. This doesn't directly impact algorithm choice but defines input value range.

- **Concept**: Two-Pass Iterative Dynamic Programming (General Principle)
- **Context**: A common technique for problems with bidirectional dependencies (e.g., a child's candy count depends on both left and right neighbors).
- **Example**: Apply one pass L-R, then another R-L to satisfy all conditions.

- **Concept**: Two-Pass Iterative DP: Initialization
- **Context**: The first step in two-pass iterative DP solutions for this problem.
- **Example**: Create a `candies` array of size `n` and initialize all elements to `1`. `candies = [1, 1, 1]` for `n=3`.

- **Concept**: Two-Pass Iterative DP: Left-to-Right Pass
- **Context**: Ensures the condition `ratings[i] > ratings[i-1]` leads to `candies[i] > candies[i-1]`.
- **Example**: If `ratings[i] > ratings[i-1]`, set `candies[i] = candies[i-1] + 1`.

- **Concept**: Two-Pass Iterative DP: Right-to-Left Pass (Crucial Max Operation)
- **Context**: Ensures the condition `ratings[i] > ratings[i+1]` leads to `candies[i] > candies[i+1]`, while respecting prior L-R adjustments.
- **Example**: If `ratings[i] > ratings[i+1]`, set `candies[i] = max(candies[i], candies[i+1] + 1)`. The `max` is vital.

- **Concept**: Time Complexity of Two-Pass Iterative DP
- **Context**: Analyzing the efficiency of the common two-pass approach.
- **Example**: O(N) because it involves a constant number of linear passes (initialization, L-R, R-L, sum).

- **Concept**: Space Complexity of Two-Pass Iterative DP
- **Context**: Analyzing the memory usage of the common two-pass approach.
- **Example**: O(N) for storing the `candies` array. (Whether one or two arrays are used for intermediate results, total is O(N)).

- **Concept**: Recursive Dynamic Programming with Memoization
- **Context**: An alternative O(N) time/space approach that breaks down the problem into subproblems defined by directional dependencies.
- **Example**: Define `get_left_candies(i)` and `get_right_candies(i)` functions.

- **Concept**: `get_left_candies(i)` in Recursive DP
- **Context**: Computes minimum candies for child `i` considering only its left neighbor.
- **Example**: If `ratings[i] > ratings[i-1]`, result is `1 + get_left_candies(i-1)`; otherwise `1`.

- **Concept**: `get_right_candies(i)` in Recursive DP
- **Context**: Computes minimum candies for child `i` considering only its right neighbor.
- **Example**: If `ratings[i] > ratings[i+1]`, result is `1 + get_right_candies(i+1)`; otherwise `1`.

- **Concept**: Combining Results in Recursive DP
- **Context**: To satisfy both left and right neighbor conditions for a child `i`.
- **Example**: `candies_for_i = max(get_left_candies(i), get_right_candies(i))`.

- **Concept**: `sys.setrecursionlimit` in Python for Recursive DP
- **Context**: Necessary for deeply recursive solutions in Python to prevent "RecursionError: maximum recursion depth exceeded" when `N` is large.
- **Example**: `sys.setrecursionlimit(2 * 10**4 + 5)` for `N` up to `2 * 10^4`.

- **Concept**: O(1) Space Optimization (Slope Tracking)
- **Context**: An advanced, more complex approach to solve the problem with minimal auxiliary space.
- **Example**: Achieves O(1) space by carefully tracking increasing/decreasing slope lengths without extra arrays.

- **Concept**: BFS/Queue-based Approach
- **Context**: Views the problem as propagating candy counts from "local minima" (valleys) outwards.
- **Example**: Initialize local minima with 1 candy, add to queue, then spread candies to higher-rated neighbors.

- **Concept**: Sorting by Rating Approach
- **Context**: Processes children in increasing order of their ratings.
- **Example**: Create `(rating, index)` pairs, sort them, then iterate and update `candies[index]` based on neighbors.

- **Concept**: Time Complexity of Sorting by Rating Approach
- **Context**: Analyzing efficiency if sorting is used.
- **Example**: O(N log N) due to the sorting step, making it less optimal than O(N) DP solutions.

- **Concept**: Greedy Local Decisions leading to Global Optimality
- **Context**: Incrementing candies by 1 based on a higher rating, when combined with two-pass or `max` strategies, accumulates to the overall minimum.
- **Example**: Giving `candies[i-1] + 1` to `candies[i]` for `ratings[i] > ratings[i-1]` is a local greedy choice.

- **Concept**: Handling Equal Ratings
- **Context**: When `ratings[i] == ratings[i-1]`, it breaks a "greater than neighbor" chain.
- **Example**: Children with equal ratings typically only need 1 candy from that specific side, as no "strictly greater" condition applies.

- **Concept**: Edge Case: `n = 1` (Single Child)
- **Context**: How solutions behave with only one child.
- **Example**: The child correctly receives 1 candy (due to initialization or base cases).

- **Concept**: Edge Case: All Same Ratings
- **Context**: `ratings = [2,2,2]`.
- **Example**: Each child correctly receives 1 candy; the "higher rating" rule is never met.

- **Concept**: Edge Case: Strictly Increasing Ratings
- **Context**: `ratings = [1,2,3,4,5]`.
- **Example**: Candies `[1,2,3,4,5]`. The L-R pass handles this, R-L makes no further changes.

- **Concept**: Edge Case: Strictly Decreasing Ratings
- **Context**: `ratings = [5,4,3,2,1]`.
- **Example**: Candies `[5,4,3,2,1]`. The L-R pass initializes to 1s; the R-L pass propagates the correct counts.

- **Concept**: Edge Case: V-Shape Ratings
- **Context**: `ratings = [3,2,1,2,3]`.
- **Example**: Candies `[3,2,1,2,3]`. The valley child gets 1, and values increase outwards from both sides.

- **Concept**: Edge Case: A-Shape Ratings
- **Context**: `ratings = [1,2,3,2,1]`.
- **Example**: Candies `[1,2,3,2,1]`. The peak child correctly receives `max` from its left and right conditions.