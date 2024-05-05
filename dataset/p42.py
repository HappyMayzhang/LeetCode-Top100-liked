from resounds import completions

def trap(height: list[int]) -> int:
    """给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。"""

code = completions(trap)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
