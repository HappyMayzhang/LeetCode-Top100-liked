from resounds import completions

def findDuplicate(nums: list[int]) -> int:
    """给定一个包含n+1个整数的数组nums，其数字都在[1, n]范围内（包括 1 和 n），可知至少存在一个重复的整数。假设nums只有一个重复的整数，返回这个重复的数。"""

code = completions(findDuplicate)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(findDuplicate([1,3,4,2,2]))
