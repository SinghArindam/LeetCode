Here's a set of atomic notes for LeetCode problem 3799 - Unique 3-Digit Even Numbers:

-   **Concept**: Problem Goal - Count Distinct 3-Digit Even Numbers
    **Context**: The primary objective is to find how many unique numbers exist that meet all specified criteria.
    **Example**: Given `digits = [1,2,2]`, `122` is one such number. If `212` can also be formed, both count.

-   **Concept**: Three-Digit Number Constraint
    **Context**: Formed numbers must fall within the range of 100 to 999 inclusive.
    **Example**: `100` is valid, `99` is not.

-   **Concept**: Even Number Constraint
    **Context**: The formed number's units (last) digit must be an even number (0, 2, 4, 6, or 8).
    **Example**: `124` is valid, `123` is not.

-   **Concept**: No Leading Zero Constraint
    **Context**: The hundreds (first) digit of the formed number cannot be 0.
    **Example**: `012` is invalid, `102` is valid.

-   **Concept**: Digit Copy Usage Rule
    **Context**: Each *specific copy* of a digit from the input `digits` array can be used only once per formed number.
    **Example**: If `digits = [1,2,2]`, forming `122` uses `digits[0]=1`, `digits[1]=2`, and `digits[2]=2`. This means `222` would not be possible if `digits` only contains two `2`s.

-   **Concept**: Counting Distinct Final Numbers
    **Context**: If the same numerical value (e.g., 122) can be formed in multiple ways using different digit copies from the input, it should only be counted once in the final result.
    **Example**: If `digits = [1,2,2]` can form `122` using `digits[1]` for tens and `digits[2]` for units, and also using `digits[2]` for tens and `digits[1]` for units, `122` is still counted only once.

-   **Concept**: Input Array Size Constraint (Small N)
    **Context**: The `digits.length` is very small (3 to 10). This implies that even approaches with polynomial time complexity relative to `N` (e.g., O(N^3)) will be performant enough.
    **Example**: For `N=10`, `N^3 = 1000`, which is a negligible number of operations.

-   **Concept**: Brute-Force Permutation Approach (Distinct Indices)
    **Context**: One solution involves using three nested loops to select three *distinct indices* (i, j, k) from the `digits` array. This naturally handles the "each copy once" rule by referencing unique positions.
    **Example**: `for i in range(n): for j in range(n): for k in range(n): if i!=j and j!=k and i!=k: ...`

-   **Concept**: Set for Uniqueness (Brute-Force Approach)
    **Context**: In permutation-based approaches, a `set` data structure is used to store the formed numbers. This automatically filters out duplicate numerical values, ensuring only distinct numbers are counted.
    **Example**: After forming a valid `num`, `s.add(num)` guarantees `num` is only stored once even if formed by different permutations of input digits.

-   **Concept**: Optimal Approach - Iterate Target Output Space
    **Context**: When the range of desired *output* values is fixed and relatively small (like 3-digit even numbers from 100 to 998), it's often more efficient to iterate through every possible output candidate and check if it can be formed from the given input digits.
    **Example**: Looping `for n in range(100, 1000, 2)` instead of generating permutations from `digits`.

-   **Concept**: Frequency Map (`collections.Counter`) for Digit Availability
    **Context**: To efficiently determine if a candidate number can be formed, `collections.Counter` (or a hash map) is used to store the counts of available digits from the input and required digits for the candidate number.
    **Example**: `c_available = collections.Counter(digits)` and `n_c = collections.Counter(int(d) for d in str(n))`.

-   **Concept**: Digit Availability Check Logic (Frequency Maps)
    **Context**: To validate if a number `n` can be formed, compare the counts of its constituent digits (from `n_c`) against the available counts of digits (from `c_available`). All required counts must be less than or equal to available counts.
    **Example**: `if c_available.get(digit, 0) < count_needed: is_formable = False; break`.

-   **Concept**: Time Complexity (Optimal Approach - Effectively O(1))
    **Context**: The approach iterating through all 3-digit even numbers (100-998) performs a fixed number of operations (450 iterations, each involving constant time frequency map lookups for 3 digits). Therefore, its time complexity is effectively constant.
    **Example**: `O(M * D)` where `M=450` (number of 3-digit evens) and `D=10` (number of distinct digits), thus `O(1)` overall.

-   **Concept**: Space Complexity (Frequency Maps - O(1))
    **Context**: Frequency maps for digits (0-9) will store at most 10 entries (constant `D` digits). This makes their space usage constant.
    **Example**: `collections.Counter` objects require O(1) auxiliary space.

-   **Concept**: Handling Edge Case - No Even Numbers Possible
    **Context**: If the input `digits` array contains no even digits (e.g., `[1,3,5]`), the solution must correctly return 0.
    **Example**: Brute-force: `digits[k] % 2 == 0` check will always fail. Optimal: `is_formable` will always be `False` because no even digits are available in `c_available`.

-   **Concept**: Handling Edge Case - Presence of Zeros
    **Context**: The algorithms must correctly handle the digit 0: rejecting it as a leading digit, but allowing it in tens or units place if available.
    **Example**: For `digits = [0,2,2]`, `022` is rejected, but `202` and `220` are valid numbers and correctly counted.

-   **Concept**: General Pattern - Iterating Output Space vs. Input Space
    **Context**: A common optimization for combinatorial problems where the desired *output* domain is small and enumerable. It's often more efficient to check each possible output rather than generating and filtering combinations/permutations from the input.
    **Example**: The optimal solution in LeetCode 3799 demonstrates this by iterating through 100-998 directly.

-   **Concept**: General Pattern - Frequency Maps for Resource Tracking
    **Context**: `collections.Counter` (or a hash map) is an indispensable tool for problems that involve tracking counts of available or required elements (like digits, characters, or items) to fulfill certain conditions.
    **Example**: Used to manage the "each copy once" rule by comparing `count_needed` with `c_available`.

-   **Concept**: General Pattern - Sets for Distinct Result Aggregation
    **Context**: When a generation process might produce the same result through different input paths, using a `set` is the most straightforward and efficient way to store and count only unique final results.
    **Example**: Crucial in the brute-force approach to ensure `122` is counted only once even if multiple permutations form it.

-   **Concept**: General Principle - Small Constraints Allow Simpler Solutions
    **Context**: When problem constraints are extremely small, a conceptually simpler "brute-force" approach (even if theoretically less optimal) is often acceptable and faster to implement, as performance impact is minimal.
    **Example**: An O(N^3) solution for `N=10` is perfectly fine and often preferred for its simplicity.