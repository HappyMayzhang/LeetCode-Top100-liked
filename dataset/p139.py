from resounds import completions

def wordBreak(s: str, wordDict: list[str]) -> bool:
    """给你一个字符串s和一个字符串列表wordDict作为字典。如果可以利用字典中出现的一个或多个单词拼接出s则返回true。注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。"""

code = completions(wordBreak)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(wordBreak("leetcode", ["leet", "code"]))
