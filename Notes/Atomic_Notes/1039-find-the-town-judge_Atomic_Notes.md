Here is a set of atomic notes for LeetCode problem 1039-find-the-town-judge, designed for spaced repetition learning:

---

-   **Concept**: Problem Goal - Find Town Judge
    **Context**: Given `n` people and trust relationships, identify a unique "Town Judge".
    **Example**: Return the label (1 to `n`) of the judge, or `-1` if none.

-   **Concept**: Judge Property 1 - Trusts Nobody
    **Context**: The town judge must not initiate any trust relationships with anyone else.
    **Example**: If person 3 is the judge, `[3, X]` will not appear in the `trust` list for any `X`.

-   **Concept**: Judge Property 2 - Trusted By All Others
    **Context**: All `n-1` other people in the town must trust the judge.
    **Example**: If `n=3` and person 3 is the judge, then persons 1 and 2 must both trust person 3.

-   **Concept**: Judge Property 3 - Uniqueness
    **Context**: There is exactly one person who satisfies both "trusts nobody" and "trusted by all others" properties. This simplifies the search.
    **Example**: Once a candidate satisfying the rules is found, it's the unique judge.

-   **Concept**: Input `n` (Number of People)
    **Context**: An integer representing the total number of people in the town, labeled from 1 to `n`.
    **Example**: `n=3` means people are labeled 1, 2, 3.

-   **Concept**: Input `trust` (Trust Relationships)
    **Context**: A list of lists, where `trust[i] = [a, b]` indicates that person `a` trusts person `b`.
    **Example**: `[[1,2], [1,3]]` means person 1 trusts person 2, and person 1 trusts person 3.

-   **Concept**: Constraint - Number of People (`n`) Range
    **Context**: `1 <= n <= 1000`. This constraint guides the acceptable time complexity, making `O(N)` or `O(N log N)` solutions efficient enough.
    **Example**: For `n=1000`, an `O(N^2)` solution might be too slow.

-   **Concept**: Constraint - Number of Trust Relationships (`M`) Range
    **Context**: `0 <= trust.length <= 10^4`. This constraint similarly informs complexity, making `O(M)` or `O(M log M)` solutions efficient.
    **Example**: For `M=10^4`, an `O(M^2)` solution would be too slow.

-   **Concept**: Constraint - Unique Trust Pairs
    **Context**: All `[a_i, b_i]` pairs in the `trust` list are guaranteed to be unique. This simplifies counting; no need to handle duplicate entries.
    **Example**: The input will not contain `[[1,2], [1,2]]`.

-   **Concept**: Constraint - No Self-Trust
    **Context**: `a_i != b_i` is guaranteed for all `trust` pairs. A person cannot trust themselves.
    **Example**: The input will not contain `[1,1]`.

-   **Concept**: Graph Model - Nodes
    **Context**: In a graph representation of the problem, each person (labeled 1 to `n`) is a node.
    **Example**: For `n=3`, there are three nodes: 1, 2, and 3.

-   **Concept**: Graph Model - Directed Edges
    **Context**: A trust relationship `a` trusts `b` is represented as a directed edge from node `a` to node `b` (`a -> b`).
    **Example**: `[1,2]` implies a directed edge from node 1 to node 2.

-   **Concept**: Graph Term - Out-degree
    **Context**: The out-degree of a node is the number of edges originating from that node, representing the number of people that person trusts.
    **Example**: If person 1 trusts person 2 and person 3, the out-degree of node 1 is 2.

-   **Concept**: Graph Term - In-degree
    **Context**: The in-degree of a node is the number of edges terminating at that node, representing the number of people who trust that person.
    **Example**: If person 1 trusts person 3 and person 2 trusts person 3, the in-degree of node 3 is 2.

-   **Concept**: Judge's Out-degree Property
    **Context**: Based on "The town judge trusts nobody," the judge's out-degree must be 0.
    **Example**: If person 3 is the judge, their out-degree (number of people they trust) is 0.

-   **Concept**: Judge's In-degree Property
    **Context**: Based on "Everybody (except for the town judge) trusts the town judge," the judge's in-degree must be `n-1`.
    **Example**: If `n=3` and person 3 is the judge, their in-degree (number of people who trust them) is 2.

-   **Concept**: Optimal Approach - Single Trust Balance Array
    **Context**: An efficient way to find the judge by combining in-degree and out-degree into a single "net trust score" for each person.
    **Example**: Instead of two arrays for `in_degree` and `out_degree`, use one `trust_balance` array.

