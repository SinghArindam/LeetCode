Here are concise short notes for quick revision of LeetCode problem 13-roman-to-integer:

---

**LeetCode 13: Roman to Integer - Quick Revision Notes**

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Convert Roman numeral string (e.g., "MCMXCIV") to integer.
*   **Symbols & Values:** I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
*   **Additive Rule (General):** Numerals usually sum up (e.g., "XII" = 10+1+1=12).
*   **Subtractive Rule (Exceptions):**
    *   I before V or X (IV=4, IX=9).
    *   X before L or C (XL=40, XC=90).
    *   C before D or M (CD=400, CM=900).
*   **Constraints:**
    *   `1 <= s.length <= 15` (Input string is very short).
    *   Contains only valid Roman characters.
    *   **Guaranteed valid Roman numeral** in range `[1, 3999]` (simplifies, no validation needed).

**2. Core Algorithmic Approach (Based on Provided Solution):**
*   **Strategy:** String Replacement / Normalization.
*   **Steps:**
    1.  Create mappings for single Roman characters and special two-character subtractive pairs.
    2.  **Crucially: Iterate and replace all *subtractive pairs first*** (e.g., "IV" -> "4 ", "CM" -> "900 "). Append a space to facilitate splitting.
    3.  Then, iterate and replace all remaining *single characters* (e.g., "I" -> "1 ", "M" -> "1000 ").
    4.  Split the resulting string by spaces and sum up all the converted integer parts.

**3. Time/Space Complexity Facts:**
*   **Provided Solution (String Replacement):**
    *   **Time:** O(N) - String `replace` operations take O(N) for string copies/scans. Since there's a constant number of replacements, it's effectively O(N) total.
    *   **Space:** O(N) - For the modified string and the list created by `s.split()`.
*   **Optimal Alternative (Right-to-Left Parsing):**
    *   **Time:** O(N) - Single pass through the string.
    *   **Space:** O(1) - Constant space for the dictionary map. (Generally preferred for elegance and pure O(1) space).

**4. Critical Edge Cases to Remember:**
*   **Guaranteed Valid Input:** This is a major simplification. You don't need to handle invalid Roman numeral formats.
*   **Smallest input:** "I" (handles correctly as a single char).
*   **Purely Additive:** "III", "MDCLXVI" (subtractive rules won't trigger).
*   **Purely Subtractive:** "IV", "CM" (handled by explicit rules or right-to-left logic).
*   **Mixed Cases:** "MCMXCIV", "LVIII" (demonstrates combining additive and subtractive rules).
*   **Short String Constraint (N <= 15):** Makes less efficient O(N) or O(N*k) solutions perfectly acceptable performance-wise.

**5. Key Patterns or Techniques Used:**
*   **Mapping / Dictionary:** Essential for quick symbol-to-value lookups.
*   **Prioritized Processing:** Handling special rules (subtraction) before general rules (addition) is a common strategy.
*   **String Transformation:** Converting input into a more parsable form (like space-separated numbers).
*   **Right-to-Left Iteration (Optimal Pattern):** A powerful technique for problems where a character's value depends on its *right* neighbor (e.g., if current < right, subtract; else add). This elegantly captures the subtractive rule in one pass.