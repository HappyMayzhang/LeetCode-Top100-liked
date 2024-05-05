from resounds import completions

def lengthOfLongestSubstring(s: str) -> int:
    """给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。"""

code = completions(lengthOfLongestSubstring)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
