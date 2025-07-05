Here's a concise summary of LeetCode 1819 for quick revision:

---

### LeetCode 1819: Construct the Lexicographically Largest Valid Sequence

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Construct a sequence `A` of length `2n - 1`.
*   **Rules:**
    *   `1` appears once.
    *   `2` to `n` each appear twice.
    *   For `i` from `2` to `n`, the two occurrences of `i` must be exactly `i` positions apart (distance `|idx1 - idx2| = i`).
*   **Output:** The **lexicographically largest** valid sequence.
*   **Constraints:** `1 <= n <= 20`.
*   **Guarantee:** A solution always exists.

**2. Core Algorithmic Approach:**
*   **Backtracking (Depth-First Search):**
    *   Builds the sequence `res` element by element, filling positions from `index = 0` to `2n - 2`.
    *   **Lexicographical Priority:** At each `index`, iterate through possible numbers `i` from `n` **down to `1`** (largest first) to ensure the first valid solution found is lexicographically largest.
    *   **State Tracking:**
        *   `res`: The `vector<int>` storing the current sequence (initialized with `0`s for empty slots).
        *   `used`: `vector<bool>` to track if a number `i` has been fully placed (single `1` or both `i, i` pairs).
    *   **Placement Logic:**
        *   If placing `1`: `res[index] = 1`.
        *   If placing `i > 1`: `res[index] = i`, `res[index + i] = i`.
    *   **Base Case:** If `index == res.size()`, a valid sequence is found, return `true`.
    *   **Recursive Call:** `backtrack(index + 1, n)`. If it returns `true`, propagate `true` upwards (found solution, no need to explore further).

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** Exponential in `N`, but highly optimized by pruning. Efficient enough for `N=20`. (Not `O((2N-1)!)` or `O(N^(2N-1))`).
*   **Space Complexity:** `O(N)`
    *   `res` vector: `O(2N - 1) = O(N)`.
    *   `used` vector: `O(N)`.
    *   Recursion Stack Depth: `O(2N - 1) = O(N)`.

**4. Critical Edge Cases & Handling:**
*   **`n = 1`:** Sequence length is 1. Output `[1]`. Handled correctly by base cases and `i=1` logic.
*   **`index + i` Out of Bounds:** Checked by `index + i < res.size()` before placing `i > 1`.
*   **Second Position Already Occupied:** Checked by `res[index + i] == 0` before placing `i > 1`.
*   **Current `res[index]` Already Occupied:** If `res[index] != 0` (meaning it was filled by a prior placement like `res[k+val] = val`), skip attempts to place new numbers at `index` and move to `backtrack(index + 1, n)`. This is a crucial optimization.
*   **Guaranteed Solution:** Simplifies the logic as the initial call `backtrack(0, n)` is guaranteed to return `true`.

**5. Key Patterns / Techniques Used:**
*   **Backtracking:** Standard for sequence/permutation/combination generation problems with constraints.
*   **Greedy Choice for Lexicographical Order:** To get the lexicographically largest result, always try the largest possible values first at each position.
*   **Effective Pruning:** Critical for performance in exponential time algorithms:
    *   Using a `used` array.
    *   Bounds checking (`index + i < res.size()`).
    *   Availability checking (`res[index + i] == 0`).
    *   Skipping already filled positions (`if (res[index] != 0)`).
*   **Problems with Paired Placements & Distance Constraints:** Similar patterns can appear in problems where items must be placed in pairs with specific relative positions.
*   **Small `N` as a Hint:** `N <= 20` often suggests that an exponential solution with strong pruning will pass.