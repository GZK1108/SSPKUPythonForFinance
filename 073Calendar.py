# 073:万年历
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 给定年月日，求星期几。已知2020年11月18日是星期三。另外，本题有公元0年，这个和真实的纪年不一样
#
# 输入
# 第一行是n(n <=30)，表示有n组数据
# 接下来n行，每行是一组数据。
# 每行三个整数y,m,d，分别代表年，月，日。(-1000000<=y<=1000000)
#
# 若今年是2017年，则往前就是2016年，2015年....一直数到2年，1年，再往前就是0年，-1年，-2年.....
# 输出
# 对每组数据，输出星期几，星期几分别用
#
# "Sunday","Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday" 表示
#
# 如果月份和日期不合法，输出"Illegal"
# 样例输入
# 6
# 2017 2 29
# 2017 13 2
# 0 1 1
# -2 3 4
# 2017 10 18
# 2015 12 31
# 样例输出
# Illegal
# Illegal
# Saturday
# Wednesday
# Wednesday
# Thursday

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
n = int(input())
for _ in range(n):
    y, m, d = map(int, input().split())
    if m < 1 or m > 12:
        print('Illegal')
    elif d < 1 or d > 31:
        print('Illegal')
    elif m in [4, 6, 9, 11] and d > 30:
        print('Illegal')
    elif m == 2 and d > 29:
        print('Illegal')
    elif m == 2 and d == 29 and y % 4 != 0:
        print('Illegal')
    else:
        if m < 3:
            m += 12
            y -= 1
        w = (y + y // 4 + y // 400 - y // 100 + (13 * (m + 1)) // 5 + d) % 7  # 基姆拉尔森公式
        # print(week[(w + 6) % 7])  # 和基姆拉尔森公式有一点儿偏差，所以要加6再取余，原因不明
        print(week[w])

