from resounds import completions

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：每行的元素从左到右升序排列。每列的元素从上到下升序排列。"""

code = completions(searchMatrix)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(searchMatrix([
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ], 5))
