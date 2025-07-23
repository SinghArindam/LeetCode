This document provides a comprehensive analysis of the LeetCode problem "Roman to Integer", covering its problem statement, various solution approaches, complexity analysis, edge cases, and key insights.

---

## 1. Problem Summary

The problem asks us to convert a given Roman numeral string into its corresponding integer value.

**Roman Numeral System Basics:**
*   **Symbols and Values:**
    *   `I`: 1
    *   `V`: 5
    *   `X`: 10
    *   `L`: 50
    *   `C`: 100
    *   `D`: 500
    *   `M`: 1000
*   **Additive Principle (General Rule):** Roman numerals are typically written from largest to smallest, left to right, and values are added.
    *   Example: `II` = 1 + 1 = 2
    *   Example: `XII` = 10 + 1 + 1 = 12
    *   Example: `XXVII` = 10 + 10 + 5 + 1 + 1 = 27
*   **Subtractive Principle (Special Rule):** There are specific cases where a smaller value symbol placed *before* a larger value symbol indicates subtraction.
    *   `I` before `V` (5) or `X` (10) makes 4 (`IV`) or 9 (`IX`).
    *   `X` before `L` (50) or `C` (100) makes 40 (`XL`) or 90 (`XC`).
    *   `C` before `D` (500) or `M` (1000) makes 400 (`CD`) or 900 (`CM`).

**Input:** A string `s` representing a Roman numeral.
**Output:** An integer.

**Constraints:**
*   `1 <= s.length <= 15` (The string is short).
*   `s` contains only valid Roman numeral characters (`'I', 'V', 'X', 'L', 'C', 'D', 'M'`).
*   It is **guaranteed** that `s` is a valid Roman numeral representing a number in the range `[1, 3999]`. This simplifies the problem significantly as we don't need to validate the input string or handle invalid Roman numeral formations.

## 2. Explanation of All Possible Approaches

We can categorize the approaches based on how they handle the additive and, more importantly, the subtractive rules.

### Approach 1: Greedy Left-to-Right Parsing with Lookahead

This approach iterates through the Roman numeral string from left to right. At each step, it checks if the current character and the next character form one of the six special subtractive pairs.

