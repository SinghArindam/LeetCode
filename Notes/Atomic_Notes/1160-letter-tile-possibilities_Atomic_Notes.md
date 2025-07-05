Here is a set of atomic notes for LeetCode problem 1160-letter-tile-possibilities, formatted for spaced repetition learning:

-   **Concept**: Problem Objective for Letter Tile Possibilities
    -   **Context**: Find the total count of distinct non-empty letter sequences that can be formed using a given set of tiles.
    -   **Example**: For `tiles = "AAB"`, the unique sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

-   **Concept**: Tile Usage Constraint
    -   **Context**: Each letter tile from the input can be used at most once when forming a sequence.
    -   **Example**: If `tiles = "AB"`, the sequence "AAB" is not possible because 'A' is used twice.

-   **Concept**: Sequence Order Matters
    -   **Context**: The order of letters within a sequence is significant; "AB" is considered a distinct sequence from "BA".
    -   **Example**: For `tiles = "AB"`, "AB" and "BA" are counted as two separate unique possibilities.

-   **Concept**: Handling Duplicate Tiles in Input
    -   **Context**: The input string `tiles` can contain duplicate characters (e.g., "AAB"). The solution must correctly account for distinct sequences formed from these.
    -   **Example**: With `tiles = "AAB"`, sequences like "AA" are possible by using the two distinct 'A' tiles.

-   **Concept**: Problem Constraints (Length)
    -   **Context**: The length of the `tiles` string is very small (1 to 7). This often hints that solutions with factorial-related time complexities (`N!`) might be acceptable.
    -   **Example**: `tiles.length = 7` suggests that `7!` (5040) is a reasonable number of operations to consider.

-   **Concept**: Primary Algorithm for Letter Tile Possibilities
    -   **Context**: The most efficient approach involves Depth-First Search (DFS) with recursive backtracking to explore all possible sequence constructions.
    -   **Example**: The `dfs` function recursively tries to append each available character to a growing sequence.

-   **Concept**: Duplicate Tile Management (Frequency Map)
    -   **Context**: To handle duplicate tiles efficiently and avoid re-counting permutations of identical tiles, a frequency map (e.g., an array `int[26]`) is used to store counts of each available character.
    -   **Example**: For `tiles = "AAB"`, the frequency map would be `{'A': 2, 'B': 1}`.

-   **Concept**: DFS Initialization
    -   **Context**: Before starting the recursive `dfs` process, the input `tiles` string must be pre-processed into a frequency map to represent the initial available tiles.
    -   **Example**: `std::vector<int> freq(26, 0); for (char c : tiles) freq[c - 'A']++;`

-   **Concept**: Accumulating Count in DFS (Current Choice)
    -   **Context**: Inside the `dfs` loop, when a character `c` is chosen (`freq[c] > 0`), `count++` accounts for the unique sequence formed *by choosing just that character* (or extending a prefix by `c`).
    -   **Example**: If the current state is from `tiles="AAB"` and 'A' is picked, `count++` registers "A".

-   **Concept**: Accumulating Count in DFS (Recursive Extensions)
    -   **Context**: After decrementing the chosen character's frequency, `count += dfs(freq)` recursively adds all unique sequences that can be built by appending *further characters* to the sequence currently being formed.
    -   **Example**: After picking 'A' (forming "A"), the recursive call `dfs({'A':1, 'B':1})` would add counts for "AA", "AAB", "AB", "ABA".

-   **Concept**: Backtracking Step in DFS
    -   **Context**: After a recursive call returns, the frequency of the chosen character must be restored (`freq[i]++`). This undoes the current choice, allowing other branches of the recursion tree to consider that tile.
    -   **Example**: After exploring all sequences starting with "A", the count of 'A' is restored so the algorithm can explore sequences starting with "B".

-   **Concept**: Time Complexity (DFS with Frequency Map)
    -   **Context**: The time complexity is approximately `O(AlphabetSize * NumberOfUniqueSequences)`. In the worst case (all characters distinct), this can be bounded by `O(26 * N!)`.
    -   **Example**: For `N=7`, `26 * 7! = 26 * 5040 = 131,040` operations, which is very efficient.

-   **Concept**: Space Complexity (DFS with Frequency Map)
    -   **Context**: The space complexity is `O(AlphabetSize)` for the frequency map plus `O(N)` for the recursion stack depth.
    -   **Example**: Given a fixed alphabet size (26) and small `N` (`<=7`), this is effectively `O(1)` constant space.

-   **Concept**: Brute Force (std::set) Time Complexity Drawback
    -   **Context**: An alternative approach using `std::set<string>` to store unique permutations is significantly slower due to string copying/comparison and logarithmic set insertion overhead.
    -   **Example**: `O(N * N! * N * log(N!))` is much less efficient than `O(26 * N!)`.

-   **Concept**: Brute Force (std::set) Space Complexity Drawback
    -   **Context**: Using `std::set<string>` requires storing all unique sequences as strings, leading to higher space consumption.
    -   **Example**: `O(NumberOfUniqueSequences * N)` can be substantial for even small `N` compared to `O(1)` for the frequency map approach.

-   **Concept**: Single Tile Input Edge Case
    -   **Context**: The solution correctly handles cases where `tiles.length = 1`.
    -   **Example**: `numTilePossibilities("V")` returns `1` (for sequence "V").

-   **Concept**: All Duplicate Tiles Edge Case
    -   **Context**: The solution correctly handles inputs where all tiles are the same.
    -   **Example**: `numTilePossibilities("AAA")` returns `3` (for sequences "A", "AA", "AAA").

-   **Concept**: All Unique Tiles Edge Case
    -   **Context**: The solution correctly handles inputs where all tiles are unique.
    -   **Example**: `numTilePossibilities("ABC")` returns `15` (for all permutations of lengths 1, 2, and 3).

-   **Concept**: Backtracking as a General Pattern
    -   **Context**: This problem exemplifies the backtracking/DFS pattern for combinatorial enumeration, which involves making a choice, recursing, and then undoing the choice to explore alternatives.
    -   **Example**: Applicable in problems like permutations, combinations, and subsets.

-   **Concept**: Frequency Map for Multiset Problems (General Applicability)
    -   **Context**: Using frequency maps is a general and effective technique for solving combinatorial problems (permutations, combinations, subsets) when the input collection may contain duplicate elements (a multiset).
    -   **Example**: Used in LeetCode 47 (Permutations II), 40 (Combination Sum II), and 90 (Subsets II).

-   **Concept**: Constraint Interpretation as Hint
    -   **Context**: Small input constraints on `N` are strong indicators that solutions with factorial time complexity (e.g., backtracking for permutations) are likely intended and acceptable.
    -   **Example**: `tiles.length <= 7` hints towards `N!` being acceptable.