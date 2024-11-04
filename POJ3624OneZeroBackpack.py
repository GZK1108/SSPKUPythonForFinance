# 有N件物品和一个容积为M的背包。第i件物品的体积w[i]，价值是d[i]。求解将哪些物品装入背包可使价值总和最大。
# 每种物品只有一件，可以选择放或者不放(N<=3500,M <= 13000)。

def OneZeroBackpack(N,M,w,d):
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # dp[i][j] 总体积为j时，前i个物品的最大价值
    # 边界条件
    for j in range(M+1):
        if j >= w[0]:
            dp[0][j] = d[0]
    # dp
    for i in range(1, N):
        for j in range(1, M+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+d[i])
    return dp[N-1][M]


if __name__ == '__main__':
    N, M = map(int, input().split())
    w = []
    d = []
    for _ in range(N):
        a, b = map(int, input().split())
        w.append(a)
        d.append(b)
    print(OneZeroBackpack(N, M, w, d))
