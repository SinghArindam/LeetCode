class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Approach 1
        # mod = 10**9 + 7
        # even = (n + 1) // 2
        # odd = n // 2
        # a = pow(5, even, mod)
        # b = pow(4, odd, mod)
        # return (a * b) % mod

        # Approach 2
        # mod = 10**9 + 7
        # p = pow(20, n // 2, mod)
        # if n % 2 == 1:
        #     return (p * 5) % mod
        # return p

        # Approach 3
        mod = 10**9 + 7
        even = (n+1)//2
        odd = n//2
        def power(x, n, mod):
            res = 1
            while n>0:
                if n%2==1:
                    res = (res*x) % mod
                x = (x*x) % mod
                n = n//2
            return res

        return (power(5, even, mod) * power(4, odd, mod)) % mod