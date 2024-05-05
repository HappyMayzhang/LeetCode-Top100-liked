from resounds import completions

def productExceptSelf(nums: list[int]) -> list[int]:
    """给你一个整数数组nums，返回数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。题目数据保证数组nums之中任意元素的全部前缀元素和后缀的乘积都在32位整数范围内。请不要使用除法，且在O(n)时间复杂度内完成此题。"""

code = completions(productExceptSelf)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))
