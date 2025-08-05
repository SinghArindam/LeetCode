Here are concise short notes for quick revision of LeetCode problem 2050, "Count Good Numbers":

---

### LeetCode 2050: Count Good Numbers - Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Definition of "Good String":**
    *   Digits at **even indices** (0, 2, 4...) must be **even** (0, 2, 4, 6, 8) -> **5 choices**.
    *   Digits at **odd indices** (1, 3, 5...) must be **prime** (2, 3, 5, 7) -> **4 choices**.
*   **Output:** Total count of good strings of length `n`, **modulo (10^9 + 7)**.
*   **Crucial Constraint:** `1 <= n <= 10^15` (n is very large, requires efficient exponentiation).

**2. Core Algorithmic Approach:**
*   **Combinatorial Counting:** Choices for each position are independent.
*   **Count Even/Odd Indices:**
    *   Number of even positions: `even_count = (n + 1) // 2`
    *   Number of odd positions: `odd_count = n // 2`
*   **Total Combinations:** `(5 ^ even_count) * (4 ^ odd_count)`
*   **Modular Exponentiation (Binary Exponentiation):**
    *   **Purpose:** To compute `(base ^ exponent) % modulus` efficiently when `exponent` is very large.
    *   **Method:** Recursively (or iteratively) calculate `(base^(exp/2))^2` and multiply by `base` if `exp` is odd. Apply modulo at each multiplication.
    *   **Example (Python's `pow`):** `pow(base, exponent, modulus)`

**3. Important Time/Space Complexity:**
*   **Time Complexity:** `O(log n)`
    *   Dominated by two modular exponentiation calls, each taking `O(log(n/2))` which is `O(log n)`.
*   **Space Complexity:**
    *   `O(log n)` for recursive modular exponentiation (call stack depth).
    *   `O(1)` for iterative modular exponentiation or Python's built-in `pow()`.

**4. Critical Edge Cases / Considerations:**
*   **`n = 1`:**
    *   `even_count = (1+1)//2 = 1`
    *   `odd_count = 1//2 = 0`
    *   Result: `(5^1 * 4^0) % MOD = 5`. (Correct: "0", "2", "4", "6", "8").
*   **Maximum `n` (`10^15`):** Highlights the absolute necessity of **Modular Exponentiation**. Direct `5**large_exp` or `math.pow` will lead to **integer overflow** or **precision loss**.
*   **Modulo Arithmetic:** Must apply `% (10^9 + 7)` at *each multiplication step* within the power function and for the final product to prevent intermediate results from overflowing.

**5. Key Patterns/Techniques Used:**
*   **Combinatorial Counting (Principle of Multiplication):** Breaking down a problem into independent choices for positions.
*   **Modular Arithmetic:** Handling computations with very large intermediate results by applying modulo throughout.
*   **Modular Exponentiation (Binary Exponentiation):** Standard algorithm for efficient `(a^b % m)` calculation when `b` is large.
*   **Problem Decomposition:** Separating the problem into independent parts (even vs. odd indices).

---