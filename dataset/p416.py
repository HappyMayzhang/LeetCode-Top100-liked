from resounds import completions

def canPartition(nums: list[int]) -> bool:
    """给你一个只包含正整数的非空数组nums。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。"""

code = completions(canPartition)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(canPartition([1,5,11,5]))
