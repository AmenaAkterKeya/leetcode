class Solution:
    
    def tribonacci(self, n: int) -> int:
        # dp = [0] * (n+1)

        # if n == 0:
        #     return 0
        
        # if n == 1 or n == 2:
        #     return 1

        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1

        # for i in range(3, n+1):
        #     dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        # ------2nd approach----
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        t0, t1, t2 = 0, 1, 1
        for _ in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        
        return t2

        