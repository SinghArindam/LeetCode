Here are the atomic notes for LeetCode problem 2021-remove-all-occurrences-of-a-substring, formatted for spaced repetition learning:

-   **Concept**: Problem Goal - Repeated Leftmost Substring Removal
    -   **Context**: The objective is to repeatedly find and remove the *leftmost* occurrence of a `part` string within a main string `s` until no more occurrences of `part` exist.
    -   **Example**: For `s = "daabcbaabcbc"` and `part = "abc"`, the process is:
        1. `da**abc**baabcbc` -> `dabaabcbc`
        2. `daba**abc**bc` -> `dababc`
        3. `dab**abc**` -> `dab`. Final result: `dab`.

-   **Concept**: Challenge of Cascading Removals
    -   **Context**: Removing a substring can cause previously non-adjacent characters to become adjacent, potentially forming new occurrences of the `part` string.
    -   **Example**: If `s = "axxxxyyyyb"` and `part = "xy"`, after removing the first "xy" (from "axxx**xy**yyb"), the string becomes "axxxxyyyb". The remaining 'y' can now form a new "xy" with the 'x' before it, leading to further removals.

-   **Concept**: Naive Approach - Direct Simulation
    -   **Context**: This approach directly implements the problem description by repeatedly using string `find` to locate the leftmost `part` and string `erase` to remove it in a loop.
    -   **Example**: `while (s.find(part) != string::npos) { s.erase(s.find(part), part.length()); }`

-   **Concept**: Inefficiency of Naive String Operations
    -   **Context**: String operations like `string::find` (O(N*M)) and `string::erase` (O(N), especially if not at the end) on large strings can be computationally expensive when performed repeatedly in a loop.
    -   **Example**: For `s` and `part` lengths up to 1000, `string::find` and `string::erase` within a loop can lead to `O(N^2 * M)` complexity, which is too slow (e.g., `1000^3 = 10^9` operations).

-   **Concept**: Optimized Approach - Stack-like String Building
    -   **Context**: Instead of modifying `s` in-place, build a new `result` string character by character. This `result` string effectively acts like a stack.
    -   **Example**: Loop through `s`, append `c` to `result`, then check the end of `result` for `part`.

-   **Concept**: Implicit Handling of "Leftmost" in Stack Approach
    -   **Context**: By processing `s` from left to right and checking for `part` at the *end* of the `result` string, the stack-like approach naturally addresses the "leftmost" requirement. Any `part` formed by newly added characters combined with existing `result` characters represents the earliest (leftmost) opportunity for a match in the currently evolving string.
    -   **Example**: When `result` becomes `...XYZ` where `XYZ` is `part`, it's removed. This is the leftmost occurrence that *can be formed* at this point in the sequential scan.

-   **Concept**: Core Logic of Stack-like Solution (Append & Conditional Remove)
    -   **Context**: Iterate through each character `c` of the input string `s`. Append `c` to `result`. If `result` is at least as long as `part` and `result` ends with `part`, remove `part` from `result`'s end.
    -   **Example**:
        ```cpp
        result.push_back(c);
        if (result.size() >= pLen && result.compare(result.size() - pLen, pLen, part) == 0) {
            result.erase(result.size() - pLen, pLen);
        }
        ```

-   **Concept**: Efficient String Operations for Stack Approach
    -   **Context**: `std::string::push_back` has amortized O(1) time complexity. `std::string::erase` from the end of a string is efficient, taking O(M) time (where M is the length of the substring being erased), avoiding costly character shifts.
    -   **Example**: Using `result.push_back(c)` and `result.erase(result.size() - pLen, pLen)` is significantly faster than repeated `s.find()` and `s.erase(mid_pos, len)` operations.

-   **Concept**: Time Complexity of Optimized Approach
    -   **Context**: The optimized (stack-like) solution iterates through each character of `s` once. Inside the loop, string operations (push_back, compare, erase) take at most `O(M)` time (where M is `part.length()`).
    -   **Example**: Total time complexity is `O(N * M)` for `N = s.length()` and `M = part.length()`. For N, M = 1000, this is `10^6` operations, which is efficient.

-   **Concept**: Space Complexity of Optimized Approach
    -   **Context**: The `result` string can grow up to the original length of `s` in the worst case (e.g., if `part` is never found).
    -   **Example**: The space complexity is `O(N)`.

-   **Concept**: Edge Case - `part` Longer Than `s`
    -   **Context**: If the `part` string is longer than the current `result` string (which initially starts as `s`), no matches for `part` can be formed.
    -   **Example**: If `s = "abc"` and `part = "abcd"`, `result` will accumulate to "abc". The condition `result.size() >= pLen` will never be met for a match, and `s` ("abc") will be returned correctly.

-   **Concept**: Edge Case - `part` Not Found in `s`
    -   **Context**: If `part` never appears in `s` (or at the end of the `result` string), no removals occur.
    -   **Example**: If `s = "hello"` and `part = "xyz"`, `result` will become "hello" and be returned, as no `xyz` match is found.

-   **Concept**: Edge Case - `s` Consists of Repeated `part`
    -   **Context**: If the input string `s` is entirely composed of `part` repeated multiple times, the final `result` should be an empty string.
    -   **Example**: For `s = "abcabcabc"` and `part = "abc"`, each `abc` will be appended to `result` and then immediately removed, resulting in `""`.

-   **Concept**: Pattern - Stack-like Processing for Sequence Transformations
    -   **Context**: This pattern is highly effective for problems where processing an element in a sequence can "backtrack" or create new conditions involving previously processed elements, especially for removals or pair-matching.
    *   **Example**: Similar problems include "Remove All Adjacent Duplicates In String" (LeetCode 1047) and parentheses/bracket balancing problems.

-   **Concept**: Pattern - Prioritizing Efficient String Operations
    -   **Context**: When performing numerous modifications on a string in languages like C++ (`std::string`), prioritize operations that are efficient at the ends of the string (`push_back`, `pop_back`, `erase` from end) over costly operations in the middle (`find`, `insert`, `erase` in middle).
    *   **Example**: Using a temporary string built with `push_back` and `erase` from end, rather than repeatedly calling `find` and `erase` on the original string object.

-   **Concept**: Pattern - Greedy Approach in Local Optimization
    -   **Context**: The solution applies a greedy strategy by immediately removing `part` whenever it is formed at the end of the `result` string. This local decision contributes to achieving the global goal of removing all occurrences.
    -   **Example**: As soon as "abc" forms at the end of `result` (e.g., `dabc`), it's removed, without waiting for the full `s` to be processed, which helps expose subsequent matches.