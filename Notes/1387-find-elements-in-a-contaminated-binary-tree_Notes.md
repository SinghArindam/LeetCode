This comprehensive note covers the LeetCode problem "Find Elements in a Contaminated Binary Tree," detailing its problem statement, various approaches, complexity analysis, edge cases, and provides a well-commented optimal solution.

---

## LeetCode 1387: Find Elements in a Contaminated Binary Tree

### 1. Problem Summary

The problem asks us to implement a `FindElements` class for a binary tree that has been "contaminated" by changing all node values to `-1`. We are given specific rules for how the original, uncontaminated tree's values were generated:
1. The root node's value (`root.val`) was `0`.
2. For any node with value `x`:
   - Its left child (if it exists) had a value of `2 * x + 1`.
   - Its right child (if it exists) had a value of `2 * x + 2`.

The `FindElements` class needs two main components:
- **`FindElements(TreeNode* root)` (Constructor):** This initializes the object with the contaminated tree and "recovers" it, meaning it must determine the original values of all nodes.
- **`bool find(int target)`:** This method should return `true` if the `target` value exists in the *recovered* binary tree, and `false` otherwise.

**Constraints:**
- Node values are initially `-1`.
- Tree height is at most `20`. This implies a maximum of `2^(20+1) - 1` nodes, which is roughly 2 million, but the total number of nodes is capped at `10^4`. This height constraint is important for recursion depth limits.
- Total nodes: `[1, 10^4]`.
- Total calls to `find()`: `[1, 10^4]`.
- `target` value: `[0, 10^6]`.

### 2. Explanation of All Possible Approaches

Let's explore different ways to approach this problem, from naive to the most optimized.

#### 2.1 Naive Approach: On-Demand Traversal for Each `find` Call

**Concept:**
The constructor `FindElements(TreeNode* root)` does minimal work, perhaps just storing the pointer to the contaminated root. When `find(target)` is called, we perform a tree traversal (e.g., Depth-First Search or Breadth-First Search) starting from the `root`. As we traverse, we dynamically calculate the correct value for each node based on the given rules (root is 0, left child `2x+1`, right child `2x+2`). If the calculated value matches `target`, we immediately return `true`. If the entire tree is traversed without finding `target`, we return `false`.

**Logic:**
- **Constructor:** `FindElements(TreeNode* root)`:
    - Simply store the `root` pointer in a member variable. No recovery is done here.
- **`find(int target)`:**
    - Initialize a queue (for BFS) or use recursion (for DFS) for traversal.
    - Start with a pair `(node, calculated_val)` where `node` is the original root and `calculated_val` is `0`.
    - During traversal:
        - If `calculated_val == target`, return `true`.
        - For a `node` with `calculated_val`:
            - If `node->left` exists, add `(node->left, 2 * calculated_val + 1)` to the queue/recursive call.
            - If `node->right` exists, add `(node->right, 2 * calculated_val + 2)` to the queue/recursive call.
    - If traversal completes, return `false`.

**Limitations:**
- This approach re-computes the values for potentially the entire tree on *every single* call to `find`. Given `10^4` calls to `find` and `10^4` nodes, this could lead to `10^4 * 10^4 = 10^8` operations in the worst case, which is too slow (Time Limit Exceeded).

#### 2.2 Optimized Approach: Pre-computation with Hash Set (The Provided Solution's Strategy)

**Concept:**
The key bottleneck in the naive approach is redundant computation during `find` calls. Since `find` can be called many times, it makes sense to do all the "recovery" work once during the constructor and store the results in an efficient data structure for fast lookups. A hash set (like `std::unordered_set` in C++ or `HashSet` in Java) is ideal for checking the existence of an element in O(1) average time.

**Logic:**
- **Data Structure:** A private member variable, `std::unordered_set<int> values;`, will store all the correct, recovered values from the tree.
- **Constructor `FindElements(TreeNode* root)`:**
    - This is where the recovery happens. We'll use a recursive helper function (DFS is natural for this).
    - Call a helper function, say `recover(TreeNode* node, int current_val)`.
    - The initial call will be `recover(root, 0)`.
- **Helper `void recover(TreeNode* node, int current_val)`:**
    - **Base Case:** If `node` is `nullptr`, return.
    - **Action:**
        - Insert `current_val` into the `values` hash set: `values.insert(current_val);`.
        - (Optional, but done in the provided solution) Update the node's value: `node->val = current_val;`. This isn't strictly necessary for the `find` method if we're using a separate set, but it literally "recovers" the tree's values.
    - **Recursive Calls:**
        - `recover(node->left, 2 * current_val + 1);`
        - `recover(node->right, 2 * current_val + 2);`
