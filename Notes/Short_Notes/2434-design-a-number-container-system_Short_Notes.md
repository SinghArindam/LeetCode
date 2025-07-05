Here are concise short notes for quick revision of LeetCode problem 2434:

---

### **LeetCode 2434: Design a Number Container System - Revision Notes**

**1. Key Problem Characteristics & Constraints:**
*   **Operations:** `change(index, number)` (insert/replace), `find(number)` (return *smallest* index).
*   **Data Range:** `index`, `number` up to `10^9`. Implies map/hash-based solutions, *not* arrays.
*   **Call Count:** Max `10^5` total calls (`change` + `find`). Requires efficient `O(log N)` or `O(1)` amortized solutions.
*   **"Smallest Index":** Directs towards min-heap or sorted structures.

**2. Core Algorithmic Approach:**
*   **Two Hash Maps:**
    1.  `self.index_to_number = {}`: `index -> current_number`. The *single source of truth* for what an index currently holds.
    2.  `self.num_to_indices = defaultdict(list)`: `number -> min-heap (list used with `heapq`) of `index`es.
*   **`change(index, number)`:**
    1.  Update `self.index_to_number[index] = number`.
    2.  `heapq.heappush(self.num_to_indices[number], index)`.
    3.  **Crucial:** Old index from previous number's heap is *NOT* immediately removed (`lazy deletion`).
*   **`find(number)`:**
    1.  Get the min-heap for `number` (`self.num_to_indices[number]`). If no such number, return -1.
    2.  **Lazy Deletion Loop:** While heap is not empty AND `self.index_to_number.get(heap[0]) != number` (i.e., smallest index in heap is *stale*), `heapq.heappop(heap)`.
    3.  Return `heap[0]` if heap not empty after loop, else -1.

**3. Important Time/Space Complexity Facts:**
*   **`__init__`**: `O(1)`.
*   **`change`**: `O(log K)` where `K` is the size of the target number's heap. Max `K` is total changes `M`. So, `O(log M)`.
*   **`find`**: Amortized `O(log M)`. Each `index` pushed into a heap once per `change` and popped due to staleness at most once. Total `heappops` across all `find` calls is bounded by total `heappushes`.
*   **Overall Time**: `O(C * log C)` for `C` total calls (`C <= 10^5`). Efficient.
*   **Space**: `O(M)` where `M` is the total number of unique `index`es ever touched by `change` operations (`M <= 10^5`).

**4. Critical Edge Cases to Remember:**
*   **`find(number)` not in system:** Handled by initial check `if number not in self.num_to_indices: return -1`.
*   **`find(number)` all indices replaced:** Lazy deletion loop correctly pops all stale entries, leading to empty heap and returns -1.
*   **`change(index, number)` where `index` already had `number`:** `index` gets re-pushed into heap, resulting in duplicate entries. Lazy deletion handles this (smallest valid one is found).
*   **Large `index`, `number` values:** Hash maps (`dict`) naturally handle sparse keys efficiently without large memory allocation.

**5. Key Patterns or Techniques Used:**
*   **Hash Maps:** For `O(1)` average-case lookups and handling large/sparse keys.
*   **Min-Heaps (Priority Queues):** For efficient retrieval of the smallest element in a dynamic set (`O(1)` min, `O(log K)` push/pop).
*   **Lazy Deletion/Invalidation:** Key technique for performance. Instead of costly immediate removal of invalid elements, mark them as invalid (via a "source of truth" map) and prune them during retrieval. This amortizes deletion cost.
*   **Amortized Analysis:** Understanding that while a single operation might be costly, the total cost over a sequence of operations is efficient.