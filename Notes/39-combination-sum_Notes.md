This document provides a comprehensive analysis of the LeetCode problem "Combination Sum", including a problem summary, various solution approaches from naive to optimized, detailed explanations, complexity analysis, edge case discussions, a well-commented optimal solution, and key insights.

---

### 1. Problem Summary

**Problem Title:** Combination Sum

**Problem Statement:**
Given an array of **distinct** integers `candidates` and a target integer `target`, the task is to find all **unique combinations** of `candidates` where the chosen numbers sum up to `target`.
Key characteristics:
*   Numbers from `candidates` can be chosen an **unlimited number of times**.
*   Combinations are unique if the frequency of at least one number is different (e.g., `[2,2,3]` is different from `[7]`, and `[2,3,2]` is considered the same as `[2,2,3]`).
*   The order of numbers within a combination does not matter for uniqueness (e.g., `[2,3,2]` is the same as `[2,2,3]`).
*   The output list of combinations can be in any order.

**Constraints:**
*   `1 <= candidates.length <= 30`
*   `2 <= candidates[i] <= 40`
*   All elements of `candidates` are **distinct**.
*   `1 <= target <= 40`

**Examples:**
*   **Example 1:** `candidates = [2,3,6,7], target = 7`
    *   `Output: [[2,2,3],[7]]`
    *   Explanation: `2 + 2 + 3 = 7`, and `7 = 7`.
*   **Example 2:** `candidates = [2,3,5], target = 8`
    *   `Output: [[2,2,2,2],[2,3,3],[3,5]]`
*   **Example 3:** `candidates = [2], target = 1`
    *   `Output: []`

---

### 2. Explanation of All Possible Approaches

This problem is a classic combinatorial search problem, often solvable using Backtracking or Dynamic Programming. The provided solution code snippet explores several approaches.

#### Approach 1: Brute-force with `itertools.combinations_with_replacement`

*   **Concept:** This approach leverages Python's `itertools.combinations_with_replacement` function. Since numbers can be used an unlimited number of times, this function is suitable. The challenge is that we don't know the length of the combination beforehand. We can estimate a `max_len` (e.g., `target // min(candidates) + 1`) and then iterate through all possible lengths from 1 up to `max_len`. For each length, generate all combinations with replacement, sum them up, and if the sum equals `target`, add it to the result.
*   **Suitability:** Simple to implement due to `itertools`. However, it generates many combinations that won't sum to the target, leading to inefficiency.
*   **Code Sketch (from provided solution):**
    ```python
    # result = []
    # if not candidates: return [] # Redundant due to constraints
    # max_len = target // min(candidates) + 1
    # for length in range(1, max_len):
    #     for combo in itertools.combinations_with_replacement(candidates, length):
    #         if sum(combo) == target:
    #             result.append(list(combo))    
    # return result
    ```

#### Approach 2: Backtracking (Basic)

*   **Concept:** Backtracking is a recursive algorithm that builds a solution incrementally. If a partial solution cannot be completed to a valid solution, it "backtracks" to an earlier state by undoing the last choice and trying another.
*   For this problem:
    *   We maintain a `current_combination` list and `current_sum`.
    *   At each step, we iterate through the `candidates` array.
    *   To avoid duplicate combinations (e.g., `[2,3]` and `[3,2]`), we use a `start_index`. When considering `candidates[i]`, we only consider elements from `candidates[i]` onwards for the next recursive call. This implicitly handles the order.
    *   Since a number can be used multiple times, the next recursive call for `candidates[i]` starts again from `index i`, not `i+1`.
    *   **Base Cases:**
        *   If `current_sum == target`: A valid combination is found. Add a copy of `current_combination` to the result.
        *   If `current_sum > target`: This path is invalid. Prune it.
*   **Code Sketch (from provided solution):**
    ```python
    # result = []
    # def backtrack(start_index, combination, current_sum):
    #     if current_sum == target:
    #         result.append(list(combination))
    #         return
    #     if current_sum > target:
    #         return
    #     for i in range(start_index, len(candidates)):
    #         num = candidates[i]
    #         combination.append(num)
    #         backtrack(i, combination, current_sum + num) # 'i' allows reuse
    #         combination.pop() # Backtrack: remove last added number
    # backtrack(0, [], 0)
    # return result
    ```

#### Approach 3: Backtracking (Optimized with Sorting and Early Pruning) - **Optimal Backtracking**

*   **Concept:** This is an improvement over Approach 2.
    *   **Sorting `candidates`:** Sort the `candidates` array in ascending order. This allows for an important optimization.
    *   **Early Pruning:** If `current_sum + num` already exceeds `target`, then any subsequent numbers (which are larger, due to sorting) will also exceed `target`. Thus, we can `break` the loop, rather than just `return` (which would only stop the current branch). This significantly reduces unnecessary recursive calls.
*   **Suitability:** This is a highly efficient and commonly used approach for this type of problem. It's generally preferred for its performance and clarity.
*   **Code Sketch (from provided solution):**
    ```python
    # result = []
    # candidates.sort() # Key optimization: sort the candidates
    # def backtrack(start_index, combination, current_sum):
    #     if current_sum == target:
    #         result.append(list(combination))
    #         return
    #     # No need for `if current_sum > target` here because of the loop condition
    #     for i in range(start_index, len(candidates)):
    #         num = candidates[i]
    #         if current_sum + num > target: # Early pruning enabled by sorting
    #             break # All subsequent numbers will also be too large
    #         combination.append(num)
    #         backtrack(i, combination, current_sum + num) # 'i' allows reuse
    #         combination.pop() # Backtrack: remove last added number
    # backtrack(0, [], 0)
    # return result
    ```

