# 052:N皇后问题
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 国际象棋的棋盘是由8×8共64个方格构成，棋子放在方格里面。如果两个皇后棋子在同一行、同一列，或者在某个正方形的对角线上，那么这两个皇后就会互相攻击。请在棋盘上摆放8个皇后，使得它们都不会互相攻击。这是经典的8皇后问题。
#
# 现在要解决N皇后问题：将N个皇后摆放在一个N行N列的国际象棋棋盘上，要求任何两个皇后不能互相攻击。输入皇后数N(1<=N<=9),输出所有的摆法。无解输出"NO ANSWER"。行列号都从0开始算。
#
# 输入
# 一个整数N，表示要把N个皇后摆放在一个N行N列的国际象棋棋盘上
# 输出
# 所有的摆放放案。每个方案一行，依次是第0行皇后位置、第1行皇后位置......第N-1行皇后位置。
# 多种方案输出顺序如下：优先输出第0行皇后列号小的方案。如果两个方案第0行皇后列号一致，那么优先输出第1行皇后列号小的方案......以此类推
# 样例输入
# 4
# 样例输出
# 1 3 0 2
# 2 0 3 1

class NQueen:
    def __init__(self, n):
        self.n = n
        self.record = [0] * n
        self.result = []

    def check(self, x, y):
        for i in range(x):
            if self.record[i] == y or abs(self.record[i] - y) == abs(i - x):
                return False
        return True

    def print_board(self):
        self.result.append(self.record[:])

    def n_queen(self):
        def dfs(index):
            if index == self.n:
                self.print_board()
                return
            for i in range(self.n):
                if self.check(index, i):
                    self.record[index] = i
                    dfs(index + 1)
        dfs(0)



N = int(input())
nq = NQueen(N)
nq.n_queen()
if not nq.result:
    print('NO ANSWER')
else:
    for r in nq.result:
        print(' '.join(str(x) for x in r))
