from resounds import completions

def partition(s: str) -> list[list[str]]:
    """给你一个字符串s，请你将s分割成一些子串，使每个子串都是回文串。返回s所有可能的分割方案。"""

code = completions(partition)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(partition("aab"))
