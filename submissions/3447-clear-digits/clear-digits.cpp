class Solution {
public:
    string clearDigits(string s) {
        string ans;
        for (char c : s) {
            if (isdigit(c)) {
                // Remove the closest non-digit character to its left.
                if (!ans.empty())
                    ans.pop_back();
            } else {
                ans.push_back(c);
            }
        }
        return ans;
    }
};
