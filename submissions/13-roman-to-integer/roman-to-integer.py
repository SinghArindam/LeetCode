class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        i = 1
        num = 0
        cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        while i < n+1:
            if i<n and (str(s[i-1] + s[i]) in cases):
                num += nums[str(s[i-1] + s[i])]
                i += 2
                continue
            num += nums[s[i-1]]
            i += 1
        return num
        