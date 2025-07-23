Here is a set of atomic notes generated from the comprehensive and short notes for LeetCode problem 13-roman-to-integer, formatted for spaced repetition:

- **Concept**: Problem Goal
- **Context**: LeetCode 13: Roman to Integer
- **Example**: Convert "MCMXCIV" to 1994.

- **Concept**: Roman Numeral Symbols and Values
- **Context**: Fundamental mapping for conversion.
- **Example**: `I=1`, `V=5`, `X=10`, `L=50`, `C=100`, `D=500`, `M=1000`

- **Concept**: Roman Numeral Additive Principle
- **Context**: General rule for Roman numeral conversion. Larger or equal value symbols typically add up.
- **Example**: `XII` = `X` (10) + `I` (1) + `I` (1) = 12

- **Concept**: Roman Numeral Subtractive Principle
- **Context**: Special rule where a smaller value symbol placed *before* a larger value symbol indicates subtraction.
- **Example**: `IV` (I before V) = 5 - 1 = 4

- **Concept**: Specific Subtractive Pairs
- **Context**: Exhaustive list of all valid subtractive combinations in Roman numerals.
- **Example**: `IV` (4), `IX` (9), `XL` (40), `XC` (90), `CD` (400), `CM` (900)

- **Concept**: Input String Length Constraint
- **Context**: Constraint on the input Roman numeral string `s`.
- **Example**: `1 <= s.length <= 15`. This indicates strings are very short.

- **Concept**: Input Validity Guarantee
- **Context**: Crucial constraint that simplifies problem solving.
- **Example**: `s` is **guaranteed** to be a valid Roman numeral representing a number in `[1, 3999]`. No input validation is required.

- **Concept**: Approach 1: Greedy Left-to-Right Parsing with Lookahead
- **Context**: Iterative solution strategy for conversion.
- **Example**: Check `s[i:i+2]` for a subtractive pair; if found, add combined value and advance by 2; otherwise, add `s[i]`'s value and advance by 1.

- **Concept**: Complexity of Left-to-Right Parsing Approach
- **Context**: Efficiency of the greedy left-to-right parsing method.
- **Example**: Time: O(N) due to single pass. Space: O(1) for constant map and variables.

- **Concept**: Approach 2: String Replacement / Normalization
- **Context**: Strategy used in the provided solution; transforms the string before summing.
- **Example**: Replace `IV` with `"4 "` then `I` with `"1 "`; then `split()` and `sum()`.

- **Concept**: Order of Replacement in String Replacement Approach
- **Context**: Critical detail for the string replacement strategy to work correctly.
- **Example**: **Subtractive pairs MUST be replaced *first*** (e.g., `IV` before `I`) to avoid incorrect partial replacements.

- **Concept**: Complexity of String Replacement Approach
- **Context**: Efficiency of the string replacement method.
- **Example**: Time: O(N) due to string `replace` operations (constant number of passes, each potentially O(N)). Space: O(N) for intermediate strings and split list.

- **Concept**: Approach 3: Optimized Right-to-Left Parsing
- **Context**: Most elegant and efficient solution strategy.
- **Example**: Iterate from right-to-left. If `current_value < value_to_its_right`, subtract `current_value`; else, add `current_value`.

- **Concept**: Complexity of Right-to-Left Parsing Approach
- **Context**: Efficiency of the optimized right-to-left parsing method.
- **Example**: Time: O(N) due to single pass. Space: O(1) for constant map and variables.

- **Concept**: Importance of Dictionary/Map for Lookups
- **Context**: General programming pattern for symbol-to-value conversions.
- **Example**: Using `{'I': 1, 'V': 5, ...}` for fast O(1) average-time value retrieval.

- **Concept**: Handling Exceptions with Prioritized Processing or Contextual Logic
- **Context**: General pattern for systems with regular rules and special cases.
- **Example**: In Roman numerals, handling subtractive rules before additive ones (as in string replacement) or using lookahead/lookback (as in single-pass iterations).

- **Concept**: Leverage Constraints in Algorithm Design
- **Context**: How problem constraints can simplify implementation.
- **Example**: The guarantee of a "valid Roman numeral" means no error checking or complex validation is needed, simplifying code.

- **Concept**: Performance for Short Strings
- **Context**: How string length constraints influence choice of algorithm.
- **Example**: For `N <= 15`, even O(N) operations involving string copies (like `replace` in Python) are fast enough, so the `O(N)` vs `O(1)` space difference might not be a practical concern.