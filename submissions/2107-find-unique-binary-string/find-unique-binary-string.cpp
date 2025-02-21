class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        string ans(n, ' ');
        for (int i = 0; i < n; ++i) {
            // Flip the i-th character from the i-th string.
            ans[i] = (nums[i][i] == '0') ? '1' : '0';
        }
        return ans;
    }
};
