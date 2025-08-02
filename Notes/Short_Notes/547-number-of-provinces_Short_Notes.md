Here are concise notes for LeetCode 547: Number of Provinces, suitable for quick revision:

---

### LeetCode 547: Number of Provinces - Quick Revision Notes

**1. Key Problem Characteristics & Constraints:**
*   **Goal:** Count "provinces" (connected components) in a graph.
*   **Input:** `n x n` `isConnected` matrix (adjacency matrix).
    *   `isConnected[i][j] = 1`: city `i` & `j` are directly connected.
    *   `isConnected[i][j] = 0`: not connected.
*   **Graph Properties:**
    *   Undirected: `isConnected[i][j] == isConnected[j][i]`.
    *   Self-loops: `isConnected[i][i] == 1` (cities are connected to themselves; doesn't affect distinct connectivity).
*   **Constraints:** `1 <= n <= 200` (N is small, N^2 solutions are fine).

**2. Core Algorithmic Approaches:**

*   **A. Graph Traversal (DFS or BFS) - Preferred Method:**
    1.  Initialize `count = 0` (for provinces) and `visited` set.
    2.  Iterate through each city `i` from `0` to `n-1`.
    3.  If `i` is *not* visited:
        *   Increment `count` (found a new province).
        *   Start a traversal (DFS or BFS) from `i` to visit all cities reachable from `i`, marking them `visited`. This explores the entire current province.
    4.  Return `count`.

*   **B. Disjoint Set Union (DSU / Union-Find):**
    1.  Initialize `n` sets, each city in its own set (initial `count = n`).
    2.  Iterate through unique pairs `(i, j)` where `isConnected[i][j] == 1`.
    3.  If `i` and `j` are in *different* sets (checked using `find` operation):
        *   `union` their sets.
        *   Decrement `count`.
    4.  Return final `count`.

**3. Important Time/Space Complexity Facts:**

*   **DFS/BFS (on Adjacency Matrix):**
    *   Time: `O(N^2)` (Each city visited once. For each city, iterate N potential neighbors in matrix.)
    *   Space: `O(N)` (For `visited` set and recursion stack/queue).

*   **Disjoint Set Union:**
    *   Time: `O(N^2 * α(N))` (Iterate N^2 pairs, `α(N)` is amortized time for `find`/`union` with optimizations, practically constant).
    *   Space: `O(N)` (For `parent` array).

*   **Adjacency List (build + traversal):**
    *   Time: `O(N^2)` (Building adjacency list from matrix takes N^2).
    *   Space: `O(N^2)` (For adjacency list in worst case, dense graph). Generally less optimal space for dense graphs than direct matrix traversal.

**4. Critical Edge Cases:**

*   **`n = 1` (single city):** Correctly returns 1 province.
*   **Completely disconnected graph:** Returns `n` provinces.
*   **Completely connected graph:** Returns 1 province.
*   **Self-loops and symmetry:** Handled naturally by graph traversal/DSU logic; they don't cause issues or infinite loops.

**5. Key Patterns or Techniques:**

*   **Finding Connected Components:** A fundamental graph problem.
*   **Graph Traversal:** DFS and BFS are standard algorithms for exploring graphs.
*   **Adjacency Matrix:** Direct interpretation of input as a graph representation.
*   **Disjoint Set Union (DSU):** Powerful data structure for dynamic connectivity problems. Key optimizations:
    *   **Path Compression:** Speeds up `find` operations.
    *   **Union by Rank/Size:** Balances tree structure for `union` operations.

---