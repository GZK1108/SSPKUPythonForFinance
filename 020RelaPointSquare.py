# 020:点和正方形的关系
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 有一个正方形，四个角的坐标（x,y)分别是（1，-1），（1，1），（-1，-1），（-1，1），x是横轴，y是纵轴。写一个程序，判断一个给定的点是否在这个正方形内（包括正方形边界）。
#
# 输入
# 输入一行，包括两个整数x、y，以一个空格分开，表示坐标(x,y)。
# 输出
# 输出一行，如果点在正方形内，则输出yes，否则输出no。
# 样例输入
# 1 1
# 样例输出
# yes

x, y = input().split()
x = int(x)
y = int(y)
if -1 <= x <= 1 and -1 <= y <= 1:
    print("yes")
else:
    print("no")
