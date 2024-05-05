from resounds import completions

def subarraySum(nums: list[int], k: int) -> int:
    """给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的子数组的个数 。子数组是数组中元素的连续非空序列。"""

code = completions(subarraySum)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(subarraySum([1, 1, 1], 2))
