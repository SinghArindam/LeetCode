Here's a concise summary for quick revision of LeetCode 2456:

---

## LeetCode 2456: Construct Smallest Number From DI String (Medium)

**1. Key Problem Characteristics & Constraints:**
*   **Input:** `pattern` string of length `n` (`'I'` for increasing, `'D'` for decreasing).
*   **Output:** `num` string of length `n+1`.
*   **Digits:** '1' to '9', each used **at most once**.
*   **Rules:** `pattern[i] == 'I' -> num[i] < num[i+1]`; `pattern[i] == 'D' -> num[i] > num[i+1]`.
*   **Goal:** Lexicographically **smallest** `num`.
*   **Constraints:** `1 <= n <= 8`. (Crucial: `n+1` is max 9, perfectly fitting digits '1'-'9').

**2. Core Algorithmic Approach (Greedy with Stack):**
*   **Idea:** Iterate from `i=0` to `n`. Always push `i+1` (next smallest available digit) onto a stack.
*   **Commit Point:** If `pattern[i] == 'I'` OR `i == n` (end of pattern), pop ALL elements from the stack and append them to the `result` string.
*   **Mechanism:**
    *   For 'D' sequences (e.g., `DDD`): Digits like `1, 2, 3, 4` are pushed. At the end (or an 'I'), they are popped in reverse `4, 3, 2, 1`, forming the smallest possible decreasing sequence.
    *   For 'I' sequences: Digits are pushed and immediately popped, maintaining increasing order.
*   **Greedy:** Always attempts to use the smallest available digits (`1, 2, 3, ...`) and only "commits" them when forced by an 'I' or the end of the pattern, ensuring lexicographical minimality.

**3. Important Time/Space Complexity Facts:**
*   **Time Complexity:** `O(N)`, where `N = pattern.length`. Each digit (from 1 to `N+1`) is pushed onto the stack once and popped once.
*   **Space Complexity:** `O(N)` for the stack (can hold up to `N+1` elements) and the `result` string.

**4. Critical Edge Cases to Remember:**
*   **`n=1` (Smallest `pattern.length`):**
    *   `"I"` -> "12" (Push 1, pop 1. Push 2, pop 2).
    *   `"D"` -> "21" (Push 1, Push 2. At end, pop 2 then 1).
    *   Handled correctly due to the loop condition `i <= pattern.size()` and stack logic.
*   **All 'I's (`"IIII"`):** Results in "12345". Each push is immediately followed by a pop.
*   **All 'D's (`"DDD"`):** Results in "4321". All digits are pushed, then popped in reverse only at the very end of the loop.
*   **Digit Uniqueness:** The algorithm naturally uses `1` through `N+1` exactly once, which perfectly aligns with the '1' to '9' constraint given `N <= 8`.

**5. Key Patterns or Techniques Used:**
*   **Greedy Strategy:** Making locally optimal choices (using smallest available digits) to achieve global optimum (lexicographically smallest string).
*   **Stack for Reversal:** Clever use of the LIFO property to convert an increasing sequence of pushed numbers into a decreasing sequence when popped, ideal for `'D'` segments.
*   **Delimiter/Boundary-Driven Processing:** The `'I'` character (or end of input) acts as a signal to process and "flush" the accumulated elements from the stack.