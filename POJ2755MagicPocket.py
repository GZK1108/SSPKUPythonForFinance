# 有一个神奇的口袋，总的容积是40，用这个口袋可以变出一些物品，这些物品的总体积必须是40。John现在有n个想要得到的物品，
# 每个物品的体积分别是a1，a2……an。John可以从这些物品中选择一些，如果选出的物体的总体积是40，那么利用这个神奇的口袋，
# John就可以得到这些物品。现在的问题是，John有多少种不同的选择物品的方式。
#
# 输入
# 输入的第一行是正整数n (1 <= n <= 20)，表示不同的物品的数目。接下来的n行，每行有一个1到40之间的正整数，分别给出a1，a2……an的值。
#
# 输出
# 输出不同的选择物品的方式的数目。
#
# 样例输入
# 3
# 20
# 20
# 20
# 样例输出
# 3


def countWays(A, v):
    n = len(A)
    dp = [[0 for _ in range(v+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n):
        for j in range(v+1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]
                if j-A[i] >= 0:
                    dp[i][j] += dp[i-1][j-A[i]]
    return dp[n-1][v]


n = int(input())
A = [0]
for _ in range(n):
    A.append(int(input()))

print(countWays(A, 40))