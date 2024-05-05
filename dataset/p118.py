from resounds import completions

def generate(numRows: int) -> list[list[int]]:
    """给定一个非负整数numRows，生成「杨辉三角」的前numRows行。在「杨辉三角」中，每个数是它左上方和右上方的数的和。"""

code = completions(generate)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(generate(5))
