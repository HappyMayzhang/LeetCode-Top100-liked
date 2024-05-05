from resounds import completions

def findAnagrams(s: str, p: str) -> list[int]:
    """给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。异位词指由相同字母重排列形成的字符串（包括相同的字符串）。"""

code = completions(findAnagrams)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))
