def solution(m, n, puddles):
    MOD = 1000000007
    puddle_set = set(map(tuple, puddles))
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if r == 1 and c == 1:
                continue
            if (c, r) in puddle_set:
                dp[r][c] = 0
            else:
                up   = dp[r-1][c] if r > 1 else 0
                left = dp[r][c-1] if c > 1 else 0
                dp[r][c] = (up + left) % MOD
    
    return dp[n][m]