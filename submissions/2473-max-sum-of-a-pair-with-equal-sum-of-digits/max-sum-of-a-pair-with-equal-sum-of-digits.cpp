class Solution {
public:
    int maximumSum(vector<int>& nums) {
        // Lambda function to compute the sum of digits for a given number.
        auto digitSum = [](int num) {
            int s = 0;
            while (num > 0) {
                s += num % 10;
                num /= 10;
            }
            return s;
        };
        
        // For each digit sum, we store a pair (first, second) representing 
        // the largest and second largest number with that digit sum.
        unordered_map<int, pair<int, int>> mp;
        int ans = -1;
        
        for (int num : nums) {
            int s = digitSum(num);
            auto &p = mp[s];
            // Update the pair for this digit sum.
            if (num > p.first) {
                p.second = p.first;
                p.first = num;
            } else if (num > p.second) {
                p.second = num;
            }
        }
        
        // Check all groups; if a group has at least two numbers, update the answer.
        for (auto &kv : mp) {
            auto p = kv.second;
            if (p.second != 0) { // Since all numbers are positive, p.second==0 means no valid pair.
                ans = max(ans, p.first + p.second);
            }
        }
        
        return ans;
    }
};
