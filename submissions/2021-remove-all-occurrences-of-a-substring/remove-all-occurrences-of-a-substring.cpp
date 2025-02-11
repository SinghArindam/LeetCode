class Solution {
public:
    string removeOccurrences(string s, string part) {
        int pLen = part.size();
        string result;
        for (char c : s) {
            result.push_back(c);
            // If the end of result matches 'part', remove it.
            if (result.size() >= pLen &&
                result.compare(result.size() - pLen, pLen, part) == 0) {
                result.erase(result.size() - pLen, pLen);
            }
        }
        return result;
    }
};
