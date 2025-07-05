## LeetCode Problem 2107: Find Unique Binary String

### 1. Problem Summary

Given an array of `n` unique binary strings, where each string has a length of `n`, the task is to return any binary string of length `n` that is not present in the input array `nums`.

**Key Constraints & Properties:**
*   `n == nums.length` (number of strings equals their length)
*   `1 <= n <= 16` (small `n` implies that exponential solutions might pass)
*   `nums[i].length == n`
*   `nums[i]` consists only of '0' or '1'.
*   All strings in `nums` are unique.
*   Any valid unique string is acceptable as an answer.

### 2. Explanation of Possible Approaches

We'll explore approaches ranging from a straightforward brute-force to the most optimal, constructive solution.

#### Approach 1: Brute-Force (Generate All & Linear Search)

**Concept:**
There are $2^n$ possible binary strings of length `n`. Since the input `nums` contains only `n` strings, and `n` is much smaller than $2^n$ (for `n >= 1`), there will always be at least one string that is not in `nums`. This approach systematically generates all possible binary strings from "00...0" to "11...1" and checks if each generated string exists in the `nums` array. The first one found that is not present is returned.

**Steps:**
1.  Iterate through all integers from `0` to `2^n - 1`.
2.  For each integer `k`, convert it into its `n`-bit binary string representation. This usually involves converting to binary and padding with leading zeros to ensure length `n`.
3.  For each generated binary string, iterate through the `nums` array to see if it matches any string.
4.  If a match is not found after checking all strings in `nums`, return the generated string.

#### Approach 2: Optimized Brute-Force (Using a Hash Set)

**Concept:**
This approach improves upon the basic brute-force by optimizing the lookup process. Instead of linearly searching through `nums` for each generated string, we first store all strings from `nums` into a hash set (`std::unordered_set` in C++, `HashSet` in Java, `set` in Python). This allows for average `O(string_length)` time complexity for checking existence.

**Steps:**
1.  Create a hash set and insert all strings from `nums` into it.
2.  Iterate through all integers from `0` to `2^n - 1`.
3.  Convert each integer `k` into its `n`-bit binary string representation.
4.  Check if the generated binary string exists in the hash set using the set's `count()` or `find()` method.
5.  If the string is *not* found in the hash set, return it.

#### Approach 3: Constructive Approach (Cantor's Diagonalization Principle) - Optimal Solution

**Concept:**
This is the approach implemented in the provided solution. It leverages a mathematical concept similar to Cantor's Diagonal Argument. Instead of searching, it directly constructs a unique string that is guaranteed not to be in `nums`.

**The Core Idea:**
Construct a new binary string `ans` of length `n`. For each position `i` (from `0` to `n-1`), the `i`-th character of `ans` is chosen to be different from the `i`-th character of the `i`-th string in `nums` (i.e., `nums[i][i]`).

**Steps:**
1.  Initialize an empty binary string `ans` of length `n`.
2.  Iterate `i` from `0` to `n-1`:
    *   Look at the `i`-th string in the input array: `nums[i]`.
    *   Consider its `i`-th character: `nums[i][i]`.
    *   Set the `i`-th character of `ans` (`ans[i]`) to be the *opposite* of `nums[i][i]`.
        *   If `nums[i][i]` is '0', set `ans[i]` to '1'.
        *   If `nums[i][i]` is '1', set `ans[i]` to '0'.
3.  After the loop, `ans` is the required unique binary string.

### 3. Detailed Explanation of Logic

#### Approach 1: Brute-Force (Generate All & Linear Search)
*   **Logic:** This method explores the entire search space. It's conceptually simple. The conversion from integer `k` to `n`-bit binary string typically involves a loop that repeatedly takes `k % 2` for the last bit and then `k /= 2`, or using built-in functions that convert integers to binary strings and then padding.
*   **Why it works:** As discussed, `2^n - n` strings will always be missing. This method is guaranteed to find one because it systematically checks every possibility.

#### Approach 2: Optimized Brute-Force (Using a Hash Set)
*   **Logic:** The use of a hash set (`std::unordered_set`) is a standard optimization technique for problems requiring frequent lookups. By pre-processing `nums` into a set, each `count()` or `find()` operation becomes, on average, `O(L)` where `L` is the string length (for hashing and potential comparison), instead of `O(N*L)` for a linear scan through the original `vector`. This significantly reduces the constant factor and improves average-case performance.
*   **Why it works:** Same reason as Approach 1: there's always a missing string, and the hash set just makes finding it faster.

