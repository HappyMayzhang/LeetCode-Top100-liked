from resounds import completions

def longestPalindrome(s: str) -> str:
    """给你一个字符串s，找到s中最长的回文子串。
    如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。"""

code = completions(longestPalindrome)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(longestPalindrome("babad"))