#### Approach 4: Backtracking (Alternative Structure - Include/Exclude)

*   **Concept:** Another common backtracking pattern involves making two choices at each step for the current element:
    1.  **Include** the current `candidates[index]` in the combination: Make a recursive call with `index` unchanged (as the number can be used again) and updated `current_sum`.
    2.  **Exclude** the current `candidates[index]` from the combination: Make a recursive call with `index + 1` (moving to the next distinct number) and `current_sum` unchanged.
*   **Suitability:** While valid, for "unlimited use" problems, the `start_index` iteration (Approach 3) is often more intuitive and potentially performs better due to fewer redundant paths explored (it doesn't explicitly explore `[2]` then `[3]` after which it might re-add `2` if it was at `index+1` for `3`). This pattern is more typical for "each element can be used once" problems.
*   **Code Sketch (from provided solution):**
    ```python
    # result = []
    # def backtrack(index, combination, current_sum):
    #     if current_sum == target:
    #         result.append(list(combination))
    #         return
    #     if current_sum > target or index >= len(candidates): # Base cases for pruning/termination
    #         return
    #     
    #     # Option 1: Include candidates[index]
    #     combination.append(candidates[index])
    #     backtrack(index, combination, current_sum + candidates[index]) # Stay at index for reuse
    #     combination.pop() # Backtrack
    #     
    #     # Option 2: Exclude candidates[index]
    #     backtrack(index + 1, combination, current_sum) # Move to next candidate
    # backtrack(0, [], 0)
    # return result
    ```

#### Approach 5: Backtracking with Generators (Pythonic)

*   **Concept:** This is essentially Approach 3, but instead of appending to a `result` list directly, it `yield`s combinations as they are found. This is a Pythonic way to handle sequences, potentially saving memory if not all combinations are needed at once (though here, we convert to `list()` at the end, negating some memory benefits for the final output).
*   **Suitability:** Good for large numbers of combinations where you might process them one by one. Functionally similar to Approach 3 for this problem's requirements.
*   **Code Sketch (from provided solution):**
    ```python
    # def find_combinations(start_index, combination, current_sum):
    #     if current_sum == target:
    #         yield list(combination) # Yield a copy
    #         return
    #     if current_sum > target:
    #         return
    #     for i in range(start_index, len(candidates)):
    #         num = candidates[i]
    #         combination.append(num)
    #         yield from find_combinations(i, combination, current_sum + num) # Yield from nested calls
    #         combination.pop()
    # return list(find_combinations(0, [], 0))
    ```

#### Approach 6: Iterative Backtracking (using a Stack)

*   **Concept:** Converts the recursive backtracking (e.g., Approach 3's logic) into an iterative process using an explicit stack. Each element in the stack typically represents a state: `(start_index, current_combination, current_sum)`.
*   **Suitability:** Avoids recursion depth limits, but can be less intuitive to write and debug than recursive backtracking. The `combination + [num]` part in the `stack.append` creates new lists, which can be less memory efficient than modifying a single list and backtracking with `pop()` as in recursive versions.
*   **Code Sketch (from provided solution):**
    ```python
    # result = []
    # stack = [(0, [], 0)] # (start_index, current_combination, current_sum)
    # while stack:
    #     start_index, combination, current_sum = stack.pop() # DFS-like
    #     
    #     if current_sum > target:
    #         continue # Prune
    #     if current_sum == target:
    #         result.append(combination) # Found a combination
    #         continue
    #     
    #     # Explore next choices (in reverse order for correct DFS traversal with pop)
    #     # Note: Iterating from `len(candidates)-1` down to `start_index`
    #     # so that smaller numbers (which are processed first in recursion) are processed last by pop.
    #     # This isn't implicitly sorted as in the recursive version. If sorting is needed, sort candidates first.
    #     for i in range(start_index, len(candidates)): # Assumes candidates might be sorted externally
    #         num = candidates[i]
    #         stack.append((i, combination + [num], current_sum + num))
    # return result
    ```
    *Self-correction for Approach 6:* The `for i in range(start_index, len(candidates))` loop in the iterative version needs careful consideration with `stack.pop()`. If you iterate `0` to `N-1` and `pop` from the top, you're essentially doing DFS. The original recursive approach explores `candidates[start_index]` first. To mimic this, the `for` loop in iterative DFS needs to push elements onto the stack in reverse order of how they should be processed. If `candidates` are sorted, iterating `start_index` to `len-1` and pushing means `candidates[len-1]` is processed first. A `for i in range(len(candidates)-1, start_index-1, -1)` loop would ensure elements are processed in ascending order when popped. The provided code does `range(start_index, len(candidates))` which means the *last* candidate in that range will be pushed *last* onto the stack, and thus popped *first*. This is a valid DFS order, just different. The key pruning `if current_sum + num > target: break` would need `candidates.sort()` and the loop to be `for i in range(start_index, len(candidates)): ... if current_sum + num > target: break`.

#### Approach 7: Dynamic Programming (DP) - **Optimal DP**

*   **Concept:** This approach builds up solutions for smaller `target` values and uses them to construct solutions for larger `target` values.
*   We create a `dp` array where `dp[i]` stores a list of all unique combinations that sum up to `i`.
*   **Initialization:** `dp[0]` is initialized with `[[]]` (an empty list represents the sum of 0).
*   **Iteration:**
    1.  Iterate through each `num` in `candidates`.
    2.  For each `num`, iterate from `i = num` up to `target`.
    3.  For each `i`, consider the combinations that sum to `i - num` (stored in `dp[i - num]`).
    4.  For every `combo` in `dp[i - num]`, add `num` to it and append this new combination `(combo + [num])` to `dp[i]`.
*   **Result:** `dp[target]` will contain all unique combinations that sum to `target`.
*   **Handling Uniqueness:** The outer loop iterating through `num` in `candidates` and the inner loop iterating for `i` from `num` to `target` ensures that combinations are built in a canonical order (e.g., `[2,3]` will be formed when `num=3` is considered after `num=2`, by appending `3` to `dp[2]`. `[3,2]` would not be formed because when `num=2` is considered, we only look at `dp[i-2]`, and `dp[i-2]` would have already been formed using numbers less than or equal to the *current* `num` being processed or earlier `num`s from candidates). This way, `[2,3]` is distinct from `[3,2]` in construction (it only creates `[2,3]`).
*   **Code Sketch (from provided solution):**
    ```python
    # dp = [[] for _ in range(target + 1)]
    # dp[0] = [[]] # Base case: one way to make sum 0 is to choose nothing
    # for num in candidates: # Iterate through each candidate
    #     for i in range(num, target + 1): # For each sum from num up to target
    #         for combo in dp[i - num]: # Take all combinations that sum to (i - num)
    #             dp[i].append(combo + [num]) # Add current num to them to form new combinations for sum i
    # return dp[target]
    ```

---

### 3. Detailed Explanation of Logic (Focus on Backtracking & DP)

#### Logic for Approach 3: Backtracking (Optimized)

The backtracking approach systematically explores all possible combinations using recursion.

1.  **Initialization:**
    *   `result = []`: This list will store all the valid combinations found.
    *   `candidates.sort()`: This is a crucial step. Sorting the `candidates` array (e.g., `[2,3,6,7]` becomes `[2,3,6,7]`) enables an important optimization for pruning the search space.

2.  **`backtrack` Function:**
    *   `def backtrack(start_index, combination, current_sum):`
        *   `start_index`: An integer representing the index in `candidates` from which we can start picking numbers for the current combination. This is key to preventing duplicate combinations (e.g., `[2,3]` and `[3,2]`) and allowing numbers to be used multiple times. By starting from `start_index`, we ensure that elements are picked in a non-decreasing order of their original index, which implicitly handles unique combinations.
        *   `combination`: The current list of numbers that form a partial combination. This is passed by reference, so modifications are shared across recursive calls at the same depth.
        *   `current_sum`: The sum of numbers in `combination`.

3.  **Base Cases / Termination Conditions:**
    *   `if current_sum == target:`: If the `current_sum` exactly matches the `target`, we've found a valid combination. We append a *copy* (`list(combination)`) of the `combination` to the `result` list. We use `list(combination)` because `combination` is modified by reference, and we need to store its state *at this moment*. After adding it, we `return` to explore other paths.
    *   Notice there's no explicit `if current_sum > target:` return here, as the loop condition handles it more efficiently.

4.  **Recursive Step (Exploring Choices):**
    *   `for i in range(start_index, len(candidates)):`
        *   This loop iterates through the `candidates` array, starting from `start_index`. This ensures that we only consider numbers that come *after or are the same as* the last chosen number (due to `i` being passed to the next recursive call) to maintain non-decreasing order and prevent duplicates like `[2,3]` and `[3,2]`.
        *   `num = candidates[i]`: Get the current number to consider.
        *   **Pruning Optimization:** `if current_sum + num > target: break`
            *   Because `candidates` is sorted, if adding `num` (the current smallest available number from `candidates[i]` onwards) makes the `current_sum` exceed `target`, then adding any subsequent number (`candidates[i+1]`, `candidates[i+2]`, etc., which are all greater than or equal to `num`) will also exceed `target`.
            *   Therefore, we can `break` out of the loop. This effectively prunes all subsequent branches from this point in the current recursion level, significantly reducing unnecessary computations.
        *   **Include current number:**
            *   `combination.append(num)`: Add the `num` to the `current_combination`.
            *   `backtrack(i, combination, current_sum + num)`: Make a recursive call.
                *   Crucially, `i` (not `i + 1`) is passed as the new `start_index`. This is because the same number `num` can be used multiple times. If we passed `i + 1`, each number could only be used once.
                *   `current_sum + num`: Update the sum.
        *   **Backtrack (Undo Choice):**
            *   `combination.pop()`: After the recursive call returns (meaning all combinations starting with the current `num` have been explored), we remove `num` from `combination`. This allows the algorithm to explore other choices (i.e., the next number in the `for` loop) at the current `start_index`.

5.  **Initial Call:** `backtrack(0, [], 0)`: Start the process with `start_index = 0`, an empty `combination` list, and `current_sum = 0`.

**Example Walkthrough (candidates = [2,3,6,7], target = 7):**

1.  `candidates` becomes `[2,3,6,7]` (already sorted).
2.  `backtrack(0, [], 0)`
    *   `i = 0, num = 2`: `combination = [2]`, `sum = 2`. Call `backtrack(0, [2], 2)`
        *   `i = 0, num = 2`: `combination = [2,2]`, `sum = 4`. Call `backtrack(0, [2,2], 4)`
            *   `i = 0, num = 2`: `combination = [2,2,2]`, `sum = 6`. Call `backtrack(0, [2,2,2], 6)`
                *   `i = 0, num = 2`: `combination = [2,2,2,2]`, `sum = 8`. `8 > 7`, `break`.
                *   `i = 1, num = 3`: `combination = [2,2,2,3]`, `sum = 9`. `9 > 7`, `break`.
                *   `i = 2, num = 6`: `combination = [2,2,2,6]`, `sum = 12`. `12 > 7`, `break`.
                *   `i = 3, num = 7`: `combination = [2,2,2,7]`, `sum = 13`. `13 > 7`, `break`.
                *   `pop()`, `combination = [2,2,2]`
            *   `pop()`, `combination = [2,2]`
            *   `i = 1, num = 3`: `combination = [2,2,3]`, `sum = 7`. Call `backtrack(1, [2,2,3], 7)`
                *   `current_sum == target` (7 == 7). Add `[2,2,3]` to `result`. `return`.
            *   `pop()`, `combination = [2,2]`
            *   `i = 2, num = 6`: `combination = [2,2,6]`, `sum = 10`. `10 > 7`, `break`.
            *   `pop()`, `combination = [2]`
        *   `pop()`, `combination = [2]`
        *   `i = 1, num = 3`: `combination = [2,3]`, `sum = 5`. Call `backtrack(1, [2,3], 5)`
            *   `i = 1, num = 3`: `combination = [2,3,3]`, `sum = 8`. `8 > 7`, `break`.
            *   `pop()`, `combination = [2,3]`
            *   `i = 2, num = 6`: `combination = [2,3,6]`, `sum = 11`. `11 > 7`, `break`.
            *   `pop()`, `combination = [2]`
        *   `pop()`, `combination = []`
    *   `i = 1, num = 3`: `combination = [3]`, `sum = 3`. Call `backtrack(1, [3], 3)`
        *   `i = 1, num = 3`: `combination = [3,3]`, `sum = 6`. Call `backtrack(1, [3,3], 6)`
            *   `i = 1, num = 3`: `combination = [3,3,3]`, `sum = 9`. `9 > 7`, `break`.
            *   `pop()`, `combination = [3,3]`
            *   `i = 2, num = 6`: `combination = [3,3,6]`, `sum = 12`. `12 > 7`, `break`.
            *   `pop()`, `combination = [3]`
        *   `pop()`, `combination = []`
    *   `i = 2, num = 6`: `combination = [6]`, `sum = 6`. Call `backtrack(2, [6], 6)`
        *   `i = 2, num = 6`: `combination = [6,6]`, `sum = 12`. `12 > 7`, `break`.
        *   `pop()`, `combination = [6]`
        *   `i = 3, num = 7`: `combination = [6,7]`, `sum = 13`. `13 > 7`, `break`.
        *   `pop()`, `combination = []`
    *   `i = 3, num = 7`: `combination = [7]`, `sum = 7`. Call `backtrack(3, [7], 7)`
        *   `current_sum == target` (7 == 7). Add `[7]` to `result`. `return`.
    *   `pop()`, `combination = []`

Final `result = [[2,2,3],[7]]`.

#### Logic for Approach 7: Dynamic Programming (DP)

This approach uses a bottom-up DP strategy, building combinations for smaller sums first.

1.  **`dp` Array Initialization:**
    *   `dp = [[] for _ in range(target + 1)]`: Creates a list of lists, where `dp[s]` will eventually store all combinations that sum up to `s`.
    *   `dp[0] = [[]]`: This is the base case. There is one way to achieve a sum of 0: by choosing an empty set of numbers. This empty list `[]` acts as a starting point for building combinations.

2.  **Outer Loop (`for num in candidates`):**
    *   This loop iterates through each `candidate` number one by one. The order of `candidates` here is important for correctly building unique combinations without duplicates. By processing numbers one by one from `candidates`, we ensure that any combination `[a, b, c]` where `a <= b <= c` is formed correctly. When we process `num`, we are essentially saying "now we consider `num` as a possible element to add to existing combinations".

3.  **Inner Loop (`for i in range(num, target + 1)`):**
    *   For each `num` from `candidates`, this loop iterates through possible sums `i` from `num` up to `target`.
    *   We start `i` from `num` because any sum less than `num` cannot possibly include `num`.

4.  **Innermost Loop (`for combo in dp[i - num]`):**
    *   For the current sum `i` and current candidate `num`, we look at `dp[i - num]`. `dp[i - num]` contains all combinations that sum up to `i - num`.
    *   For each `combo` (which is a list of numbers) in `dp[i - num]`:
        *   `dp[i].append(combo + [num])`: We create a new combination by taking `combo` and appending the current `num`. This new combination `(combo + [num])` now sums to `(i - num) + num = i`. This new combination is added to `dp[i]`.

**How Uniqueness is Handled (DP):**
The order of loops (`for num in candidates` then `for i in range(num, target + 1)`) is critical for uniqueness.
*   When `num = 2` is processed, `dp[2]` gets `[[2]]`, `dp[4]` gets `[[2,2]]`, etc.
*   When `num = 3` is processed:
    *   `i = 3`: `dp[3]` gets `[[3]]` (from `dp[0]` + `3`).
    *   `i = 5`: `dp[5]` gets `[[2,3]]` (from `dp[2]` + `3`). Note that `[3,2]` is *not* generated. This is because when `num=2` was processed, `dp[3]` didn't exist yet for us to add `2` to `dp[1]`. When `num=3` is processed, we only append `3` to existing combinations from `dp[i-3]`. Since `dp[i-3]` would only contain elements `<=3` (if processed in a specific candidate order) or elements processed prior to `3` in `candidates` list, we ensure elements are added in non-decreasing order.
This construction method implicitly enforces uniqueness, similar to how `start_index` works in backtracking.

**Example Walkthrough (candidates = [2,3,6,7], target = 7):**

`dp = [[] for _ in range(8)]` (0 to 7)
`dp[0] = [[]]`

**Process `num = 2`:**
*   `i = 2`: `dp[2-2] = dp[0] = [[]]`. Add `2` to `[]`. `dp[2] = [[2]]`
*   `i = 3`: `dp[3-2] = dp[1] = []`. Nothing to add.
*   `i = 4`: `dp[4-2] = dp[2] = [[2]]`. Add `2` to `[2]`. `dp[4] = [[2,2]]`
*   `i = 5`: `dp[5-2] = dp[3] = []`. Nothing.
*   `i = 6`: `dp[6-2] = dp[4] = [[2,2]]`. Add `2` to `[2,2]`. `dp[6] = [[2,2,2]]`
*   `i = 7`: `dp[7-2] = dp[5] = []`. Nothing.
Current `dp`: `dp[0]=[[]], dp[2]=[[2]], dp[4]=[[2,2]], dp[6]=[[2,2,2]]` (others empty)

**Process `num = 3`:**
*   `i = 3`: `dp[3-3] = dp[0] = [[]]`. Add `3` to `[]`. `dp[3] = [[3]]` (first time it's not empty)
*   `i = 4`: `dp[4-3] = dp[1] = []`. Nothing. (Note: `dp[4]` still `[[2,2]]` from `num=2`)
*   `i = 5`: `dp[5-3] = dp[2] = [[2]]`. Add `3` to `[2]`. `dp[5] = [[2,3]]`
*   `i = 6`: `dp[6-3] = dp[3] = [[3]]`. Add `3` to `[3]`. `dp[6]` becomes `[[2,2,2], [3,3]]` (appending to existing)
*   `i = 7`: `dp[7-3] = dp[4] = [[2,2]]`. Add `3` to `[2,2]`. `dp[7] = [[2,2,3]]`
Current `dp`: `dp[0]=[[]], dp[2]=[[2]], dp[3]=[[3]], dp[4]=[[2,2]], dp[5]=[[2,3]], dp[6]=[[2,2,2],[3,3]], dp[7]=[[2,2,3]]`

**Process `num = 6`:**
*   `i = 6`: `dp[6-6] = dp[0] = [[]]`. Add `6` to `[]`. `dp[6]` becomes `[[2,2,2],[3,3],[6]]`
*   `i = 7`: `dp[7-6] = dp[1] = []`. Nothing.
Current `dp`: ... `dp[6]=[[2,2,2],[3,3],[6]], dp[7]=[[2,2,3]]`

**Process `num = 7`:**
*   `i = 7`: `dp[7-7] = dp[0] = [[]]`. Add `7` to `[]`. `dp[7]` becomes `[[2,2,3],[7]]` (appending to existing)
Final `dp[7] = [[2,2,3],[7]]`.

---

### 4. Time and Space Complexity Analysis

Let `N` be the number of candidates (`len(candidates)`) and `T` be the `target` value.
Let `M` be the maximum length of a combination (roughly `T / min(candidates)`).
Let `K` be the number of unique combinations that sum to `target`.

#### Approach 1: Brute-force with `itertools.combinations_with_replacement`

*   **Time Complexity:**
    *   The number of combinations with replacement of `N` items chosen `L` times is `C(N + L - 1, L)`.
    *   `L` goes up to `M`. So, we generate and check `sum(C(N + L - 1, L))` combinations.
    *   For each combination, `sum()` takes `O(L)` time.
    *   Worst case: extremely high. Even for small `N, T`, `L` can be up to `T/2` (if `min(candidates)=2`). This can be `O(C(N+T/2, T/2) * T/2)`. This is very inefficient as many combinations will not sum to `target`.
*   **Space Complexity:** `O(M)` for `combo` list in `sum()`. The `result` list can store up to `K` combinations, each of length up to `M`, so `O(K * M)`.

#### Approach 2 & 3: Backtracking (Basic and Optimized)

*   **Time Complexity:**
    *   This is tricky to provide a tight upper bound for all cases because it depends heavily on the input values and the effectiveness of pruning.
    *   In the worst case, without effective pruning, it can be exponential. Consider `candidates = [1]`, `target = T`. It would make `T` recursive calls.
    *   A loose upper bound can be thought of as `O(N^(T / min(candidates)))`. Each recursive call might branch up to `N` times, and the maximum depth is `T / min(candidates)`.
    *   Each successful combination `C` (of length `L_c`) takes `O(L_c)` to copy to `result`.
    *   More accurately, the complexity is related to the number of nodes in the recursion tree. The number of nodes can be bounded by `N^(T/min_val)`. At each node, `O(N)` work (loop). So `O(N * N^(T/min_val))`.
    *   The `break` optimization in Approach 3 significantly prunes branches, but the theoretical worst-case remains exponential.
    *   A tighter estimate based on the number of valid solutions (K) and their max length (M) might be `O(K * M + N * (some_exponent_of_target))`. The total work is proportional to the number of states visited in the recursion tree.
    *   **Practical estimation**: Due to constraints (`target <= 40`, `candidates[i] >= 2`), `M` is at most `40/2 = 20`. `N` is at most 30.
        The overall complexity for combination problems is often considered `O(K * M)` (for storing the output) plus the cost of building the combinations. The branching factor `N` and depth `M` lead to an exponential time in the number of recursive calls `O(N^M)`. But given the tight constraints, the actual number of combinations found is limited (less than 150), and the pruning is effective. A rough, often cited estimate for these types of problems is related to `O(N * 2^T)` or `O(N^M)`.
*   **Space Complexity:**
    *   `O(M)` for the recursion stack depth (max length of a combination, `target / min(candidates)`).
    *   `O(M)` for the `combination` list.
    *   `O(K * M)` for storing the `result` list (K combinations, each of average length M). This is the dominant space factor for output storage.
    *   Total: `O(M + K * M)`.

#### Approach 4 & 5: Backtracking (Alternative Structure / Generators)

*   **Time Complexity:** Similar to Approach 2/3. The include/exclude pattern can sometimes lead to more states being visited than the `start_index` loop, but the asymptotic complexity remains in the same class.
*   **Space Complexity:** Similar to Approach 2/3.

#### Approach 6: Iterative Backtracking (using a Stack)

*   **Time Complexity:** Same as recursive backtracking, but without recursion overhead. `O(N^M)` in worst case, often much better in practice due to pruning.
*   **Space Complexity:**
    *   `O(M)` for the explicit stack to store states (number of active paths). In worst case, stack depth could be `M`.
    *   The `combination + [num]` creates new lists at each step, which can lead to higher memory usage than modifying a single list and backtracking with `pop()`. This effectively means `O(M)` copies of combination lists on the stack.
    *   `O(K * M)` for the `result` list.
    *   Total: `O(M^2 + K * M)` (because of the list copies).

#### Approach 7: Dynamic Programming (DP)

*   **Time Complexity:**
    *   Outer loop: `N` iterations (for each candidate).
    *   Middle loop: `T` iterations (for each sum from `num` to `target`).
    *   Inner loop: Iterates through combinations in `dp[i - num]`. The number of combinations can be `K_i` for sum `i`. Appending to a list takes `O(L_c)` where `L_c` is the length of `combo`. `L_c` can be up to `M`.
    *   So, roughly `O(N * T * K_avg * M)`, where `K_avg` is the average number of combinations for intermediate sums.
    *   A tighter bound: `O(N * T * M_max_combinations_for_a_sum * M)`. Given the constraints, `M` is small (max 20). The number of combinations for any sum `i` up to `target` might be high, but the problem states total `K < 150`. If `dp[i - num]` can have `P` items, and each is of length `Q`, then it's `O(P * Q)`.
    *   Rough practical bound: `O(N * T * (avg_num_combinations_per_sum) * M)`. If `M` is max length (20) and `N, T` are 40, this is `40 * 40 * 150 * 20` in the *absolute worst case* if all 150 combinations were generated for every `i`.
    *   More reasonable: `O(N * T * K_max_at_any_i * M)`.
*   **Space Complexity:**
    *   `O(T * K_max_at_any_i * M)`. The `dp` array stores lists of combinations for each sum `0` to `target`. Each `dp[i]` can contain multiple combinations, and each combination can be up to length `M`. The total number of combinations stored across all `dp[i]` can be significant. Given `K < 150`, total elements across all `dp[i]` might be `T * K_avg * M`.
    *   Total space: `O(T * K_{max} * M)`.

**Summary Comparison:**

| Approach                                | Time Complexity                                     | Space Complexity                 | Notes                                                                                                                                              |
| :-------------------------------------- | :-------------------------------------------------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Itertools Brute-Force                | High exponential, `O(C(N+M, M) * M)`                | `O(K * M)`                       | Simplistic, but generates too many invalid candidates.                                                                                             |
| 2. Backtracking (Basic)                 | Exponential, roughly `O(N^(T/min_val) * (T/min_val))` | `O(M + K * M)`                   | Standard recursive solution.                                                                                                                       |
| **3. Backtracking (Optimized)**         | Exponential, but highly pruned. Often practical.    | `O(M + K * M)`                   | **Generally optimal and preferred for competitive programming.** Sorting and pruning are key.                                                    |
| 4. Backtracking (Include/Exclude)       | Exponential, similar to 2.                          | `O(M + K * M)`                   | Alternative recursive structure. Less direct for "unlimited use" than `start_index`.                                                               |
| 5. Backtracking (Generators)            | Same as 3                                           | `O(M + K * M)`                   | Pythonic, but performance/memory similar to 3 when `list()` is called at the end.                                                                  |
| 6. Iterative Backtracking (Stack)       | Same as 3                                           | `O(M^2 + K * M)`                 | Avoids recursion limit. `combination + [num]` can be memory intensive due to repeated list creation.                                                 |
| **7. Dynamic Programming**              | `O(N * T * K_{max_i} * M)`                          | `O(T * K_{max_i} * M)`           | **Optimal for some scenarios, guaranteed polynomial (if K is bounded).** Can be slower than optimized backtracking for small K due to constants. |

*Self-reflection on DP complexity*: The constraint "number of unique combinations that sum up to target is less than 150" (`K < 150`) *only applies to the final target*. For intermediate `dp[i]` values, the number of combinations could theoretically be larger. However, for given constraints `T <= 40`, `M <= 20`, the actual runtime for DP is quite acceptable.

---

### 5. Edge Cases and How They Are Handled

1.  **`candidates` list is empty:**
    *   **Problem Constraint:** `1 <= candidates.length`. So this edge case is technically not possible based on constraints.
    *   **Handling (if it were possible):** All approaches would correctly return `[]` (empty list) for an empty `candidates` list. Backtracking would immediately terminate, DP would result in `dp[target]` being empty unless `target=0`.
2.  **`target` is 0:**
    *   **Problem Constraint:** `1 <= target`. So this edge case is technically not possible.
    *   **Handling (if it were possible):**
        *   **Backtracking:** If `target = 0`, `backtrack(0, [], 0)` would immediately hit `current_sum == target`, add `[]` to `result`, and return `[[]]`. This is usually the correct behavior for "how many ways to make 0 sum".
        *   **DP:** `dp[0]` is initialized to `[[]]`. `dp[target]` would directly return `[[]]`. This is also correct.
3.  **`target` is less than `min(candidates)`:** (e.g., `candidates = [2,3], target = 1`)
    *   **Backtracking (Approach 3):**
        *   `backtrack(0, [], 0)`.
        *   Loop `for i in range(0, len(candidates))`.
        *   `num = candidates[0] = 2`.
        *   `current_sum + num (0+2)` is `2`, which is `> target (1)`. The `if current_sum + num > target: break` condition triggers.
        *   The loop breaks, no recursive calls are made, and `result` remains `[]`. Correctly handled.
    *   **DP (Approach 7):**
        *   `dp` array initialized. `dp[0]=[[]]`.
        *   For `num = 2`: `range(2, target+1)` -> `range(2, 2)` which is empty. No sums are processed for `num = 2`.
        *   For `num = 3`: `range(3, target+1)` -> `range(3, 2)` which is empty. No sums are processed for `num = 3`.
        *   `dp[target]` (`dp[1]`) remains `[]`. Correctly handled.
4.  **All numbers in `candidates` are greater than `target`:** (e.g., `candidates = [5,6], target = 3`)
    *   This is a specific case of #3, handled identically.
5.  **`candidates` contains only one number:** (e.g., `candidates = [2], target = 7`)
    *   **Backtracking:** It will try to use `2` repeatedly. `[2] -> [2,2] -> [2,2,2] -> [2,2,2,2]` (sum 8). When sum becomes 8, it prunes. `[2,2,2]` would try to add `2` again, prune. `[2,2]` would try `2` again. No exact sum for 7. Returns `[]`. Correct.
    *   **DP:** `dp[2]=[[2]], dp[4]=[[2,2]], dp[6]=[[2,2,2]]`. `dp[7]` remains `[]`. Correct.
6.  **`target` is a multiple of one of the candidates:** (e.g., `candidates = [2,3], target = 6`)
    *   Both Backtracking and DP will correctly find `[[2,2,2], [3,3], [2,2,2]]` (implicitly `[[2,2,2], [3,3]]` if order is managed). This is exactly what the algorithms are designed for and they will work correctly.

---

### 6. Clean, Well-Commented Version of the Optimal Solution

The most commonly adopted and performant optimal solution in competitive programming for this type of problem is **Backtracking with Sorting and Pruning (Approach 3)** due to its balance of simplicity, readability, and efficiency. The **Dynamic Programming (Approach 7)** is also optimal in its own right, especially for problems with very specific sum constraints or when intermediate sums need to be reused extensively. I'll provide Approach 3 as the primary optimal solution.

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum up to target.
        Numbers can be chosen an unlimited number of times.

        Args:
            candidates: A list of distinct integers.
            target: The target sum.

        Returns:
            A list of lists, where each inner list is a unique combination.
        """
        
        result = [] # This list will store all valid combinations

        # Sort the candidates array. This is crucial for two reasons:
        # 1. To enable the pruning optimization: if current_sum + num > target,
        #    then all subsequent numbers (which are larger) will also exceed target.
        # 2. To implicitly handle uniqueness: by always picking numbers in a non-decreasing
        #    order (via start_index), we avoid duplicate combinations like [2,3] and [3,2].
        candidates.sort()

        def backtrack(start_index: int, current_combination: List[int], current_sum: int):
            """
            Recursive helper function to explore combinations.

            Args:
                start_index: The index in 'candidates' from which to start considering numbers.
                             This ensures that combinations are unique and numbers are considered
                             in a non-decreasing order to avoid permutations.
                current_combination: The list of numbers currently chosen for the combination.
                current_sum: The sum of numbers in 'current_combination'.
            """
            
            # Base Case 1: If the current sum equals the target, we found a valid combination.
            if current_sum == target:
                # Append a copy of the current_combination to the result.
                # We append a copy because 'current_combination' is a mutable list
                # that will be modified by subsequent recursive calls.
                result.append(list(current_combination))
                return # Stop exploring this path

            # Base Case 2: If the current sum exceeds the target, this path is invalid.
            # No need for an explicit check here if 'current_sum + num > target'
            # is checked within the loop, especially after sorting.
            # However, for general backtracking, 'if current_sum > target: return' is a common prune.
            # In this optimized version, the loop's 'break' handles this proactively.

            # Explore choices: Iterate through candidates from start_index onwards
            for i in range(start_index, len(candidates)):
                num = candidates[i]

                # Pruning Optimization:
                # If adding the current number 'num' makes the sum exceed target,
                # then because 'candidates' is sorted, any subsequent numbers
                # (candidates[i+1], candidates[i+2], etc.) will also be
                # greater than or equal to 'num', and thus will also exceed target.
                # So, we can stop exploring this branch and its subsequent siblings.
                if current_sum + num > target:
                    break # Prune this path and all subsequent choices at this level

                # Include the current number in the combination
                current_combination.append(num)

                # Recursive Call:
                # Pass 'i' (not 'i + 1') as the new start_index. This is crucial
                # because the same number can be used multiple times.
                # If we passed 'i + 1', each number could only be used once.
                backtrack(i, current_combination, current_sum + num)

                # Backtrack: Remove the last added number to explore other possibilities.
                # This undoes the choice made in the current step, allowing the loop
                # to proceed to the next candidate at the current recursion level.
                current_combination.pop()

        # Initial call to start the backtracking process
        # Start from index 0, with an empty combination list, and a sum of 0.
        backtrack(0, [], 0)
        
        return result

```

**Alternative Optimal Solution: Dynamic Programming (Approach 7)**

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum up to target using Dynamic Programming.
        Numbers can be chosen an unlimited number of times.

        Args:
            candidates: A list of distinct integers.
            target: The target sum.

        Returns:
            A list of lists, where each inner list is a unique combination.
        """
        
        # dp[i] will store a list of all unique combinations that sum up to 'i'.
        # Initialize dp array with empty lists for sums from 0 to target.
        dp = [[] for _ in range(target + 1)]
        
        # Base case: There is one way to make a sum of 0, which is by choosing an empty set of numbers.
        # This empty list acts as a starting point for building combinations.
        dp[0] = [[]]
        
        # Iterate through each candidate number.
        # The order of processing candidates is important for ensuring uniqueness
        # and avoiding permutations (e.g., [2,3] vs [3,2]).
        for num in candidates:
            # For each candidate 'num', iterate through possible sums 'i' from 'num' up to 'target'.
            # We start 'i' from 'num' because any sum less than 'num' cannot possibly include 'num'.
            for i in range(num, target + 1):
                # For the current sum 'i', consider combinations that sum to 'i - num'.
                # These combinations are already stored in dp[i - num].
                for combo in dp[i - num]:
                    # Create a new combination by appending the current 'num' to an existing 'combo'.
                    # This new combination sums to (i - num) + num = i.
                    # Append this new combination to dp[i].
                    # The combination is built in a way that numbers are added in non-decreasing order
                    # based on the 'candidates' iteration, thus ensuring uniqueness of combinations.
                    dp[i].append(combo + [num])
                    
        # The result is the list of combinations stored at dp[target].
        return dp[target]

```

---

### 7. Key Insights and Patterns that Can Be Applied to Similar Problems

1.  **Backtracking for Combinatorial Search:**
    *   **Core Idea:** Backtracking is a general algorithmic technique for solving problems that involve searching for a set of solutions or a single solution among a large number of candidates. It builds candidates for the solution incrementally and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
    *   **Structure:** Typically recursive, with base cases for successful completion or invalid paths, and a recursive step that iterates through choices.
    *   **State Management:** Always consider what information needs to be passed to the next recursive call (e.g., current index, current partial solution, current sum/state).
    *   **Choices & Undoing:** For each choice, perform it (`append`), recurse, then undo it (`pop`) to explore other possibilities.

2.  **Handling Unique Combinations (Avoiding Permutations):**
    *   **`start_index` Parameter:** In backtracking, pass a `start_index` to the recursive call. This index dictates that elements can only be chosen from `candidates[start_index]` onwards. This ensures that `[2,3]` is formed, but `[3,2]` is not, because when `3` is picked, `2` (which is at an earlier index) won't be considered for subsequent picks in that branch.
    *   **Sorting `candidates`:** Sorting the input array allows for better pruning and sometimes simplifies the logic for handling uniqueness.

3.  **Handling "Unlimited Use" of Elements:**
    *   **Backtracking:** When an element `candidates[i]` is chosen, the next recursive call should start from `index i` (not `i + 1`). This allows the current element to be chosen again. If each element could be used only once, `i + 1` would be passed.
    *   **Dynamic Programming:** The inner loop `for i in range(num, target + 1)` (iterating sums from `num` upwards) ensures that `num` can be added to any prior combination (from `dp[i - num]`), effectively allowing `num` to be reused.

4.  **Pruning the Search Space:**
    *   **`current_sum > target`:** If the sum exceeds the target, that path is invalid. Return immediately.
    *   **Sorting + `break`:** If the input is sorted, `if current_sum + num > target: break` is a powerful optimization. It allows you to abandon not just the current choice but all subsequent choices at the current level of recursion because they would also exceed the target.

5.  **Dynamic Programming for Sum/Combination Problems:**
    *   **`dp[i]` Represents:** For problems asking for "number of ways to sum to `i`" or "list of combinations to sum to `i`", a DP array `dp[i]` is often suitable.
    *   **Building Solutions:** The pattern `dp[i].append(dp[i - num] + [num])` is very common for "unbounded knapsack" type problems where items can be reused. The outer loop typically iterates over items (candidates), and the inner loop iterates over sums.
    *   **Order of Loops for Uniqueness:** The order of iterating through items (`for num in candidates`) and then sums (`for i in range(num, target + 1)`) ensures that unique combinations are generated (e.g., `[2,3]` is built, `[3,2]` is not). If the order of elements within combinations mattered (permutations), or if elements could be used only once, the loop structures would differ.

**Similar Problems:**
*   **Combination Sum II (LeetCode 40):** Each number in `candidates` can be used only once, and `candidates` might contain duplicates. Requires careful handling of duplicates to ensure unique combinations.
*   **Subsets (LeetCode 78) / Subsets II (LeetCode 90):** Finding all subsets of a set.
*   **Permutations (LeetCode 46) / Permutations II (LeetCode 47):** Finding all permutations of a set.
*   **Coin Change (LeetCode 322):** Finding the minimum number of coins to make a sum (often DP).
*   **Partition Equal Subset Sum (LeetCode 416):** Determining if a set can be partitioned into two subsets with equal sums.

Understanding these patterns and their variations (especially how `start_index`, sorting, and loop order affect unique vs. non-unique, and single-use vs. multi-use) is key to solving a wide range of combinatorial problems.