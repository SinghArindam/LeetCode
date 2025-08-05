## Comprehensive Notes on LeetCode Problem 2050: Count Good Numbers

### 1. Problem Summary

The problem asks us to count the total number of "good" digit strings of a given length `n`. A digit string is defined as "good" if it satisfies two conditions:
1.  Digits at **even indices** (0-indexed: 0, 2, 4, ...) must be **even** (0, 2, 4, 6, 8).
2.  Digits at **odd indices** (0-indexed: 1, 3, 5, ...) must be **prime** (2, 3, 5, 7).

Since the number of good strings can be very large, the final answer must be returned modulo `10^9 + 7`. The input `n` can be as large as `10^15`.

**Example:**
*   For `n = 1`, good numbers are "0", "2", "4", "6", "8". Output: 5.
*   For `n = 4`, an example good number is "2582".
    *   Index 0 (even): '2' is even.
    *   Index 1 (odd): '5' is prime.
    *   Index 2 (even): '8' is even.
    *   Index 3 (odd): '2' is prime.

### 2. Explanation of All Possible Approaches

#### 2.1 Naive/Brute Force Approach (Impractical)

A naive approach would be to generate all possible digit strings of length `n` and then check each one for the "good" property.
*   There are `10^n` possible digit strings of length `n`.
*   Given `n` can be up to `10^15`, `10^10^15` is an astronomically large number. Generating and checking even a tiny fraction of these strings is impossible within practical time limits.
This approach immediately tells us that we need a mathematical, combinatorial approach.

#### 2.2 Combinatorial Approach (Core Idea)

The key insight is that the choice of a digit at any index is independent of the choice of a digit at any other index, as long as it adheres to its respective index type (even/odd).

Let's identify the number of valid choices for each type of index:
*   **For even indices (0, 2, 4, ...):** The allowed digits are `0, 2, 4, 6, 8`. There are **5** choices.
*   **For odd indices (1, 3, 5, ...):** The allowed digits are `2, 3, 5, 7`. There are **4** choices.

Now, we need to count how many even and odd indices exist for a given length `n`.
*   Let `count_even` be the number of even indices.
*   Let `count_odd` be the number of odd indices.

Consider examples:
*   If `n = 1`: Indices are `[0]`. `count_even = 1`, `count_odd = 0`.
*   If `n = 2`: Indices are `[0, 1]`. `count_even = 1`, `count_odd = 1`.
*   If `n = 3`: Indices are `[0, 1, 2]`. `count_even = 2`, `count_odd = 1`.
*   If `n = 4`: Indices are `[0, 1, 2, 3]`. `count_even = 2`, `count_odd = 2`.

From these patterns, we can derive the general formulas:
*   `count_even = (n + 1) // 2` (using integer division)
*   `count_odd = n // 2`

Let's verify:
*   `n=1`: `count_even = (1+1)//2 = 1`, `count_odd = 1//2 = 0`. Correct.
*   `n=2`: `count_even = (2+1)//2 = 1`, `count_odd = 2//2 = 1`. Correct.
*   `n=3`: `count_even = (3+1)//2 = 2`, `count_odd = 3//2 = 1`. Correct.
*   `n=4`: `count_even = (4+1)//2 = 2`, `count_odd = 4//2 = 2`. Correct.

Since the choices for each position are independent, the total number of good strings is the product of the number of choices for each position.
Total good numbers = (Choices for even index)^`count_even` * (Choices for odd index)^`count_odd`
Total good numbers = `5^count_even * 4^count_odd`

#### 2.3 Optimization: Modular Exponentiation

The exponents (`count_even` and `count_odd`) can be as large as `n/2`, which is `10^15 / 2 = 5 * 10^14`. Calculating `5^(5*10^14)` directly would result in an impossibly large number that exceeds standard integer data types. We need to compute this value modulo `10^9 + 7`.

This requires **Modular Exponentiation** (also known as Exponentiation by Squaring or Binary Exponentiation). This algorithm computes `(base^exponent) % modulus` in `O(log exponent)` time.

The general idea of modular exponentiation:
To compute `x^n % m`:
*   If `n = 0`, result is `1`.
*   If `n` is even, `x^n = (x^(n/2))^2`. So, `x^n % m = ((x^(n/2) % m) * (x^(n/2) % m)) % m`.
*   If `n` is odd, `x^n = x * x^(n-1) = x * (x^((n-1)/2))^2`. So, `x^n % m = (x % m * ((x^((n-1)/2) % m) * (x^((n-1)/2) % m)) % m) % m`.

By repeatedly halving the exponent, we reach the base case `n=0` in `O(log n)` steps. At each step, we perform a constant number of multiplications and modulo operations.

