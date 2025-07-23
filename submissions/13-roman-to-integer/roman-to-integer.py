class Solution:
    def romanToInt(self, s: str) -> int:
        # Approach 1
        # n = len(s)
        # i = 1
        # num = 0
        # cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        # nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
        #         'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        # while i < n+1:
        #     if i<n and (str(s[i-1] + s[i]) in cases):
        #         num += nums[str(s[i-1] + s[i])]
        #         i += 2
        #         continue
        #     num += nums[s[i-1]]
        #     i += 1

        # Approach 2
        # nums_single = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # nums_double = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        # for i in nums_double:
        #     s = s.replace(i, str(nums_double[i])+ ' ')
        # for i in nums_single:
        #     s = s.replace(i, str(nums_single[i])+ ' ')
        # # s = [int(i) for i in s.split()]
        # # num = sum(s)

        # num = sum([int(i) for i in s.split()])
        # print(s)
        # print(len(nums_double))

        # Approach 3
        nums_single = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        prev_num = 0
        for i in range(len(s)-1, -1, -1):
            curr_num = nums_single[s[i]]
            if i != len(s)-1:
                prev_num = nums_single[s[i+1]]
            print(i, s[i], curr_num, prev_num)
            if curr_num < prev_num:
                num -= curr_num
            else:
                num += curr_num

        return num
        