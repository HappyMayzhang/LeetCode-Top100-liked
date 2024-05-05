from resounds import completions

def firstMissingPositive(nums: list[int]) -> int:
    """给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。"""

code = completions(firstMissingPositive)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(firstMissingPositive([1,2,0]))
