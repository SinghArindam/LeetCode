Here are concise short notes for LeetCode problem 1516, "The k-th Lexicographical String of All Happy Strings of Length n":

---

### **LeetCode 1516: K-th Lexicographical Happy String**

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Find the `k`-th lexicographically smallest "happy string" of length `n`. Return `""` if less than `k` such strings exist.
*   **Happy String Rules:**
    1.  Consists only of `'a', 'b', 'c'`.
    2.  `s[i] != s[i+1]` (adjacent characters must be different).
*   **Constraints:** `1 <= n <= 10`, `1 <= k <= 100`. *(Crucial: Small `n` allows `O(N * 2^N)` solutions; small `k` is a hint for direct construction.)*

**2. Core Algorithmic Approaches:**

*   **A. Backtracking (DFS - Provided Solution Logic):**
    *   **Idea:** Recursively build happy strings character by character.
        *   At each step, iterate through `'a', 'b', 'c'`.
        *   Add character only if it's different from the last one (or if it's the first character).
        *   `Choose` char, `Explore` recursively, `Unchoose` (backtrack) to try other options.
        *   **Lexicographical Order:** By iterating choices `('a' then 'b' then 'c')`, strings are naturally generated in lexicographical order. Store them in a list.
    *   **Count of Happy Strings:** `3 * 2^(n-1)` total happy strings of length `n`. (3 choices for first char, 2 for each subsequent).
    *   **When to Use:** Simple to implement, efficient enough for small `N`.

*   **B. Optimal: Digit-by-Digit Construction (Mathematical Pruning):**
    *   **Idea:** Don't generate all strings. Directly construct the `k`-th string.
        *   Calculate how many happy strings start with 'a', 'b', or 'c' for the remaining length (`2^(remaining_len-1)` for fixed first char).
        *   Use `k` to determine which character to pick at the current position:
            *   If `k` falls within the count of strings starting with the first *valid* character, pick it.
            *   Otherwise, subtract that branch's count from `k` and check the next *valid* character.
        *   Repeat `n` times (for each character position).
    *   **When to Use:** Most efficient, best for larger `N` or when `K` might be very small in a huge search space.

**3. Important Time/Space Complexity Facts:**

*   **Backtracking (A):**
    *   **Time:** `O(3 * 2^(n-1) * n)` or `O(H * n)`, where `H` is the total happy strings. For `n=10`, `~1536 * 10 = ~15k` operations. **Efficient.**
    *   **Space:** `O(H * n)` for storing all happy strings + `O(n)` recursion stack. For `n=10`, `~15KB`. **Efficient.**
*   **Digit-by-Digit (B):**
    *   **Time:** `O(n)`. Iterates `n` times, constant work per iteration. **Extremely efficient.**
    *   **Space:** `O(n)` for the result string. **Extremely efficient.**

**4. Critical Edge Cases:**
*   `n=1`: Happy strings are "a", "b", "c". Handled by both approaches correctly.
*   `k` is too large (e.g., `n=1, k=4`): Return `""`. Both solutions explicitly check `k > total_happy_strings` and return `""`.
*   Smallest/Largest `n` and `k` within constraints are handled.

**5. Key Patterns or Techniques Used:**
*   **Backtracking / DFS:** A fundamental technique for generating permutations, combinations, or sequences with constraints. (Pattern: choose, explore, unchoose).
*   **Lexicographical Ordering:** Achieved by iterating choices (`'a' < 'b' < 'c'`) at each step.
*   **Counting and Pruning (Ranked Element Finding):** For finding the K-th element in a large generated set without full enumeration. Involves calculating branch sizes and adjusting `k`.
*   **Bit Manipulation (Powers of Two):** `(1 << x)` is an efficient way to calculate `2^x`, common in problems with binary choices (like `s[i] != s[i+1]`).
*   **Constraints Analysis:** Always check `n` and `k` limits to guide algorithm selection. For small `n`, even slightly less optimal algorithms might pass.