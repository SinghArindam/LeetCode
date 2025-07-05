Here are concise short notes for LeetCode problem 1160 (Letter Tile Possibilities):

---

### LeetCode 1160: Letter Tile Possibilities - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   Find **number of unique non-empty sequences** from given `tiles`.
*   Each tile used **at most once**.
*   **Order matters** ("AB" != "BA").
*   Input `tiles` can have **duplicate letters** (e.g., "AAB").
*   **Constraints:** `1 <= tiles.length <= 7` (very small `N`).

**2. Core Algorithmic Approach (DFS with Frequency Map):**
*   **Strategy:** Recursive Backtracking (Depth-First Search - DFS).
*   **Duplicate Handling:** Use a `frequency map` (or array `int[26]`) to store counts of each available character, rather than tracking specific tile indices. This inherently handles duplicates efficiently.
*   **DFS Logic (`dfs(freq_map)`):**
    1.  Initialize `count = 0`.
    2.  Iterate through all possible characters ('A' to 'Z').
    3.  If a character `c` is available (`freq[c] > 0`):
        *   **Increment `count` by 1:** This accounts for the sequence formed by just picking `c` (or extending the current prefix by `c`).
        *   **Decrement `freq[c]`:** "Use" one tile of `c`.
        *   **Recursive Call:** `count += dfs(freq_map)`. Add all further unique sequences that can be built by appending more characters to `c`.
        *   **Backtrack:** Increment `freq[c]` back to restore the state for other branches.
    4.  Return `count`.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(AlphabetSize * NumberOfUniqueSequences)`.
    *   Roughly `O(26 * N!)` in worst case (all unique chars). For `N=7`, this is `26 * 7! = 131,040` operations, very fast.
*   **Space Complexity:** `O(AlphabetSize + N)`
    *   `O(26)` for frequency map.
    *   `O(N)` for recursion stack depth.
    *   Effectively **`O(1)`** (constant space) given fixed alphabet size and small `N`.

**4. Critical Edge Cases to Remember:**
*   **`tiles = "V"` (N=1):** Correctly returns 1 ("V").
*   **`tiles = "AAA"` (All same):** Correctly returns 3 ("A", "AA", "AAA").
*   **`tiles = "ABC"` (All unique):** Correctly returns `3*(1+1+1) + 3*2*(1+1) + 3*2*1*1 = 3 + 6 + 6 = 15` (A,B,C, AB,AC,BA,BC,CA,CB, ABC,ACB,BAC,BCA,CAB,CBA).

**5. Key Patterns or Techniques Used:**
*   **Backtracking/DFS:** Standard approach for combinatorial enumeration.
*   **Frequency Map:** Essential for handling multisets (collections with duplicates) efficiently in permutation/combination problems.
*   **Cumulative Recursive Counting:** The pattern `count++` followed by `count += dfs(...)` is key to correctly sum sequences at different lengths and branches.
*   **Constraint Hint:** Small `N` (up to 7) strongly suggests `N!` related complexity is acceptable.