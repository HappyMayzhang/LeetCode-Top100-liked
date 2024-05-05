from resounds import completions

def largestRectangleArea(heights: list[int]) -> int:
    """给定n个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。求在该柱状图中，能够勾勒出来的矩形的最大面积。"""

code = completions(largestRectangleArea)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))
