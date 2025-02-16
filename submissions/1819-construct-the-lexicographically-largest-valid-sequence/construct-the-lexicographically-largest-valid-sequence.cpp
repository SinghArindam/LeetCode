class Solution {
public:
    vector<int> res;
    vector<bool> used;

    bool backtrack(int index, int n) {
        if (index == res.size()) return true; // Base case: sequence is complete

        if (res[index] != 0) return backtrack(index + 1, n); // Skip if already filled

        for (int i = n; i >= 1; --i) { // Try placing larger numbers first
            if (used[i]) continue;

            // Place number i at res[index] and res[index + i] if possible
            if (i == 1 || (index + i < res.size() && res[index + i] == 0)) {
                res[index] = i;
                if (i != 1) res[index + i] = i;
                used[i] = true;

                if (backtrack(index + 1, n)) return true; // Recurse to next index

                // Undo choice (Backtrack)
                res[index] = 0;
                if (i != 1) res[index + i] = 0;
                used[i] = false;
            }
        }
        return false;
    }

    vector<int> constructDistancedSequence(int n) {
        int size = 2 * n - 1;
        res.assign(size, 0);
        used.assign(n + 1, false);

        backtrack(0, n);
        return res;
    }
};
