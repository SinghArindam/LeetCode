Here is a set of atomic notes derived from the comprehensive and short notes for LeetCode problem 3447-clear-digits, formatted for spaced repetition learning:

---

-   **Concept**: LeetCode 3447 Problem Goal
    -   **Context**: Given a string `s` (lowercase English letters and digits), repeatedly remove the *first* digit and its *closest non-digit character to its left*. Return the final string.
    -   **Example**: `s = "cb34"` -> First '3' removes 'b', string becomes `"c4"`. Then '4' removes 'c', string becomes `""`. Result: `""`.

-   **Concept**: Input Guarantee for LeetCode 3447
    -   **Context**: The problem guarantees that it is always possible to delete all digits in the input string. This implies a valid non-digit will always be found to the left if needed for a deletion, or the digit can simply vanish if none exists.
    -   **Example**: N/A

-   **Concept**: Naive String Modification Approach
    -   **Context**: Directly simulating the deletion rule by repeatedly finding the first digit, then its closest left non-digit, and using a string `erase()` operation to remove both.
    -   **Example**: In C++, `s.erase(non_digit_idx, 1); s.erase(digit_idx - 1, 1);`

-   **Concept**: Time Complexity of Naive String Modification
    -   **Context**: Repeated `string::erase()` operations on a string or `std::vector` often lead to quadratic time complexity because each erase requires shifting subsequent characters, taking O(N) time.
    -   **Example**: For "Clear Digits" naive approach, `O(N^2)` because there can be up to N/2 deletions, each taking O(N).

-   **Concept**: Stack/LIFO Property for "Closest Left" Problems
    -   **Context**: Problems requiring operations on the "closest element to its left" (or most recently added/active element) can often be solved efficiently using a stack or a data structure that exhibits Last-In, First-Out (LIFO) behavior.
    -   **Example**: In LeetCode 3447, the "closest non-digit to its left" is precisely the last non-digit character `push_back`ed to the `result` string.

-   **Concept**: Building a New String for String Transformations
    -   **Context**: When performing deletions or insertions in a string, especially when positions change, it's generally more efficient and less error-prone to build a new result string (e.g., using `push_back`) rather than modifying the original string in-place with operations like `erase()`.
    -   **Example**: In LeetCode 3447, an empty `std::string ans;` is initialized, and characters are added/removed from its end.

-   **Concept**: Handling Non-Digit Characters (Letters) in Optimal Approach
    -   **Context**: When iterating through the input string, if the current character is a non-digit (letter), it is added to the temporary result string, making it a candidate for future consumption by a digit.
    -   **Example**: If `c` is `'a'`, `ans.push_back('a')`.

-   **Concept**: Handling Digit Characters in Optimal Approach
    -   **Context**: If the current character is a digit, it "consumes" the most recently added non-digit character. This means removing the last character from the temporary result string. The digit itself is not added.
    -   **Example**: If `c` is `'3'`, `ans.pop_back()` (after checking if `ans` is not empty).

-   **Concept**: Amortized O(1) Operations
    -   **Context**: Operations like `std::string::push_back()` and `std::string::pop_back()` (and `std::vector` equivalents) provide amortized constant time complexity. While a single operation might reallocate memory (O(N)), the average cost over many operations remains O(1).
    -   **Example**: The optimal solution for LeetCode 3447 achieves O(N) time complexity due to these amortized O(1) operations.

-   **Concept**: Time Complexity of Optimal Solution
    -   **Context**: The optimal solution involves a single pass through the input string, with each character processed in amortized O(1) time.
    -   **Example**: LeetCode 3447 optimal solution has a time complexity of `O(N)`.

-   **Concept**: Space Complexity of Optimal Solution
    -   **Context**: When building a new result string or container, the auxiliary space used can be up to the size of the original input.
    -   **Example**: LeetCode 3447 optimal solution uses `O(N)` space for the `ans` string in the worst case (e.g., input contains no digits).

-   **Concept**: Edge Case: Input String with No Digits
    -   **Context**: How the algorithm behaves if the input string contains only non-digit characters.
    -   **Example**: If `s = "abc"`, the optimal solution will `push_back` all characters, resulting in `"abc"`. The `isdigit()` check is never true.

-   **Concept**: Edge Case: Input String with Only Digits
    -   **Context**: How the algorithm behaves if the input string contains only digit characters.
    -   **Example**: If `s = "123"`, the `ans.pop_back()` operation is always skipped because `ans` remains empty. The result is `""`.

-   **Concept**: Edge Case: Input String Starting with a Digit
    -   **Context**: How the algorithm handles a digit character at the very beginning of the input string.
    -   **Example**: If `s = "1ab"`, the '1' is processed, `ans` is empty, so `pop_back()` is skipped. The '1' effectively "vanishes". Subsequent letters 'a' and 'b' are added. Result: `"ab"`.

-   **Concept**: Greedy Approach Principle
    -   **Context**: A problem-solving strategy where the algorithm makes the locally optimal choice at each step with the hope that this choice will lead to a globally optimal solution. Often applicable when rules are deterministic and localized.
    -   **Example**: LeetCode 3447's rule to remove the *first* digit and *closest left* non-digit allows for a single-pass greedy solution.

-   **Concept**: Character Classification Utility
    -   **Context**: Using standard library functions to robustly determine the type of a character (e.g., digit, letter, alphanumeric).
    -   **Example**: `std::isdigit(c)` is used in C++ to check if character `c` is a digit.