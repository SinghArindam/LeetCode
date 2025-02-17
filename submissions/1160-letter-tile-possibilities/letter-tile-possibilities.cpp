class Solution {
public:
    int numTilePossibilities(string tiles) {
        // Frequency array for uppercase letters
        vector<int> freq(26, 0);
        for (char c : tiles) {
            freq[c - 'A']++;
        }
        return dfs(freq);
    }
    
private:
    // Recursive helper that returns the number of sequences possible
    int dfs(vector<int>& freq) {
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                // Use this letter as the next in sequence and count it
                count++;
                freq[i]--;
                // Add the number of sequences that can be built from the remaining letters
                count += dfs(freq);
                // Backtrack: restore the count for the current letter
                freq[i]++;
            }
        }
        return count;
    }
};
