from resounds import completions

def jump(nums: list[int]) -> int:
    """每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
        0 <= j <= nums[i] 
        返回到达nums[n - 1]的最小跳跃次数。"""

code = completions(jump)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(jump([2,3,1,1,4]))