#### Approach 3: Constructive Approach (Cantor's Diagonalization Principle) - Optimal
*   **Logic:** This approach is extremely elegant and efficient because it *constructs* the answer directly rather than searching for it.
    *   Let's say `nums` is:
        ```
        nums[0] = s0_0 s0_1 s0_2 ... s0_n-1
        nums[1] = s1_0 s1_1 s1_2 ... s1_n-1
        nums[2] = s2_0 s2_1 s2_2 ... s2_n-1
        ...
        nums[n-1] = sn-1_0 sn-1_1 sn-1_2 ... sn-1_n-1
        ```
    *   The `ans` string is constructed as follows:
        ```
        ans = a0 a1 a2 ... an-1
        ```
    *   Where `ai` is the opposite of `si_i` (the character on the "diagonal").
        *   `a0` = opposite of `s0_0`
        *   `a1` = opposite of `s1_1`
        *   `a2` = opposite of `s2_2`
        *   ...
        *   `an-1` = opposite of `sn-1_n-1`
*   **Why it works (Proof by Contradiction):**
    1.  Assume, for the sake of contradiction, that the constructed string `ans` *is* present in `nums`.
    2.  If `ans` is in `nums`, then `ans` must be equal to some `nums[k]` for some specific index `k` (where `0 <= k < n`).
    3.  If `ans == nums[k]`, then by definition, every character must be the same, so `ans[k]` *must be equal* to `nums[k][k]`.
    4.  However, by our construction method, we explicitly set `ans[k]` to be the *opposite* of `nums[k][k]`. Therefore, `ans[k] != nums[k][k]`.
    5.  This creates a contradiction: `ans[k] == nums[k][k]` (from assumption) and `ans[k] != nums[k][k]` (from construction) cannot both be true.
    6.  Therefore, our initial assumption that `ans` is present in `nums` must be false.
    7.  Hence, the constructed string `ans` is guaranteed to be unique and not present in `nums`.

### 4. Time and Space Complexity Analysis

Let `N` be `nums.length` (which is also the length of each string).

#### Approach 1: Brute-Force (Generate All & Linear Search)
*   **Time Complexity:**
    *   Generating `2^N` binary strings: `O(2^N * N)` (each string conversion takes `O(N)`).
    *   For each generated string, linear search through `N` strings in `nums`, each comparison takes `O(N)`. So, one lookup is `O(N * N)`.
    *   Total: `O(2^N * N^2)`.
    *   For `N = 16`, this is `2^16 * 16^2 = 65536 * 256 ≈ 1.6 * 10^7` operations. This might barely pass within typical time limits but is inefficient.
*   **Space Complexity:** `O(N)` to store the current generated string.

#### Approach 2: Optimized Brute-Force (Using a Hash Set)
*   **Time Complexity:**
    *   Populating the hash set with `N` strings, each of length `N`: `O(N * N)` on average.
    *   Generating `2^N` binary strings, each of length `N`: `O(2^N * N)`.
    *   For each generated string, checking presence in hash set: `O(N)` on average (for hashing and comparison).
    *   Total: `O(N^2 + 2^N * N)`. Since `2^N` dominates `N^2`, this simplifies to `O(2^N * N)`.
    *   For `N = 16`, this is `2^16 * 16 ≈ 10^6` operations. This is generally well within typical time limits.
*   **Space Complexity:** `O(N * N)` to store all `N` strings (each of length `N`) in the hash set.

#### Approach 3: Constructive Approach (Cantor's Diagonalization Principle) - Optimal
*   **Time Complexity:**
    *   The algorithm iterates `N` times (from `i = 0` to `N-1`).
    *   In each iteration, it performs constant time operations (accessing `nums[i][i]` and assigning `ans[i]`).
    *   Total: `O(N)`.
    *   For `N = 16`, this is `O(16)`, which is incredibly fast.
*   **Space Complexity:** `O(N)` to store the resulting `ans` string. (Does not count input storage).

### 5. Edge Cases and How They Are Handled

*   **Smallest `n` (`n = 1`)**:
    *   Input `nums = ["0"]`: The algorithm picks `nums[0][0]` which is '0'. It flips it to '1' and returns "1". Correct.
    *   Input `nums = ["1"]`: The algorithm picks `nums[0][0]` which is '1'. It flips it to '0' and returns "0". Correct.
    *   The constructive approach inherently handles `n=1` correctly, as the loop runs once and applies the logic.
*   **Largest `n` (`n = 16`)**:
    *   This is where the `O(N)` efficiency of the optimal solution shines. Even with `n=16`, the solution performs only 16 character flips, making it extremely fast. The brute-force methods would be significantly slower, though the hash set version would still likely pass.
