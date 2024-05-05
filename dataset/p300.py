from resounds import completions

def lengthOfLIS(nums: list[int]) -> int:
    """给你一个整数数组nums，找到其中最长严格递增子序列的长度。子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]的子序列。"""

code = completions(lengthOfLIS)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(lengthOfLIS([10,9,2,5,3,7,101,18]))
