from resounds import completions

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """给你一个满足下述两条属性的mxn整数矩阵：
    每行中的整数从左到右按非严格递增顺序排列。
    每行的第一个整数大于前一行的最后一个整数。
    给你一个整数target，如果target在矩阵中，返回true；否则，返回false。"""

code = completions(searchMatrix)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
