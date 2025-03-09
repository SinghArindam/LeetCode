class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        // Create diff array where diff[i] = 1 if colors[i] != colors[(i+1)%n]
        vector<int> diff(n);
        for (int i = 0; i < n; i++) {
            diff[i] = (colors[i] != colors[(i + 1) % n]) ? 1 : 0;
        }
        
        int windowSize = k - 1;  // We need k-1 differences to validate an alternating sequence
        // Extend diff array to handle circular wrap-around
        vector<int> ext(2 * n);
        for (int i = 0; i < 2 * n; i++) {
            ext[i] = diff[i % n];
        }
        
        // Calculate the sum for the first window of size windowSize
        int sum = 0;
        for (int i = 0; i < windowSize; i++) {
            sum += ext[i];
        }
        
        int count = 0;
        if (sum == windowSize) count++;
        
        // Slide the window for each possible starting index in the circle
        for (int i = 1; i < n; i++) {
            sum = sum - ext[i - 1] + ext[i + windowSize - 1];
            if (sum == windowSize)
                count++;
        }
        
        return count;
    }
};
