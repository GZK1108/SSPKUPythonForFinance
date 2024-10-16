# 062:单词出现频率统计
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 统计单词出现次数并排序输出
#
# 输入
# 最多60,000个单词，每个一行。单词由小写字母构成，不超过30个字符。
# 输出
# 按单词出现次数从高到低输出所有单词。次数相同的，按照词典序从小到大排。
# 样例输入
# about
# send
# about
# me
# 样例输出
# 2 about
# 1 me


word_count = {}

try:
    # 不断读取输入，直到EOF（如从标准输入流读取）
    while True:
        word = input().strip()  # 读取并去除两端空格
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
except EOFError:
    pass  # 捕获EOF错误，当输入结束时退出循环。windows Ctrl+Z, Linux Ctrl+D，pycharm Ctrl+D

# 将单词按频率降序排序，频率相同则按词典序升序排列
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# 输出结果
for count, word in sorted_words:
    print(f"{word} {count}")

