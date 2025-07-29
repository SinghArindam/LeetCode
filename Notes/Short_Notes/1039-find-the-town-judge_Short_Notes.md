Here's a concise summary of the LeetCode problem "Find the Town Judge" (1039) for quick revision:

---

### LeetCode 1039: Find the Town Judge - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**

*   **Goal:** Find a unique "Town Judge" among `n` people (labeled 1 to `n`).
*   **Judge's Properties:**
    1.  Trusts nobody (Out-degree = 0).
    2.  Trusted by everyone else (`n-1` people) (In-degree = `n-1`).
    3.  Exactly one person satisfies both properties.
*   **Input:** `n` (total people), `trust` (list of `[a, b]` meaning `a` trusts `b`).
*   **Constraints:**
    *   `1 <= n <= 1000`
    *   `0 <= trust.length <= 10^4`
    *   `trust` pairs are **unique** and `a_i != b_i`.

**2. Core Algorithmic Approach (Optimal):**

*   **Method:** Single Trust Balance Array.
*   **Idea:** Track a "net trust score" for each person.
    *   Initialize `trust_balance` array of size `n+1` with zeros (for 1-based indexing).
    *   For each `[truster, trustee]` in `trust`:
        *   Decrement `trust_balance[truster]` by 1 (represents an outgoing trust).
        *   Increment `trust_balance[trustee]` by 1 (represents an incoming trust).
    *   **Judge's `trust_balance`:** Must be `n-1`. (0 outgoing trusts * -1 + `n-1` incoming trusts * +1).
*   **Steps:**
    1.  `if len(trust) < n - 1:` return `-1` (Early exit: not enough trusts for a judge to exist, unless `n=1`).
    2.  Process all `trust` relationships to populate `trust_balance`.
    3.  Iterate persons `1` to `n`: if `trust_balance[p] == n-1`, `p` is the judge, return `p`.
    4.  If loop finishes, no judge found, return `-1`.

**3. Important Time/Space Complexity Facts:**

*   **Time Complexity:** `O(N + M)`
    *   `O(N)` for array initialization and final scan.
    *   `O(M)` for processing `M` trust relationships.
*   **Space Complexity:** `O(N)` for the `trust_balance` array.

**4. Critical Edge Cases to Remember:**

*   **`n = 1`:** Person 1 is always the judge. (Handled correctly: `n-1=0`, balance will be 0 if `trust` is empty).
*   **`trust` array is empty (`M=0`):**
    *   If `n=1`, return 1.
    *   If `n>1`, no one trusts anyone, so no one can be trusted by `n-1` people. Returns -1 (often caught by early exit `len(trust) < n-1`).
*   **No judge exists:** The algorithm correctly returns `-1` if no person satisfies the `n-1` balance condition.
*   **Unique trust pairs & `a_i != b_i`:** Simplifies logic, no need to handle duplicates or self-trust.

**5. Key Patterns/Techniques Used:**

*   **Graph Representation:** Problem inherently models as a directed graph (people = nodes, trust = edges).
*   **In-degree/Out-degree:** The judge's properties directly map to these graph concepts.
*   **Accumulation/Balance Metric:** Combining in-degree and out-degree into a single score for efficiency and conciseness.
*   **Leveraging Problem Guarantees:** "Exactly one judge" allows immediate return upon finding a match.
*   **Early Exit Conditions:** Pre-checks improve average-case performance by identifying impossible scenarios quickly.
*   **1-Based Indexing:** Using `n+1` size arrays to directly map person labels to array indices.