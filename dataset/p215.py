from resounds import completions

def findKthLargest(nums: list[int], k: int) -> int:
    """给定整数数组nums和整数k，请返回数组中第k个最大的元素。请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。"""

code = completions(findKthLargest)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))
