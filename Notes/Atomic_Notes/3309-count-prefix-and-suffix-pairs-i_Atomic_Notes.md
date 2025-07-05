Here is a set of atomic notes for LeetCode problem 3309-count-prefix-and-suffix-pairs-i, formatted for spaced repetition learning:

---

-   **Concept**: Problem Goal
    -   **Context**: Count specific pairs of strings `(words[i], words[j])` from a given array `words`.
    -   **Example**: Return total `(i, j)` where `i < j` and `words[i]` is a prefix AND suffix of `words[j]`.

-   **Concept**: Input Array Size Constraint (N)
    -   **Context**: The number of words in the input `words` array.
    -   **Example**: `1 <= words.length (N) <= 50`.

-   **Concept**: String Length Constraint (L)
    -   **Context**: The maximum length of any individual string in the `words` array.
    -   **Example**: `1 <= words[i].length (L) <= 10`.

-   **Concept**: Character Set Constraint
    -   **Context**: The type of characters allowed in the strings.
    -   **Example**: `words[i]` consists only of lowercase English letters.

-   **Concept**: Brute-Force Approach
    -   **Context**: The most straightforward solution strategy to count valid pairs.
    -   **Example**: Use nested loops to iterate through all possible unique pairs `(i, j)` where `i < j`.

-   **Concept**: Optimality of Brute-Force for Constraints
    -   **Context**: Why a simple brute-force approach is considered the best for this problem.
    -   **Example**: Given `N <= 50` and `L <= 10`, an `O(N^2 * L)` solution is extremely fast (`25,000` operations) and avoids complex overhead.

-   **Concept**: Iterating Unique Pairs (`i < j`)
    -   **Context**: Standard nested loop pattern to ensure each pair `(words[i], words[j])` is considered exactly once, with `i` always preceding `j`.
    -   **Example**:
        ```cpp
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                // Process (words[i], words[j])
            }
        }
        ```

-   **Concept**: `isPrefixAndSuffix` - Length Pre-check
    -   **Context**: An essential initial check when determining if `str1` is a prefix/suffix of `str2`.
    -   **Example**: `if (str1.length() > str2.length()) { return false; }`. A longer string cannot be a prefix or suffix of a shorter one.

-   **Concept**: `isPrefixAndSuffix` - Manual Prefix Check
    -   **Context**: How to programmatically check if `str1` is a prefix of `str2` using `substr`.
    -   **Example**: `(str2.substr(0, str1.length()) == str1)`.

-   **Concept**: `isPrefixAndSuffix` - Manual Suffix Check
    -   **Context**: How to programmatically check if `str1` is a suffix of `str2` using `substr`.
    -   **Example**: `(str2.substr(str2.length() - str1.length()) == str1)`.

-   **Concept**: `isPrefixAndSuffix` - C++20 `starts_with`
    -   **Context**: A concise and modern C++ feature for checking if a string begins with another.
    -   **Example**: `str2.starts_with(str1)`.

-   **Concept**: `isPrefixAndSuffix` - C++20 `ends_with`
    -   **Context**: A concise and modern C++ feature for checking if a string ends with another.
    -   **Example**: `str2.ends_with(str1)`.

-   **Concept**: Implicit Length Handling (C++20 `starts_with`/`ends_with`)
    -   **Context**: How C++20's string methods simplify length checks.
    -   **Example**: `str2.starts_with(str1)` and `str2.ends_with(str1)` will implicitly return `false` if `str1` is longer than `str2`.

-   **Concept**: Time Complexity Analysis
    -   **Context**: The total time required for the brute-force solution.
    -   **Example**: `O(N^2 * L)`, where `N` is `words.length` and `L` is `max(words[i].length)`.

-   **Concept**: Space Complexity Analysis
    -   **Context**: The auxiliary memory used by the brute-force solution.
    -   **Example**: `O(L)`, primarily for temporary string copies made during `substr` operations or aliases.

-   **Concept**: Edge Case: `words.length = 1`
    -   **Context**: How the algorithm handles an input array with only one word.
    -   **Example**: The nested loops (`j` starts from `i+1`) correctly result in `0` pairs being counted.

-   **Concept**: Edge Case: Identical Strings (`str1 == str2`)
    -   **Context**: Behavior when comparing a word to itself (if `i` and `j` were allowed to be equal) or two identical words in different positions.
    -   **Example**: `isPrefixAndSuffix("a", "a")` correctly evaluates to `true`, as a string is both a prefix and suffix of itself.

-   **Concept**: Edge Case: `str1.length() > str2.length()`
    -   **Context**: How the algorithm handles a candidate prefix/suffix string that is longer than the target string.
    -   **Example**: `isPrefixAndSuffix("abc", "ab")` correctly evaluates to `false` due to the initial length check.

-   **Concept**: Problem Decomposition (Helper Function)
    -   **Context**: Improving code readability and modularity by separating distinct logic.
    -   **Example**: Extracting the `isPrefixAndSuffix` condition into its own `bool` helper function.

-   **Concept**: Simplicity Principle for Small Constraints
    -   **Context**: A general approach to problem-solving, especially in competitive programming.
    -   **Example**: For problems with very small constraints, prioritize clear, correct, and simple solutions (like brute-force) over complex, theoretically faster but higher-overhead algorithms. Avoid premature optimization.