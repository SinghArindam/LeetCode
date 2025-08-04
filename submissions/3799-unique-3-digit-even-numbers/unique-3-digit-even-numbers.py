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
        # c = collections.Counter(digits)
        # ans = 0
        # for n in range(100, 1000, 2):
        #     n_c = collections.Counter(int(digit) for digit in str(n))
        #     if all(n_c[k] <= c.get(k, 0) for k in n_c):
        #         ans += 1
        # return ans

        # Approach 4
        # s = set()
        # for p in itertools.permutations(digits, 3):
        #     if p[0] != 0 and p[2] % 2 == 0:
        #         num = p[0] * 100 + p[1] * 10 + p[2]
        #         s.add(num)
        # return len(s)

        # Approach 5
        # s = set()
        # n = len(digits)
        
        # def find(path, used_mask):
        #     if len(path) == 3:
        #         if path[0] != 0 and path[2] % 2 == 0:
        #             s.add(path[0] * 100 + path[1] * 10 + path[2])
        #         return

        #     for i in range(n):
        #         if not used_mask[i]:
        #             used_mask[i] = True
        #             find(path + [digits[i]], used_mask)
        #             used_mask[i] = False

        # find([], [False] * n)
        # return len(s)

        # Approach 6
        # return len({i * 100 + j * 10 + k for i, j, k in itertools.permutations(digits, 3) if i != 0 and k % 2 == 0})

        # Approach 7
        n = len(digits)
        s = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    if digits[i] != 0 and digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        s.add(num)
        return len(s)
