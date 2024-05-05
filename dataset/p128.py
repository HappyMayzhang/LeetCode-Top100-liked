from resounds import completions

def longestConsecutive(nums: list[int]) -> int:
    """给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。请你设计并实现时间复杂度为 O(n) 的算法解决此问题。"""

code = completions(longestConsecutive)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
