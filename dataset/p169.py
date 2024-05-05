from resounds import completions

def majorityElement(nums: list[int]) -> int:
    """给定一个大小为n的数组nums，返回其中的多数元素。多数元素是指在数组中出现次数大于⌊n/2⌋的元素。你可以假设数组是非空的，并且给定的数组总是存在多数元素。"""

code = completions(majorityElement)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(majorityElement([3,2,3]))
