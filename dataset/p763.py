from resounds import completions

def partitionLabels(s: str) -> list[int]:
    """给你一个字符串s。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是s。返回一个表示每个字符串片段的长度的列表。"""

code = completions(partitionLabels)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))
