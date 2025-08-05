Here is a set of atomic notes for LeetCode problem 2050 "Count Good Numbers", formatted for spaced repetition learning:

---

1.  **Concept**: Problem Goal - Count "Good Numbers"
    **Context**: LeetCode 2050 asks to count the total number of "good" digit strings of a given length `n`.
    **Example**: For `n=1`, good strings are "0", "2", "4", "6", "8".

2.  **Concept**: Good String Rule - Even Indices
    **Context**: For a "good" digit string, digits at even 0-indexed positions (0, 2, 4, ...) must be even.
    **Example**: Allowed digits: 0, 2, 4, 6, 8 (5 choices).

3.  **Concept**: Good String Rule - Odd Indices
    **Context**: For a "good" digit string, digits at odd 0-indexed positions (1, 3, 5, ...) must be prime.
    **Example**: Allowed prime digits: 2, 3, 5, 7 (4 choices).

4.  **Concept**: Modulo Operation Requirement
    **Context**: The final count of good numbers must be returned modulo `10^9 + 7`. This indicates results can be extremely large.
    **Example**: If calculation yields `X`, return `X % (10^9 + 7)`.

5.  **Concept**: Input Constraint (Large `n`)
    **Context**: The input string length `n` can be up to `10^15`. This large value for `n` requires an efficient exponentiation method.
    **Example**: `n = 10^15` means exponents can be up to `~5 * 10^14`.

6.  **Concept**: Naive Approach Infeasibility
    **Context**: Generating and checking all `10^n` possible digit strings is computationally impossible for large `n`. This forces a mathematical/combinatorial approach.
    **Example**: `10^(10^15)` is an astronomically large number.

7.  **Concept**: Combinatorial Principle of Multiplication
    **Context**: When choices for different positions in a sequence are independent, the total number of arrangements is the product of the number of choices for each position.
    **Example**: If Position A has `X` choices and Position B has `Y` choices, total arrangements = `X * Y`.

8.  **Concept**: Calculating Count of Even Indices
    **Context**: For a string of length `n` (0-indexed), the number of even positions is determined by whether `n` is even or odd.
    **Example**: `count_even = (n + 1) // 2`. (e.g., `n=3` -> `(3+1)//2=2` (indices 0, 2); `n=4` -> `(4+1)//2=2` (indices 0, 2)).

9.  **Concept**: Calculating Count of Odd Indices
    **Context**: For a string of length `n` (0-indexed), the number of odd positions is determined by whether `n` is even or odd.
    **Example**: `count_odd = n // 2`. (e.g., `n=3` -> `3//2=1` (index 1); `n=4` -> `4//2=2` (indices 1, 3)).

10. **Concept**: Formula for Total Good Numbers
    **Context**: The total count of good numbers is the product of the number of choices for even positions raised to their count, and similarly for odd positions.
    **Example**: `Total Good Numbers = (5 ^ count_even) * (4 ^ count_odd)`.

11. **Concept**: Necessity of Modular Exponentiation
    **Context**: To compute `(base^exponent) % modulus` when the exponent is extremely large, modular exponentiation (also known as binary exponentiation or exponentiation by squaring) is crucial to prevent integer overflow.
    **Example**: Direct calculation of `5^(5*10^14)` will overflow standard data types.

12. **Concept**: Modular Exponentiation Algorithm (Principle)
    **Context**: This algorithm computes `(x^n) % m` in `O(log n)` time by recursively or iteratively leveraging the property that `x^n = (x^(n/2))^2` if `n` is even, and `x^n = x * (x^((n-1)/2))^2` if `n` is odd.
    **Example**: To compute `x^5 % m`, calculate `x^2 % m`, then `(x^2)^2 % m`, then `(result * x) % m`.

13. **Concept**: Modular Exponentiation (Modulo at Each Step)
    **Context**: To prevent intermediate results from overflowing, the modulo operation must be applied at *every multiplication step* within the modular exponentiation function, not just at the end.
    **Example**: `(A * B) % M` should be computed as `((A % M) * (B % M)) % M`.

14. **Concept**: Time Complexity of Solution
    **Context**: The dominant operation is two calls to modular exponentiation. Each call takes `O(log(exponent))` time. Since exponents are `O(n)`, the overall time complexity is highly efficient.
    **Example**: Total Time Complexity: `O(log n)`.

15. **Concept**: Space Complexity of Solution
    **Context**: The space complexity depends on the implementation of modular exponentiation. Recursive versions use call stack space, while iterative versions use constant space.
    **Example**: Recursive: `O(log n)` space (for call stack). Iterative/Python's `pow()`: `O(1)` space.

16. **Concept**: Modulus Value
    **Context**: The specific modulus for the problem, `10^9 + 7`, is a common large prime number used in competitive programming.

17. **Concept**: Edge Case `n=1`
    **Context**: The logic correctly handles the smallest `n`. For `n=1`, there's one even index (0) and zero odd indices.
    **Example**: `count_even = (1+1)//2 = 1`, `count_odd = 1//2 = 0`. Result: `(5^1 * 4^0) % MOD = 5`.

18. **Concept**: Pitfall - Direct Exponentiation
    **Context**: Directly computing `base**exponent` (e.g., in Python) or `math.pow(base, exponent)` (in Python/Java/C++) *before* applying modulo will lead to integer overflow or precision loss for large exponents.
    **Example**: `(5**(5*10^14)) % MOD` will fail because `5**(5*10^14)` is too large to store.

19. **Concept**: Python's Built-in `pow()` for Modular Exponentiation
    **Context**: Python's `pow(base, exp, mod)` function provides a highly optimized C-level implementation for modular exponentiation, making it the most concise and often preferred solution.
    **Example**: `result = pow(5, even_indices_count, MOD)`.

20. **Concept**: Unnecessary Memoization
    **Context**: Memoization (caching results of subproblems) is not beneficial for the `power` function in this problem because it is called only a few times with distinct `(base, exponent)` pairs, preventing significant cache hits.
    **Example**: `power(5, even_count, MOD)` and `power(4, odd_count, MOD)` are distinct calls that don't benefit from caching each other.

21. **Concept**: Problem Decomposition into Independent Subproblems
    **Context**: The problem can be naturally decomposed because the rules for even-indexed digits and odd-indexed digits are entirely independent of each other. This allows separate calculations and then multiplication of results.
    **Example**: Calculate ways for even positions, calculate ways for odd positions, then multiply the two results.