from resounds import completions

def decodeString(s: str) -> str:
    """给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的encoded_string正好重复k次。注意k保证为正整数。"""

code = completions(decodeString)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(decodeString("3[a]2[bc]"))
