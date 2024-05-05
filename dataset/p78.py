from resounds import completions

def subsets(nums: list[int]) -> list[list[int]]:
    """给你一个整数数组 nums ，数组中的元素互不相同 。返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。你可以按任意顺序返回解集。"""

code = completions(subsets)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(subsets([1,2,3]))
