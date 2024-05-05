from resounds import completions

def searchInsert(nums: list[int], target: int) -> int:
    """给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。"""

code = completions(searchInsert)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 5))
