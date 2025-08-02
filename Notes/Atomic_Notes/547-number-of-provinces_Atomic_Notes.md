Here's a set of atomic notes for LeetCode 547: Number of Provinces, suitable for spaced repetition:

---

-   **Concept**: Definition of a "Province"
-   **Context**: LeetCode 547: Number of Provinces
-   **Example**: A province is a group of cities where every city in the group is directly or indirectly connected to every other city in the group, and there are no connections from cities within the group to cities outside the group.

-   **Concept**: Problem as a Graph Theory Equivalence
-   **Context**: LeetCode 547: Number of Provinces
-   **Example**: Counting "provinces" in the given city connection graph is equivalent to finding the number of "connected components" in an undirected graph.

-   **Concept**: Graph Representation (Adjacency Matrix)
-   **Context**: LeetCode 547: Input `isConnected` matrix
-   **Example**: The `isConnected[i][j]` matrix serves as an adjacency matrix where `1` indicates an edge (direct connection) between city `i` and city `j`.

-   **Concept**: Graph Property - Undirected
-   **Context**: LeetCode 547: `isConnected` matrix property
-   **Example**: `isConnected[i][j] == isConnected[j][i]` implies the graph is undirected; connections are symmetric.

-   **Concept**: Graph Property - Self-Loops
-   **Context**: LeetCode 547: `isConnected` matrix property
-   **Example**: `isConnected[i][i] == 1` means each city is directly connected to itself. This doesn't affect distinct province counting as a city is always part of its own province, and graph traversals handle it by marking nodes as visited.

-   **Concept**: DFS/BFS Core Idea for Connected Components
-   **Context**: LeetCode 547: Graph Traversal approach
-   **Example**: Iterate through all nodes. If a node is unvisited, increment a province counter and start a traversal (DFS or BFS) from it, visiting and marking all reachable nodes within that component as visited.

-   **Concept**: DFS/BFS on Adjacency Matrix - Time Complexity
-   **Context**: LeetCode 547: Graph Traversal approach
-   **Example**: `O(N^2)`. Each node is visited once. For each visited node, its connections to `N` other nodes are checked by iterating through the matrix row/column.

-   **Concept**: DFS/BFS on Adjacency Matrix - Space Complexity
-   **Context**: LeetCode 547: Graph Traversal approach
-   **Example**: `O(N)`. This is due to storing the `visited` set and the recursion stack (for DFS) or queue (for BFS), which can hold up to `N` elements.

-   **Concept**: DSU/Union-Find Core Idea for Connected Components
-   **Context**: LeetCode 547: Disjoint Set Union approach
-   **Example**: Initialize `N` distinct sets (one for each city). Iterate through all connections. If two connected cities `i` and `j` are in different sets, `union` their sets and decrement the province count. The final count of sets is the answer.

-   **Concept**: DSU `find` Operation with Path Compression
-   **Context**: LeetCode 547: Disjoint Set Union optimization
-   **Example**: `find(i)` returns the root (representative) of city `i`'s set. Path compression flattens the tree by making all nodes on the path from `i` to its root directly point to the root, optimizing future `find` calls.

-   **Concept**: DSU `union` Operation with Union by Rank/Size
-   **Context**: LeetCode 547: Disjoint Set Union optimization
-   **Example**: `union(i, j)` merges the sets containing `i` and `j`. Union by rank/size attaches the smaller/shorter tree under the root of the larger/taller tree, keeping the overall tree structure balanced for efficient operations.

-   **Concept**: DSU/Union-Find - Time Complexity
-   **Context**: LeetCode 547: Disjoint Set Union approach
-   **Example**: `O(N^2 * α(N))`. The `N^2` comes from iterating through all pairs in the `isConnected` matrix. `α(N)` (inverse Ackermann function) is the amortized time for `find`/`union` operations with optimizations, which is practically constant.

-   **Concept**: DSU/Union-Find - Space Complexity
-   **Context**: LeetCode 547: Disjoint Set Union approach
-   **Example**: `O(N)`. This is primarily for the `parent` array (or equivalent structure) which stores `N` integers.

-   **Concept**: Adjacency List Approach for Dense Graphs
-   **Context**: LeetCode 547: Comparing graph representations
-   **Example**: Building an adjacency list from an `N x N` adjacency matrix takes `O(N^2)` time and `O(N^2)` space in the worst-case (dense graph), as the number of edges `E` can be up to `O(N^2)`. For this problem, direct matrix traversal is often preferred for space efficiency.

-   **Concept**: Edge Case - Single City (`N=1`)
-   **Context**: LeetCode 547: Problem constraints
-   **Example**: If `isConnected = [[1]]`, the algorithms correctly identify 1 province. The DFS/BFS will visit the single city, increment `count` to 1, and return. DSU starts with 1 province and no unions occur.

-   **Concept**: Edge Case - Completely Disconnected Graph
-   **Context**: LeetCode 547: Problem constraints
-   **Example**: For `isConnected = [[1,0,0],[0,1,0],[0,0,1]]` (3 cities, no connections between them), the algorithms correctly return `N` (3) provinces. Each city triggers a new DFS/BFS call or remains in its own DSU set.

-   **Concept**: Edge Case - Completely Connected Graph
-   **Context**: LeetCode 547: Problem constraints
-   **Example**: If all `isConnected[i][j] = 1`, the algorithms correctly return 1 province. The first DFS/BFS call (from city 0) will visit all other cities. DSU will union all sets into one.

-   **Concept**: Graph Problem Pattern - Connected Components
-   **Context**: General pattern for similar problems
-   **Example**: Any problem asking to group elements based on direct or indirect relations, or to count distinct groups formed by connections, is likely a connected components problem solvable by DFS, BFS, or DSU.

-   **Concept**: Optimal Solution Choice for LeetCode 547
-   **Context**: LeetCode 547: Problem analysis
-   **Example**: For `N <= 200`, DFS/BFS directly on the adjacency matrix (O(N^2) time, O(N) space) or DSU (O(N^2 * α(N)) time, O(N) space) are optimal and highly efficient enough. Direct matrix traversal often has better constant factors for space over explicit adjacency list for dense graphs.