-   **Concept**: Trust Balance Calculation
    **Context**: For each `[truster, trustee]` pair in the `trust` list, decrement the `trust_balance` of the `truster` by 1 (outgoing trust) and increment the `trust_balance` of the `trustee` by 1 (incoming trust).
    **Example**: For `[1, 2]`, `trust_balance[1]` decreases by 1, `trust_balance[2]` increases by 1.

-   **Concept**: Judge's Expected Trust Balance Value
    **Context**: The judge's final `trust_balance` must be `n-1`. This is derived from `0` (from their own 0 outgoing trusts) + `(n-1)` (from `n-1` incoming trusts).
    **Example**: If `n=5`, the judge's `trust_balance` should be `4`.

-   **Concept**: Early Exit Optimization - Insufficient Trusts
    **Context**: If the total number of trust relationships (`len(trust)`) is less than `n-1` (and `n > 1`), it's impossible for any person to be trusted by `n-1` distinct people. Return `-1` early.
    **Example**: For `n=3`, if `trust=[[1,2]]` (length 1), `n-1=2`. Since `1 < 2`, return `-1` without further calculation.

-   **Concept**: Optimal Time Complexity
    **Context**: `O(N + M)`. This is achieved by initializing arrays (`O(N)`), iterating through trust relationships once (`O(M)`), and then iterating through all people once (`O(N)`).
    **Example**: With `N=1000` and `M=10^4`, this is efficient enough.

-   **Concept**: Optimal Space Complexity
    **Context**: `O(N)`. This is for storing the `trust_balance` array (or separate in/out-degree arrays), which is proportional to the number of people.
    **Example**: For `N=1000`, an array of 1001 integers is negligible space.

-   **Concept**: Edge Case - Single Person Town (`n = 1`)
    **Context**: If there's only one person, `n-1=0`. This person automatically satisfies both judge properties (trusts nobody, trusted by 0 others). The main logic correctly returns person 1.
    **Example**: `n=1, trust=[]` correctly returns 1.

-   **Concept**: Edge Case - Empty `trust` Array
    **Context**: If `trust.length = 0`: If `n=1`, person 1 is the judge. If `n > 1`, no one trusts anyone, so no judge exists. The early exit `len(trust) < n-1` handles this for `n > 1`.
    **Example**: `n=5, trust=[]` returns `-1`.

-   **Concept**: Edge Case - No Judge Exists
    **Context**: If, after processing all trust relationships, no person satisfies the judge's `n-1` balance condition, the algorithm correctly returns `-1`.
    **Example**: Cyclic trusts, or everyone trusts someone, or no one is trusted by `n-1` others.

-   **Concept**: Pattern - Graph Representation for Relationships
    **Context**: Problems involving entities and relationships (like trust, dependencies, connections) can often be effectively modeled as directed or undirected graphs.
    **Example**: Social networks, flow problems, dependency management.

-   **Concept**: Pattern - In-degree and Out-degree Analysis
    **Context**: For directed graphs, in-degree (incoming connections) and out-degree (outgoing connections) are fundamental properties, crucial for identifying sources, sinks, or nodes with specific interaction patterns.
    **Example**: Finding tasks with no prerequisites (in-degree 0) or no dependents (out-degree 0).

-   **Concept**: Pattern - Accumulation/Balance Metrics
    **Context**: Sometimes, combining multiple related properties (e.g., in-degree and out-degree) into a single "net" score can simplify logic and make code cleaner.
    **Example**: Net change, profit/loss calculations.

-   **Concept**: Pattern - Leveraging Problem Guarantees
    **Context**: Specific guarantees in problem statements (e.g., "exactly one," "unique," "sorted") can simplify algorithm design by removing the need to handle complex edge cases or multiple valid solutions.
    **Example**: "Exactly one judge" means you can return the first valid candidate found.

-   **Concept**: Pattern - Early Exit Conditions
    **Context**: Analyzing minimum requirements for a solution to exist and adding pre-checks can significantly improve average-case performance by quickly rejecting impossible scenarios.
    **Example**: Checking if there are enough total trust relationships for a judge to exist.

-   **Concept**: Pattern - 1-Based vs. 0-Based Indexing
    **Context**: When inputs are 1-based (e.g., people 1 to `n`), using arrays of size `n+1` (and ignoring index 0) often makes code cleaner and less error-prone than constantly converting to 0-based indices.
    **Example**: `trust_balance[person_label]` is more intuitive than `trust_balance[person_label - 1]`.