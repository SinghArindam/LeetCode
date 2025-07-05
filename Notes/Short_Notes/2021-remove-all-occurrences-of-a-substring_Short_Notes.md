Here are concise notes for quick revision of LeetCode problem 2021: "Remove All Occurrences of a Substring".

---

### LeetCode 2021: Remove All Occurrences of a Substring

1.  **Key Problem Characteristics & Constraints:**
    *   **Goal:** Repeatedly remove the **leftmost** occurrence of `part` from `s` until no occurrences remain.
    *   **Input:** `s` (main string), `part` (substring to remove).
    *   **Constraints:** `1 <= s.length, part.length <= 1000`. Both consist of lowercase English letters.

2.  **Core Algorithmic Approach (Optimal Solution):**
    *   **Method:** Build a new string (`result`) acting like a stack.
    *   **Process:** Iterate through each character `c` of `s` from left to right:
        1.  Append `c` to `result` (`result.push_back(c)`).
        2.  **Crucial Step:** Check if `result` (the "active" modified string) now ends with `part`.
        3.  If `result` ends with `part`, remove `part` from the end of `result` (`result.erase(...)`).
    *   **Why it works (Leftmost):** This stack-like behavior naturally handles the "leftmost" requirement. By processing `s` left-to-right and immediately removing `part` when it forms at the `result`'s end, it ensures that any `part` that exists *at the current active end* (which corresponds to the leftmost currently available match in the evolving string) is removed first, including cascading removals.
    *   **Avoids:** Inefficient `string::find` on the whole string and costly mid-string `string::erase` operations inherent in a naive simulation.

3.  **Important Time/Space Complexity Facts:**
    *   **Optimal Solution (Stack-like):**
        *   **Time:** `O(N * M)`
            *   `N` iterations (for each char in `s`).
            *   Inside loop: `push_back` (amortized `O(1)`), `compare` and `erase` from end (`O(M)`) where `M` is `part.length()`.
        *   **Space:** `O(N)` (for the `result` string, which can grow up to `s.length()`).
    *   **Naive Simulation (Direct `string::find`/`erase` loop):**
        *   **Time:** `O(N^2 * M)` in worst case (too slow for `N, M = 1000`).

4.  **Critical Edge Cases to Remember:**
    *   **`part` not found in `s`:** `result` will simply become `s` (correct).
    *   **`s` is entirely `part` repeated (e.g., "abcabc", "abc"):** `result` will become an empty string (correct).
    *   **Cascading removals creating new matches:** The stack-like approach handles this automatically (e.g., `s="axxxxyyyyb"`, `part="xy"` -> `axxxx` after first `xy` removal, then `axxxy` forms and is removed, etc., leading to `ab`).
    *   **Constraints:** `s` and `part` are guaranteed not to be empty.

5.  **Key Patterns or Techniques Used:**
    *   **Stack-like Processing / Dynamic String:** Ideal for sequence transformation problems where operations (like removals) depend on the most recently added elements and can "backtrack" or expose earlier elements to new conditions. (Similar to: Remove All Adjacent Duplicates, Parentheses balancing).
    *   **Efficient String Manipulation:** Prioritizing `push_back` and `erase` from the end of a string over expensive `find`/`erase`/`insert` operations in the middle or beginning.
    *   **Greedy Approach:** Locally removing a `part` as soon as it forms at the end of `result` contributes to the global goal.