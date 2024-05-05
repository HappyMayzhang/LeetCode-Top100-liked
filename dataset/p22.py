from resounds import completions

def generateParenthesis(n: int) -> list[str]:
    """数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。"""

code = completions(generateParenthesis)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(generateParenthesis(3))
