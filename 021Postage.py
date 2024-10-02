# 021:计算邮资
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 根据邮件的重量和用户是否选择加急计算邮费。计算规则：重量在1000克以内(包括1000克), 基本费8元。超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；如果用户选择加急，多收5元。
#
# 输入
# 输入一行，包含整数和一个字符，以一个空格分开，分别表示重量（单位为克）和是否加急。如果字符是y，说明选择加急；如果字符是n，说明不加急。
# 输出
# 输出一行，包含一个整数，表示邮费。
# 样例输入
# 1200 y
# 样例输出
# 17
from math import ceil
w, e = input().split()
w = int(w)  # weight
if w <= 1000:
    if e == "y":
        print(8+5)
    elif e == "n":
        print(8)
else:
    if e == "y":
        print(8+5+(ceil((w-1000)/500))*4)
    elif e == "n":
        print(8+(ceil((w-1000)/500))*4)
