from resounds import completions

def letterCombinations(digits: str) -> list[str]:
    """给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。给出数字到字母的映射如下（与电话按键相同）。注意1不对应任何字母。"""

code = completions(letterCombinations)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(letterCombinations("23"))
