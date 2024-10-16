# 050:上台阶
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 有n级台阶（0<n<20），从下面开始走要走到所有台阶上面，每步可以走一级或两级，问有多少种不同的走法。
#
# 输入
# 一个整数n
# 输出
# 走法总数
# 样例输入
# 4
# 样例输出
# 5

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)


n = int(input())
print(climbStairs(n))
