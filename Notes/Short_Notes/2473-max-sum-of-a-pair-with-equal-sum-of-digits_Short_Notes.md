Here are concise short notes for quick revision of LeetCode problem 2473:

---

### **LeetCode 2473: Max Sum of a Pair With Equal Sum of Digits**

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Find maximum `nums[i] + nums[j]` where `i != j` and `sum_of_digits(nums[i]) == sum_of_digits(nums[j])`.
*   Return `-1` if no such pair exists.
*   **`nums[i]` are POSITIVE integers.** (Crucial for `0` sentinel).
*   **Constraints:**
    *   `N` (`nums.length`): `1 <= N <= 10^5` (Rules out `O(N^2)`).
    *   `nums[i]` value: `1 <= nums[i] <= 10^9` (Max 10 digits for `digitSum`).

**2. Core Algorithmic Approach (Optimized Solution):**
*   **Strategy:** Group numbers by their digit sum. For each group, find the two largest numbers.
*   **Data Structure:** `unordered_map<int, pair<int, int>> mp;`
    *   **Key:** `digit_sum` (int).
    *   **Value:** `pair<int, int>` storing `(largest_num, second_largest_num)` seen so far for that `digit_sum`.
        *   `p.first` = largest, `p.second` = second largest.
        *   Initialize values to `(0, 0)` (implicitly by `unordered_map` default for `int`).
*   **Steps:**
    1.  Helper function `digitSum(int num)`: Calculates sum of digits (`num % 10`, `num /= 10` loop).
    2.  Initialize `max_sum = -1`.
    3.  **Pass 1 (Populate Map):** Iterate `num` in `nums`:
        *   Calculate `s = digitSum(num)`.
        *   Update `mp[s]`'s pair:
            *   If `num > mp[s].first`: `mp[s].second = mp[s].first`, `mp[s].first = num`.
            *   Else if `num > mp[s].second`: `mp[s].second = num`.
    4.  **Pass 2 (Calculate Max Sum):** Iterate `(key, value_pair)` in `mp`:
        *   If `value_pair.second != 0` (meaning at least two positive numbers were found for this digit sum):
            *   `max_sum = max(max_sum, value_pair.first + value_pair.second)`.
    5.  Return `max_sum`.

**3. Important Time/Space Complexity Facts:**
*   **`digitSum` time:** `O(D)` where `D` is number of digits (`D <= 10` for `10^9`). Effectively `O(log(max_num))`.
*   **Map Size:** Max possible digit sum `M_DS` for `10^9` is `9*9=81`. So `M_DS` is a small constant.
*   **Time Complexity:** `O(N * D)`. (N numbers processed, each with `D` digit-sum calc and `O(1)` average map op).
*   **Space Complexity:** `O(M_DS)` for the map. Effectively `O(1)` as `M_DS` is a small constant (not dependent on N).

**4. Critical Edge Cases to Remember:**
*   **No valid pairs:** `max_sum` starts at `-1` and remains so if no pair meets criteria.
*   **Only one number for a digit sum:** `mp[s].second` will remain `0`, correctly skipping calculation for that `s`.
*   **Duplicate numbers in `nums`:** Handled correctly. E.g., `[18, 18]` for digit sum 9 will result in `mp[9] = {18, 18}`, yielding `18+18=36`. The logic finds the two largest values *among all occurrences*.
*   **`nums[i]` are positive:** Allows `0` to act as a reliable sentinel value for "not found" or "only one number found" in the `pair<int, int>`.

**5. Key Patterns or Techniques Used:**
*   **Grouping by Derived Property (Hashing):** Efficiently categorizing elements based on a computed attribute.
*   **Efficient Top-K (K=2) Finding:** Maintaining the two largest values directly with simple comparisons, avoiding full sorting of lists.
*   **Digit Manipulation:** Standard technique for number-based problems.
*   **Sentinel Value:** Using a specific value (`-1`, `0`) to represent initial states or specific edge conditions.
*   **Constraints-Driven Design:** `N=10^5` mandates an `O(N)` or `O(N log N)` solution. `nums[i]` range informs `digitSum` complexity and map size.