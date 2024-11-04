# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# 在上面的数字三角形中寻找一条从顶部到底边的路径，使得
# 路径上所经过的数字之和最大。路径上的每一步都只能往左下或
# 右下走。只需要求出这个最大和即可，不必给出具体路径。
# 三角形的行数大于1小于等于100，数字为0 - 99

# 输入格式：
# 5 //三角形行数。下面是三角形
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# 要求输出最大和


# def maxSum(triangle):
#     n = len(triangle)
#     dp = [[-1 for _ in range(i)] for i in range(1, n+1)]
#     for i in range(n-1, -1, -1):
#         for j in range(i+1):
#             if i == n-1:
#                 dp[i][j] = triangle[i][j]
#             else:
#                 dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
#     return dp[0][0]



def maxSum(triangle):
    n = len(triangle)
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


n = int(input())
D = []
for _ in range(n):
    D.append(list(map(int, input().split())))
print(maxSum(D))