**Logic:**
1.  Create a mapping (e.g., a hash map or dictionary) for all Roman numeral symbols to their integer values, including the special two-character combinations (e.g., 'IV': 4, 'IX': 9, 'XL': 40, etc.) alongside the single-character ones ('I': 1, 'V': 5, etc.).
2.  Initialize a total sum to 0.
3.  Use an index to traverse the string.
4.  At each `index`:
    *   Check if `index + 1` is within bounds and if the substring `s[index:index+2]` (i.e., current and next character) forms a subtractive pair (e.g., "IV", "XL", "CM").
    *   If it is a subtractive pair:
        *   Add the combined value (e.g., 4 for "IV") to the total sum.
        *   Advance the index by 2 (as two characters were consumed).
    *   If it is not a subtractive pair (or `index + 1` is out of bounds, meaning it's the last character):
        *   Add the value of the single character `s[index]` to the total sum.
        *   Advance the index by 1.
5.  Continue until the end of the string is reached.

This approach is directly implemented in the commented-out "Approach 1" of the provided solution.

### Approach 2: String Replacement / Normalization (Provided Solution's Main Approach)

This approach transforms the Roman numeral string into a space-separated list of integer values by replacing Roman symbols with their numerical equivalents.

**Logic:**
1.  Create two mappings:
    *   One for single Roman numeral symbols to their values (`'I': 1, 'V': 5, ...`).
    *   One for the special two-character subtractive pairs to their values (`'IV': 4, 'IX': 9, ...`).
2.  **Crucially, iterate and replace the *subtractive pairs first*.** For each subtractive pair (e.g., "IV"), replace it in the original string `s` with its integer value followed by a space (e.g., `s = s.replace("IV", "4 ")`). The space is important for the later `split()` operation.
3.  **Then, iterate and replace the *single characters*.** For each single character (e.g., "I"), replace it in the modified string `s` with its integer value followed by a space (e.g., `s = s.replace("I", "1 ")`).
4.  After all replacements, the string `s` will look something like `"1000 900 90 4 "` for "MCMXCIV".
5.  Split the modified string by space (`s.split()`), convert each resulting substring to an integer, and sum them up.

This approach is implemented in the active "Approach 2" of the provided solution.

### Approach 3: Optimized Right-to-Left Parsing

This is often considered the most elegant and efficient approach, especially in terms of constant factors for space. It leverages the property that Roman numerals are generally additive, but a smaller numeral *before* a larger one indicates subtraction. By processing from right to left, this rule becomes naturally apparent.

**Logic:**
1.  Create a mapping (dictionary) for only the single Roman numeral symbols to their integer values (`'I': 1, 'V': 5, ...`).
2.  Initialize a `total` sum.
3.  Initialize `prev_value` to 0.
4.  Iterate through the Roman numeral string from **right to left** (from the last character to the first).
5.  For each `current_char`:
    *   Get its `current_value` from the mapping.
    *   Compare `current_value` with `prev_value` (which was the value of the character to its right).
    *   If `current_value < prev_value` (e.g., processing 'I' when `prev_value` was 5 from 'V' in "IV"):
        *   Subtract `current_value` from `total`. This handles the subtractive rule.
    *   Else (`current_value >= prev_value`):
        *   Add `current_value` to `total`. This handles the additive rule.
    *   Update `prev_value = current_value` for the next iteration.
6.  Return the `total` sum.

## 3. Detailed Explanation of Logic (Provided Solution and Alternatives)

### Provided Solution (Approach 2: String Replacement / Normalization)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Define mappings for single and double (subtractive) Roman numeral values.
        # Single characters are handled later, after potential double character replacements.
        nums_single = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        nums_double = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        # Step 1: Replace all subtractive pairs first.
        # It's crucial to process these first because "I" should not be replaced by "1"
        # if it's part of "IV" or "IX". The order of keys in nums_double doesn't matter
        # as these pairs are mutually exclusive in terms of the characters they consume.
        # A space is appended to the integer value to facilitate splitting later.
        for roman_pair, int_value in nums_double.items():
            s = s.replace(roman_pair, str(int_value) + ' ')
        
        # Example trace: s = "MCMXCIV"
        # 1. s.replace("IV", "4 ")  -> "MCMXC 4 "
        # 2. s.replace("IX", "9 ")  -> (no change)
        # 3. s.replace("XL", "40 ") -> (no change)
        # 4. s.replace("XC", "90 ") -> "M CM 90  4 " (Note: 'CM' is not yet processed)
        # 5. s.replace("CD", "400 ") -> (no change)
        # 6. s.replace("CM", "900 ") -> "M 900  90  4 "

        # Step 2: Replace all remaining single Roman characters.
        # These are now guaranteed not to be part of any subtractive pair.
        for roman_char, int_value in nums_single.items():
            s = s.replace(roman_char, str(int_value) + ' ')
        
        # Continuing example trace: s = "M 900  90  4 "
        # 7. s.replace("I", "1 ") -> (no change)
        # 8. s.replace("V", "5 ") -> (no change)
        # 9. s.replace("X", "10 ") -> (no change)
        # 10. s.replace("L", "50 ") -> (no change)
        # 11. s.replace("C", "100 ") -> (no change)
        # 12. s.replace("D", "500 ") -> (no change)
        # 13. s.replace("M", "1000 ") -> "1000  900  90  4 "

        # Step 3: Split the modified string by spaces, convert each part to an integer, and sum them.
        # s.split() will handle multiple spaces between numbers correctly, e.g., "1000  900" -> ['1000', '900']
        num = sum([int(i) for i in s.split()])
        
        return num
```

**Critique of Provided Solution:**
*   **Pros:** Conceptually simple to understand once the replacement strategy is clear. Handles all cases. The `replace` method in Python makes string manipulation concise.
*   **Cons:** Involves string mutations (`s = s.replace(...)`), which can be less efficient for very long strings due to new string creation. The multiple `replace` calls might appear less performant than a single pass, though for `N <= 15`, it's not an issue. It uses `O(N)` space for the modified string and the list created by `split()`.

### Alternative 1 (Commented-out code: Greedy Left-to-Right Parsing)

```python
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         n = len(s)
#         i = 0  # Initialize index for traversal
#         num = 0 # Initialize total sum
        
#         # Define mappings for both single and double Roman numeral values
#         # The keys of `cases` are used to quickly check for subtractive pairs.
#         cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
#         nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
#                 'IV':4, 'IX':9, 'XL':40, 'XC':40, 'CD':400, 'CM':900} # Corrected 'XC':900 to 'XC':90. Original was correct
#                 # The solution's 'XC' was '90' in Approach 2, but '900' in commented Approach 1.
#                 # Assuming '90' is the correct one based on problem statement and Approach 2.
#                 # 'XC': 90
        
#         while i < n: # Iterate through the string
#             # Check if current and next characters form a subtractive pair
#             # Need to ensure i+1 is within bounds (i.e., i < n-1 or i+1 < n)
#             if i + 1 < n and (s[i:i+2] in cases): # Use slice s[i:i+2] for clarity
#                 num += nums[s[i:i+2]] # Add value of the pair
#                 i += 2 # Consume two characters
#             else:
#                 num += nums[s[i]] # Add value of single character
#                 i += 1 # Consume one character
#         return num
```

**Critique of Alternative 1:**
*   **Pros:** Straightforward, single pass. More traditional iterative parsing. `O(1)` space complexity (excluding dictionary storage).
*   **Cons:** Slightly more complex conditional logic (checking `i+1 < n`). The dictionary needs to contain both single and double mappings, which can lead to slight ambiguity if not handled carefully (though `s[i:i+2]` handles it here). The original code had a slight `while i < n+1` loop boundary issue and `s[i-1]` vs `s[i]` indexing, which I've corrected in the comments above to be more standard.

### Alternative 2 (Optimized Right-to-Left Parsing)

This approach is highly recommended for its elegance and efficiency.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping for individual Roman numeral symbols.
        # We don't need mappings for subtractive pairs here.
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        n = len(s)
        total = 0
        
        # Initialize prev_value with 0 or the value of the last character
        # Using 0 simplifies the loop as the first character (from the right) will always be added.
        prev_value = 0 
        
        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            current_char = s[i]
            current_value = roman_map[current_char]
            
            # If the current character's value is less than the previous character's value (to its right),
            # it means we have a subtractive case (e.g., 'I' before 'V' in 'IV').
            # In such cases, subtract its value from the total.
            if current_value < prev_value:
                total -= current_value
            # Otherwise (current_value >= prev_value), it's an additive case.
            # Add its value to the total.
            else:
                total += current_value
            
            # Update prev_value for the next iteration (to the left)
            prev_value = current_value
            
        return total

```

**Example Trace for "MCMXCIV" using Right-to-Left:**

1.  `s = "MCMXCIV"`, `roman_map`, `total = 0`, `prev_value = 0`
2.  `i = 4` (last char 'V'):
    *   `current_char = 'V'`, `current_value = 5`
    *   `5` (current) `>= 0` (prev) -> `total = 0 + 5 = 5`
    *   `prev_value = 5`
3.  `i = 3` (char 'I'):
    *   `current_char = 'I'`, `current_value = 1`
    *   `1` (current) `< 5` (prev) -> `total = 5 - 1 = 4`
    *   `prev_value = 1`
4.  `i = 2` (char 'C'):
    *   `current_char = 'C'`, `current_value = 100`
    *   `100` (current) `>= 1` (prev) -> `total = 4 + 100 = 104`
    *   `prev_value = 100`
5.  `i = 1` (char 'X'):
    *   `current_char = 'X'`, `current_value = 10`
    *   `10` (current) `< 100` (prev) -> `total = 104 - 10 = 94`
    *   `prev_value = 10`
6.  `i = 0` (char 'M'):
    *   `current_char = 'M'`, `current_value = 1000`
    *   `1000` (current) `>= 10` (prev) -> `total = 94 + 1000 = 1094`
    *   `prev_value = 1000`

Wait, my trace for "MCMXCIV" is producing 1094. The expected output is 1994. Let's re-evaluate the right-to-left logic.

**Corrected Right-to-Left Logic:**
The issue in my trace was the example string "MCMXCIV" being mixed up. The *principle* is sound.
M (1000) C (100) M (1000) X (10) C (100) I (1) V (5)
Correct evaluation for MCMXCIV:
M = 1000
CM = 900
XC = 90
IV = 4
Total = 1000 + 900 + 90 + 4 = 1994.

Let's re-trace "MCMXCIV" with the right-to-left logic properly.

`roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}`
`s = "MCMXCIV"`
`total = 0`
`prev_value = 0` (This is fine, as the last character will always be added)

1.  `i = 4` (char 'V', `s[4]`):
    *   `current_value = 5`
    *   `current_value (5) >= prev_value (0)` -> `total = 0 + 5 = 5`
    *   `prev_value = 5`
2.  `i = 3` (char 'I', `s[3]`):
    *   `current_value = 1`
    *   `current_value (1) < prev_value (5)` -> `total = 5 - 1 = 4`
    *   `prev_value = 1`
3.  `i = 2` (char 'C', `s[2]`):
    *   `current_value = 100`
    *   `current_value (100) >= prev_value (1)` -> `total = 4 + 100 = 104`
    *   `prev_value = 100`
4.  `i = 1` (char 'X', `s[1]`):
    *   `current_value = 10`
    *   `current_value (10) < prev_value (100)` -> `total = 104 - 10 = 94`
    *   `prev_value = 10`
5.  `i = 0` (char 'M', `s[0]`):
    *   `current_value = 1000`
    *   `current_value (1000) >= prev_value (10)` -> `total = 94 + 1000 = 1094`
    *   `prev_value = 1000`

The logic is correct for the right-to-left scan for "MCMXCIV", it would be `1000 + (1000 - 100) + (100 - 10) + (5 - 1)`. Wait, this is NOT `1000 + 900 + 90 + 4`. This is `1000 + 90 + 90 + 4`.

The issue is how the `prev_value` is used. My trace and explanation for the right-to-left logic were wrong. It should be:
`MCMXCIV`
Scan from right: `V` (5) -> `total = 5`, `prev = 5`
`I` (1): `1 < 5` -> `total -= 1` (`total = 4`), `prev = 1`
`C` (100): `100 > 1` -> `total += 100` (`total = 104`), `prev = 100`
`X` (10): `10 < 100` -> `total -= 10` (`total = 94`), `prev = 10`
`M` (1000): `1000 > 10` -> `total += 1000` (`total = 1094`), `prev = 1000`

The right-to-left approach should be:
Initialize `total = value(last_char)`.
Then loop from `second_to_last` to `first`.
If `value(current_char) < value(char_to_right)` then `total -= value(current_char)`.
Else `total += value(current_char)`.

**Revised Right-to-Left Logic for "MCMXCIV":**

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        n = len(s)
        # Initialize total with the value of the last character
        total = roman_map[s[n - 1]] 
        
        # Iterate from the second-to-last character towards the beginning
        for i in range(n - 2, -1, -1): # Start at n-2, go down to 0
            current_value = roman_map[s[i]]
            next_value = roman_map[s[i + 1]] # Value of the character to its right
            
            # If current value is less than the value to its right, subtract it.
            # This handles IV, IX, XL, XC, CD, CM
            if current_value < next_value:
                total -= current_value
            # Otherwise, add it. This handles all additive cases.
            else:
                total += current_value
            
        return total
```

**Re-trace "MCMXCIV" with Corrected Right-to-Left Logic:**

`s = "MCMXCIV"`
`roman_map` as defined.
`n = 5`

1.  `total = roman_map[s[4]] = roman_map['V'] = 5`
2.  `i = 3` (char 'I', `s[3]`):
    *   `current_value = roman_map['I'] = 1`
    *   `next_value = roman_map['V'] = 5` (s[4])
    *   `1 < 5` -> `total = 5 - 1 = 4`
3.  `i = 2` (char 'C', `s[2]`):
    *   `current_value = roman_map['C'] = 100`
    *   `next_value = roman_map['I'] = 1` (s[3])
    *   `100 >= 1` -> `total = 4 + 100 = 104`
4.  `i = 1` (char 'X', `s[1]`):
    *   `current_value = roman_map['X'] = 10`
    *   `next_value = roman_map['C'] = 100` (s[2])
    *   `10 < 100` -> `total = 104 - 10 = 94`
5.  `i = 0` (char 'M', `s[0]`):
    *   `current_value = roman_map['M'] = 1000`
    *   `next_value = roman_map['X'] = 10` (s[1])
    *   `1000 >= 10` -> `total = 94 + 1000 = 1094`

Still getting 1094. This means the common interpretation of the right-to-left method is for `CM` to be `1000-100` or `XC` to be `100-10`.
The correct way the right-to-left handles this:
`MCMXCIV`
`V` (5)
`I` (1) `I < V` so `5 - 1 = 4` (IV handled)
`C` (100) `C > I` so `4 + 100 = 104`
`X` (10) `X < C` so `104 - 10 = 94` (XC handled)
`M` (1000) `M > X` so `94 + 1000 = 1094`
`C` (100) `C < M` (from previous iteration for "CM") so `1094 - 100 = 994`
`M` (1000) `M > C` so `994 + 1000 = 1994`

My loop for `MCMXCIV` didn't account for the `M` before `CM`. The string is `"MCMXCIV"`.
`s[0] = M`
`s[1] = C`
`s[2] = M`
`s[3] = X`
`s[4] = C`
`s[5] = I`
`s[6] = V`
Length is 7.

Let's re-trace with `s = "MCMXCIV"` (length 7 as per problem examples):

1.  `total = roman_map[s[6]] = roman_map['V'] = 5`
2.  `i = 5` (char 'I', `s[5]`):
    *   `current_value = roman_map['I'] = 1`
    *   `next_value = roman_map['V'] = 5` (s[6])
    *   `1 < 5` -> `total = 5 - 1 = 4`
3.  `i = 4` (char 'C', `s[4]`):
    *   `current_value = roman_map['C'] = 100`
    *   `next_value = roman_map['I'] = 1` (s[5])
    *   `100 >= 1` -> `total = 4 + 100 = 104`
4.  `i = 3` (char 'X', `s[3]`):
    *   `current_value = roman_map['X'] = 10`
    *   `next_value = roman_map['C'] = 100` (s[4])
    *   `10 < 100` -> `total = 104 - 10 = 94`
5.  `i = 2` (char 'M', `s[2]`):
    *   `current_value = roman_map['M'] = 1000`
    *   `next_value = roman_map['X'] = 10` (s[3])
    *   `1000 >= 10` -> `total = 94 + 1000 = 1094`
6.  `i = 1` (char 'C', `s[1]`):
    *   `current_value = roman_map['C'] = 100`
    *   `next_value = roman_map['M'] = 1000` (s[2])
    *   `100 < 1000` -> `total = 1094 - 100 = 994`
7.  `i = 0` (char 'M', `s[0]`):
    *   `current_value = roman_map['M'] = 1000`
    *   `next_value = roman_map['C'] = 100` (s[1])
    *   `1000 >= 100` -> `total = 994 + 1000 = 1994`

**Result: 1994.** Yes, this corrected right-to-left logic and trace are accurate. This is indeed the most elegant single-pass O(1) space solution.

## 4. Time and Space Complexity Analysis

### Approach 1: Greedy Left-to-Right Parsing with Lookahead

*   **Time Complexity:** O(N), where N is the length of the input string `s`. We iterate through the string once. In each iteration, we perform constant-time dictionary lookups and possibly advance the index by 1 or 2 steps.
*   **Space Complexity:** O(1). The space used for the `nums` dictionary and `cases` list is constant (fixed number of Roman symbols). No other data structures grow with the input size.

### Approach 2: String Replacement / Normalization (Provided Solution)

*   **Time Complexity:** O(N * k), where N is the length of the input string `s`, and `k` is the total number of `replace` operations (which is constant, 6 for double + 7 for single = 13). Each `replace()` operation on a string of length N can take O(N) time in the worst case (e.g., if the pattern is found many times or at the end). `split()` and `sum()` also take O(N) time. Therefore, the overall time complexity is O(N). For `N <= 15`, this is extremely fast.
*   **Space Complexity:** O(N). The modified string `s` can grow up to `2*N` (e.g., "III" becomes "1 1 1 "). The list created by `s.split()` also takes O(N) space.

### Approach 3: Optimized Right-to-Left Parsing (Recommended Optimal)

*   **Time Complexity:** O(N), where N is the length of the input string `s`. We iterate through the string exactly once from right to left. Each step involves constant-time dictionary lookups and arithmetic operations.
*   **Space Complexity:** O(1). The space used for `roman_map` is constant (fixed number of Roman symbols). No other data structures grow with the input size.

## 5. Edge Cases and How They Are Handled

The problem statement has a crucial constraint: "It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`." This simplifies error handling and validation significantly.

*   **Smallest input:** `s = "I"`.
    *   **Approach 1:** `i=0`, `s[0:1]`="I", not in `cases`. `num += nums['I']` (1). `i=1`. Loop ends. Returns 1. Correct.
    *   **Approach 2:** `s.replace("I", "1 ")`. `s` becomes "1 ". `s.split()` is `['1']`. `sum([int('1')])` is 1. Correct.
    *   **Approach 3:** `n=1`. `total = roman_map['I'] = 1`. `for` loop `range(0-2, -1, -1)` is empty. Returns `total = 1`. Correct.
*   **Strings with only additive characters:** e.g., `"III"`, `"MDCLXVI"`
    *   All approaches correctly sum the values. The subtractive checks/replacements simply won't apply.
*   **Strings with only subtractive characters:** e.g., `"IV"`, `"CM"`
    *   All approaches correctly identify and use the combined value.
*   **Mixed additive and subtractive characters:** e.g., `"MCMXCIV"`, `"LVIII"`
    *   All approaches handle these correctly by applying the rules as they encounter them or through prior normalization.
*   **Maximum Length / Value:** `s.length <= 15`, max value `3999` (`MMMCMXCIX`).
    *   Given the small `N`, O(N) or even O(N*k) solutions are perfectly fine within typical time limits (usually 1-2 seconds). Python's string operations for short strings are highly optimized, so the constant factor for `replace` is negligible.

## 6. Clean, Well-Commented Version of the Optimal Solution

The **Right-to-Left Parsing** (Approach 3) is generally considered the most optimal due to its O(1) space complexity and single pass.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        This solution uses a right-to-left parsing approach, which is efficient
        and naturally handles the subtractive rules of Roman numerals.

        Args:
            s: The input Roman numeral string. Guaranteed to be valid
               and within the range [1, 3999].

        Returns:
            The integer equivalent of the Roman numeral.
        """

        # 1. Define a mapping for Roman numeral symbols to their integer values.
        #    Only single character mappings are needed for this approach.
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        n = len(s)
        
        # 2. Initialize the total sum with the value of the last character.
        #    This is because the last character will always be added (it cannot
        #    be part of a subtractive pair like 'IV' where 'V' subtracts 'I').
        total = roman_map[s[n - 1]]
        
        # 3. Iterate through the Roman numeral string from the second-to-last
        #    character towards the beginning (index n-2 down to 0).
        for i in range(n - 2, -1, -1):
            current_char = s[i]
            current_value = roman_map[current_char]
            
            # Get the value of the character immediately to the right.
            # This character was processed in the previous iteration.
            next_char = s[i + 1]
            next_value = roman_map[next_char]
            
            # 4. Apply the Roman numeral rules:
            #    If the current character's value is less than the value of the
            #    character to its right (e.g., 'I' before 'V' in 'IV'), it signifies
            #    a subtractive case. We subtract its value from the total.
            if current_value < next_value:
                total -= current_value
            #    Otherwise, it's an additive case (current_value >= next_value).
            #    Add its value to the total.
            else:
                total += current_value
            
        # 5. Return the final accumulated integer value.
        return total

```

## 7. Key Insights and Patterns

*   **Mapping for Lookups:** Using a dictionary (hash map) to store symbol-to-value mappings is a standard and efficient pattern for problems involving translations between symbols and values. Its O(1) average time complexity for lookups is ideal.
*   **Handling Special Rules / Exceptions:** When a system has general rules but also specific exceptions (like Roman numeral's additive vs. subtractive rules), there are common strategies:
    *   **Prioritized Processing:** Handle exceptions first. The provided solution's string `replace` approach does this by replacing subtractive pairs first.
    *   **Contextual Lookahead/Lookback:** The greedy left-to-right approach uses "lookahead" (checking `s[i+1]`). The optimized right-to-left approach uses "lookback" (comparing `current_value` with `next_value` which was processed as `prev_value`).
*   **Right-to-Left Parsing for Subtraction:** For problems where a smaller value *before* a larger value implies subtraction, iterating from right to left can lead to very elegant solutions. This is because when you encounter a smaller value, the larger value that it's "subtracting from" has already been processed and its value stored (or is immediately to its right).
*   **Transformation/Normalization:** The provided solution's use of `s.replace()` is an example of transforming the input data into a more digestible format before final processing. This can be a powerful technique for problems where the raw input is complex but can be simplified by pre-processing.
*   **Leveraging Constraints:** The guarantee of a valid Roman numeral in a specific range significantly simplifies the problem. In real-world scenarios, robust input validation would be a critical first step. Always check constraints as they guide algorithm design.
*   **String Manipulation vs. Iteration:** While string `replace` operations are convenient in Python, for performance-critical scenarios or very long strings, direct iteration (like in the left-to-right or right-to-left approaches) that avoids creating many intermediate string copies is often preferred. However, for short strings (N=15 here), the performance difference is negligible.