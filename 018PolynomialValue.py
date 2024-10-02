# 018:计算多项式的值
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 对于多项式f(x) = ax3 + bx2 + cx + d 和给定的a, b, c, d, x，计算f(x)的值。
#
# 输入
# 输入仅一行，包含5个实数，分别是x，及参数a、b、c、d的值，每个数都是绝对值不超过100的双精度浮点数。数与数之间以一个空格分开。
# 输出
# 输出一个实数，即f(x)的值，保留到小数点后7位。
# 样例输入
# 2.31 1.2 2 2 3
# 样例输出
# 33.0838692

numb = input().split()
x = float(numb[0])
a = float(numb[1])
b = float(numb[2])
c = float(numb[3])
d = float(numb[4])
print(f'{a*x**3+b*x**2+c*x+d:.7f}')
