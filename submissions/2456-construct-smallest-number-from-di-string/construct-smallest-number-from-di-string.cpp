class Solution {
public:
    string smallestNumber(string pattern) {
        string result = "";
        stack<int> stk;

        // Iterate through the pattern and push numbers into the stack
        for (int i = 0; i <= pattern.size(); i++) {
            stk.push(i + 1);  // Push numbers from 1 to n+1
            
            // If we encounter 'I' or reach the end, pop from the stack
            if (i == pattern.size() || pattern[i] == 'I') {
                while (!stk.empty()) {
                    result += to_string(stk.top());
                    stk.pop();
                }
            }
        }

        return result;
    }
};
