from resounds import completions

def singleNumber(nums: list[int]) -> int:
    """给你一个非空整数数组nums，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。"""

code = completions(singleNumber)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(singleNumber([2,2,1]))
