from resounds import completions

def sortColors(nums: list[int]) -> None:
    """给定一个包含红色、白色和蓝色、共n个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。我们使用整数0、1和2分别表示红色、白色和蓝色。必须在不使用库内置的sort函数的情况下解决这个问题。"""

code = completions(sortColors)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)