- **`find(int target)`:**
    - Simply check if `target` exists in the `values` hash set: `return values.count(target);` (or `values.find(target) != values.end();`).

#### 2.3 Alternative Optimized Approach: Pre-computation by Modifying the Tree

**Concept:**
Similar to the optimized approach, this method also pre-computes the values in the constructor. However, instead of storing them in a separate data structure like a hash set, it directly updates the `val` field of each `TreeNode` to its correct recovered value.

**Logic:**
- **Constructor `FindElements(TreeNode* root)`:**
    - Use a recursive helper function, `recoverTree(TreeNode* node, int current_val)`.
    - The initial call is `recoverTree(root, 0)`.
- **Helper `void recoverTree(TreeNode* node, int current_val)`:**
    - **Base Case:** If `node` is `nullptr`, return.
    - **Action:** Set `node->val = current_val;`.
    - **Recursive Calls:**
        - `recoverTree(node->left, 2 * current_val + 1);`
        - `recoverTree(node->right, 2 * current_val + 2);`
- **`find(int target)`:**
    - Perform a tree traversal (DFS or BFS) on the *now recovered* tree.
    - At each `node`, check `if (node->val == target)`. If true, return `true`.
    - If the entire tree is traversed, return `false`.

**Comparison to Approach 2.2:**
- This approach saves space on the `unordered_set` itself.
- However, the `find` operation becomes O(N) again in the worst case, as it still requires a full tree traversal for each call. This is inefficient given the high number of `find` calls.
- Modifying the input tree directly might not always be desired or allowed in general scenarios, although for this specific problem, it fits the "recover" description.

**Conclusion on Approaches:**
Approach 2.2 (Pre-computation with Hash Set) is clearly the most optimal solution due to its O(1) average time complexity for the `find` operation, which is critical given the constraint on `10^4` calls to `find`.

### 3. Detailed Explanation of the Logic Behind the Provided Solution

The provided solution implements **Approach 2.2: Pre-computation with Hash Set**.

**Core Idea:**
The problem asks to `find` elements quickly. Since the tree structure is fixed and the value generation rules are deterministic, we can calculate all possible values in the tree *once* during the `FindElements` constructor and store them in a data structure that allows for very fast lookups. An `unordered_set` is perfect for this.

**Class Structure Breakdown:**

```cpp
#include <unordered_set> // Required for std::unordered_set

using namespace std;

// TreeNode definition (commented out as it's usually provided by LeetCode env)
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class FindElements {
private:
    // 1. Data Member: unordered_set to store all recovered values
    // This allows for O(1) average time complexity for 'find' operations.
    unordered_set<int> values;

    // 2. Helper Method: Recursive DFS for tree recovery
    // This function traverses the tree, calculates the correct value for each node,
    // and inserts it into the 'values' set.
    void recover(TreeNode* node, int val) {
        // Base case: If the current node is null, there's nothing to recover, so return.
        if (!node) {
            return;
        }

        // Assign the calculated value to the current node.
        // This 'recovers' the node's value as per the problem statement.
        // While not strictly necessary for the 'find' operation if 'values' set is used,
        // it fulfills the 'recovers it' part of the constructor's description.
        node->val = val; 
        
        // Insert the calculated value into our set for quick lookups later.
        values.insert(val);
        
        // Recursively call for the left child:
        // Left child's value is (2 * parent_val + 1).
        recover(node->left, 2 * val + 1);
        
        // Recursively call for the right child:
        // Right child's value is (2 * parent_val + 2).
        recover(node->right, 2 * val + 2);
    }

public:
    // 3. Constructor: Initializes the FindElements object
    // It triggers the recovery process for the given contaminated tree.
    FindElements(TreeNode* root) {
        // Start the recovery process from the root.
        // The root's correct value is defined as 0.
        // We only proceed if the root is not null (though constraints guarantee N >= 1).
        if (root) {
            recover(root, 0); 
        }
    }
    
    // 4. Public Method: Checks if a target value exists in the recovered tree
    // Thanks to the pre-computation and the unordered_set, this operation is very fast.
    bool find(int target) {
        // unordered_set::count(key) returns 1 if key is found, 0 otherwise.
        // This is an efficient way to check for existence.
        return values.count(target);
    }
};
```

### 4. Time and Space Complexity Analysis

#### Approach 2.1: Naive (On-Demand Traversal)

-   **`FindElements(TreeNode* root)` (Constructor):**
    -   Time: O(1) - Only stores the root pointer.
    -   Space: O(1) - Stores a single pointer.
-   **`find(int target)`:**
    -   Time: O(N) in the worst case, where N is the total number of nodes. A full tree traversal might be needed for each query.
    -   Space: O(H) for the recursion stack (DFS) or queue (BFS), where H is the height of the tree.
