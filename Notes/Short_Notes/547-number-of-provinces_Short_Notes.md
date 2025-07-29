Here are concise short notes for quick revision of LeetCode problem 547 - Number of Provinces:

---

### **LeetCode 547: Number of Provinces - Quick Revision Notes**

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Count "provinces" (connected components) in a network of `n` cities.
*   **Graph Type:** Undirected. `isConnected[i][j] == isConnected[j][i]`.
*   **Input Format:** `n x n` adjacency matrix `isConnected`.
*   **Self-loops:** `isConnected[i][i] == 1` (city connected to itself) - generally doesn't affect province count.
*   **Constraints:** `1 <= n <= 200`. Small `n` allows `O(N^2)` solutions.

**2. Core Algorithmic Approach:**
*   **Method 1: Graph Traversal (DFS or BFS) - Recommended & Simpler:**
    1.  Initialize `provinces = 0` and `visited` set/array.
    2.  Iterate `i` from `0` to `n-1` (for each city).
    3.  If city `i` is **unvisited**:
        *   Increment `provinces` (found a new one).
        *   Start a DFS/BFS from city `i` to traverse and mark all reachable cities within its province as `visited`.
    4.  Return `provinces`.
*   **Method 2: Disjoint Set Union (DSU) / Union-Find:**
    1.  Initialize `n` disjoint sets (each city `i` is its own set), `provinces = n`.
    2.  Iterate through all pairs `(i, j)` where `isConnected[i][j] == 1` and `i != j`.
    3.  If `find(i) != find(j)` (i.e., `i` and `j` are in different provinces):
        *   Perform `union(i, j)` to merge their provinces.
        *   Decrement `provinces`.
    4.  Return `provinces`.
    *   **DSU Optimizations:** Path compression (for `find`) and Union by Rank/Size (for `union`) are crucial for efficiency.

**3. Important Time/Space Complexity Facts:**
*   **DFS/BFS:**
    *   **Time:** `O(N^2)` - Each city visited once, but iterating through `N` potential neighbors for each city results in `N * N` operations in total (equivalent to visiting all edges in a dense adjacency matrix).
    *   **Space:** `O(N)` - For `visited` set/array and recursion stack (DFS) or queue (BFS).
*   **DSU:**
    *   **Time:** `O(N^2 * α(N))` - `N^2` connections scanned, each union/find takes nearly constant `α(N)` time. Practically `O(N^2)`.
    *   **Space:** `O(N)` - For `parent` and `rank` arrays.
*   **Overall:** Both are optimal for adjacency matrix input as `N^2` entries must be at least read.

**4. Critical Edge Cases to Remember:**
*   **`n = 1` (Single city):** Always 1 province.
*   **All cities connected:** `isConnected` matrix is all `1`s. Result: 1 province.
*   **No cities connected (identity matrix):** Result: `n` provinces.
*   **Self-loops (`isConnected[i][i] == 1`):** Handled naturally; doesn't affect counts.

**5. Key Patterns or Techniques Used:**
*   **Connected Components:** A fundamental graph theory problem.
*   **Graph Traversal:** DFS/BFS are standard algorithms for exploring graph connectivity.
*   **Adjacency Matrix:** Common graph representation for dense graphs.
*   **`visited` set/array:** Essential to prevent cycles, redundant work, and ensure each node/component is processed exactly once.
*   **Disjoint Set Union (DSU):** Powerful data structure for dynamic connectivity problems.
*   **Generalization:** This pattern applies to other "grouping," "clustering," or "reachability" problems in graphs (e.g., flood fill).