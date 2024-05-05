from resounds import completions

def setZeroes(matrix: list[list[int]]) -> None:
    """给定一个m x n的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用原地算法。"""

code = completions(setZeroes)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)
    print(matrix)