-   **Overall (Amortized):**
    -   If `Q` is the number of `find` queries: `O(Q * N)` time. This is too slow for given constraints (10^4 * 10^4 = 10^8 operations).

#### Approach 2.2: Optimized (Pre-computation with Hash Set - Provided Solution)

-   **`FindElements(TreeNode* root)` (Constructor):**
    -   **Time:** O(N), where N is the total number of nodes. The `recover` function performs a Depth-First Search (DFS) that visits each node exactly once. For each node, it performs a constant number of operations (assigning value, inserting into `unordered_set`). Insertion into an `unordered_set` is O(1) on average.
    -   **Space:** O(N) for storing all `N` unique values in the `unordered_set`. Additionally, O(H) for the recursion stack space during the DFS traversal, where H is the height of the tree. Since N can be much larger than H (e.g., in a complete tree, H ~ log N), the dominant factor is O(N).
-   **`find(int target)`:**
    -   **Time:** O(1) on average. Hash set lookups (using `count()` or `find()`) have average time complexity of O(1). In the worst-case scenario (due to extremely poor hash function or hash collisions for specific data), it could degrade to O(N), but this is very rare in practice with `std::unordered_set`.
    -   **Space:** O(1) - Only requires space for the `target` parameter.
-   **Overall (Amortized):**
    -   If `Q` is the number of `find` queries: `O(N + Q)` time. This is `10^4 + 10^4 = 2 * 10^4` operations, which is highly efficient and well within limits.

#### Approach 2.3: Alternative Optimized (Pre-computation by Modifying Tree)

-   **`FindElements(TreeNode* root)` (Constructor):**
    -   **Time:** O(N) for DFS traversal, updating each node's value.
    -   **Space:** O(H) for the recursion stack.
-   **`find(int target)`:**
    -   **Time:** O(N) in the worst case, as it still requires a full tree traversal of the modified tree.
    -   **Space:** O(H) for the recursion stack.
-   **Overall (Amortized):**
    -   If `Q` is the number of `find` queries: `O(N + Q * N)` time. This is similar to the naive approach in terms of query time, making it less optimal than using a hash set.

**Conclusion:** The provided solution (Approach 2.2) offers the best performance profile, especially when `find` is called multiple times, by front-loading the computation.

### 5. Edge Cases and How They Are Handled

1.  **Empty Tree (Root is `nullptr`):**
    *   **Constraint Note:** The problem states "The total number of nodes is between `[1, 10^4]`", which implies `root` will never be `nullptr`.
    *   **Handling in Code:** The constructor includes an `if (root)` check. If `root` were `nullptr`, the `recover` function would not be called, and the `values` `unordered_set` would remain empty. A subsequent `find(target)` call would correctly return `false` because `values.count(target)` on an empty set yields `0`.

2.  **Single Node Tree:**
    *   **Input:** `root` points to a node `[-1, null, null]`.
    *   **Constructor:** `FindElements(root)` calls `recover(root, 0)`.
        *   `node->val` becomes `0`.
        *   `values.insert(0)` adds `0` to the set.
        *   `recover(node->left, 1)` and `recover(node->right, 2)` are called, which immediately hit their base case (`!node`) and return.
    *   **`find(0)`:** Returns `true` (since `0` is in `values`).
    *   **`find(any_other_value)`:** Returns `false` (since `any_other_value` is not in `values`). This is correct.

3.  **Skewed Tree (e.g., all left children or all right children):**
    *   The DFS `recover` function handles skewed trees correctly as it simply follows the existing links.
    *   The maximum height constraint of `20` is important here. A DFS recursive call depth matches the height of the tree. A height of 20 is well within typical stack limits for recursion (often thousands). Without this constraint, a very deep skewed tree could lead to a stack overflow.

4.  **`target` Value Range:**
    *   `0 <= target <= 10^6`.
    *   The values generated in the tree (0, 1, 2, 3, 4, 5, 6, ...) grow exponentially. At height 20, the maximum possible value for a node would be approximately `2^(20+1) - 2` which is around `2 * 10^6`. The `target` value of `10^6` is well within this range, meaning it's a plausible value to find. `int` data type is sufficient to hold these values.
    *   Negative `target` values are excluded by the constraint, so no special handling is needed for them.

5.  **Duplicate Values:**
    *   The generation rules (`2x+1`, `2x+2`) for a standard binary tree structure ensure that all values are unique. If node A has value `x` and node B has value `y`, then all descendants of A will have values different from all descendants of B (unless B is a descendant of A). Specifically, `2x+1` and `2x+2` ensure that all values are distinct and non-negative. Therefore, `unordered_set` storing unique values works perfectly, as there won't be collisions in the actual node values.

