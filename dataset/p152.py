from resounds import completions

def maxProduct(nums: list[int]) -> int:
    """给你一个整数数组nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。"""

code = completions(maxProduct)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))
