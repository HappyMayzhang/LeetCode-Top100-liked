from resounds import completions

def rotate(nums: list[int], k: int) -> None:
    """给定一个整数数组nums，将数组中的元素向右轮转k个位置，其中k是非负数。"""

code = completions(rotate)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    rotate(nums, 3)
    print(nums)