*   **"All strings are unique"**: This simplifies the problem by removing the need to handle duplicates in the input. If duplicates were allowed, `nums.size()` could be less than `n` (the common length), potentially breaking the diagonal argument, but the problem statement explicitly avoids this.
*   **"Return any of them"**: This crucial phrase is what enables the constructive solution. If a specific unique string (e.g., the lexicographically smallest or largest) were required, the problem would become a search problem, and the hash set approach would be preferred (as it naturally iterates through strings in lexicographical order).

### 6. Clean, Well-Commented Version of the Optimal Solution

```cpp
#include <vector> // Required for std::vector
#include <string> // Required for std::string

class Solution {
public:
    std::string findDifferentBinaryString(std::vector<std::string>& nums) {
        // Get the number of strings, which by problem constraints, is also
        // the length of each individual binary string.
        int n = nums.size();
        
        // Initialize the result string 'ans' with 'n' characters.
        // The characters will be filled in the subsequent loop.
        std::string ans(n, ' '); 
        
        // This solution employs a constructive approach inspired by Cantor's Diagonalization principle.
        // The goal is to build a new binary string 'ans' such that it is guaranteed
        // to be different from every string already present in the 'nums' array.
        //
        // The strategy is as follows:
        // For each index 'i' from 0 to n-1:
        // 1. Consider the i-th string in the input array: nums[i].
        // 2. Look at the character at the i-th position within that string: nums[i][i].
        //    (This is the 'diagonal' element relative to the string's index).
        // 3. Set the i-th character of our answer string, ans[i], to be the opposite
        //    of nums[i][i].
        //    - If nums[i][i] is '0', set ans[i] to '1'.
        //    - If nums[i][i] is '1', set ans[i] to '0'.
        //
        // Proof of correctness (by contradiction):
        // Assume, for the sake of contradiction, that the constructed 'ans' string
        // IS present in the 'nums' array.
        // If 'ans' is in 'nums', then 'ans' must be identical to some specific string
        // nums[k] for some index 'k' (where 0 <= k < n).
        //
        // If ans == nums[k], then every character at every position must match.
        // Specifically, their k-th characters must be equal: ans[k] == nums[k][k].
        //
        // However, according to our construction logic, we explicitly set ans[k] to be
        // the opposite of nums[k][k].
        // Therefore, ans[k] != nums[k][k].
        //
        // We now have a contradiction: ans[k] == nums[k][k] AND ans[k] != nums[k][k].
        // This contradiction implies that our initial assumption (that 'ans' is in 'nums')
        // must be false.
        // Hence, the constructed string 'ans' is guaranteed to be a unique binary string
        // not found in the input 'nums' array.
        for (int i = 0; i < n; ++i) {
            // Flip the character at the i-th position of the i-th string.
            // If nums[i][i] is '0', make ans[i] '1'. Otherwise, make it '0'.
            ans[i] = (nums[i][i] == '0') ? '1' : '0';
        }
        
        // Return the uniquely constructed binary string.
        return ans;
    }
};

```

### 7. Key Insights and Patterns

*   **Cantor's Diagonalization**: This problem is a textbook example of applying Cantor's diagonalization argument in an algorithmic context. It's a powerful technique for constructing an element that is guaranteed to be outside a given set by systematically making it differ from each element in the set at a unique, corresponding position. This pattern is relatively rare but extremely efficient when applicable.
*   **Constructive Solutions vs. Search Solutions**: When a problem asks for "any valid answer" and the constraints are small (e.g., `N` is small), consider if a direct construction of the answer is possible, rather than just searching through all possibilities. Constructive proofs often lead to `O(N)` or `O(1)` solutions, which are significantly faster than search-based solutions (like `O(2^N)` or `O(N log N)`).
*   **Leveraging Constraints**: The specific constraints `n == nums.length` and `nums[i].length == n` are crucial. They create the square-like structure (`n` strings, each of length `n`) that allows for the diagonal strategy to work perfectly. If these constraints were different, the diagonal argument might not apply directly.
*   **Small `N` as a Hint**: While `N <= 16` allows `O(2^N * N)` solutions, the existence of an `O(N)` solution highlights the importance of always seeking a more optimal approach, even if a seemingly exponential one might pass. This problem serves as a good reminder that a simple observation can dramatically improve efficiency.
*   **Bit Manipulation/String Manipulation**: For binary string problems, remember that they can often be treated as integers (for generation) or manipulated character by character. The optimal solution here uses simple character manipulation.