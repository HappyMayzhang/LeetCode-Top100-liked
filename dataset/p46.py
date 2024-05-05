from resounds import completions

def permute(nums: list[int]) -> list[list[int]]:
    """给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。"""

code = completions(permute)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(permute([1,2,3]))