Therefore, the optimized approach is:
1.  Calculate `count_even = (n + 1) // 2`.
2.  Calculate `count_odd = n // 2`.
3.  Compute `term1 = (5 ^ count_even) % MOD` using modular exponentiation.
4.  Compute `term2 = (4 ^ count_odd) % MOD` using modular exponentiation.
5.  The final result is `(term1 * term2) % MOD`.

### 3. Detailed Explanation of the Provided Solution and Alternative Approaches

The provided solution explores several ways to implement the core combinatorial and modular exponentiation logic. All valid approaches essentially boil down to `(5^((n+1)//2) * 4^(n//2)) % MOD`.

The `MOD` value is `10^9 + 7`.

Let's analyze the approaches present in the solution code:

*   **`Approach 1` (Python's `pow` built-in)**
    ```python
    # mod = 10**9 + 7
    # even = (n + 1) // 2
    # odd = n // 2
    # a = pow(5, even, mod) # Python's built-in modular exponentiation
    # b = pow(4, odd, mod)
    # return (a * b) % mod
    ```
    This is the most concise and idiomatic Python solution. The `pow(base, exp, mod)` function efficiently calculates `(base^exp) % mod`. This is generally the preferred approach in Python due to its C-level implementation for speed.

*   **`Approach 2` (Combined base optimization)**
    ```python
    # mod = 10**9 + 7
    # p = pow(20, n // 2, mod) # Calculate (20^(n//2)) % mod
    # if n % 2 == 1:
    #     return (p * 5) % mod # If n is odd, there's one extra 5
    # return p
    ```
    This approach observes that `5^count_even * 4^count_odd` can be simplified.
    *   If `n` is even, `count_even = n/2` and `count_odd = n/2`.
        The expression becomes `5^(n/2) * 4^(n/2) = (5*4)^(n/2) = 20^(n/2)`.
    *   If `n` is odd, `count_even = (n+1)/2` and `count_odd = (n-1)/2`.
        The expression becomes `5^((n+1)/2) * 4^((n-1)/2) = 5 * 5^((n-1)/2) * 4^((n-1)/2) = 5 * (5*4)^((n-1)/2) = 5 * 20^((n-1)/2)`.
    This approach correctly combines the terms when possible, reducing one `pow` call. It's a clever optimization, but functionally equivalent to `Approach 1` in terms of complexity.

*   **`Approach 3` (Iterative Modular Exponentiation)**
    ```python
    # mod = 10**9 + 7
    # even = (n+1)//2
    # odd = n//2
    # def power(x, n, mod):
    #     res = 1
    #     while n>0:
    #         if n%2==1: # If current bit is 1, multiply result by x
    #             res = (res*x) % mod
    #         x = (x*x) % mod # Square x (x^2, x^4, x^8, ...)
    #         n = n//2 # Move to next bit
    #     return res
    # return (power(5, even, mod) * power(4, odd, mod)) % mod
    ```
    This approach implements the iterative version of modular exponentiation. It's a standard and efficient way to compute powers modulo `M` when the built-in `pow` is not available or desired.

*   **`Approach 4` (Recursive Modular Exponentiation - Uncommented Solution)**
    ```python
    mod = 10**9 + 7
    even = (n+1)//2
    odd = n//2
    def power(x, n, mod):
        if n == 0: # Base case: x^0 = 1
            return 1
        half = power(x, n//2, mod) # Calculate x^(n/2) recursively
        res = (half * half) % mod # x^n = (x^(n/2))^2
        if n%2==1: # If n is odd, multiply by x one more time
            res = (res*x) % mod
        return res
    return (power(5, even, mod) * power(4, odd, mod)) % mod
    ```
    This is the recursive implementation of modular exponentiation. It directly follows the mathematical definition of squaring and multiplying by `x` for odd exponents. This is the approach provided as the active solution.

*   **`Approach 5` (Bitwise calculation for even/odd counts)**
    ```python
    # mod = 10**9 + 7
    # odd = n >> 1 # Equivalent to n // 2 (bit shift for efficiency)
    # even = n - odd # Equivalent to (n+1)//2 when n is odd, n//2 when n is even.
                  # More precisely, if n is even, n = 2k, odd = k, even = 2k - k = k.
                  # If n is odd, n = 2k+1, odd = k, even = (2k+1) - k = k+1.
                  # This correctly calculates (n+1)//2 and n//2 for both cases.
    # a = pow(5, even, mod)
    # b = pow(4, odd, mod)
    # return (a * b) % mod
    ```
    This is functionally identical to `Approach 1` but uses bitwise operators (`>>`) for calculating `n // 2`, which can be slightly faster for integer division in some languages/contexts, though modern compilers/interpreters often optimize `// 2` similarly. The logic for `even` and `odd` counts is robust.

*   **`Approach 6` & `Approach 7` (Modular Exponentiation with Memoization/LRU Cache)**
    ```python
    # Approach 6 (Manual Memoization)
    # mod = 10**9 + 7
    # memo = {}
    # def power(b, exp):
    #     if (b, exp) in memo: return memo[(b, exp)]
    #     if exp == 0: return 1
    #     half = power(b, exp // 2)
    #     res = (half * half) % mod
    #     if exp % 2 == 1: res = (res * b) % mod
    #     memo[(b, exp)] = res
    #     return res
    # even = (n + 1) // 2
    # odd = n // 2
    # return (power(5, even) * power(4, odd)) % mod

    # Approach 7 (functools.lru_cache)
    # mod = 10**9 + 7
    # @lru_cache(None) # Requires 'from functools import lru_cache'
    # def power(b, exp):
    #     if exp == 0: return 1
    #     half = power(b, exp // 2)
    #     res = (half * half) % mod
    #     if exp % 2 == 1: res = (res * b) % mod
    #     return res
    # even = (n + 1) // 2
    # odd = n // 2
    # return (power(5, even) * power(4, odd)) % mod
    ```
    These approaches add memoization (either manual `memo` dictionary or `functools.lru_cache`) to the recursive modular exponentiation. While memoization is generally useful for dynamic programming or recursive functions with overlapping subproblems, it is **unnecessary overhead in this specific problem**. The `power` function is called only twice (once for base 5, once for base 4) with *different* exponent values (`even` and `odd`). There are no repeated `(base, exponent)` pairs for memoization to cache and reuse.

*   **`Approach 8` & `Approach 9` (Incorrect direct exponentiation)**
    ```python
    # Approach 8
    # m = 10**9 + 7
    # e = (n + 1) // 2
    # o = n // 2
    # return ((5**e) * (4**o)) % m # Fails for large n

    # Approach 9
    # m = 10**9 + 7
    # e = (n + 1) // 2
    # o = n // 2
    # res = (math.pow(5, e)%m) * (math.pow(4, o)%m) # Fails for large n
    # return (int(res) % m) %m
    ```
    These approaches demonstrate a common mistake: attempting to calculate `base^exponent` first and *then* applying the modulo. For `n` up to `10^15`, `e` and `o` can be up to `5 * 10^14`. `5^(5*10^14)` is an extremely large number that will **overflow** standard integer types (even Python's arbitrary precision integers will struggle with memory for such a colossal number) long before the modulo operation can be applied. `math.pow` operates on floats, which lose precision for large integers. This is precisely why **modular exponentiation** (where the modulo operation is applied at each step of multiplication) is indispensable.

### 4. Time and Space Complexity Analysis

The complexity analysis focuses on the optimal approach (which involves modular exponentiation).

*   **Time Complexity:**
    *   Calculating `count_even` and `count_odd`: O(1) operations (simple arithmetic).
    *   Modular exponentiation (`power(base, exp, mod)`): This algorithm runs in O(log `exp`) time. Since `exp` is `even` or `odd`, which are proportional to `n`, each `power` call takes O(log `n`) time.
    *   We perform two `power` calls and a final multiplication and modulo.
    *   Total Time Complexity: **O(log n)**. This is highly efficient and handles `n` up to `10^15` effectively.

*   **Space Complexity:**
    *   Variables for `mod`, `even`, `odd`, `a`, `b`: O(1) space.
    *   Recursive modular exponentiation (`Approach 4`): The recursion depth is `log n`, so it uses O(log `n`) space on the call stack.
    *   Iterative modular exponentiation (`Approach 3`): Uses O(1) space, as it avoids recursion.
    *   Built-in `pow()` (`Approach 1`, `5`): Uses O(1) auxiliary space (implementation details might vary but generally optimized for space).
    *   Memoization (`Approach 6`, `7`): If it were actually beneficial (which it isn't here), it would add O(log `n`) space for storing cached results.
    *   Total Space Complexity: **O(log n)** for the recursive solution, **O(1)** for iterative or built-in `pow`. Given `log(10^15)` is relatively small (around 50 for base 2), O(log n) space is perfectly acceptable.

### 5. Edge Cases

*   **`n = 1` (Minimum `n` from constraints):**
    *   `count_even = (1 + 1) // 2 = 1`
    *   `count_odd = 1 // 2 = 0`
    *   Result: `(5^1 * 4^0) % MOD = (5 * 1) % MOD = 5`.
    *   This matches Example 1, where good numbers are "0", "2", "4", "6", "8". The solution correctly handles this smallest `n`.

*   **Maximum `n` (`10^15`):**
    *   This is the primary reason why modular exponentiation is critical. The `O(log n)` time complexity ensures the solution remains efficient even for such large inputs, preventing time limit exceed or integer overflow.

*   **Modulo Operation:**
    *   The modulo `10^9 + 7` is a prime number often used in competitive programming. Applying modulo at each multiplication step (`(a * b) % M`) is crucial to prevent intermediate results from overflowing and to ensure the final result is within the required range. The `power` function correctly incorporates this.

### 6. Clean, Well-Commented Version of the Optimal Solution

We will use `Approach 4` (recursive modular exponentiation) as it was the uncommented one in the provided code, making it the "selected" optimal solution for detailed explanation.

```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Define the modulus as per problem statement: 10^9 + 7
        MOD = 10**9 + 7

        # Calculate the number of even and odd indices.
        # For a string of length n:
        # Even indices: 0, 2, 4, ...
        # Odd indices: 1, 3, 5, ...
        # If n is odd (e.g., n=3, indices 0,1,2), there's one more even index than odd.
        #   even_count = (3+1)//2 = 2, odd_count = 3//2 = 1
        # If n is even (e.g., n=4, indices 0,1,2,3), there's an equal number of even and odd indices.
        #   even_count = (4+1)//2 = 2, odd_count = 4//2 = 2
        even_indices_count = (n + 1) // 2
        odd_indices_count = n // 2

        # Define a helper function for modular exponentiation (x^n % mod)
        # This function calculates (base ^ exponent) % modulus efficiently.
        # It uses the "exponentiation by squaring" (binary exponentiation) algorithm.
        def power(base: int, exponent: int, modulus: int) -> int:
            # Base case: any number to the power of 0 is 1.
            if exponent == 0:
                return 1

            # Recursive step:
            # Calculate (base^(exponent // 2)) % modulus
            # This halves the exponent in each step, leading to O(log exponent) complexity.
            half_power = power(base, exponent // 2, modulus)

            # Square the result of half_power: (base^(exponent // 2))^2 = base^exponent
            # Apply modulo at each multiplication to prevent overflow.
            res = (half_power * half_power) % modulus

            # If the original exponent was odd, we missed one 'base' factor.
            # For example, x^5 = x * x^4 = x * (x^2)^2.
            # We already calculated (x^2)^2, so we need to multiply by 'x' one more time.
            if exponent % 2 == 1:
                res = (res * base) % modulus

            return res

        # Calculate the number of ways for even positions: 5 choices (0, 2, 4, 6, 8) raised to even_indices_count
        ways_even_pos = power(5, even_indices_count, MOD)

        # Calculate the number of ways for odd positions: 4 choices (2, 3, 5, 7) raised to odd_indices_count
        ways_odd_pos = power(4, odd_indices_count, MOD)

        # The total number of good strings is the product of ways for even and odd positions.
        # Apply modulo one final time.
        total_good_numbers = (ways_even_pos * ways_odd_pos) % MOD

        return total_good_numbers

```

### 7. Key Insights and Patterns

1.  **Combinatorial Counting / Principle of Multiplication:** When independent choices are made for different positions, the total number of arrangements is the product of the number of choices for each position. This is the fundamental principle applied here. For `N` positions, if position `i` has `C_i` choices, the total combinations are `C_1 * C_2 * ... * C_N`.
2.  **Modular Arithmetic for Large Numbers:** Problems asking for counts modulo a large prime (like `10^9 + 7`) almost always imply that intermediate results will exceed standard integer limits. The modulo operation must be applied at every multiplication step (`(A * B) % M = ((A % M) * (B % M)) % M`) to keep numbers within bounds and prevent overflow.
3.  **Modular Exponentiation (Binary Exponentiation / Exponentiation by Squaring):** This is a critical algorithm for calculating `(base^exponent) % modulus` efficiently when the exponent is very large. Its `O(log exponent)` time complexity makes problems with `n` up to `10^18` solvable. It's a standard pattern for competitive programming and algorithm questions.
4.  **Decomposition into Independent Subproblems:** The problem constraints for even indices are entirely separate from odd indices. This allows us to calculate the counts for each type of index independently and then multiply the results.
5.  **Understanding Indexing and Counts:** Carefully calculating the number of even vs. odd indices for a given `n` (especially considering `n` being odd or even) is a common mini-problem in combinatorial questions. Formulas like `(n+1)//2` and `n//2` or `n - (n//2)` are useful for this.
6.  **Avoid Premature Optimization (e.g., Memoization here):** While techniques like memoization are powerful, understand *when* they are beneficial. In this problem, `power` is called only twice with distinct parameters, so memoization provides no benefit and adds overhead.
7.  **Beware of Naive Exponentiation:** Directly using `**` or `math.pow` without integrated modulo for large exponents is a common pitfall that leads to overflow. Always use modular exponentiation when `exponent` is large and `modulo` is required.