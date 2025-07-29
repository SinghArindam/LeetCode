Here is a set of atomic notes for LeetCode problem 547-number-of-provinces, formatted for spaced repetition learning:

-   **Concept**: Problem Goal (Number of Provinces)
    **Context**: LeetCode problem 547 asks to count the number of "provinces" in a network of cities.
    **Example**: Given city connections, determine how many distinct groups of connected cities exist.

-   **Concept**: Province Definition
    **Context**: A province is a group of cities where every city in the group is directly or indirectly connected to every other city in the same group, and no city outside the group is connected to any city inside.
    **Example**: If City A is connected to B, and B to C, then {A, B, C} form one province.

-   **Concept**: Equivalence to Connected Components
    **Context**: Finding the number of provinces is a classic graph problem equivalent to finding the number of connected components in an undirected graph.
    **Example**: Each "province" directly corresponds to one "connected component."

-   **Concept**: Adjacency Matrix Graph Representation
    **Context**: The input `isConnected` is an `n x n` matrix representing the graph's adjacency matrix.
    **Example**: `isConnected[i][j] = 1` signifies a direct connection (an edge) between city `i` and city `j`.

-   **Concept**: Number of Cities (`n`)
    **Context**: `n` denotes the total number of cities (nodes) in the graph.
    **Example**: `n = len(isConnected)`. Cities are typically indexed from `0` to `n-1`.

-   **Concept**: Undirected Graph Property
    **Context**: The graph is undirected, meaning if there's an edge from city `i` to city `j`, there's also one from `j` to `i`.
    **Example**: The constraint `isConnected[i][j] == isConnected[j][i]` confirms this.

-   **Concept**: Self-loops
    **Context**: `isConnected[i][i] == 1` indicates that a city is connected to itself.
    **Example**: Self-loops are standard in such matrices but do not affect the total number of distinct provinces.

-   **Concept**: Core Idea of Graph Traversal (DFS/BFS) for Connected Components
    **Context**: To count connected components, iterate through all nodes. If an unvisited node is found, increment the province count and start a traversal (DFS or BFS) from it to mark all reachable nodes as visited.
    **Example**: Each time a traversal starts from a new unvisited city, a new province is identified.

-   **Concept**: `visited` Data Structure in Traversal
    **Context**: A `set` or boolean array (`visited`) is crucial in graph traversals to track processed nodes, prevent cycles, and avoid redundant work.
    **Example**: `visited.add(node)` marks a city; `if node not in visited:` checks if it needs exploration.

-   **Concept**: Depth-First Search (DFS) Mechanism
    **Context**: DFS explores a graph by going as deep as possible along each branch before backtracking.
    **Example**: Implemented recursively (using the call stack) or iteratively with an explicit stack.

-   **Concept**: Breadth-First Search (BFS) Mechanism
    **Context**: BFS explores a graph level by level, visiting all immediate neighbors at the current depth before moving to the next level.
    **Example**: Implemented iteratively using a queue (`collections.deque` in Python).

-   **Concept**: Disjoint Set Union (DSU) Core Idea
    **Context**: DSU is a data structure that keeps track of a set of elements partitioned into disjoint (non-overlapping) subsets.
    **Example**: Each subset initially represents a city's "province," which can then be merged.

-   **Concept**: DSU `find` Operation
    **Context**: A DSU operation that determines the representative (root) of the set an element belongs to.
    **Example**: `find(element)` returns the root ID for `element`.

-   **Concept**: DSU `union` Operation
    **Context**: A DSU operation that merges the subsets containing two specified elements into a single subset.
    **Example**: `union(element1, element2)` merges their respective provinces if they are different.

-   **Concept**: DSU Path Compression Optimization
    **Context**: An optimization for the `find` operation that flattens the tree structure of sets by making every node in the path directly point to the root.
    **Example**: `parent[i] = find(parent[i])` during the `find` function's recursive call.

-   **Concept**: DSU Union by Rank/Size Optimization
    **Context**: An optimization for the `union` operation that attaches the smaller tree under the root of the larger tree to keep the overall tree structure flatter.
    **Example**: Attaching `root_j` to `root_i` if `rank[root_j] < rank[root_i]`.

-   **Concept**: DFS/BFS Time Complexity (Adjacency Matrix)
    **Context**: For a graph represented by an `N x N` adjacency matrix, DFS/BFS runs in `O(N^2)` time.
    **Example**: The algorithm effectively checks all `N^2` possible connections in the matrix.

-   **Concept**: DFS/BFS Space Complexity
    **Context**: DFS/BFS requires `O(N)` space for the `visited` set/array and the recursion stack (DFS) or queue (BFS).
    **Example**: Storing up to `N` city indices in the `visited` set.

-   **Concept**: DSU Time Complexity (Adjacency Matrix)
    **Context**: The DSU approach with optimizations for an `N x N` adjacency matrix runs in `O(N^2 * α(N))` time, where `α(N)` is the inverse Ackermann function (practically constant).
    **Example**: The `N^2` iterations through matrix connections dominate, each `union` operation being nearly constant time.

-   **Concept**: DSU Space Complexity
    **Context**: DSU requires `O(N)` space for the `parent` and `rank` (or `size`) arrays.
    **Example**: `parent = list(range(n))` initializes an array of size `N`.

-   **Concept**: Optimal Complexity for Adjacency Matrix Input
    **Context**: Both DFS/BFS and DSU provide optimal time complexity for graphs given as an adjacency matrix.
    **Example**: `O(N^2)` is optimal because, in the worst case, all `N^2` entries of the matrix might need to be examined.

-   **Concept**: DSU Province Count Initialization
    **Context**: When using DSU, the number of provinces is initially set to `n`, assuming each city is its own separate province.
    **Example**: `num_provinces = n` at the start.

-   **Concept**: Decrementing Province Count in DSU
    **Context**: In DSU, the total province count is decremented only when a `union` operation successfully merges two previously distinct sets.
    **Example**: `if find(i) != find(j): union(i, j); num_provinces -= 1`.

-   **Concept**: Edge Case: Single City (`n=1`)
    **Context**: If there is only one city, it forms a single province.
    **Example**: `isConnected = [[1]]` results in 1 province.

-   **Concept**: Edge Case: All Cities Connected
    **Context**: If all cities are directly or indirectly connected to each other, they form a single province.
    **Example**: For `n>1`, an `isConnected` matrix filled with `1`s results in 1 province.

-   **Concept**: Edge Case: No Connections Between Distinct Cities
    **Context**: If no cities are connected to other distinct cities (only to themselves).
    **Example**: `isConnected` is an identity matrix (e.g., `[[1,0,0],[0,1,0],[0,0,1]]`) results in `n` provinces.

-   **Concept**: General Graph Connectivity Pattern
    **Context**: This problem applies to a broad range of graph problems involving "grouping," "clustering," "networks," or "reachability."
    **Example**: Flood fill algorithms or determining if two nodes are connected.