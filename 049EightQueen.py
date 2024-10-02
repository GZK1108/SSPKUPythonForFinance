# 049:八皇后问题
# 查看提交统计提问
# 总时间限制: 10000ms 内存限制: 65536kB
# 描述
# 在国际象棋棋盘上放置八个皇后，要求每两个皇后之间不能直接吃掉对方。
# 输入
# 无输入。
# 输出
# 按给定顺序和格式输出所有八皇后问题的解（见Sample Output）。
# 样例输入
# 样例输出
# No. 1
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0 0
# No. 2
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 0 1 0 0 0 0 0
# No. 3
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 1 0 0 0 0
# 0 1 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# No. 4
# 1 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 0 0 0 0 1 0 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# No. 5
# 0 0 0 0 0 1 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 1 0 0 0 0
# No. 6
# 0 0 0 1 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# No. 7
# 0 0 0 0 1 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1
# 0 0 0 1 0 0 0 0
# 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# No. 8
# 0 0 1 0 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# No. 9
# 0 0 0 0 1 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 1
# 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 1 0 0 0 0 0
# ...以下省略

"""
注意这个代码过不了oj平台，因为oj要求输出顺序，本代码输出结果顺序与答案不相同
"""

class NQueen:
    def __init__(self, n):
        self.n = n
        self.record = [0] * n
        self.count = 0

    def check(self, x, y):
        for i in range(x):
            if self.record[i] == y or abs(self.record[i] - y) == abs(i - x):
                return False
        return True

    def print_board(self):
        print(f'No. {self.count + 1}')
        for i in range(self.n):
            for j in range(self.n):
                if j == self.record[i]:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            print()

    def n_queen(self):
        def dfs(index):
            if index == self.n:
                self.print_board()
                self.count += 1
                return
            for i in range(self.n):
                if self.check(index, i):
                    self.record[index] = i
                    dfs(index + 1)
        dfs(0)

nq = NQueen(8)
nq.n_queen()