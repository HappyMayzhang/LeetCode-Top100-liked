from resounds import completions

def minPathSum(grid: list[list[int]]) -> int:
    """给定一个包含非负整数的mxn网格grid，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。"""

code = completions(minPathSum)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
