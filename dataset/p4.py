from resounds import completions

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    """给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数。算法的时间复杂度应该为 O(log (m+n)) 。"""

code = completions(findMedianSortedArrays)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(findMedianSortedArrays([1,3], [2]))
