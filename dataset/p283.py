from resounds import completions

def moveZeroes(nums: list[int]) -> None:
    """给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。请注意，必须在不复制数组的情况下原地对数组进行操作。"""

code = completions(moveZeroes)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)
