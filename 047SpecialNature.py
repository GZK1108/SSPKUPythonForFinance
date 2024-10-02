# 047:求特殊自然数
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 一个十进制自然数,它的七进制与九进制表示都是三位数，且七进制与九进制的三位数码表示顺序正好相反。编程求此自然数,并输出显示。
#
# 输入
# 无。
# 输出
# 三行：
# 第一行是此自然数的十进制表示；
# 第二行是此自然数的七进制表示；
# 第三行是此自然数的九进制表示。
# 样例输入
# （无）
# 样例输出
# （不提供）


def ten_to_seven(n):
    seven = ''
    while n:
        seven = str(n % 7) + seven
        n //= 7
    return seven


def ten_to_nine(n):
    nine = ''
    while n:
        nine = str(n % 9) + nine
        n //= 9
    return nine


i = 99
while True:
    i += 1
    seven = ten_to_seven(i)
    nine = ten_to_nine(i)
    if seven[::-1] == nine and len(seven) == 3:
        print(i)
        print(seven)
        print(nine)
        break
