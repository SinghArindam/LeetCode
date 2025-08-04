class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Approach 1
        # n = len(digits)
        # s = set()
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i == j or j == k or i == k:
        #                 continue
        #             if digits[i] != 0 and digits[k] % 2 == 0:
        #                 num = digits[i] * 100 + digits[j] * 10 + digits[k]
        #                 s.add(num)
        # return len(s)

        # Approach 2
        # cnt = collections.Counter(digits)
        # ans = 0
        # for i in range(1, 10):
        #     for j in range(0, 10):
        #         for k in range(0, 10, 2):
        #             c = cnt.copy()
        #             c[i] -= 1
        #             c[j] -= 1
        #             c[k] -= 1
        #             if min(c.values()) >= 0:
        #                 ans += 1
        # return ans

        # Approach 3
        c = collections.Counter(digits)
        ans = 0
        for n in range(100, 1000, 2):
            n_c = collections.Counter(int(digit) for digit in str(n))
            if all(n_c[k] <= c.get(k, 0) for k in n_c):
                ans += 1
        return ans