from resounds import completions

def rotate(matrix: list[list[int]]) -> None:
    """给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转90度。你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。"""

code = completions(rotate)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)
