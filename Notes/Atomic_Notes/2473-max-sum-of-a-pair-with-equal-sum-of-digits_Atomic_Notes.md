Here's a set of atomic notes generated from the comprehensive and short notes for LeetCode problem 2473:

-   **Concept**: Problem Goal - Maximum Pair Sum
-   **Context**: Find the maximum `nums[i] + nums[j]` from a given array `nums`.
-   **Example**: Where `i != j` and `sum_of_digits(nums[i]) == sum_of_digits(nums[j])`.

-   **Concept**: Default Return Value
-   **Context**: If no pair of distinct numbers with equal digit sums is found.
-   **Example**: Return `-1`.

-   **Concept**: Input Constraint - Array Size (N)
-   **Context**: `nums.length` is up to `10^5`.
-   **Example**: This constraint rules out `O(N^2)` brute-force solutions as too slow.

-   **Concept**: Input Constraint - Element Value
-   **Context**: `nums[i]` can be up to `10^9`.
-   **Example**: This means `nums[i]` can have at most 10 digits (e.g., `999,999,999`), impacting `digitSum` calculation time.

-   **Concept**: Input Constraint - Positivity of Elements
-   **Context**: All `nums[i]` are positive integers (`>= 1`).
-   **Example**: This property is crucial for using `0` as a reliable sentinel value in the `unordered_map`'s `pair` values.

-   **Concept**: Naive Approach - Brute Force
-   **Context**: Checks all possible distinct pairs `(nums[i], nums[j])`.
-   **Example**: Using nested loops where `0 <= i < j < nums.length` and calculating `digitSum` for each pair.

-   **Concept**: Brute Force Time Complexity
-   **Context**: For the naive brute-force approach.
-   **Example**: `O(N^2 * D)`, where `D` is the number of digits. Too slow for `N=10^5`.

-   **Concept**: Optimized Approach - Grouping Strategy
-   **Context**: The core idea to efficiently find pairs with equal digit sums.
-   **Example**: Group numbers in the array by their calculated sum of digits.

-   **Concept**: Digit Sum Calculation Algorithm
-   **Context**: How to compute the sum of digits for an integer.
-   **Example**: `int s = 0; while (num > 0) { s += num % 10; num /= 10; } return s;`

-   **Concept**: Digit Sum Calculation Time Complexity
-   **Context**: For the `digitSum` helper function.
-   **Example**: `O(D)` or `O(log10(num))`, where `D` is the number of digits (at most 10 for `10^9`).

-   **Concept**: Optimized Data Structure
-   **Context**: Used to store grouped numbers efficiently.
-   **Example**: `unordered_map<int, pair<int, int>> mp;` where key is `digit_sum`, value is `(largest_num, second_largest_num)`.

-   **Concept**: Sentinel Value for `pair` Initialization
-   **Context**: How `0` is used in the `unordered_map`'s `pair` values.
-   **Example**: `mp[s]` defaults to `{0, 0}`. Since `nums[i]` are positive, `0` reliably indicates an uninitialized slot or that only one number has been found.

-   **Concept**: Updating Top Two Values Logic
-   **Context**: Logic inside the first pass to maintain the largest (`p.first`) and second largest (`p.second`) numbers for a given digit sum.
-   **Example**: `if (num > p.first) { p.second = p.first; p.first = num; } else if (num > p.second) { p.second = num; }`

-   **Concept**: Two-Pass Algorithmic Strategy
-   **Context**: The overall structure of the optimized solution.
-   **Example**: First pass populates the `unordered_map`; second pass iterates the map to find the maximum sum.

-   **Concept**: Optimized Time Complexity
-   **Context**: The overall time complexity of the optimized solution.
-   **Example**: `O(N * D)` (N iterations, D time for `digitSum`, O(1) average for map ops). This is efficient for `N=10^5`.

-   **Concept**: Optimized Space Complexity
-   **Context**: The space complexity of the `unordered_map`.
-   **Example**: `O(M_DS)`, where `M_DS` is the maximum possible digit sum (~81 for `10^9`), making it effectively `O(1)` constant space.

-   **Concept**: Edge Case - No Valid Pairs Found
-   **Context**: How the problem handles scenarios where no numbers meet the criteria.
-   **Example**: The `max_sum` variable is initialized to `-1` and remains so if no valid pair is found.

-   **Concept**: Edge Case - Only One Number per Digit Sum
-   **Context**: How groups with fewer than two numbers are handled.
-   **Example**: If `mp[s].second` remains `0` after processing all numbers, it correctly indicates no second positive number was found, preventing invalid sum calculations.

-   **Concept**: Edge Case - Duplicate Numbers in Input
-   **Context**: How the solution handles `nums` containing identical values.
-   **Example**: `nums = [18, 18, 36]` results in `mp[9] = {36, 18}`, correctly finding the two largest values (36 and 18) for digit sum 9, even if they originated from duplicates or distinct values.

-   **Concept**: Algorithmic Pattern - Grouping by Derived Property
-   **Context**: A general technique where elements are categorized by a computed attribute.
-   **Example**: Using a hash map with `digit_sum` as keys to organize numbers.

-   **Concept**: Algorithmic Pattern - Efficient Top-K Finding (K=2)
-   **Context**: Strategy to find the largest two elements without sorting a full list.
-   **Example**: Maintaining `first_largest` and `second_largest` variables directly for each group.

-   **Concept**: Algorithmic Pattern - Digit Manipulation
-   **Context**: Common operations on numbers based on their digits.
-   **Example**: Calculating sum of digits using modulo and division by 10.

-   **Concept**: Algorithmic Pattern - Sentinel Value Usage
-   **Context**: Using specific values to represent initial states or special conditions.
-   **Example**: `-1` for `max_sum` initialization and `0` for `pair` elements.

-   **Concept**: Algorithmic Pattern - Constraints-Driven Design
-   **Context**: How problem constraints guide the choice of algorithm and data structures.
-   **Example**: `N=10^5` demands an `O(N)` or `O(N log N)` solution, ruling out `O(N^2)`.