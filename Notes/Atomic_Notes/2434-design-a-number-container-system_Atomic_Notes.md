Here's a set of atomic notes for LeetCode problem 2434-design-a-number-container-system, formatted for spaced repetition learning:

---

-   **Concept**: Problem Objective - `change` operation
-   **Context**: Design a `NumberContainers` system. The `change(index, number)` operation assigns `number` to `index`, replacing any existing number.
-   **Example**: `change(2, 10)` means index 2 now holds the number 10. If index 2 previously held 5, it's now 10.

-   **Concept**: Problem Objective - `find` operation
-   **Context**: Design a `NumberContainers` system. The `find(number)` operation must return the *smallest* `index` that currently holds the given `number`.
-   **Example**: If 10 is at indices {5, 2, 8}, `find(10)` should return 2. If 10 is not stored, return -1.

-   **Concept**: Constraint - Large `index` and `number` values
-   **Context**: `index` and `number` can be up to `10^9`. This implies traditional array-based storage is not feasible due to memory limitations for sparse data.
-   **Example**: An array of size `10^9` is too large; a hash map is suitable.

-   **Concept**: Constraint - Total calls
-   **Context**: A maximum of `10^5` total calls (`change` + `find`) will be made. This requires operations to be efficient (e.g., `O(log N)` or `O(1)` amortized).
-   **Example**: A linear scan (`O(M)`) for `find` on each call would be too slow (`10^5 * 10^5` is `10^{10}`).

-   **Concept**: Data Structure - `self.index_to_number` (Primary Source of Truth)
-   **Context**: A hash map (`dict` in Python) storing `index -> current_number`. It reflects the true, current state of each container.
-   **Example**: `self.index_to_number = {2: 10, 1: 20}` means index 2 has 10, index 1 has 20. Used to verify validity of entries in heaps.

-   **Concept**: Data Structure - `self.num_to_indices` (Min-Heaps)
-   **Context**: A hash map (`defaultdict(list)`) where each `number` maps to a min-heap (implemented using Python's `heapq`) of `index`es where that number is present. Used to quickly find the smallest index.
-   **Example**: `self.num_to_indices = {10: [1, 2, 3], 20: [5]}` where `[1, 2, 3]` and `[5]` are min-heaps.

-   **Concept**: `change` operation logic
-   **Context**: How `change(index, number)` updates the system.
-   **Example**: `self.index_to_number[index] = number` updates the truth. `heapq.heappush(self.num_to_indices[number], index)` adds the index to the new number's heap.

-   **Concept**: Lazy Deletion Strategy (in `change`)
-   **Context**: When `change(index, new_number)` occurs and `index` previously held `old_number`, `index` is *not* immediately removed from `self.num_to_indices[old_number]`'s heap.
-   **Example**: If index 5 changed from 10 to 20, 5 remains in `self.num_to_indices[10]`. This keeps `change` `O(log K)`.

-   **Concept**: `find` operation logic (Lazy Validation Loop)
-   **Context**: How `find(number)` retrieves the smallest index, incorporating lazy deletion.
-   **Example**: `while heap and self.index_to_number.get(heap[0]) != number: heapq.heappop(heap)`. This loop removes stale (invalid) entries from the heap until a valid one is found or the heap is empty.

-   **Concept**: Stale Entry (in heaps)
-   **Context**: An `index` in a `number`'s heap (`self.num_to_indices[number]`) is "stale" if `self.index_to_number[index]` no longer holds that `number`. This means the `index` was reassigned.
-   **Example**: If `self.num_to_indices[10]` contains `5`, but `self.index_to_number[5]` is now `20`, then `5` is a stale entry in `self.num_to_indices[10]`.

-   **Concept**: Time Complexity of `change`
-   **Context**: The `change` operation.
-   **Example**: `O(log K)` where `K` is the number of elements in the target number's heap. In the worst case, `K` can be up to `M` (total `change` operations), so `O(log M)`.

-   **Concept**: Amortized Time Complexity of `find`
-   **Context**: While a single `find` call might pop many stale elements, the total cost across all operations is efficient.
-   **Example**: Each `index` is pushed into a heap at most once per `change` and popped due to staleness at most once. Thus, total `heappop` operations are bounded by total `heappush` operations. This leads to `O(log M)` amortized per `find` call.

-   **Concept**: Overall Time Complexity
-   **Context**: For `C` total operations (`change` + `find`).
-   **Example**: `O(C * log C)`. With `C = 10^5`, this is roughly `10^5 * 17`, which is efficient enough.

-   **Concept**: Space Complexity
-   **Context**: Memory usage of the data structures.
-   **Example**: `O(M)` where `M` is the total number of unique `index`es ever touched by `change` operations (`M <= 10^5`). Both `self.index_to_number` and `self.num_to_indices` store roughly `M` entries combined.

-   **Concept**: Edge Case - `find(number)` not in system
-   **Context**: When `find` is called for a `number` that has never been assigned to any index, or all its indices were reassigned.
-   **Example**: Handled by `if number not in self.num_to_indices:` (initial check) or by the lazy deletion loop emptying the heap, resulting in `-1`.

-   **Concept**: Edge Case - `change(index, number)` where `index` already had `number`
-   **Context**: Reassigning the same number to an index.
-   **Example**: `index` is pushed into the heap again, creating a duplicate. The lazy deletion logic in `find` will handle this correctly, eventually finding the smallest *valid* entry.

-   **Concept**: Pattern - Hash Maps for Sparse Data
-   **Context**: Using dictionaries (`dict`, `defaultdict`) is ideal when keys (like `index` or `number`) can be large and sparse, as they don't require large pre-allocated arrays and provide `O(1)` average lookups.
-   **Example**: Directly mapping `10^9` to a value is fine for a hash map.

-   **Concept**: Pattern - Min-Heaps (Priority Queues) for Extremum Retrieval
-   **Context**: When the problem asks for the "smallest" or "largest" element in a dynamic collection.
-   **Example**: `heapq.heappush` and `heapq.heappop` maintain the min-heap property, ensuring `heap[0]` is always the smallest element efficiently.

-   **Concept**: Amortized Analysis Principle
-   **Context**: A technique where the average cost of an operation over a sequence of operations is considered, rather than the worst-case cost of a single operation. Useful for algorithms with varying operation costs.
-   **Example**: `find` operation might be costly in a single instance if many stale elements are popped, but the total number of pops over all calls is limited, making the *average* cost low.