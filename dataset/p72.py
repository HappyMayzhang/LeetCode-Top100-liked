from resounds import completions

def minDistance(word1: str, word2: str) -> int:
    """给你两个单词word1和word2，请返回将word1转换成word2所使用的最少操作数。你可以对一个单词进行如下三种操作：插入一个字符、删除一个字符、替换一个字符"""

code = completions(minDistance)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(minDistance("horse", "ros"))
