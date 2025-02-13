#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        for (int num : nums)
            pq.push((long long)num);
            
        int operations = 0;
        while (pq.top() < k) {
            if (pq.size() < 2)
                return -1; // safeguard, though problem guarantees an answer exists.
                
            long long x = pq.top(); pq.pop();
            long long y = pq.top(); pq.pop();
            long long newVal = 2 * x + y;
            pq.push(newVal);
            ++operations;
        }
        return operations;
    }
};
