from resounds import completions

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """给你一个m行n列的矩阵 matrix ，请按照顺时针螺旋顺序，返回矩阵中的所有元素。"""

code = completions(spiralOrder)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
