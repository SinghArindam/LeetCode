class Solution {
public:
    string getHappyString(int n, int k) {
        string cur;
        vector<string> happy;
        backtrack(n, cur, happy);
        if(k > happy.size()) return "";
        return happy[k-1];
    }
    
private:
    void backtrack(int n, string &cur, vector<string>& happy) {
        if(cur.size() == n) {
            happy.push_back(cur);
            return;
        }
        // iterate in lexicographical order
        for(char c : {'a', 'b', 'c'}) {
            if(cur.empty() || cur.back() != c) {
                cur.push_back(c);
                backtrack(n, cur, happy);
                cur.pop_back();
            }
        }
    }
};