### 6. Clean, Well-Commented Version of the Optimal Solution

```cpp
#include <unordered_set> // Required for std::unordered_set to store unique elements for fast lookup

// Definition for a binary tree node.
// This struct is typically provided by the LeetCode environment.
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class FindElements {
private:
    // A hash set (unordered_set) is used to store all the valid, recovered
    // integer values present in the binary tree.
    // This provides average O(1) time complexity for checking if a target exists.
    std::unordered_set<int> recovered_values;

    /**
     * @brief Recursive helper function to traverse the contaminated tree,
     *        calculate the correct value for each node, and store it.
     * @param node The current TreeNode being processed.
     * @param current_val The correctly calculated value for the 'node'.
     */
    void recover_tree_and_collect_values(TreeNode* node, int current_val) {
        // Base case: If the current node is null, we've reached the end of a path.
        // There's nothing to process, so we simply return.
        if (!node) {
            return;
        }

        // 1. Recover the node's value: Assign the calculated 'current_val' to the node.
        //    While not strictly necessary for the 'find' operation (as values are stored
        //    in the hash set), this step literally "recovers" the tree's internal state
        //    as per the problem's description for the constructor.
        node->val = current_val;

        // 2. Store the recovered value: Add 'current_val' to our hash set.
        //    This makes it available for quick lookups by the 'find' method.
        recovered_values.insert(current_val);

        // 3. Recurse for children:
        //    If the left child exists, calculate its value (2 * parent_val + 1)
        //    and recursively call this function for it.
        if (node->left) {
            recover_tree_and_collect_values(node->left, 2 * current_val + 1);
        }

        //    If the right child exists, calculate its value (2 * parent_val + 2)
        //    and recursively call this function for it.
        if (node->right) {
            recover_tree_and_collect_values(node->right, 2 * current_val + 2);
        }
    }

public:
    /**
     * @brief Constructor for the FindElements class.
     *        Initializes the object by recovering the contaminated binary tree.
     * @param root The root of the contaminated binary tree (all values are -1).
     */
    FindElements(TreeNode* root) {
        // The recovery process starts from the root node.
        // According to the problem rules, the root's original value is 0.
        // We ensure root is not null before starting traversal, though constraints state N >= 1.
        if (root) {
            recover_tree_and_collect_values(root, 0);
        }
    }

    /**
     * @brief Checks if a target value exists in the recovered binary tree.
     * @param target The integer value to search for.
     * @return true if the target value exists in the recovered tree, false otherwise.
     */
    bool find(int target) {
        // Use the 'count' method of unordered_set to efficiently check for existence.
        // 'count(key)' returns 1 if 'key' is found in the set, and 0 otherwise.
        // This operation has an average time complexity of O(1).
        return recovered_values.count(target);
    }
};

```

### 7. Key Insights and Patterns

1.  **Pre-computation for Frequent Queries:** When an object is initialized with data, and there will be many subsequent queries (`find` operations in this case) on that data, it's a strong indicator that you should pre-process or pre-compute relevant information during initialization. This shifts the computational cost from `Q` repeated queries to a single setup phase.

2.  **Tree Traversal for Data Processing:** Problems involving processing every node in a tree often lend themselves to standard tree traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS). DFS (recursive or iterative) is particularly natural when the value of a child node depends on its parent's value, as state (the calculated parent value) can easily be passed down through recursion.

3.  **Hash Sets for Fast Existence Checks:** When the primary requirement is to quickly check if an element "exists" within a collection, an `unordered_set` (or `HashSet` in Java) is an excellent choice. It provides average O(1) time complexity for insertion and lookup operations, making it highly efficient for problems with many queries.

4.  **Tree Properties (Value Generation):** The rules `root.val=0`, `left=2x+1`, `right=2x+2` are standard for representing a *complete* binary tree in an array where the root is at index 0. This problem applies these rules to an arbitrary binary tree structure. This property guarantees that all generated values are unique and non-negative, which simplifies handling (e.g., no need to worry about duplicate values causing issues in the `unordered_set`).

5.  **State Passing in Recursion:** In recursive tree traversals where child values depend on parent values (or other contextual information), passing this "state" as a parameter to the recursive function is a common and effective pattern (e.g., `recover(node, current_val)` where `current_val` is the value passed from the parent).

6.  **Constraints Guidance:** Always pay attention to constraints. The height constraint (<= 20) reassures us that recursive DFS won't hit stack overflow limits. The total nodes (N <= 10^4) and total find calls (Q <= 10^4) strongly push towards an `O(N + Q)` or `O(N + Q log N)` solution, ruling out `O(N * Q)`. This guides the choice of `unordered_set`.