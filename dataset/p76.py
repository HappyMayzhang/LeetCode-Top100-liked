from resounds import completions

def minWindow(s: str, t: str) -> str:
    """给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 。"""

code = completions(minWindow)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))
