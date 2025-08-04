Here are concise short notes for quick revision of LeetCode problem 3799 - Unique 3-Digit Even Numbers:

---

### LeetCode 3799: Unique 3-Digit Even Numbers - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
    *   **Goal:** Count *distinct* 3-digit even numbers formable from `digits` array.
    *   **Number Rules:**
        *   **3-Digit:** Between 100 and 999.
        *   **Even:** Last digit must be 0, 2, 4, 6, or 8.
        *   **No Leading Zero:** First digit cannot be 0.
        *   **Each Copy Once:** If `digits = [1,2,2]`, you can use both '2's to form `122`.
    *   **Input Constraints:** `3 <= digits.length <= 10`, `0 <= digits[i] <= 9`.
        *   *Crucial:* `digits.length` is very small.

**2. Core Algorithmic Approach:**
    *   **Primary Solution (Brute-Force Permutations):**
        1.  Use three nested loops (`i`, `j`, `k`) to pick three *distinct indices* from `digits`.
        2.  Form `num = digits[i]*100 + digits[j]*10 + digits[k]`.
        3.  Validate: `digits[i] != 0` (no leading zero) and `digits[k] % 2 == 0` (even).
        4.  Add valid `num` to a `set` to ensure distinctness.
        5.  Return `len(set)`.
    *   **Optimal Approach (Iterate Target Numbers):**
        1.  Pre-count available digits in `digits` using `collections.Counter`.
        2.  Iterate `n` from `100` to `998` with a step of `2` (covers all 3-digit even numbers).
        3.  For each `n`, get its digit frequency (e.g., `220` -> `{2:2, 0:1}`).
        4.  Check if all digits required for `n` are available in sufficient quantities from `digits`' `Counter`.
        5.  If yes, increment count.
        6.  Return total count. (No set needed as `n` is inherently distinct).

**3. Important Time/Space Complexity Facts:**
    *   Let `N = len(digits)` (max 10).
    *   Let `M = 450` (fixed count of 3-digit even numbers).
    *   **Brute-Force Permutations:**
        *   Time: O(N^3). (For N=10, 1000 operations, very fast).
        *   Space: O(M) for the `set`, effectively O(1).
    *   **Optimal (Iterate Target Numbers):**
        *   Time: O(M) or effectively O(1) as M is a fixed constant. (450 iterations, each constant time operations).
        *   Space: O(1) for Counters (max 10 distinct digits).
    *   **Overall:** Both approaches are highly efficient due to the extremely small input constraints.

**4. Critical Edge Cases:**
    *   **No even numbers possible:** `digits = [1,3,5]` -> Correctly outputs 0.
    *   **Only one unique number:** `digits = [6,6,6]` -> Correctly outputs 1 (for 666).
    *   **Presence of zeros:** `digits = [0,2,2]` -> Correctly outputs 2 (for 202, 220).
        *   Handles no leading zero (`022` rejected).
        *   Handles using available duplicate digits (`2` appears twice).
    *   **Duplicate digits in input:** `digits = [1,2,2,3]` -> Correctly allows `122`. Handled by index distinctness (brute-force) or frequency counts (optimal).

**5. Key Patterns/Techniques Used:**
    *   **Iterating Output Space vs. Input Space:** When the target output range is small and fixed (like 3-digit even numbers here), iterating through the *output* candidates and validating is often more robust and cleaner than generating combinations/permutations from the *input*.
    *   **Frequency Maps (`collections.Counter`):** Indispensable for problems involving tracking counts of available/needed elements (digits, characters). Simplifies availability checks.
    *   **Sets for Uniqueness:** Automatically handles duplicate results when generation might produce the same number via different input permutations.
    *   **Systematic Constraint Handling:** Explicitly checking for "no leading zero" and "even number" conditions.