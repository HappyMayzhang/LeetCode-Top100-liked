from resounds import completions

def numSquares(n: int) -> int:
    """给你一个整数n，返回和为n的完全平方数的最少数量 。完全平方数是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而3和11不是。"""

code = completions(numSquares)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(numSquares(12))
