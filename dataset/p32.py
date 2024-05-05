from resounds import completions

def longestValidParentheses(s: str) -> int:
    """给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。"""

code = completions(longestValidParentheses)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(longestValidParentheses("(()"))
