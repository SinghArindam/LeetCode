Here is a set of atomic notes for LeetCode problem 1387, formatted as requested:

-   **Concept**: Problem Goal - Contaminated Binary Tree Recovery
-   **Context**: Implement a `FindElements` class to recover a binary tree whose nodes are all `-1` (contaminated) and then efficiently check if a `target` value exists in the recovered tree.
-   **Example**: The constructor fixes the tree's values; the `find(target)` method returns `true` if `target` is one of the fixed values.

-   **Concept**: Root Node Value Rule
-   **Context**: During the recovery process, the root node's value is always initialized to `0`.
-   **Example**: If the input `root.val` is `-1`, it becomes `0` after recovery.

-   **Concept**: Left Child Value Rule
-   **Context**: For any node with an original value `x`, its left child's original value (if it exists) is determined by the formula `2 * x + 1`.
-   **Example**: A parent node with value `3` will have a left child with value `2*3 + 1 = 7`.

-   **Concept**: Right Child Value Rule
-   **Context**: For any node with an original value `x`, its right child's original value (if it exists) is determined by the formula `2 * x + 2`.
-   **Example**: A parent node with value `3` will have a right child with value `2*3 + 2 = 8`.

-   **Concept**: Tree Height Constraint Significance
-   **Context**: The maximum tree height of 20 is a small constraint that ensures recursive Depth-First Search (DFS) traversals will not cause a stack overflow.
-   **Example**: A recursive `recover` function's call stack depth will not exceed 20, which is well within typical system limits.

-   **Concept**: Node and Query Count Constraints
-   **Context**: There are up to 10^4 total nodes (N) and up to 10^4 total calls to the `find()` method (Q).
-   **Example**: An `O(N*Q)` approach (e.g., re-traversing the tree for each `find` call) would be `10^4 * 10^4 = 10^8` operations, which is too slow. This indicates a need for `O(N+Q)` or `O(N + Q log N)`.

-   **Concept**: Target Value Range & Data Type
-   **Context**: Target values range from `0` to `10^6`.
-   **Example**: Standard `int` data type is sufficient to store all possible target and recovered node values without overflow.

-   **Concept**: Pre-computation Strategy for Frequent Queries
-   **Context**: When an object is initialized and then subjected to many subsequent queries, it's efficient to perform all necessary data processing/calculation once during initialization (pre-computation).
-   **Example**: All valid tree values are calculated and stored in the `FindElements` constructor to enable fast lookups for subsequent `find` calls.

-   **Concept**: Hash Set for Efficient Existence Checks
-   **Context**: An `unordered_set` (or `HashSet` in Java) is the ideal data structure for quickly checking if an element exists within a collection, offering average O(1) time complexity for lookups and insertions.
-   **Example**: Storing all recovered node values in an `unordered_set<int>` allows the `find(target)` method to return `true` or `false` very quickly.

-   **Concept**: Depth-First Search (DFS) for Tree Recovery
-   **Context**: DFS is a natural choice for traversing the binary tree in the constructor because it easily allows passing the parent's calculated value down to children to determine their own values.
-   **Example**: A recursive helper function `recover(node, current_val)` is called, where `current_val` is passed from the parent.

-   **Concept**: `FindElements` Constructor Time Complexity
-   **Context**: The time complexity for the `FindElements` constructor is O(N), where N is the total number of nodes in the tree.
-   **Example**: This is because a single DFS traversal visits each node exactly once, and each operation (value assignment, hash set insertion) is O(1) on average.

-   **Concept**: `FindElements` Constructor Space Complexity
-   **Context**: The space complexity for the `FindElements` constructor is O(N) for storing all unique node values in the hash set, plus O(H) for the recursion stack (where H is tree height).
-   **Example**: For a tree with 10^4 nodes, the `unordered_set` will store 10^4 integers.

-   **Concept**: `find(target)` Method Time Complexity
-   **Context**: The time complexity for the `find(target)` method is O(1) on average.
-   **Example**: This is achieved by performing a direct lookup in the pre-computed `unordered_set`.

-   **Concept**: `find(target)` Method Space Complexity
-   **Context**: The space complexity for the `find(target)` method is O(1).
-   **Example**: It only requires space for the input `target` parameter and temporary internal operations, not for large data structures.

-   **Concept**: Optimal Overall Time Complexity
-   **Context**: The combination of O(N) constructor time and O(1) average `find` time results in an overall highly efficient O(N + Q) time complexity for the problem.
-   **Example**: For N=10^4 nodes and Q=10^4 queries, the total operations are approximately `10^4 + 10^4 = 2 * 10^4`, which is very fast.

-   **Concept**: Unique Node Values Property
-   **Context**: The value generation rules (`root=0`, `left=2x+1`, `right=2x+2`) inherently ensure that all generated node values within a valid binary tree structure are unique and non-negative.
-   **Example**: This property simplifies the solution, as an `unordered_set` works perfectly without needing to handle duplicate values originating from different paths.

-   **Concept**: State Passing in Recursive Tree Traversal
-   **Context**: In recursive tree algorithms, when properties of child nodes depend on their parent's properties, the parent's relevant "state" is passed as a parameter to the recursive call.
-   **Example**: Passing `current_val` (the parent's value) to `recover_tree_and_collect_values(node->left, 2 * current_val + 1)` allows the child to compute its own value.

-   **Concept**: Constraints as Algorithm Design Guiding Principle
-   **Context**: Thorough analysis of problem constraints (like N, Q, H, value ranges) is crucial for identifying inefficient approaches and selecting the most optimal algorithmic strategy.
-   **Example**: The `N=10^4` and `Q=10^4` constraints immediately suggest that an `O(N*Q)` solution will TLE, pushing towards pre-computation for `O(N+Q)` efficiency.