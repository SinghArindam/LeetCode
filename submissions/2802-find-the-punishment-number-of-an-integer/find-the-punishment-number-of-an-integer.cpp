class Solution {
public:
    bool isValid(int num, int square, int target, int index) {
        if (index == to_string(square).size()) 
            return target == 0;
        
        string s = to_string(square);
        int sum = 0;
        
        for (int i = index; i < s.size(); i++) {
            sum = sum * 10 + (s[i] - '0');  
            if (sum > target) break;  
            if (isValid(num, square, target - sum, i + 1)) 
                return true;
        }
        
        return false;
    }

    int punishmentNumber(int n) {
        int sum = 0;
        
        for (int i = 1; i <= n; i++) {
            int square = i * i;
            if (isValid(i, square, i, 0)) 
                sum += square;
        }
        
        return sum;
    }
};
