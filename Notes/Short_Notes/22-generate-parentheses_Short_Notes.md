Here's a concise summary of the notes for LeetCode 22: Generate Parentheses, suitable for quick revision:

---

### LeetCode 22: Generate Parentheses - Quick Notes

1.  **Key Problem Characteristics & Constraints:**
    *   **Goal:** Generate *all unique combinations* of *well-formed* parentheses given `n` pairs.
    *   **Well-formed Rules:**
        1.  Total `(` count equals `n`, total `)` count equals `n`.
        2.  Properly nested (e.g., `(())` valid, `)(` invalid).
        3.  Balance (open count - close count) never negative during traversal.
        4.  Final balance must be zero.
        5.  Total string length is `2n`.
    *   **Constraints:** `1 <= n <= 8`. Small `n` allows for exponential time complexity relative to `n`.

2.  **Core Algorithmic Approach (Backtracking / Recursive DFS - Most Common Optimal):**
    *   **Idea:** Build the parenthesis string character by character, making choices and pruning invalid paths early.
    *   **State:** `(current_string, open_count, balance)`
        *   `open_count`: Number of `(` added so far.
        *   `balance`: `open_count - close_count` (unmatched open parens).
    *   **Recursive Rules (Choices & Pruning):**
        1.  **Add `(`:** If `open_count < n`. (Can still add an opening parenthesis).
        2.  **Add `)`:** If `balance > 0`. (Only if there's an unmatched `(` to close).
    *   **Base Case:** If `len(current_string) == 2 * n` AND `balance == 0`, add `current_string` to results.

3.  **Important Time/Space Complexity Facts:**
    *   **Number of solutions:** `C_n` (n-th Catalan number), grows exponentially. For `n=8`, `C_8 = 1430`.
    *   **Backtracking (DFS):**
        *   **Time:** `O(C_n * n)` – Number of valid strings * length of each string (due to string construction).
        *   **Space:** `O(n)` – Maximum recursion stack depth (max string length).
    *   **Dynamic Programming (Alternative):**
        *   **Time:** `O(C_n * n)` – Similar to DFS.
        *   **Space:** `O(C_n * n)` – Stores all intermediate results.
    *   Both are efficient enough for `n <= 8`. DFS is often preferred for better space efficiency.

4.  **Critical Edge Cases:**
    *   `n = 1`: Output `["()"]`.
    *   (Implicitly `n = 0` for generality, though outside constraints): Output `[""]`.
    *   The `open_count < n` and `balance > 0` pruning rules correctly handle these by limiting additions and ensuring validity at each step.

5.  **Key Patterns or Techniques Used:**
    *   **Backtracking (DFS):** Standard for generating all combinations/permutations with constraints. Involves state, choices, pruning, and base cases.
    *   **Parentheses Balance Counter:** A common technique for validating or generating well-formed bracket sequences.
    *   **Combinatorial Generation:** This problem is a classic example of generating all valid instances of a combinatorial object.
    *   **Catalan Numbers:** Indicates the problem's underlying structure and provides a lower bound for solution complexity.
    *   **(Optional) Dynamic Programming (DP):** Can be solved using DP `dp[i] = (A)B` where A has `j` pairs and B has `i-1-j` pairs.