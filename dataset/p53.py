from resounds import completions

def maxSubArray(nums: list[int]) -> int:
    """给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。子数组是数组中的一个连续部分。"""

code = completions(maxSubArray)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
